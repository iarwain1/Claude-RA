"""
Report generation tools for the Claude Agent SDK.

These tools allow the agent to generate various reports and exports.
"""

from datetime import datetime
from pathlib import Path
from typing import Any

from claude_code_sdk import tool

from ..models import ReferenceStatus, Priority
from ..utils.persistence import export_to_bibtex, export_to_markdown
from .reference_tools import get_ref_manager
from .note_tools import get_note_manager
from .subtopic_tools import get_subtopic_manager


# Output directory
_output_dir: Path | None = None


def init_report_tools(output_dir: Path) -> None:
    """Initialize report tools with output directory."""
    global _output_dir
    _output_dir = output_dir
    _output_dir.mkdir(parents=True, exist_ok=True)


def get_output_dir() -> Path:
    """Get the output directory."""
    if _output_dir is None:
        return Path("output")
    return _output_dir


@tool(
    name="generate_progress_report",
    description="Generate a progress report showing current status of the literature review.",
    input_schema={
        "type": "object",
        "properties": {
            "include_recent": {
                "type": "boolean",
                "description": "Include recently added references",
                "default": True
            },
            "include_findings": {
                "type": "boolean",
                "description": "Include key findings",
                "default": True
            }
        }
    }
)
async def generate_progress_report(args: dict[str, Any]) -> dict:
    """Generate a progress report."""
    ref_manager = get_ref_manager()
    note_manager = get_note_manager()
    subtopic_manager = get_subtopic_manager()

    ref_stats = ref_manager.get_statistics()
    note_stats = note_manager.get_statistics()
    subtopic_stats = subtopic_manager.get_statistics()

    lines = [
        "# Literature Review Progress Report",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        "## Reference Statistics",
        f"- Total references: {ref_stats['total']}",
        "",
        "### By Status:",
    ]

    for status, count in ref_stats["by_status"].items():
        if count > 0:
            lines.append(f"  - {status}: {count}")

    lines.extend([
        "",
        "### By Priority:",
    ])
    for priority, count in ref_stats["by_priority"].items():
        if count > 0:
            lines.append(f"  - {priority}: {count}")

    lines.extend([
        "",
        "## Notes",
        f"- Total notes: {note_stats['total']}",
        f"- References with notes: {note_stats['references_with_notes']}",
    ])

    if note_stats["by_type"]:
        lines.append("")
        lines.append("### By Type:")
        for note_type, count in note_stats["by_type"].items():
            lines.append(f"  - {note_type}: {count}")

    lines.extend([
        "",
        "## Subtopics",
        f"- Total subtopics: {subtopic_stats['total']}",
        f"- Key findings recorded: {subtopic_stats['total_findings']}",
        f"- Open questions: {subtopic_stats['total_questions']}",
    ])

    # Recent references
    if args.get("include_recent", True):
        refs = ref_manager.get_all()
        recent = sorted(refs, key=lambda r: r.discovered_at, reverse=True)[:5]
        if recent:
            lines.extend([
                "",
                "## Recently Added References",
            ])
            for ref in recent:
                lines.append(f"- {ref.title[:60]}...")

    # Key findings
    if args.get("include_findings", True):
        findings = note_manager.get_key_findings()[:5]
        if findings:
            lines.extend([
                "",
                "## Recent Key Findings",
            ])
            for finding in findings:
                lines.append(f"- {finding.content[:100]}...")

    # Reading queue status
    queue = ref_manager.get_reading_queue()
    if queue:
        lines.extend([
            "",
            f"## Reading Queue: {len(queue)} papers waiting",
            "Top 3 in queue:",
        ])
        for ref in queue[:3]:
            lines.append(f"- [{ref.priority.value}] {ref.title[:50]}...")

    return {"content": [{"type": "text", "text": "\n".join(lines)}]}


@tool(
    name="export_references_bibtex",
    description="Export all references to BibTeX format for use in academic writing.",
    input_schema={
        "type": "object",
        "properties": {
            "filename": {
                "type": "string",
                "description": "Output filename (default: references.bib)",
                "default": "references.bib"
            },
            "completed_only": {
                "type": "boolean",
                "description": "Only export completed (read) references",
                "default": False
            }
        }
    }
)
async def export_references_bibtex(args: dict[str, Any]) -> dict:
    """Export references to BibTeX."""
    manager = get_ref_manager()

    refs = manager.get_all()
    if args.get("completed_only", False):
        refs = [r for r in refs if r.status == ReferenceStatus.COMPLETED]

    if not refs:
        return {"content": [{"type": "text", "text": "No references to export."}]}

    output_path = get_output_dir() / args.get("filename", "references.bib")
    export_to_bibtex(refs, output_path)

    return {
        "content": [{
            "type": "text",
            "text": f"Exported {len(refs)} references to {output_path}"
        }]
    }


@tool(
    name="export_references_markdown",
    description="Export references and notes to a markdown file.",
    input_schema={
        "type": "object",
        "properties": {
            "filename": {
                "type": "string",
                "description": "Output filename (default: literature_export.md)",
                "default": "literature_export.md"
            },
            "include_notes": {
                "type": "boolean",
                "description": "Include notes for each reference",
                "default": True
            },
            "group_by_subtopic": {
                "type": "boolean",
                "description": "Group references by subtopic",
                "default": True
            }
        }
    }
)
async def export_references_markdown(args: dict[str, Any]) -> dict:
    """Export references to markdown."""
    ref_manager = get_ref_manager()
    note_manager = get_note_manager()

    refs = ref_manager.get_all()
    notes = note_manager.get_all() if args.get("include_notes", True) else []

    if not refs:
        return {"content": [{"type": "text", "text": "No references to export."}]}

    output_path = get_output_dir() / args.get("filename", "literature_export.md")
    export_to_markdown(refs, notes, output_path)

    return {
        "content": [{
            "type": "text",
            "text": f"Exported {len(refs)} references (with {len(notes)} notes) to {output_path}"
        }]
    }
