"""Collector for extracting and following URLs from various sources."""

import asyncio
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup

from .base import BaseCollector, CollectorResult
from ..models import Reference, ReferenceType, Author
from ..utils.text import (
    extract_urls_from_markdown,
    extract_urls_from_text,
    extract_arxiv_ids,
    extract_dois,
    is_academic_url,
    clean_text,
)


class URLCollector(BaseCollector):
    """Collector for URLs from files and web pages."""

    def __init__(self):
        super().__init__("url")
        self.session: Optional[aiohttp.ClientSession] = None

    async def _ensure_session(self) -> aiohttp.ClientSession:
        """Ensure aiohttp session exists."""
        if self.session is None or self.session.closed:
            timeout = aiohttp.ClientTimeout(total=30)
            self.session = aiohttp.ClientSession(timeout=timeout)
        return self.session

    async def close(self) -> None:
        """Close the aiohttp session."""
        if self.session and not self.session.closed:
            await self.session.close()

    async def collect(
        self,
        file_paths: Optional[list[Path]] = None,
        urls: Optional[list[str]] = None,
        follow_links: bool = True,
        max_depth: int = 1,
        **kwargs,
    ) -> CollectorResult:
        """Collect references from URL lists and files.

        Args:
            file_paths: List of files containing URLs (txt, md, etc.)
            urls: List of URLs to process directly
            follow_links: Whether to follow links found in pages
            max_depth: Maximum depth for following links

        Returns:
            CollectorResult with found references
        """
        result = CollectorResult()
        all_urls: list[tuple[str, str]] = []  # (url, anchor_text)

        # Extract URLs from files
        if file_paths:
            for file_path in file_paths:
                if not file_path.exists():
                    result.warnings.append(f"File not found: {file_path}")
                    continue

                try:
                    content = file_path.read_text(encoding="utf-8", errors="ignore")

                    if file_path.suffix.lower() in [".md", ".markdown"]:
                        extracted = extract_urls_from_markdown(content)
                    else:
                        plain_urls = extract_urls_from_text(content)
                        extracted = [(url, "") for url in plain_urls]

                    all_urls.extend(extracted)
                    self.logger.info(f"Extracted {len(extracted)} URLs from {file_path}")
                except Exception as e:
                    result.errors.append(f"Error reading {file_path}: {e}")

        # Add direct URLs
        if urls:
            all_urls.extend([(url, "") for url in urls])

        # Deduplicate
        seen = set()
        unique_urls = []
        for url, anchor in all_urls:
            if url not in seen:
                seen.add(url)
                unique_urls.append((url, anchor))

        self.logger.info(f"Processing {len(unique_urls)} unique URLs")

        # Process URLs concurrently
        session = await self._ensure_session()
        tasks = [
            self._process_url(session, url, anchor, follow_links, max_depth)
            for url, anchor in unique_urls
        ]

        refs_lists = await asyncio.gather(*tasks, return_exceptions=True)

        for refs in refs_lists:
            if isinstance(refs, Exception):
                result.errors.append(str(refs))
            elif refs:
                result.references.extend(refs)

        return result

    async def search(self, query: str, **kwargs) -> CollectorResult:
        """URL collector doesn't support search - use WebCollector instead."""
        return CollectorResult(
            warnings=["URLCollector doesn't support search. Use WebCollector instead."]
        )

    async def _process_url(
        self,
        session: aiohttp.ClientSession,
        url: str,
        anchor_text: str,
        follow_links: bool,
        max_depth: int,
        current_depth: int = 0,
    ) -> list[Reference]:
        """Process a single URL and optionally follow links.

        Args:
            session: aiohttp session
            url: URL to process
            anchor_text: Anchor text for the URL
            follow_links: Whether to follow links
            max_depth: Maximum depth for following links
            current_depth: Current recursion depth

        Returns:
            List of references found
        """
        references = []

        try:
            # Fetch the page
            headers = {
                "User-Agent": "Mozilla/5.0 (compatible; LiteratureReviewAgent/1.0)"
            }
            async with session.get(url, headers=headers, allow_redirects=True) as response:
                if response.status != 200:
                    self.logger.warning(f"HTTP {response.status} for {url}")
                    return references

                content_type = response.headers.get("Content-Type", "")

                # Handle PDFs
                if "application/pdf" in content_type:
                    ref = self._create_pdf_reference(url, anchor_text)
                    references.append(ref)
                    return references

                # Handle HTML
                if "text/html" in content_type:
                    html = await response.text()
                    ref, child_urls = await self._parse_html_page(url, html, anchor_text)

                    if ref:
                        references.append(ref)

                    # Follow links if enabled and within depth
                    if follow_links and current_depth < max_depth:
                        for child_url, child_anchor in child_urls[:10]:  # Limit children
                            if is_academic_url(child_url):
                                child_refs = await self._process_url(
                                    session,
                                    child_url,
                                    child_anchor,
                                    follow_links=False,  # Don't recurse further
                                    max_depth=max_depth,
                                    current_depth=current_depth + 1,
                                )
                                references.extend(child_refs)

        except asyncio.TimeoutError:
            self.logger.warning(f"Timeout fetching {url}")
        except Exception as e:
            self.logger.warning(f"Error processing {url}: {e}")

        return references

    async def _parse_html_page(
        self, url: str, html: str, anchor_text: str
    ) -> tuple[Optional[Reference], list[tuple[str, str]]]:
        """Parse an HTML page to extract reference info and child links.

        Args:
            url: Page URL
            html: HTML content
            anchor_text: Anchor text for the link

        Returns:
            Tuple of (Reference or None, list of child URLs)
        """
        soup = BeautifulSoup(html, "lxml")
        child_urls = []

        # Extract title
        title = None
        if soup.title:
            title = soup.title.string
        if not title:
            og_title = soup.find("meta", property="og:title")
            if og_title:
                title = og_title.get("content")
        if not title:
            title = anchor_text or url

        title = clean_text(title) if title else url

        # Extract description/abstract
        abstract = None
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc:
            abstract = meta_desc.get("content")
        if not abstract:
            og_desc = soup.find("meta", property="og:description")
            if og_desc:
                abstract = og_desc.get("content")

        # Extract authors
        authors = []
        author_meta = soup.find("meta", attrs={"name": "author"})
        if author_meta:
            author_name = author_meta.get("content")
            if author_name:
                authors.append(Author(name=author_name))

        # Detect reference type
        ref_type = self._detect_reference_type(url, soup)

        # Extract arXiv ID if present
        arxiv_id = None
        arxiv_ids = extract_arxiv_ids(url + " " + html[:5000])
        if arxiv_ids:
            arxiv_id = arxiv_ids[0]

        # Extract DOI if present
        doi = None
        dois = extract_dois(html[:5000])
        if dois:
            doi = dois[0]

        # Create reference
        ref = Reference(
            id=self._create_reference_id(url),
            title=title,
            authors=authors,
            url=url,
            arxiv_id=arxiv_id,
            doi=doi,
            abstract=abstract,
            ref_type=ref_type,
            discovered_from="url_collection",
        )

        # Extract child links
        for link in soup.find_all("a", href=True):
            href = link.get("href")
            if href and href.startswith(("http://", "https://")):
                link_text = link.get_text(strip=True)
                child_urls.append((href, link_text))

        return ref, child_urls

    def _create_pdf_reference(self, url: str, anchor_text: str) -> Reference:
        """Create a reference for a PDF URL.

        Args:
            url: PDF URL
            anchor_text: Anchor text

        Returns:
            Reference object
        """
        title = anchor_text if anchor_text else url.split("/")[-1]
        arxiv_ids = extract_arxiv_ids(url)

        return Reference(
            id=self._create_reference_id(url),
            title=title,
            url=url,
            pdf_url=url,
            arxiv_id=arxiv_ids[0] if arxiv_ids else None,
            ref_type=ReferenceType.PAPER,
            discovered_from="url_collection",
        )

    def _detect_reference_type(self, url: str, soup: BeautifulSoup) -> ReferenceType:
        """Detect the type of reference from URL and page content.

        Args:
            url: Page URL
            soup: Parsed HTML

        Returns:
            Detected reference type
        """
        url_lower = url.lower()

        if "arxiv.org" in url_lower:
            return ReferenceType.PREPRINT
        if "doi.org" in url_lower or "journal" in url_lower:
            return ReferenceType.PAPER
        if any(x in url_lower for x in ["blog", "medium.com", "substack"]):
            return ReferenceType.BLOG_POST
        if "newsletter" in url_lower:
            return ReferenceType.NEWSLETTER
        if "youtube.com" in url_lower or "vimeo.com" in url_lower:
            return ReferenceType.VIDEO
        if "book" in url_lower:
            return ReferenceType.BOOK

        # Check meta tags
        og_type = soup.find("meta", property="og:type")
        if og_type:
            og_type_value = og_type.get("content", "").lower()
            if "article" in og_type_value:
                return ReferenceType.ARTICLE
            if "video" in og_type_value:
                return ReferenceType.VIDEO

        return ReferenceType.WEBPAGE
