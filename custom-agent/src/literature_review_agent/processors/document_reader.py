"""Document reader for fetching and parsing papers and articles."""

import asyncio
from pathlib import Path
from typing import Optional
from urllib.parse import urlparse

import aiohttp
from bs4 import BeautifulSoup
from pypdf import PdfReader
import trafilatura

from ..models import Reference
from ..utils.logging import get_logger
from ..utils.text import clean_text, truncate_text


class DocumentReader:
    """Reads and extracts text from various document sources."""

    def __init__(self, cache_dir: Optional[Path] = None):
        """Initialize the document reader.

        Args:
            cache_dir: Directory to cache downloaded documents
        """
        self.logger = get_logger("document_reader")
        self.cache_dir = cache_dir
        if cache_dir:
            cache_dir.mkdir(parents=True, exist_ok=True)
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

    async def read(
        self,
        reference: Reference,
        max_chars: int = 100000,
    ) -> Optional[str]:
        """Read the full text of a reference.

        Args:
            reference: Reference to read
            max_chars: Maximum characters to return

        Returns:
            Extracted text or None
        """
        # Try local PDF first
        if reference.local_pdf_path:
            path = Path(reference.local_pdf_path)
            if path.exists():
                text = await self._read_local_pdf(path)
                if text:
                    return truncate_text(text, max_chars // 4)  # Rough token estimate

        # Try PDF URL
        if reference.pdf_url:
            text = await self._read_pdf_url(reference.pdf_url)
            if text:
                return truncate_text(text, max_chars // 4)

        # Try arXiv PDF
        if reference.arxiv_id:
            pdf_url = f"https://arxiv.org/pdf/{reference.arxiv_id}.pdf"
            text = await self._read_pdf_url(pdf_url)
            if text:
                return truncate_text(text, max_chars // 4)

        # Try web page
        if reference.url:
            text = await self._read_webpage(reference.url)
            if text:
                return truncate_text(text, max_chars // 4)

        return None

    async def read_abstract(self, reference: Reference) -> Optional[str]:
        """Get the abstract of a reference.

        Args:
            reference: Reference to get abstract for

        Returns:
            Abstract text or None
        """
        # Return existing abstract if available
        if reference.abstract:
            return reference.abstract

        # Try to fetch from arXiv
        if reference.arxiv_id:
            abstract = await self._fetch_arxiv_abstract(reference.arxiv_id)
            if abstract:
                return abstract

        # Try to extract from webpage
        if reference.url:
            text = await self._read_webpage(reference.url, extract_abstract_only=True)
            if text:
                return text[:2000]  # Limit abstract length

        return None

    async def _read_local_pdf(self, path: Path) -> Optional[str]:
        """Read text from a local PDF.

        Args:
            path: Path to PDF file

        Returns:
            Extracted text or None
        """
        try:
            loop = asyncio.get_event_loop()

            def extract():
                reader = PdfReader(path)
                text_parts = []
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        text_parts.append(page_text)
                return "\n\n".join(text_parts)

            text = await loop.run_in_executor(None, extract)
            return clean_text(text) if text else None

        except Exception as e:
            self.logger.warning(f"Error reading PDF {path}: {e}")
            return None

    async def _read_pdf_url(self, url: str) -> Optional[str]:
        """Download and read a PDF from URL.

        Args:
            url: PDF URL

        Returns:
            Extracted text or None
        """
        session = await self._ensure_session()

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (compatible; LiteratureReviewAgent/1.0)"
            }
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    self.logger.warning(f"Failed to download PDF: {url} (status {response.status})")
                    return None

                content = await response.read()

                # Save to cache if enabled
                if self.cache_dir:
                    filename = urlparse(url).path.split("/")[-1] or "document.pdf"
                    cache_path = self.cache_dir / filename
                    cache_path.write_bytes(content)
                    return await self._read_local_pdf(cache_path)

                # Read from memory
                import io
                loop = asyncio.get_event_loop()

                def extract():
                    reader = PdfReader(io.BytesIO(content))
                    text_parts = []
                    for page in reader.pages:
                        page_text = page.extract_text()
                        if page_text:
                            text_parts.append(page_text)
                    return "\n\n".join(text_parts)

                text = await loop.run_in_executor(None, extract)
                return clean_text(text) if text else None

        except Exception as e:
            self.logger.warning(f"Error reading PDF from {url}: {e}")
            return None

    async def _read_webpage(
        self,
        url: str,
        extract_abstract_only: bool = False,
    ) -> Optional[str]:
        """Read text from a webpage.

        Args:
            url: Webpage URL
            extract_abstract_only: Only try to extract abstract

        Returns:
            Extracted text or None
        """
        session = await self._ensure_session()

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
            async with session.get(url, headers=headers) as response:
                if response.status != 200:
                    return None

                html = await response.text()

                if extract_abstract_only:
                    return self._extract_abstract_from_html(html)

                # Use trafilatura for main content extraction
                loop = asyncio.get_event_loop()
                text = await loop.run_in_executor(
                    None,
                    lambda: trafilatura.extract(
                        html,
                        include_comments=False,
                        include_tables=True,
                        favor_precision=True,
                    )
                )

                if text:
                    return clean_text(text)

                # Fallback to BeautifulSoup
                soup = BeautifulSoup(html, "lxml")

                # Remove script and style elements
                for element in soup(["script", "style", "nav", "footer", "header"]):
                    element.decompose()

                # Get text from main content areas
                main_content = soup.find("main") or soup.find("article") or soup.find("body")
                if main_content:
                    text = main_content.get_text(separator="\n", strip=True)
                    return clean_text(text)

                return None

        except Exception as e:
            self.logger.warning(f"Error reading webpage {url}: {e}")
            return None

    def _extract_abstract_from_html(self, html: str) -> Optional[str]:
        """Extract abstract from HTML.

        Args:
            html: HTML content

        Returns:
            Abstract text or None
        """
        soup = BeautifulSoup(html, "lxml")

        # Common abstract selectors
        selectors = [
            'meta[name="description"]',
            'meta[property="og:description"]',
            '[class*="abstract"]',
            '[id*="abstract"]',
            'section[aria-label="Abstract"]',
            '.Abstract',
            '#abstract',
        ]

        for selector in selectors:
            element = soup.select_one(selector)
            if element:
                if element.name == "meta":
                    content = element.get("content")
                    if content:
                        return clean_text(content)
                else:
                    text = element.get_text(strip=True)
                    if text and len(text) > 50:  # Reasonable abstract length
                        return clean_text(text)

        return None

    async def _fetch_arxiv_abstract(self, arxiv_id: str) -> Optional[str]:
        """Fetch abstract from arXiv.

        Args:
            arxiv_id: arXiv ID

        Returns:
            Abstract text or None
        """
        try:
            import arxiv

            loop = asyncio.get_event_loop()
            results = await loop.run_in_executor(
                None,
                lambda: list(arxiv.Client().results(arxiv.Search(id_list=[arxiv_id])))
            )

            if results:
                return results[0].summary

        except Exception as e:
            self.logger.warning(f"Error fetching arXiv abstract for {arxiv_id}: {e}")

        return None

    async def download_pdf(
        self,
        reference: Reference,
        output_dir: Path,
    ) -> Optional[Path]:
        """Download PDF for a reference.

        Args:
            reference: Reference to download
            output_dir: Directory to save PDF

        Returns:
            Path to downloaded PDF or None
        """
        pdf_url = reference.pdf_url
        if not pdf_url and reference.arxiv_id:
            pdf_url = f"https://arxiv.org/pdf/{reference.arxiv_id}.pdf"

        if not pdf_url:
            return None

        session = await self._ensure_session()
        output_dir.mkdir(parents=True, exist_ok=True)

        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (compatible; LiteratureReviewAgent/1.0)"
            }
            async with session.get(pdf_url, headers=headers) as response:
                if response.status != 200:
                    return None

                # Generate filename
                filename = reference.arxiv_id or reference.id
                filename = f"{filename}.pdf"
                output_path = output_dir / filename

                content = await response.read()
                output_path.write_bytes(content)

                self.logger.info(f"Downloaded PDF to {output_path}")
                return output_path

        except Exception as e:
            self.logger.warning(f"Error downloading PDF: {e}")
            return None

    async def get_sections(self, text: str) -> dict[str, str]:
        """Extract sections from document text.

        Args:
            text: Document text

        Returns:
            Dictionary of section_name -> content
        """
        sections = {}
        current_section = "Introduction"
        current_content = []

        # Common section headers
        section_patterns = [
            "abstract", "introduction", "background", "related work",
            "methodology", "methods", "approach", "model", "architecture",
            "experiments", "results", "evaluation", "discussion",
            "conclusion", "conclusions", "future work", "references",
            "appendix", "supplementary"
        ]

        lines = text.split("\n")

        for line in lines:
            line_lower = line.lower().strip()

            # Check if this is a section header
            is_header = False
            for pattern in section_patterns:
                if line_lower.startswith(pattern) or line_lower == pattern:
                    # Save previous section
                    if current_content:
                        sections[current_section] = "\n".join(current_content)
                    current_section = line.strip()
                    current_content = []
                    is_header = True
                    break

            if not is_header:
                current_content.append(line)

        # Save last section
        if current_content:
            sections[current_section] = "\n".join(current_content)

        return sections
