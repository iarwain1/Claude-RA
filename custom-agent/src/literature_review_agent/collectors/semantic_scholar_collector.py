"""Collector for Semantic Scholar papers and citations."""

import asyncio
from typing import Optional

from semanticscholar import SemanticScholar

from .base import BaseCollector, CollectorResult
from ..models import Reference, ReferenceType, Author


class SemanticScholarCollector(BaseCollector):
    """Collector for Semantic Scholar papers and citation data."""

    def __init__(self, max_results: int = 50, api_key: Optional[str] = None):
        super().__init__("semantic_scholar")
        self.max_results = max_results
        self.api_key = api_key
        self._client: Optional[SemanticScholar] = None

    @property
    def client(self) -> SemanticScholar:
        """Get or create Semantic Scholar client."""
        if self._client is None:
            self._client = SemanticScholar(api_key=self.api_key) if self.api_key else SemanticScholar()
        return self._client

    async def collect(
        self,
        paper_ids: Optional[list[str]] = None,
        dois: Optional[list[str]] = None,
        arxiv_ids: Optional[list[str]] = None,
        **kwargs,
    ) -> CollectorResult:
        """Collect references by various IDs.

        Args:
            paper_ids: Semantic Scholar paper IDs
            dois: DOIs
            arxiv_ids: arXiv IDs

        Returns:
            CollectorResult with found references
        """
        result = CollectorResult()
        all_ids = []

        if paper_ids:
            all_ids.extend(paper_ids)
        if dois:
            all_ids.extend([f"DOI:{doi}" for doi in dois])
        if arxiv_ids:
            all_ids.extend([f"ARXIV:{aid}" for aid in arxiv_ids])

        if not all_ids:
            return CollectorResult(warnings=["No paper IDs provided"])

        for paper_id in all_ids:
            try:
                loop = asyncio.get_event_loop()
                paper = await loop.run_in_executor(
                    None,
                    lambda pid=paper_id: self.client.get_paper(pid)
                )
                if paper:
                    ref = self._paper_to_reference(paper)
                    result.references.append(ref)
            except Exception as e:
                result.warnings.append(f"Could not fetch {paper_id}: {e}")

        return result

    async def search(
        self,
        query: str,
        max_results: Optional[int] = None,
        year_from: Optional[int] = None,
        year_to: Optional[int] = None,
        fields_of_study: Optional[list[str]] = None,
        open_access_only: bool = False,
        **kwargs,
    ) -> CollectorResult:
        """Search Semantic Scholar for papers.

        Args:
            query: Search query
            max_results: Maximum number of results
            year_from: Start year for filtering
            year_to: End year for filtering
            fields_of_study: Fields to filter by (e.g., ["Computer Science"])
            open_access_only: Only return open access papers

        Returns:
            CollectorResult with matching references
        """
        result = CollectorResult()
        max_results = max_results or self.max_results

        self.logger.info(f"Searching Semantic Scholar: '{query}' (max {max_results})")

        try:
            # Build year filter
            year = None
            if year_from and year_to:
                year = f"{year_from}-{year_to}"
            elif year_from:
                year = f"{year_from}-"
            elif year_to:
                year = f"-{year_to}"

            loop = asyncio.get_event_loop()
            papers = await loop.run_in_executor(
                None,
                lambda: self.client.search_paper(
                    query,
                    limit=max_results,
                    year=year,
                    fields_of_study=fields_of_study,
                    open_access_pdf=open_access_only if open_access_only else None,
                )
            )

            for paper in papers:
                ref = self._paper_to_reference(paper)
                result.references.append(ref)

            self.logger.info(f"Found {len(result.references)} papers on Semantic Scholar")

        except Exception as e:
            result.errors.append(f"Semantic Scholar search error: {e}")
            self.logger.error(f"Search error: {e}")

        return result

    async def get_citations(
        self,
        paper_id: str,
        max_results: int = 100,
    ) -> CollectorResult:
        """Get papers that cite a given paper.

        Args:
            paper_id: Semantic Scholar paper ID, DOI, or arXiv ID
            max_results: Maximum number of citations to fetch

        Returns:
            CollectorResult with citing references
        """
        result = CollectorResult()

        self.logger.info(f"Fetching citations for {paper_id}")

        try:
            loop = asyncio.get_event_loop()
            paper = await loop.run_in_executor(
                None,
                lambda: self.client.get_paper(paper_id)
            )

            if not paper:
                result.errors.append(f"Paper not found: {paper_id}")
                return result

            citations = await loop.run_in_executor(
                None,
                lambda: self.client.get_paper_citations(paper_id, limit=max_results)
            )

            for citation in citations:
                if citation.citingPaper:
                    ref = self._paper_to_reference(citation.citingPaper)
                    ref.cites = [paper_id]
                    ref.discovered_from = f"citation_of_{paper_id}"
                    result.references.append(ref)

            self.logger.info(f"Found {len(result.references)} papers citing {paper_id}")

        except Exception as e:
            result.errors.append(f"Error fetching citations: {e}")
            self.logger.error(f"Citation fetch error: {e}")

        return result

    async def get_references(
        self,
        paper_id: str,
        max_results: int = 100,
    ) -> CollectorResult:
        """Get papers referenced by a given paper.

        Args:
            paper_id: Semantic Scholar paper ID, DOI, or arXiv ID
            max_results: Maximum number of references to fetch

        Returns:
            CollectorResult with referenced papers
        """
        result = CollectorResult()

        self.logger.info(f"Fetching references from {paper_id}")

        try:
            loop = asyncio.get_event_loop()
            references = await loop.run_in_executor(
                None,
                lambda: self.client.get_paper_references(paper_id, limit=max_results)
            )

            for ref_item in references:
                if ref_item.citedPaper:
                    ref = self._paper_to_reference(ref_item.citedPaper)
                    ref.cited_by = [paper_id]
                    ref.discovered_from = f"reference_in_{paper_id}"
                    result.references.append(ref)

            self.logger.info(f"Found {len(result.references)} references in {paper_id}")

        except Exception as e:
            result.errors.append(f"Error fetching references: {e}")
            self.logger.error(f"Reference fetch error: {e}")

        return result

    async def get_recommended_papers(
        self,
        paper_ids: list[str],
        max_results: int = 20,
    ) -> CollectorResult:
        """Get paper recommendations based on seed papers.

        Args:
            paper_ids: List of seed paper IDs
            max_results: Maximum number of recommendations

        Returns:
            CollectorResult with recommended papers
        """
        result = CollectorResult()

        self.logger.info(f"Getting recommendations based on {len(paper_ids)} papers")

        try:
            loop = asyncio.get_event_loop()
            recommendations = await loop.run_in_executor(
                None,
                lambda: self.client.get_recommended_papers(
                    positive_paper_ids=paper_ids,
                    limit=max_results,
                )
            )

            for paper in recommendations:
                ref = self._paper_to_reference(paper)
                ref.discovered_from = "semantic_scholar_recommendation"
                result.references.append(ref)

            self.logger.info(f"Got {len(result.references)} recommendations")

        except Exception as e:
            result.errors.append(f"Error getting recommendations: {e}")
            self.logger.error(f"Recommendation error: {e}")

        return result

    def _paper_to_reference(self, paper) -> Reference:
        """Convert Semantic Scholar paper to Reference.

        Args:
            paper: Semantic Scholar paper object

        Returns:
            Reference object
        """
        # Extract authors
        authors = []
        if hasattr(paper, 'authors') and paper.authors:
            for author in paper.authors:
                if hasattr(author, 'name') and author.name:
                    authors.append(Author(name=author.name))

        # Extract arXiv ID if present
        arxiv_id = None
        if hasattr(paper, 'externalIds') and paper.externalIds:
            arxiv_id = paper.externalIds.get('ArXiv')

        # Extract DOI
        doi = None
        if hasattr(paper, 'externalIds') and paper.externalIds:
            doi = paper.externalIds.get('DOI')

        # Get PDF URL if available
        pdf_url = None
        if hasattr(paper, 'openAccessPdf') and paper.openAccessPdf:
            pdf_url = paper.openAccessPdf.get('url')

        # Get venue
        venue = None
        if hasattr(paper, 'venue') and paper.venue:
            venue = paper.venue
        elif hasattr(paper, 'journal') and paper.journal:
            venue = paper.journal.get('name') if isinstance(paper.journal, dict) else str(paper.journal)

        # Get year
        year = None
        if hasattr(paper, 'year') and paper.year:
            year = paper.year

        # Get citation count for prioritization
        citation_count = getattr(paper, 'citationCount', 0) or 0

        # Determine reference type
        ref_type = ReferenceType.PAPER
        if arxiv_id:
            ref_type = ReferenceType.PREPRINT

        return Reference(
            id=self._create_reference_id("s2", paper.paperId if hasattr(paper, 'paperId') else str(paper)),
            title=paper.title if hasattr(paper, 'title') else "Unknown",
            authors=authors,
            year=year,
            url=f"https://www.semanticscholar.org/paper/{paper.paperId}" if hasattr(paper, 'paperId') else None,
            doi=doi,
            arxiv_id=arxiv_id,
            semantic_scholar_id=paper.paperId if hasattr(paper, 'paperId') else None,
            pdf_url=pdf_url,
            abstract=paper.abstract if hasattr(paper, 'abstract') else None,
            ref_type=ref_type,
            venue=venue,
            discovered_from="semantic_scholar",
        )
