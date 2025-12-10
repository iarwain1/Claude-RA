"""
Academic search tools for the Claude Agent SDK.

These tools allow the agent to search academic databases:
- arXiv
- Semantic Scholar
"""

import asyncio
from typing import Any

from claude_code_sdk import tool

from ..collectors import ArxivCollector, SemanticScholarCollector
from .reference_tools import get_ref_manager


# Collector instances
_arxiv_collector: ArxivCollector | None = None
_semantic_scholar: SemanticScholarCollector | None = None


def init_search_tools(arxiv_max: int = 50, s2_max: int = 50) -> None:
    """Initialize search tool collectors."""
    global _arxiv_collector, _semantic_scholar
    _arxiv_collector = ArxivCollector(max_results=arxiv_max)
    _semantic_scholar = SemanticScholarCollector(max_results=s2_max)


def get_arxiv() -> ArxivCollector:
    if _arxiv_collector is None:
        init_search_tools()
    return _arxiv_collector


def get_semantic_scholar() -> SemanticScholarCollector:
    if _semantic_scholar is None:
        init_search_tools()
    return _semantic_scholar


@tool(
    name="search_arxiv",
    description="Search arXiv for academic papers. Returns preprints in AI, ML, CS, and other fields.",
    input_schema={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query"},
            "max_results": {"type": "integer", "description": "Maximum results", "default": 20},
            "categories": {
                "type": "array",
                "items": {"type": "string"},
                "description": "arXiv categories to filter (e.g., 'cs.AI', 'cs.LG', 'cs.CL')"
            },
            "sort_by": {
                "type": "string",
                "enum": ["relevance", "lastUpdatedDate", "submittedDate"],
                "description": "Sort order",
                "default": "relevance"
            },
            "add_to_collection": {
                "type": "boolean",
                "description": "Add found papers to reference collection",
                "default": True
            }
        },
        "required": ["query"]
    }
)
async def search_arxiv(args: dict[str, Any]) -> dict:
    """Search arXiv for papers."""
    collector = get_arxiv()

    result = await collector.search(
        query=args["query"],
        max_results=args.get("max_results", 20),
        categories=args.get("categories"),
        sort_by=args.get("sort_by", "relevance"),
    )

    if result.errors:
        return {"content": [{"type": "text", "text": f"Search error: {result.errors[0]}"}]}

    if not result.references:
        return {"content": [{"type": "text", "text": "No papers found on arXiv for this query."}]}

    # Add to collection if requested
    if args.get("add_to_collection", True):
        manager = get_ref_manager()
        new_count, _ = manager.add_batch(result.references)
        add_msg = f"\nAdded {new_count} new references to collection."
    else:
        add_msg = ""

    # Format results
    lines = [f"Found {len(result.references)} papers on arXiv:\n"]
    for ref in result.references[:15]:  # Limit display
        authors = ref.authors[0].name if ref.authors else "Unknown"
        if len(ref.authors) > 1:
            authors += " et al."
        lines.append(f"- {ref.title}")
        lines.append(f"  {authors} ({ref.year or 'N/A'})")
        lines.append(f"  arXiv: {ref.arxiv_id}")
        if ref.abstract:
            lines.append(f"  {ref.abstract[:150]}...")
        lines.append("")

    lines.append(add_msg)
    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="search_semantic_scholar",
    description="Search Semantic Scholar for academic papers. Good for finding highly-cited papers and getting citation data.",
    input_schema={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query"},
            "max_results": {"type": "integer", "description": "Maximum results", "default": 20},
            "year_from": {"type": "integer", "description": "Minimum publication year"},
            "year_to": {"type": "integer", "description": "Maximum publication year"},
            "fields_of_study": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Fields to filter (e.g., 'Computer Science', 'Medicine')"
            },
            "open_access_only": {
                "type": "boolean",
                "description": "Only return open access papers",
                "default": False
            },
            "add_to_collection": {
                "type": "boolean",
                "description": "Add found papers to reference collection",
                "default": True
            }
        },
        "required": ["query"]
    }
)
async def search_semantic_scholar(args: dict[str, Any]) -> dict:
    """Search Semantic Scholar for papers."""
    collector = get_semantic_scholar()

    result = await collector.search(
        query=args["query"],
        max_results=args.get("max_results", 20),
        year_from=args.get("year_from"),
        year_to=args.get("year_to"),
        fields_of_study=args.get("fields_of_study"),
        open_access_only=args.get("open_access_only", False),
    )

    if result.errors:
        return {"content": [{"type": "text", "text": f"Search error: {result.errors[0]}"}]}

    if not result.references:
        return {"content": [{"type": "text", "text": "No papers found on Semantic Scholar."}]}

    # Add to collection if requested
    if args.get("add_to_collection", True):
        manager = get_ref_manager()
        new_count, _ = manager.add_batch(result.references)
        add_msg = f"\nAdded {new_count} new references to collection."
    else:
        add_msg = ""

    # Format results
    lines = [f"Found {len(result.references)} papers:\n"]
    for ref in result.references[:15]:
        authors = ref.authors[0].name if ref.authors else "Unknown"
        if len(ref.authors) > 1:
            authors += " et al."
        lines.append(f"- {ref.title}")
        lines.append(f"  {authors} ({ref.year or 'N/A'})")
        if ref.venue:
            lines.append(f"  Venue: {ref.venue}")
        if ref.abstract:
            lines.append(f"  {ref.abstract[:150]}...")
        lines.append("")

    lines.append(add_msg)
    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="get_paper_citations",
    description="Get papers that cite a specific paper. Useful for finding follow-up work.",
    input_schema={
        "type": "object",
        "properties": {
            "paper_id": {
                "type": "string",
                "description": "Paper ID (Semantic Scholar ID, DOI, or arXiv ID prefixed with 'ARXIV:')"
            },
            "max_results": {"type": "integer", "description": "Maximum citations to return", "default": 30},
            "add_to_collection": {
                "type": "boolean",
                "description": "Add citing papers to collection",
                "default": True
            }
        },
        "required": ["paper_id"]
    }
)
async def get_paper_citations(args: dict[str, Any]) -> dict:
    """Get papers citing a specific paper."""
    collector = get_semantic_scholar()

    result = await collector.get_citations(
        paper_id=args["paper_id"],
        max_results=args.get("max_results", 30),
    )

    if result.errors:
        return {"content": [{"type": "text", "text": f"Error: {result.errors[0]}"}]}

    if not result.references:
        return {"content": [{"type": "text", "text": "No citing papers found (or couldn't access citation data)."}]}

    # Add to collection
    if args.get("add_to_collection", True):
        manager = get_ref_manager()
        new_count, _ = manager.add_batch(result.references)
        add_msg = f"\nAdded {new_count} new references to collection."
    else:
        add_msg = ""

    lines = [f"Found {len(result.references)} papers citing this work:\n"]
    for ref in result.references[:15]:
        authors = ref.authors[0].name if ref.authors else "Unknown"
        lines.append(f"- {ref.title}")
        lines.append(f"  {authors} ({ref.year or 'N/A'})")
        lines.append("")

    lines.append(add_msg)
    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="get_paper_references",
    description="Get papers referenced/cited by a specific paper. Useful for finding foundational work.",
    input_schema={
        "type": "object",
        "properties": {
            "paper_id": {
                "type": "string",
                "description": "Paper ID (Semantic Scholar ID, DOI, or arXiv ID prefixed with 'ARXIV:')"
            },
            "max_results": {"type": "integer", "description": "Maximum references to return", "default": 30},
            "add_to_collection": {
                "type": "boolean",
                "description": "Add referenced papers to collection",
                "default": True
            }
        },
        "required": ["paper_id"]
    }
)
async def get_paper_references(args: dict[str, Any]) -> dict:
    """Get papers referenced by a specific paper."""
    collector = get_semantic_scholar()

    result = await collector.get_references(
        paper_id=args["paper_id"],
        max_results=args.get("max_results", 30),
    )

    if result.errors:
        return {"content": [{"type": "text", "text": f"Error: {result.errors[0]}"}]}

    if not result.references:
        return {"content": [{"type": "text", "text": "No references found (or couldn't access reference data)."}]}

    # Add to collection
    if args.get("add_to_collection", True):
        manager = get_ref_manager()
        new_count, _ = manager.add_batch(result.references)
        add_msg = f"\nAdded {new_count} new references to collection."
    else:
        add_msg = ""

    lines = [f"Found {len(result.references)} referenced papers:\n"]
    for ref in result.references[:15]:
        authors = ref.authors[0].name if ref.authors else "Unknown"
        lines.append(f"- {ref.title}")
        lines.append(f"  {authors} ({ref.year or 'N/A'})")
        lines.append("")

    lines.append(add_msg)
    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="get_recommendations",
    description="Get paper recommendations based on a set of seed papers. Useful for discovering related work.",
    input_schema={
        "type": "object",
        "properties": {
            "paper_ids": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of seed paper IDs to base recommendations on"
            },
            "max_results": {"type": "integer", "description": "Maximum recommendations", "default": 20},
            "add_to_collection": {
                "type": "boolean",
                "description": "Add recommendations to collection",
                "default": True
            }
        },
        "required": ["paper_ids"]
    }
)
async def get_recommendations(args: dict[str, Any]) -> dict:
    """Get paper recommendations."""
    collector = get_semantic_scholar()

    result = await collector.get_recommended_papers(
        paper_ids=args["paper_ids"],
        max_results=args.get("max_results", 20),
    )

    if result.errors:
        return {"content": [{"type": "text", "text": f"Error: {result.errors[0]}"}]}

    if not result.references:
        return {"content": [{"type": "text", "text": "No recommendations found."}]}

    # Add to collection
    if args.get("add_to_collection", True):
        manager = get_ref_manager()
        new_count, _ = manager.add_batch(result.references)
        add_msg = f"\nAdded {new_count} new references to collection."
    else:
        add_msg = ""

    lines = [f"Found {len(result.references)} recommended papers:\n"]
    for ref in result.references[:15]:
        authors = ref.authors[0].name if ref.authors else "Unknown"
        lines.append(f"- {ref.title}")
        lines.append(f"  {authors} ({ref.year or 'N/A'})")
        lines.append("")

    lines.append(add_msg)
    return {"content": [{"type": "text", "text": "\n".join(lines)}]}
