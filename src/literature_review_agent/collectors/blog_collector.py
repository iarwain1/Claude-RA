"""Collector for blogs and newsletters via RSS feeds."""

import asyncio
from datetime import datetime
from typing import Optional
from urllib.parse import urljoin, urlparse

import aiohttp
import feedparser
from bs4 import BeautifulSoup

from .base import BaseCollector, CollectorResult
from ..models import Reference, ReferenceType, Author
from ..utils.text import extract_urls_from_text, extract_arxiv_ids, clean_text


class BlogCollector(BaseCollector):
    """Collector for blogs and newsletters using RSS feeds."""

    def __init__(self):
        super().__init__("blog")
        self.session: Optional[aiohttp.ClientSession] = None

    async def _ensure_session(self) -> aiohttp.ClientSession:
        """Ensure aiohttp session exists."""
        if self.session is None or self.session.closed:
            timeout = aiohttp.ClientTimeout(total=60)
            self.session = aiohttp.ClientSession(timeout=timeout)
        return self.session

    async def close(self) -> None:
        """Close the aiohttp session."""
        if self.session and not self.session.closed:
            await self.session.close()

    async def collect(
        self,
        feed_urls: Optional[list[str]] = None,
        blog_urls: Optional[list[str]] = None,
        max_entries: int = 50,
        date_from: Optional[datetime] = None,
        extract_links: bool = True,
        **kwargs,
    ) -> CollectorResult:
        """Collect posts from blogs and newsletters.

        Args:
            feed_urls: List of RSS/Atom feed URLs
            blog_urls: List of blog URLs (will try to discover feeds)
            max_entries: Maximum entries per feed
            date_from: Only include posts after this date
            extract_links: Extract links from post content

        Returns:
            CollectorResult with found references
        """
        result = CollectorResult()
        all_feed_urls = list(feed_urls or [])

        # Discover feeds from blog URLs
        if blog_urls:
            for blog_url in blog_urls:
                discovered = await self._discover_feed(blog_url)
                if discovered:
                    all_feed_urls.append(discovered)
                else:
                    result.warnings.append(f"Could not find feed for {blog_url}")

        if not all_feed_urls:
            return CollectorResult(warnings=["No feed URLs provided or discovered"])

        # Process feeds concurrently
        tasks = [
            self._process_feed(url, max_entries, date_from, extract_links)
            for url in all_feed_urls
        ]

        feed_results = await asyncio.gather(*tasks, return_exceptions=True)

        for feed_result in feed_results:
            if isinstance(feed_result, Exception):
                result.errors.append(str(feed_result))
            else:
                result = result.merge(feed_result)

        return result

    async def search(
        self,
        query: str,
        feed_urls: Optional[list[str]] = None,
        **kwargs,
    ) -> CollectorResult:
        """Search blog posts for a query.

        This fetches all posts and filters by query terms.

        Args:
            query: Search query
            feed_urls: Feed URLs to search

        Returns:
            CollectorResult with matching references
        """
        if not feed_urls:
            return CollectorResult(warnings=["No feed URLs provided for search"])

        # First collect all posts
        all_posts = await self.collect(feed_urls=feed_urls, **kwargs)

        # Filter by query
        query_terms = query.lower().split()
        matching = []

        for ref in all_posts.references:
            searchable = f"{ref.title} {ref.abstract or ''}".lower()
            if all(term in searchable for term in query_terms):
                matching.append(ref)

        return CollectorResult(
            references=matching,
            warnings=all_posts.warnings,
            errors=all_posts.errors,
        )

    async def _discover_feed(self, blog_url: str) -> Optional[str]:
        """Discover RSS/Atom feed URL from a blog.

        Args:
            blog_url: Blog URL

        Returns:
            Feed URL if found, None otherwise
        """
        session = await self._ensure_session()

        try:
            headers = {"User-Agent": "Mozilla/5.0 (compatible; LiteratureReviewAgent/1.0)"}
            async with session.get(blog_url, headers=headers) as response:
                if response.status != 200:
                    return None

                html = await response.text()
                soup = BeautifulSoup(html, "lxml")

                # Look for feed links
                feed_selectors = [
                    'link[type="application/rss+xml"]',
                    'link[type="application/atom+xml"]',
                    'link[rel="alternate"][type*="xml"]',
                    'a[href*="feed"]',
                    'a[href*="rss"]',
                ]

                for selector in feed_selectors:
                    elem = soup.select_one(selector)
                    if elem:
                        href = elem.get("href")
                        if href:
                            return urljoin(blog_url, href)

                # Try common feed paths
                common_paths = ["/feed", "/rss", "/atom.xml", "/feed.xml", "/rss.xml", "/index.xml"]
                for path in common_paths:
                    feed_url = urljoin(blog_url, path)
                    try:
                        async with session.head(feed_url, headers=headers) as check:
                            if check.status == 200:
                                return feed_url
                    except:
                        pass

        except Exception as e:
            self.logger.warning(f"Error discovering feed for {blog_url}: {e}")

        return None

    async def _process_feed(
        self,
        feed_url: str,
        max_entries: int,
        date_from: Optional[datetime],
        extract_links: bool,
    ) -> CollectorResult:
        """Process a single RSS/Atom feed.

        Args:
            feed_url: Feed URL
            max_entries: Maximum entries to process
            date_from: Minimum date filter
            extract_links: Whether to extract links from content

        Returns:
            CollectorResult with references from feed
        """
        result = CollectorResult()
        session = await self._ensure_session()

        self.logger.info(f"Processing feed: {feed_url}")

        try:
            headers = {"User-Agent": "Mozilla/5.0 (compatible; LiteratureReviewAgent/1.0)"}
            async with session.get(feed_url, headers=headers) as response:
                if response.status != 200:
                    result.errors.append(f"Feed {feed_url} returned status {response.status}")
                    return result

                content = await response.text()

            # Parse feed
            feed = feedparser.parse(content)

            if feed.bozo and not feed.entries:
                result.errors.append(f"Invalid feed: {feed_url}")
                return result

            feed_title = feed.feed.get("title", urlparse(feed_url).netloc)

            for entry in feed.entries[:max_entries]:
                # Date filtering
                published = None
                if hasattr(entry, "published_parsed") and entry.published_parsed:
                    published = datetime(*entry.published_parsed[:6])
                elif hasattr(entry, "updated_parsed") and entry.updated_parsed:
                    published = datetime(*entry.updated_parsed[:6])

                if date_from and published and published < date_from:
                    continue

                # Create reference for the post itself
                ref = self._entry_to_reference(entry, feed_title)
                result.references.append(ref)

                # Extract links from content if enabled
                if extract_links:
                    content_html = entry.get("content", [{}])[0].get("value", "")
                    if not content_html:
                        content_html = entry.get("summary", "")

                    linked_refs = self._extract_content_links(content_html, ref.id)
                    result.references.extend(linked_refs)

            self.logger.info(f"Found {len(result.references)} items from {feed_title}")

        except Exception as e:
            result.errors.append(f"Error processing feed {feed_url}: {e}")
            self.logger.error(f"Feed error: {e}")

        return result

    def _entry_to_reference(self, entry, feed_title: str) -> Reference:
        """Convert a feed entry to a Reference.

        Args:
            entry: feedparser entry
            feed_title: Title of the feed

        Returns:
            Reference object
        """
        title = entry.get("title", "Untitled")
        link = entry.get("link", "")

        # Get author
        authors = []
        author_name = entry.get("author")
        if author_name:
            authors.append(Author(name=author_name))

        # Get year
        year = None
        if hasattr(entry, "published_parsed") and entry.published_parsed:
            year = entry.published_parsed[0]

        # Get summary/abstract
        abstract = None
        if entry.get("summary"):
            abstract = clean_text(BeautifulSoup(entry.summary, "lxml").get_text())
            if len(abstract) > 500:
                abstract = abstract[:500] + "..."

        # Determine type
        ref_type = ReferenceType.BLOG_POST
        if "newsletter" in feed_title.lower():
            ref_type = ReferenceType.NEWSLETTER

        return Reference(
            id=self._create_reference_id(link or title),
            title=title,
            authors=authors,
            year=year,
            url=link,
            abstract=abstract,
            ref_type=ref_type,
            venue=feed_title,
            discovered_from=f"feed:{feed_title}",
        )

    def _extract_content_links(
        self,
        html_content: str,
        parent_id: str,
    ) -> list[Reference]:
        """Extract linked references from post content.

        Args:
            html_content: HTML content
            parent_id: ID of the parent post

        Returns:
            List of references from links
        """
        references = []
        soup = BeautifulSoup(html_content, "lxml")

        for link in soup.find_all("a", href=True):
            href = link.get("href")
            text = link.get_text(strip=True)

            if not href or not href.startswith(("http://", "https://")):
                continue

            # Skip common non-content links
            skip_patterns = ["twitter.com", "facebook.com", "linkedin.com", "#", "mailto:"]
            if any(pattern in href.lower() for pattern in skip_patterns):
                continue

            # Check for arXiv links
            arxiv_ids = extract_arxiv_ids(href)
            arxiv_id = arxiv_ids[0] if arxiv_ids else None

            # Determine reference type
            ref_type = ReferenceType.WEBPAGE
            if arxiv_id or "arxiv.org" in href:
                ref_type = ReferenceType.PREPRINT
            elif any(x in href for x in ["doi.org", "nature.com", "science.org"]):
                ref_type = ReferenceType.PAPER
            elif "pdf" in href.lower():
                ref_type = ReferenceType.PAPER

            ref = Reference(
                id=self._create_reference_id(href),
                title=text if text else href,
                url=href,
                arxiv_id=arxiv_id,
                ref_type=ref_type,
                discovered_from=f"linked_from:{parent_id}",
            )
            references.append(ref)

        return references

    async def get_recent_posts(
        self,
        feed_url: str,
        days: int = 30,
    ) -> CollectorResult:
        """Get recent posts from a feed.

        Args:
            feed_url: Feed URL
            days: Number of days to look back

        Returns:
            CollectorResult with recent posts
        """
        from datetime import timedelta
        date_from = datetime.now() - timedelta(days=days)
        return await self.collect(feed_urls=[feed_url], date_from=date_from)
