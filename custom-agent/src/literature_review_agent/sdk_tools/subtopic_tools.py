"""
Subtopic management tools for the Claude Agent SDK.

These tools allow the agent to organize research by subtopics.
"""

from typing import Any
from pathlib import Path

from claude_code_sdk import tool

from ..models import Priority
from ..managers import SubtopicManager


# Global subtopic manager
_subtopic_manager: SubtopicManager | None = None


def init_subtopic_manager(data_dir: Path) -> None:
    """Initialize the subtopic manager."""
    global _subtopic_manager
    _subtopic_manager = SubtopicManager(data_dir)


def get_subtopic_manager() -> SubtopicManager:
    """Get the subtopic manager instance."""
    if _subtopic_manager is None:
        raise RuntimeError("Subtopic manager not initialized.")
    return _subtopic_manager


@tool(
    name="create_subtopic",
    description="Create a new subtopic for organizing the literature review.",
    input_schema={
        "type": "object",
        "properties": {
            "name": {"type": "string", "description": "Name of the subtopic"},
            "description": {"type": "string", "description": "Description of what this subtopic covers"},
            "parent": {"type": "string", "description": "Parent subtopic name (for nested organization)"},
            "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Key terms/tags for this subtopic"
            },
            "priority": {
                "type": "string",
                "enum": ["critical", "high", "medium", "low"],
                "description": "Priority of this subtopic",
                "default": "medium"
            }
        },
        "required": ["name", "description"]
    }
)
async def create_subtopic(args: dict[str, Any]) -> dict:
    """Create a new subtopic."""
    manager = get_subtopic_manager()

    # Check if parent exists
    parent_id = None
    if args.get("parent"):
        parent = manager.get_by_name(args["parent"])
        if parent:
            parent_id = parent.id

    priority_map = {
        "critical": Priority.CRITICAL,
        "high": Priority.HIGH,
        "medium": Priority.MEDIUM,
        "low": Priority.LOW,
    }
    priority = priority_map.get(args.get("priority", "medium"), Priority.MEDIUM)

    subtopic = manager.create(
        name=args["name"],
        description=args["description"],
        parent_id=parent_id,
        tags=args.get("tags", []),
        priority=priority,
    )

    return {
        "content": [{
            "type": "text",
            "text": f"Created subtopic '{subtopic.name}' (ID: {subtopic.id})"
        }]
    }


@tool(
    name="list_subtopics",
    description="List all subtopics in the research project.",
    input_schema={
        "type": "object",
        "properties": {
            "include_stats": {
                "type": "boolean",
                "description": "Include statistics for each subtopic",
                "default": True
            }
        }
    }
)
async def list_subtopics(args: dict[str, Any]) -> dict:
    """List all subtopics."""
    manager = get_subtopic_manager()

    subtopics = manager.get_all()

    if not subtopics:
        return {"content": [{"type": "text", "text": "No subtopics defined yet."}]}

    lines = [f"Subtopics ({len(subtopics)} total):\n"]

    # Group by parent
    root_subtopics = [st for st in subtopics if st.parent_id is None]

    for st in root_subtopics:
        lines.append(f"[{st.priority.value.upper()}] {st.name}")
        lines.append(f"  {st.description}")
        if args.get("include_stats", True):
            lines.append(f"  References: {len(st.reference_ids)}, Findings: {len(st.key_findings)}")
        if st.tags:
            lines.append(f"  Tags: {', '.join(st.tags)}")

        # Show children
        children = manager.get_children(st.id)
        for child in children:
            lines.append(f"  └─ {child.name}")
            lines.append(f"     {child.description}")

        lines.append("")

    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="add_subtopic_finding",
    description="Add a key finding to a subtopic.",
    input_schema={
        "type": "object",
        "properties": {
            "subtopic_name": {"type": "string", "description": "Name of the subtopic"},
            "finding": {"type": "string", "description": "The key finding to record"}
        },
        "required": ["subtopic_name", "finding"]
    }
)
async def add_subtopic_finding(args: dict[str, Any]) -> dict:
    """Add a key finding to a subtopic."""
    manager = get_subtopic_manager()

    subtopic = manager.get_by_name(args["subtopic_name"])
    if not subtopic:
        return {"content": [{"type": "text", "text": f"Subtopic '{args['subtopic_name']}' not found."}]}

    updated = manager.add_key_finding(subtopic.id, args["finding"])

    return {
        "content": [{
            "type": "text",
            "text": f"Added finding to '{updated.name}'. Total findings: {len(updated.key_findings)}"
        }]
    }


@tool(
    name="add_subtopic_question",
    description="Add an open question to a subtopic (for future research).",
    input_schema={
        "type": "object",
        "properties": {
            "subtopic_name": {"type": "string", "description": "Name of the subtopic"},
            "question": {"type": "string", "description": "The open question to record"}
        },
        "required": ["subtopic_name", "question"]
    }
)
async def add_subtopic_question(args: dict[str, Any]) -> dict:
    """Add an open question to a subtopic."""
    manager = get_subtopic_manager()

    subtopic = manager.get_by_name(args["subtopic_name"])
    if not subtopic:
        return {"content": [{"type": "text", "text": f"Subtopic '{args['subtopic_name']}' not found."}]}

    updated = manager.add_question(subtopic.id, args["question"])

    return {
        "content": [{
            "type": "text",
            "text": f"Added question to '{updated.name}'. Total questions: {len(updated.open_questions)}"
        }]
    }


@tool(
    name="set_subtopic_summary",
    description="Set or update the summary for a subtopic.",
    input_schema={
        "type": "object",
        "properties": {
            "subtopic_name": {"type": "string", "description": "Name of the subtopic"},
            "summary": {"type": "string", "description": "Summary text for the subtopic"}
        },
        "required": ["subtopic_name", "summary"]
    }
)
async def set_subtopic_summary(args: dict[str, Any]) -> dict:
    """Set the summary for a subtopic."""
    manager = get_subtopic_manager()

    subtopic = manager.get_by_name(args["subtopic_name"])
    if not subtopic:
        return {"content": [{"type": "text", "text": f"Subtopic '{args['subtopic_name']}' not found."}]}

    manager.set_summary(subtopic.id, args["summary"])

    return {
        "content": [{
            "type": "text",
            "text": f"Updated summary for '{subtopic.name}'"
        }]
    }
