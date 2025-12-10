"""Collector for local files including Obsidian notes, PDFs, and URL lists."""

import asyncio
from pathlib import Path
from typing import Optional

from pypdf import PdfReader

from .base import BaseCollector, CollectorResult
from ..models import Reference, ReferenceType, Author
from ..utils.text import (
    extract_urls_from_markdown,
    extract_urls_from_text,
    extract_arxiv_ids,
    extract_dois,
    clean_text,
)


class LocalFileCollector(BaseCollector):
    """Collector for local files and folders."""

    def __init__(self):
        super().__init__("local")

    async def collect(
        self,
        paths: Optional[list[Path]] = None,
        file_types: Optional[list[str]] = None,
        recursive: bool = True,
        extract_links: bool = True,
        **kwargs,
    ) -> CollectorResult:
        """Collect references from local files.

        Args:
            paths: List of file or directory paths
            file_types: File extensions to include (e.g., [".md", ".pdf"])
            recursive: Recursively search directories
            extract_links: Extract URLs from text files

        Returns:
            CollectorResult with found references
        """
        result = CollectorResult()

        if not paths:
            return CollectorResult(warnings=["No paths provided"])

        # Default file types
        if file_types is None:
            file_types = [".md", ".txt", ".pdf", ".markdown"]

        # Collect all files
        files_to_process = []
        for path in paths:
            if not path.exists():
                result.warnings.append(f"Path not found: {path}")
                continue

            if path.is_file():
                files_to_process.append(path)
            elif path.is_dir():
                pattern = "**/*" if recursive else "*"
                for file_type in file_types:
                    files_to_process.extend(path.glob(f"{pattern}{file_type}"))

        self.logger.info(f"Processing {len(files_to_process)} local files")

        # Process files
        for file_path in files_to_process:
            try:
                file_result = await self._process_file(file_path, extract_links)
                result = result.merge(file_result)
            except Exception as e:
                result.warnings.append(f"Error processing {file_path}: {e}")

        return result

    async def search(
        self,
        query: str,
        paths: Optional[list[Path]] = None,
        **kwargs,
    ) -> CollectorResult:
        """Search local files for a query.

        Args:
            query: Search query
            paths: Paths to search in

        Returns:
            CollectorResult with matching references
        """
        # First collect all files
        all_files = await self.collect(paths=paths, **kwargs)

        # Filter by query
        query_terms = query.lower().split()
        matching = []

        for ref in all_files.references:
            searchable = f"{ref.title} {ref.abstract or ''} {' '.join(ref.tags)}".lower()
            if all(term in searchable for term in query_terms):
                matching.append(ref)

        return CollectorResult(
            references=matching,
            warnings=all_files.warnings,
        )

    async def _process_file(
        self,
        file_path: Path,
        extract_links: bool,
    ) -> CollectorResult:
        """Process a single file.

        Args:
            file_path: Path to file
            extract_links: Whether to extract URLs

        Returns:
            CollectorResult with references from file
        """
        result = CollectorResult()
        suffix = file_path.suffix.lower()

        if suffix == ".pdf":
            ref = await self._process_pdf(file_path)
            if ref:
                result.references.append(ref)

        elif suffix in [".md", ".markdown"]:
            refs = await self._process_markdown(file_path, extract_links)
            result.references.extend(refs)

        elif suffix == ".txt":
            refs = await self._process_text(file_path, extract_links)
            result.references.extend(refs)

        return result

    async def _process_pdf(self, file_path: Path) -> Optional[Reference]:
        """Process a PDF file.

        Args:
            file_path: Path to PDF

        Returns:
            Reference object or None
        """
        try:
            loop = asyncio.get_event_loop()

            def read_pdf():
                reader = PdfReader(file_path)
                metadata = reader.metadata or {}

                # Extract text from first few pages for analysis
                text = ""
                for page in reader.pages[:5]:
                    text += page.extract_text() or ""

                return metadata, text, len(reader.pages)

            metadata, text, num_pages = await loop.run_in_executor(None, read_pdf)

            # Extract info from metadata
            title = metadata.get("/Title", file_path.stem)
            if isinstance(title, bytes):
                title = title.decode("utf-8", errors="ignore")

            author = metadata.get("/Author", "")
            if isinstance(author, bytes):
                author = author.decode("utf-8", errors="ignore")

            authors = []
            if author:
                # Split common author separators
                for sep in [";", ",", " and "]:
                    if sep in author:
                        authors = [Author(name=a.strip()) for a in author.split(sep)]
                        break
                if not authors:
                    authors = [Author(name=author)]

            # Try to extract arXiv ID and DOI from text
            arxiv_ids = extract_arxiv_ids(text[:5000])
            dois = extract_dois(text[:5000])

            # Extract abstract if possible
            abstract = None
            abstract_markers = ["abstract", "summary"]
            text_lower = text.lower()
            for marker in abstract_markers:
                start = text_lower.find(marker)
                if start != -1:
                    # Get text after "abstract"
                    end = min(start + 2000, len(text))
                    abstract_text = text[start:end]
                    # Try to find end of abstract
                    intro_pos = abstract_text.lower().find("introduction")
                    if intro_pos > 100:
                        abstract_text = abstract_text[:intro_pos]
                    abstract = clean_text(abstract_text[:1000])
                    break

            return Reference(
                id=self._create_reference_id(str(file_path)),
                title=title,
                authors=authors,
                local_pdf_path=str(file_path),
                arxiv_id=arxiv_ids[0] if arxiv_ids else None,
                doi=dois[0] if dois else None,
                abstract=abstract,
                ref_type=ReferenceType.PAPER,
                discovered_from="local_file",
            )

        except Exception as e:
            self.logger.warning(f"Error reading PDF {file_path}: {e}")
            return None

    async def _process_markdown(
        self,
        file_path: Path,
        extract_links: bool,
    ) -> list[Reference]:
        """Process a markdown file.

        Args:
            file_path: Path to markdown file
            extract_links: Whether to extract URLs

        Returns:
            List of references
        """
        references = []

        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")

            # Create reference for the note itself if it's substantial
            lines = content.split("\n")
            title = file_path.stem

            # Try to extract title from first heading
            for line in lines[:10]:
                if line.startswith("# "):
                    title = line[2:].strip()
                    break

            # Extract tags from YAML frontmatter or inline tags
            tags = self._extract_obsidian_tags(content)

            # Only create a reference for the note if it's substantial
            if len(content) > 500:
                note_ref = Reference(
                    id=self._create_reference_id(str(file_path)),
                    title=title,
                    local_pdf_path=str(file_path),  # Actually markdown path
                    tags=tags,
                    abstract=clean_text(content[:500]) + "...",
                    ref_type=ReferenceType.WEBPAGE,  # Notes treated as webpage type
                    discovered_from="local_obsidian",
                )
                references.append(note_ref)

            # Extract linked URLs
            if extract_links:
                url_refs = self._extract_urls_as_refs(content, str(file_path))
                references.extend(url_refs)

        except Exception as e:
            self.logger.warning(f"Error reading markdown {file_path}: {e}")

        return references

    async def _process_text(
        self,
        file_path: Path,
        extract_links: bool,
    ) -> list[Reference]:
        """Process a text file.

        Args:
            file_path: Path to text file
            extract_links: Whether to extract URLs

        Returns:
            List of references
        """
        references = []

        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")

            if extract_links:
                url_refs = self._extract_urls_as_refs(content, str(file_path))
                references.extend(url_refs)

        except Exception as e:
            self.logger.warning(f"Error reading text file {file_path}: {e}")

        return references

    def _extract_obsidian_tags(self, content: str) -> list[str]:
        """Extract tags from Obsidian markdown.

        Args:
            content: Markdown content

        Returns:
            List of tags
        """
        import re
        tags = []

        # YAML frontmatter tags
        yaml_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
        if yaml_match:
            yaml_content = yaml_match.group(1)
            tags_match = re.search(r"tags:\s*\[(.*?)\]", yaml_content)
            if tags_match:
                tags.extend([t.strip().strip('"\'') for t in tags_match.group(1).split(",")])
            else:
                # YAML list format
                tags_section = re.search(r"tags:\s*\n((?:\s*-\s*.+\n)+)", yaml_content)
                if tags_section:
                    tag_lines = tags_section.group(1).split("\n")
                    for line in tag_lines:
                        tag = line.strip().lstrip("-").strip()
                        if tag:
                            tags.append(tag)

        # Inline hashtags
        inline_tags = re.findall(r"(?:^|\s)#([a-zA-Z][a-zA-Z0-9_/-]*)", content)
        tags.extend(inline_tags)

        return list(set(tags))

    def _extract_urls_as_refs(
        self,
        content: str,
        source_path: str,
    ) -> list[Reference]:
        """Extract URLs from content and create references.

        Args:
            content: Text content
            source_path: Path of source file

        Returns:
            List of references from URLs
        """
        references = []

        # Try markdown extraction first
        url_tuples = extract_urls_from_markdown(content)

        for url, anchor in url_tuples:
            # Skip internal Obsidian links
            if url.startswith("obsidian://"):
                continue

            arxiv_ids = extract_arxiv_ids(url)
            dois = extract_dois(url)

            # Determine type
            ref_type = ReferenceType.WEBPAGE
            if arxiv_ids or "arxiv.org" in url:
                ref_type = ReferenceType.PREPRINT
            elif dois or "doi.org" in url:
                ref_type = ReferenceType.PAPER
            elif any(x in url for x in ["blog", "medium.com", "substack"]):
                ref_type = ReferenceType.BLOG_POST

            ref = Reference(
                id=self._create_reference_id(url),
                title=anchor if anchor else url,
                url=url,
                arxiv_id=arxiv_ids[0] if arxiv_ids else None,
                doi=dois[0] if dois else None,
                ref_type=ref_type,
                discovered_from=f"extracted_from:{source_path}",
            )
            references.append(ref)

        return references

    async def scan_obsidian_vault(
        self,
        vault_path: Path,
        include_attachments: bool = False,
    ) -> CollectorResult:
        """Scan an Obsidian vault for references.

        Args:
            vault_path: Path to Obsidian vault
            include_attachments: Include PDF attachments

        Returns:
            CollectorResult with found references
        """
        file_types = [".md", ".markdown"]
        if include_attachments:
            file_types.append(".pdf")

        return await self.collect(
            paths=[vault_path],
            file_types=file_types,
            recursive=True,
            extract_links=True,
        )
