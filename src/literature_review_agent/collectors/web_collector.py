"""Collector for web search results."""

import asyncio
from typing import Optional
from urllib.parse import quote_plus

import aiohttp
from bs4 import BeautifulSoup

from .base import BaseCollector, CollectorResult
from ..models import Reference, ReferenceType, Author
from ..utils.text import extract_arxiv_ids, extract_dois, is_academic_url


class WebCollector(BaseCollector):
    """Collector for web search results using various search engines."""

    def __init__(self):
        super().__init__("web")
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

    async def collect(self, **kwargs) -> CollectorResult:
        """Web collector requires search - use search method instead."""
        return CollectorResult(
            warnings=["WebCollector requires a search query. Use search() method."]
        )

    async def search(
        self,
        query: str,
        max_results: int = 20,
        academic_only: bool = True,
        search_engine: str = "duckduckgo",
        **kwargs,
    ) -> CollectorResult:
        """Search the web for relevant content.

        Args:
            query: Search query
            max_results: Maximum number of results
            academic_only: Filter to academic sources only
            search_engine: Search engine to use ("duckduckgo", "google_scholar")

        Returns:
            CollectorResult with found references
        """
        if search_engine == "google_scholar":
            return await self._search_google_scholar(query, max_results)
        else:
            return await self._search_duckduckgo(query, max_results, academic_only)

    async def _search_duckduckgo(
        self,
        query: str,
        max_results: int,
        academic_only: bool,
    ) -> CollectorResult:
        """Search using DuckDuckGo.

        Args:
            query: Search query
            max_results: Maximum results
            academic_only: Filter to academic sources

        Returns:
            CollectorResult with found references
        """
        result = CollectorResult()
        session = await self._ensure_session()

        # Add academic site filters if requested
        if academic_only:
            academic_sites = [
                "arxiv.org",
                "semanticscholar.org",
                "scholar.google.com",
                "openreview.net",
                "papers.nips.cc",
                "proceedings.mlr.press",
            ]
            site_filter = " OR ".join(f"site:{site}" for site in academic_sites)
            query = f"{query} ({site_filter})"

        self.logger.info(f"Searching DuckDuckGo: '{query}'")

        try:
            # DuckDuckGo HTML search
            url = f"https://html.duckduckgo.com/html/?q={quote_plus(query)}"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }

            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    result.errors.append(f"DuckDuckGo returned status {response.status}")
                    return result

                html = await response.text()
                soup = BeautifulSoup(html, "lxml")

                # Parse results
                results_found = 0
                for link_elem in soup.select(".result__a"):
                    if results_found >= max_results:
                        break

                    href = link_elem.get("href")
                    title = link_elem.get_text(strip=True)

                    if not href or not title:
                        continue

                    # Extract actual URL from DuckDuckGo redirect
                    if "uddg=" in href:
                        from urllib.parse import parse_qs, urlparse
                        parsed = urlparse(href)
                        params = parse_qs(parsed.query)
                        if "uddg" in params:
                            href = params["uddg"][0]

                    # Skip non-http URLs
                    if not href.startswith(("http://", "https://")):
                        continue

                    # Filter non-academic if required
                    if academic_only and not is_academic_url(href):
                        continue

                    ref = self._url_to_reference(href, title)
                    result.references.append(ref)
                    results_found += 1

            self.logger.info(f"Found {len(result.references)} results from DuckDuckGo")

        except Exception as e:
            result.errors.append(f"DuckDuckGo search error: {e}")
            self.logger.error(f"Search error: {e}")

        return result

    async def _search_google_scholar(
        self,
        query: str,
        max_results: int,
    ) -> CollectorResult:
        """Search using Google Scholar.

        Note: Google Scholar may block automated requests.
        Consider using Semantic Scholar for reliable academic search.

        Args:
            query: Search query
            max_results: Maximum results

        Returns:
            CollectorResult with found references
        """
        result = CollectorResult()
        session = await self._ensure_session()

        self.logger.info(f"Searching Google Scholar: '{query}'")

        try:
            url = f"https://scholar.google.com/scholar?q={quote_plus(query)}&hl=en"
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Language": "en-US,en;q=0.5",
            }

            async with session.get(url, headers=headers) as response:
                if response.status == 429:
                    result.warnings.append(
                        "Google Scholar rate limited. Use Semantic Scholar for reliable academic search."
                    )
                    return result

                if response.status != 200:
                    result.errors.append(f"Google Scholar returned status {response.status}")
                    return result

                html = await response.text()
                soup = BeautifulSoup(html, "lxml")

                # Check for CAPTCHA
                if "captcha" in html.lower():
                    result.warnings.append(
                        "Google Scholar requires CAPTCHA. Use Semantic Scholar instead."
                    )
                    return result

                # Parse results
                results_found = 0
                for result_div in soup.select(".gs_ri"):
                    if results_found >= max_results:
                        break

                    # Get title and link
                    title_elem = result_div.select_one(".gs_rt a")
                    if not title_elem:
                        continue

                    title = title_elem.get_text(strip=True)
                    href = title_elem.get("href", "")

                    # Get authors and venue
                    authors_elem = result_div.select_one(".gs_a")
                    authors_text = authors_elem.get_text(strip=True) if authors_elem else ""

                    # Get abstract
                    abstract_elem = result_div.select_one(".gs_rs")
                    abstract = abstract_elem.get_text(strip=True) if abstract_elem else None

                    ref = self._create_scholar_reference(
                        href, title, authors_text, abstract
                    )
                    result.references.append(ref)
                    results_found += 1

            self.logger.info(f"Found {len(result.references)} results from Google Scholar")

        except Exception as e:
            result.errors.append(f"Google Scholar search error: {e}")
            self.logger.error(f"Search error: {e}")

        return result

    def _url_to_reference(self, url: str, title: str) -> Reference:
        """Convert a URL to a Reference.

        Args:
            url: URL
            title: Title text

        Returns:
            Reference object
        """
        # Detect reference type and extract IDs
        ref_type = ReferenceType.WEBPAGE
        arxiv_id = None
        doi = None

        if "arxiv.org" in url:
            ref_type = ReferenceType.PREPRINT
            arxiv_ids = extract_arxiv_ids(url)
            arxiv_id = arxiv_ids[0] if arxiv_ids else None
        elif any(x in url for x in ["doi.org", "nature.com", "science.org"]):
            ref_type = ReferenceType.PAPER
            dois = extract_dois(url)
            doi = dois[0] if dois else None
        elif any(x in url for x in ["blog", "medium.com", "substack"]):
            ref_type = ReferenceType.BLOG_POST

        return Reference(
            id=self._create_reference_id(url),
            title=title,
            url=url,
            arxiv_id=arxiv_id,
            doi=doi,
            ref_type=ref_type,
            discovered_from="web_search",
        )

    def _create_scholar_reference(
        self,
        url: str,
        title: str,
        authors_text: str,
        abstract: Optional[str],
    ) -> Reference:
        """Create a reference from Google Scholar result.

        Args:
            url: Paper URL
            title: Paper title
            authors_text: Authors string from Google Scholar
            abstract: Abstract snippet

        Returns:
            Reference object
        """
        # Parse authors from "A Smith, B Jones - Journal, 2023" format
        authors = []
        year = None

        if authors_text:
            parts = authors_text.split(" - ")
            if parts:
                author_names = parts[0].split(", ")
                for name in author_names[:5]:  # Limit authors
                    name = name.strip()
                    if name and not name.startswith("…"):
                        authors.append(Author(name=name))

                # Try to extract year
                if len(parts) > 1:
                    import re
                    year_match = re.search(r"\b(19|20)\d{2}\b", parts[-1])
                    if year_match:
                        year = int(year_match.group())

        # Detect type and IDs
        ref_type = ReferenceType.PAPER
        arxiv_id = None
        doi = None

        if "arxiv.org" in url:
            ref_type = ReferenceType.PREPRINT
            arxiv_ids = extract_arxiv_ids(url)
            arxiv_id = arxiv_ids[0] if arxiv_ids else None

        dois = extract_dois(url)
        doi = dois[0] if dois else None

        return Reference(
            id=self._create_reference_id(url),
            title=title,
            authors=authors,
            year=year,
            url=url,
            arxiv_id=arxiv_id,
            doi=doi,
            abstract=abstract,
            ref_type=ref_type,
            discovered_from="google_scholar",
        )

    async def search_site(
        self,
        query: str,
        site: str,
        max_results: int = 20,
    ) -> CollectorResult:
        """Search within a specific site.

        Args:
            query: Search query
            site: Site domain to search
            max_results: Maximum results

        Returns:
            CollectorResult with found references
        """
        site_query = f"site:{site} {query}"
        return await self._search_duckduckgo(site_query, max_results, academic_only=False)
