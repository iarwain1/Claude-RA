"""
Note management tools for the Claude Agent SDK.

These tools allow the agent to create and manage research notes.
"""

from typing import Any
from pathlib import Path

from claude_code_sdk import tool

from ..managers import NoteManager


# Global note manager instance
_note_manager: NoteManager | None = None


def init_note_manager(data_dir: Path) -> None:
    """Initialize the note manager."""
    global _note_manager
    _note_manager = NoteManager(data_dir)


def get_note_manager() -> NoteManager:
    """Get the note manager instance."""
    if _note_manager is None:
        raise RuntimeError("Note manager not initialized.")
    return _note_manager


@tool(
    name="create_note",
    description="Create a research note for a reference. Use this to record key findings, quotes, questions, or other insights while reading.",
    input_schema={
        "type": "object",
        "properties": {
            "reference_id": {"type": "string", "description": "ID of the reference this note is about"},
            "content": {"type": "string", "description": "The note content"},
            "note_type": {
                "type": "string",
                "enum": ["key_finding", "methodology", "quote", "question", "critique", "connection", "general"],
                "description": "Type of note",
                "default": "general"
            },
            "quote": {"type": "string", "description": "Direct quote from the source (optional)"},
            "section": {"type": "string", "description": "Section of the paper this note is from (optional)"},
            "page_number": {"type": "integer", "description": "Page number (optional)"},
            "tags": {
                "type": "array",
                "items": {"type": "string"},
                "description": "Tags for the note"
            }
        },
        "required": ["reference_id", "content"]
    }
)
async def create_note(args: dict[str, Any]) -> dict:
    """Create a research note."""
    manager = get_note_manager()

    note = manager.create(
        reference_id=args["reference_id"],
        content=args["content"],
        note_type=args.get("note_type", "general"),
        quote=args.get("quote"),
        section=args.get("section"),
        page_number=args.get("page_number"),
        tags=args.get("tags", []),
    )

    return {
        "content": [{
            "type": "text",
            "text": f"Created {note.note_type} note (ID: {note.id}) for reference {args['reference_id']}"
        }]
    }


@tool(
    name="get_notes_for_reference",
    description="Get all notes for a specific reference.",
    input_schema={
        "type": "object",
        "properties": {
            "reference_id": {"type": "string", "description": "ID of the reference"}
        },
        "required": ["reference_id"]
    }
)
async def get_notes_for_reference(args: dict[str, Any]) -> dict:
    """Get notes for a reference."""
    manager = get_note_manager()

    notes = manager.get_for_reference(args["reference_id"])

    if not notes:
        return {"content": [{"type": "text", "text": f"No notes found for reference {args['reference_id']}"}]}

    lines = [f"Notes for reference {args['reference_id']} ({len(notes)} total):\n"]
    for note in notes:
        lines.append(f"[{note.note_type.upper()}] {note.content}")
        if note.quote:
            lines.append(f'  > "{note.quote}"')
        if note.section:
            lines.append(f"  Section: {note.section}")
        if note.tags:
            lines.append(f"  Tags: {', '.join(note.tags)}")
        lines.append("")

    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="search_notes",
    description="Search notes by content.",
    input_schema={
        "type": "object",
        "properties": {
            "query": {"type": "string", "description": "Search query"},
            "note_type": {
                "type": "string",
                "enum": ["key_finding", "methodology", "quote", "question", "critique", "connection", "general"],
                "description": "Filter by note type (optional)"
            }
        },
        "required": ["query"]
    }
)
async def search_notes(args: dict[str, Any]) -> dict:
    """Search notes."""
    manager = get_note_manager()

    notes = manager.search(args["query"])

    if args.get("note_type"):
        notes = [n for n in notes if n.note_type == args["note_type"]]

    if not notes:
        return {"content": [{"type": "text", "text": "No notes found matching query."}]}

    lines = [f"Found {len(notes)} notes:\n"]
    for note in notes[:20]:  # Limit output
        lines.append(f"[{note.note_type}] {note.content[:100]}...")
        lines.append(f"  Reference: {note.reference_id}")
        lines.append("")

    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="get_key_findings",
    description="Get all key finding notes across all references.",
    input_schema={
        "type": "object",
        "properties": {
            "limit": {"type": "integer", "description": "Maximum findings to return", "default": 20}
        }
    }
)
async def get_key_findings(args: dict[str, Any]) -> dict:
    """Get key findings."""
    manager = get_note_manager()
    limit = args.get("limit", 20)

    findings = manager.get_key_findings()[:limit]

    if not findings:
        return {"content": [{"type": "text", "text": "No key findings recorded yet."}]}

    lines = [f"Key Findings ({len(findings)} total):\n"]
    for i, note in enumerate(findings, 1):
        lines.append(f"{i}. {note.content}")
        lines.append(f"   Reference: {note.reference_id}")
        if note.quote:
            lines.append(f'   > "{note.quote[:100]}..."')
        lines.append("")

    return {"content": [{"type": "text", "text": "\n".join(lines)}]}
