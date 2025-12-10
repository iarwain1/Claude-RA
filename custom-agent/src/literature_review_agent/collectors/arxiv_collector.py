"""Collector for arXiv papers."""

import asyncio
from datetime import datetime
from typing import Optional

import arxiv

from .base import BaseCollector, CollectorResult
from ..models import Reference, ReferenceType, Author, Priority


class ArxivCollector(BaseCollector):
    """Collector for arXiv papers."""

    def __init__(self, max_results: int = 50):
        super().__init__("arxiv")
        self.max_results = max_results

    async def collect(
        self,
        arxiv_ids: Optional[list[str]] = None,
        **kwargs,
    ) -> CollectorResult:
        """Collect references by arXiv IDs.

        Args:
            arxiv_ids: List of arXiv IDs to fetch

        Returns:
            CollectorResult with found references
        """
        if not arxiv_ids:
            return CollectorResult(warnings=["No arXiv IDs provided"])

        result = CollectorResult()

        try:
            # arXiv library is synchronous, run in executor
            loop = asyncio.get_event_loop()
            papers = await loop.run_in_executor(
                None,
                lambda: list(arxiv.Client().results(arxiv.Search(id_list=arxiv_ids)))
            )

            for paper in papers:
                ref = self._paper_to_reference(paper)
                result.references.append(ref)

            self.logger.info(f"Fetched {len(result.references)} papers from arXiv")

        except Exception as e:
            result.errors.append(f"Error fetching from arXiv: {e}")
            self.logger.error(f"arXiv error: {e}")

        return result

    async def search(
        self,
        query: str,
        max_results: Optional[int] = None,
        sort_by: str = "relevance",
        categories: Optional[list[str]] = None,
        date_from: Optional[datetime] = None,
        date_to: Optional[datetime] = None,
        **kwargs,
    ) -> CollectorResult:
        """Search arXiv for papers.

        Args:
            query: Search query
            max_results: Maximum number of results
            sort_by: Sort order ("relevance", "lastUpdatedDate", "submittedDate")
            categories: arXiv categories to filter by (e.g., ["cs.AI", "cs.LG"])
            date_from: Start date for filtering
            date_to: End date for filtering

        Returns:
            CollectorResult with matching references
        """
        result = CollectorResult()
        max_results = max_results or self.max_results

        # Build query
        search_query = query
        if categories:
            cat_query = " OR ".join(f"cat:{cat}" for cat in categories)
            search_query = f"({query}) AND ({cat_query})"

        # Map sort options
        sort_map = {
            "relevance": arxiv.SortCriterion.Relevance,
            "lastUpdatedDate": arxiv.SortCriterion.LastUpdatedDate,
            "submittedDate": arxiv.SortCriterion.SubmittedDate,
        }
        sort_criterion = sort_map.get(sort_by, arxiv.SortCriterion.Relevance)

        self.logger.info(f"Searching arXiv: '{search_query}' (max {max_results})")

        try:
            search = arxiv.Search(
                query=search_query,
                max_results=max_results,
                sort_by=sort_criterion,
            )

            # Run synchronous arXiv client in executor
            loop = asyncio.get_event_loop()
            papers = await loop.run_in_executor(
                None,
                lambda: list(arxiv.Client().results(search))
            )

            for paper in papers:
                # Date filtering
                if date_from and paper.published < date_from:
                    continue
                if date_to and paper.published > date_to:
                    continue

                ref = self._paper_to_reference(paper)
                result.references.append(ref)

            self.logger.info(f"Found {len(result.references)} papers on arXiv")
            result.metadata["total_results"] = len(result.references)

        except Exception as e:
            result.errors.append(f"arXiv search error: {e}")
            self.logger.error(f"arXiv search error: {e}")

        return result

    async def get_citations(self, arxiv_id: str) -> CollectorResult:
        """Get papers that cite a given arXiv paper.

        Note: arXiv doesn't provide citation info directly.
        This returns an empty result - use SemanticScholarCollector for citations.

        Args:
            arxiv_id: arXiv ID

        Returns:
            CollectorResult (empty, with warning)
        """
        return CollectorResult(
            warnings=["arXiv doesn't provide citation data. Use Semantic Scholar instead."]
        )

    async def get_references(self, arxiv_id: str) -> CollectorResult:
        """Get papers referenced by a given arXiv paper.

        Note: arXiv doesn't provide reference info directly.
        This returns an empty result - use SemanticScholarCollector for references.

        Args:
            arxiv_id: arXiv ID

        Returns:
            CollectorResult (empty, with warning)
        """
        return CollectorResult(
            warnings=["arXiv doesn't provide reference data. Use Semantic Scholar instead."]
        )

    def _paper_to_reference(self, paper: arxiv.Result) -> Reference:
        """Convert arXiv Result to Reference.

        Args:
            paper: arXiv paper result

        Returns:
            Reference object
        """
        # Extract arXiv ID from entry_id
        arxiv_id = paper.entry_id.split("/")[-1]
        if "v" in arxiv_id:
            arxiv_id = arxiv_id.split("v")[0]

        authors = [
            Author(name=author.name)
            for author in paper.authors
        ]

        # Extract categories as tags
        tags = list(paper.categories) if paper.categories else []

        return Reference(
            id=self._create_reference_id("arxiv", arxiv_id),
            title=paper.title,
            authors=authors,
            year=paper.published.year if paper.published else None,
            url=paper.entry_id,
            arxiv_id=arxiv_id,
            doi=paper.doi,
            pdf_url=paper.pdf_url,
            abstract=paper.summary,
            ref_type=ReferenceType.PREPRINT,
            venue="arXiv",
            tags=tags,
            discovered_from="arxiv_search",
        )

    async def search_by_author(self, author_name: str, **kwargs) -> CollectorResult:
        """Search for papers by a specific author.

        Args:
            author_name: Author name to search for

        Returns:
            CollectorResult with matching references
        """
        query = f'au:"{author_name}"'
        return await self.search(query, **kwargs)

    async def search_similar(
        self,
        arxiv_id: str,
        max_results: int = 20,
    ) -> CollectorResult:
        """Find papers similar to a given arXiv paper.

        This searches using the paper's title and key terms from abstract.

        Args:
            arxiv_id: arXiv ID of the seed paper
            max_results: Maximum number of results

        Returns:
            CollectorResult with similar references
        """
        # First fetch the seed paper
        seed_result = await self.collect(arxiv_ids=[arxiv_id])
        if not seed_result.references:
            return CollectorResult(errors=[f"Could not fetch paper {arxiv_id}"])

        seed = seed_result.references[0]

        # Search using title
        query = seed.title
        result = await self.search(query, max_results=max_results)

        # Filter out the seed paper itself
        result.references = [
            ref for ref in result.references
            if ref.arxiv_id != arxiv_id
        ]

        return result
