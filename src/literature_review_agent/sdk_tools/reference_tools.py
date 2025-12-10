"""
Reference management tools for the Claude Agent SDK.

These tools allow the agent to manage the reference collection:
- Add new references
- Search and filter references
- Update priority and status
- Organize with tags and subtopics
"""

import json
from typing import Any
from pathlib import Path

from claude_code_sdk import tool

from ..models import Reference, ReferenceStatus, Priority, Author, ReferenceType
from ..managers import ReferenceManager


# Global reference manager instance (initialized by server)
_ref_manager: ReferenceManager | None = None


def init_reference_manager(data_dir: Path) -> None:
    """Initialize the reference manager with data directory."""
    global _ref_manager
    _ref_manager = ReferenceManager(data_dir)


def get_ref_manager() -> ReferenceManager:
    """Get the reference manager instance."""
    if _ref_manager is None:
        raise RuntimeError("Reference manager not initialized. Call init_reference_manager first.")
    return _ref_manager


@tool(
    name="add_reference",
    description="Add a new reference to the collection. Use this when you discover a new paper, article, or other source.",
    input_schema={
        "type": "object",
        "properties": {
            "title": {"type": "string", "description": "Title of the reference"},
            "url": {"type": "string", "description": "URL to the reference (optional)"},
            "arxiv_id": {"type": "string", "description": "arXiv ID if applicable (e.g., '2301.07041')"},
            "doi": {"type": "string", "description": "DOI if available"},
            "authors": {
                "type": "array",
                "items": {"type": "string"},
                "description": "List of author names"
            },
            "year": {"type": "integer", "description": "Publication year"},
            "abstract": {"type": "string", "description": "Abstract or summary"},
            "ref_type": {
                "type": "string",
                "enum": ["paper", "article", "blog_post", "book", "preprint", "webpage"],
                "description": "Type of reference"
            },
            "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Tags for categorization"
            },
            "discovered_from": {"type": "string", "description": "How this reference was discovered"}
        },
        "required": ["title"]
    }
)
async def add_reference(args: dict[str, Any]) -> dict:
    """Add a new reference to the collection."""
    manager = get_ref_manager()

    # Create authors list
    authors = []
    if args.get("authors"):
        authors = [Author(name=name) for name in args["authors"]]

    # Map ref_type string to enum
    ref_type_map = {
        "paper": ReferenceType.PAPER,
        "article": ReferenceType.ARTICLE,
        "blog_post": ReferenceType.BLOG_POST,
        "book": ReferenceType.BOOK,
        "preprint": ReferenceType.PREPRINT,
        "webpage": ReferenceType.WEBPAGE,
    }
    ref_type = ref_type_map.get(args.get("ref_type", ""), ReferenceType.UNKNOWN)

    # Generate ID
    import hashlib
    id_source = args["title"] + (args.get("url", "") or args.get("arxiv_id", ""))
    ref_id = hashlib.sha256(id_source.encode()).hexdigest()[:12]

    ref = Reference(
        id=ref_id,
        title=args["title"],
        authors=authors,
        year=args.get("year"),
        url=args.get("url"),
        arxiv_id=args.get("arxiv_id"),
        doi=args.get("doi"),
        abstract=args.get("abstract"),
        ref_type=ref_type,
        tags=args.get("tags", []),
        discovered_from=args.get("discovered_from", "agent_discovery"),
    )

    added_ref, was_new = manager.add(ref)

    status = "added" if was_new else "updated (duplicate found)"
    return {
        "content": [{
            "type": "text",
            "text": f"Reference {status}: '{added_ref.title}' (ID: {added_ref.id})"
        }]
    }


@tool(
    name="search_references",
    description="Search the reference collection by query, tags, status, or priority.",
    input_schema={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query (searches title and abstract)"},
            "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Filter by tags"
            },
            "status": {
                "type": "string",
                "enum": ["discovered", "queued", "reading", "completed", "skipped"],
                "description": "Filter by status"
            },
            "priority": {
                "type": "string",
                "enum": ["critical", "high", "medium", "low", "unknown"],
                "description": "Filter by priority"
            },
            "subtopic": {"type": "string", "description": "Filter by subtopic"},
            "limit": {"type": "integer", "description": "Maximum results to return", "default": 20}
        }
    }
)
async def search_references(args: dict[str, Any]) -> dict:
    """Search references with various filters."""
    manager = get_ref_manager()
    limit = args.get("limit", 20)

    # Start with all references
    refs = manager.get_all()

    # Apply filters
    if args.get("query"):
        refs = manager.search(args["query"])

    if args.get("status"):
        status_map = {
            "discovered": ReferenceStatus.DISCOVERED,
            "queued": ReferenceStatus.QUEUED,
            "reading": ReferenceStatus.READING,
            "completed": ReferenceStatus.COMPLETED,
            "skipped": ReferenceStatus.SKIPPED,
        }
        target_status = status_map.get(args["status"])
        if target_status:
            refs = [r for r in refs if r.status == target_status]

    if args.get("priority"):
        priority_map = {
            "critical": Priority.CRITICAL,
            "high": Priority.HIGH,
            "medium": Priority.MEDIUM,
            "low": Priority.LOW,
            "unknown": Priority.UNKNOWN,
        }
        target_priority = priority_map.get(args["priority"])
        if target_priority:
            refs = [r for r in refs if r.priority == target_priority]

    if args.get("tags"):
        target_tags = set(args["tags"])
        refs = [r for r in refs if target_tags.intersection(r.tags)]

    if args.get("subtopic"):
        refs = [r for r in refs if args["subtopic"] in r.subtopics]

    # Limit results
    refs = refs[:limit]

    # Format output
    if not refs:
        return {"content": [{"type": "text", "text": "No references found matching criteria."}]}

    lines = [f"Found {len(refs)} references:\n"]
    for ref in refs:
        authors_str = ", ".join(a.name for a in ref.authors[:2]) if ref.authors else "Unknown"
        if len(ref.authors) > 2:
            authors_str += " et al."
        year_str = f" ({ref.year})" if ref.year else ""
        lines.append(f"- [{ref.id}] {ref.title} - {authors_str}{year_str}")
        lines.append(f"  Status: {ref.status.value}, Priority: {ref.priority.value}")
        if ref.tags:
            lines.append(f"  Tags: {', '.join(ref.tags)}")

    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="update_reference_priority",
    description="Update the priority of a reference. Use this after evaluating relevance.",
    input_schema={
        "type": "object",
        "properties": {
            "reference_id": {"type": "string", "description": "ID of the reference to update"},
            "priority": {
                "type": "string",
                "enum": ["critical", "high", "medium", "low"],
                "description": "New priority level"
            },
            "explanation": {"type": "string", "description": "Explanation for the priority assignment"}
        },
        "required": ["reference_id", "priority"]
    }
)
async def update_reference_priority(args: dict[str, Any]) -> dict:
    """Update reference priority."""
    manager = get_ref_manager()

    priority_map = {
        "critical": Priority.CRITICAL,
        "high": Priority.HIGH,
        "medium": Priority.MEDIUM,
        "low": Priority.LOW,
    }
    priority = priority_map.get(args["priority"], Priority.MEDIUM)

    updated = manager.update_priority(
        args["reference_id"],
        priority,
        args.get("explanation")
    )

    if updated:
        return {
            "content": [{
                "type": "text",
                "text": f"Updated priority of '{updated.title}' to {priority.value}"
            }]
        }
    return {"content": [{"type": "text", "text": f"Reference {args['reference_id']} not found."}]}


@tool(
    name="update_reference_status",
    description="Update the status of a reference (e.g., mark as queued for reading, completed, etc.)",
    input_schema={
        "type": "object",
        "properties": {
            "reference_id": {"type": "string", "description": "ID of the reference to update"},
            "status": {
                "type": "string",
                "enum": ["discovered", "queued", "reading", "completed", "skipped", "unavailable"],
                "description": "New status"
            }
        },
        "required": ["reference_id", "status"]
    }
)
async def update_reference_status(args: dict[str, Any]) -> dict:
    """Update reference status."""
    manager = get_ref_manager()

    status_map = {
        "discovered": ReferenceStatus.DISCOVERED,
        "queued": ReferenceStatus.QUEUED,
        "reading": ReferenceStatus.READING,
        "completed": ReferenceStatus.COMPLETED,
        "skipped": ReferenceStatus.SKIPPED,
        "unavailable": ReferenceStatus.UNAVAILABLE,
    }
    status = status_map.get(args["status"], ReferenceStatus.DISCOVERED)

    updated = manager.update_status(args["reference_id"], status)

    if updated:
        return {
            "content": [{
                "type": "text",
                "text": f"Updated status of '{updated.title}' to {status.value}"
            }]
        }
    return {"content": [{"type": "text", "text": f"Reference {args['reference_id']} not found."}]}


@tool(
    name="get_reading_queue",
    description="Get the reading queue - references marked for reading, sorted by priority.",
    input_schema={
        "type": "object",
        "properties": {
            "limit": {"type": "integer", "description": "Maximum references to return", "default": 10}
        }
    }
)
async def get_reading_queue(args: dict[str, Any]) -> dict:
    """Get the reading queue."""
    manager = get_ref_manager()
    limit = args.get("limit", 10)

    queue = manager.get_reading_queue()[:limit]

    if not queue:
        return {"content": [{"type": "text", "text": "Reading queue is empty."}]}

    lines = [f"Reading queue ({len(queue)} papers):\n"]
    for i, ref in enumerate(queue, 1):
        authors_str = ref.authors[0].name if ref.authors else "Unknown"
        lines.append(f"{i}. [{ref.priority.value.upper()}] {ref.title}")
        lines.append(f"   ID: {ref.id} | {authors_str}")
        if ref.url or ref.arxiv_id:
            source = ref.arxiv_id or ref.url
            lines.append(f"   Source: {source}")

    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="get_reference_stats",
    description="Get statistics about the reference collection.",
    input_schema={"type": "object", "properties": {}}
)
async def get_reference_stats(args: dict[str, Any]) -> dict:
    """Get reference statistics."""
    manager = get_ref_manager()
    stats = manager.get_statistics()

    lines = [
        "Reference Collection Statistics:",
        f"  Total references: {stats['total']}",
        "",
        "By Status:",
    ]
    for status, count in stats["by_status"].items():
        lines.append(f"  - {status}: {count}")

    lines.append("")
    lines.append("By Priority:")
    for priority, count in stats["by_priority"].items():
        lines.append(f"  - {priority}: {count}")

    lines.append("")
    lines.append(f"With abstract: {stats['with_abstract']}")
    lines.append(f"With PDF available: {stats['with_pdf']}")

    if stats["by_subtopic"]:
        lines.append("")
        lines.append("By Subtopic:")
        for subtopic, count in sorted(stats["by_subtopic"].items(), key=lambda x: -x[1])[:10]:
            lines.append(f"  - {subtopic}: {count}")

    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="add_reference_tag",
    description="Add a tag to a reference for organization.",
    input_schema={
        "type": "object",
        "properties": {
            "reference_id": {"type": "string", "description": "ID of the reference"},
            "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Tags to add"
            }
        },
        "required": ["reference_id", "tags"]
    }
)
async def add_reference_tag(args: dict[str, Any]) -> dict:
    """Add tags to a reference."""
    manager = get_ref_manager()

    updated = manager.add_tags(args["reference_id"], args["tags"])

    if updated:
        return {
            "content": [{
                "type": "text",
                "text": f"Added tags {args['tags']} to '{updated.title}'"
            }]
        }
    return {"content": [{"type": "text", "text": f"Reference {args['reference_id']} not found."}]}


@tool(
    name="assign_subtopic",
    description="Assign a reference to a subtopic.",
    input_schema={
        "type": "object",
        "properties": {
            "reference_id": {"type": "string", "description": "ID of the reference"},
            "subtopic": {"type": "string", "description": "Name of the subtopic to assign"}
        },
        "required": ["reference_id", "subtopic"]
    }
)
async def assign_subtopic(args: dict[str, Any]) -> dict:
    """Assign a reference to a subtopic."""
    manager = get_ref_manager()

    updated = manager.add_subtopic(args["reference_id"], args["subtopic"])

    if updated:
        return {
            "content": [{
                "type": "text",
                "text": f"Assigned '{updated.title}' to subtopic '{args['subtopic']}'"
            }]
        }
    return {"content": [{"type": "text", "text": f"Reference {args['reference_id']} not found."}]}
