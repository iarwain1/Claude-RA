"""Persistence utilities for saving and loading project state."""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional

from ..models import ResearchProject, Reference, Note


class DateTimeEncoder(json.JSONEncoder):
    """JSON encoder that handles datetime objects."""

    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        if isinstance(obj, Path):
            return str(obj)
        return super().default(obj)


def save_project(project: ResearchProject, path: Path) -> None:
    """Save a research project to disk.

    Args:
        project: Project to save
        path: Directory to save to
    """
    path.mkdir(parents=True, exist_ok=True)

    # Save project metadata
    project_data = project.model_dump(mode="json")
    with open(path / "project.json", "w") as f:
        json.dump(project_data, f, indent=2, cls=DateTimeEncoder)


def load_project(path: Path) -> Optional[ResearchProject]:
    """Load a research project from disk.

    Args:
        path: Directory to load from

    Returns:
        Loaded project or None if not found
    """
    project_file = path / "project.json"
    if not project_file.exists():
        return None

    with open(project_file) as f:
        data = json.load(f)

    return ResearchProject(**data)


def save_references(references: list[Reference], path: Path) -> None:
    """Save references to disk.

    Args:
        references: List of references to save
        path: File path to save to
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    data = [ref.model_dump(mode="json") for ref in references]
    with open(path, "w") as f:
        json.dump(data, f, indent=2, cls=DateTimeEncoder)


def load_references(path: Path) -> list[Reference]:
    """Load references from disk.

    Args:
        path: File path to load from

    Returns:
        List of references
    """
    if not path.exists():
        return []

    with open(path) as f:
        data = json.load(f)

    return [Reference(**ref) for ref in data]


def save_notes(notes: list[Note], path: Path) -> None:
    """Save notes to disk.

    Args:
        notes: List of notes to save
        path: File path to save to
    """
    path.parent.mkdir(parents=True, exist_ok=True)

    data = [note.model_dump(mode="json") for note in notes]
    with open(path, "w") as f:
        json.dump(data, f, indent=2, cls=DateTimeEncoder)


def load_notes(path: Path) -> list[Note]:
    """Load notes from disk.

    Args:
        path: File path to load from

    Returns:
        List of notes
    """
    if not path.exists():
        return []

    with open(path) as f:
        data = json.load(f)

    return [Note(**note) for note in data]


def export_to_markdown(
    references: list[Reference],
    notes: list[Note],
    output_path: Path,
) -> None:
    """Export references and notes to markdown format.

    Args:
        references: List of references
        notes: List of notes
        output_path: Path to output markdown file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    lines = ["# Literature Review Export\n"]
    lines.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n")

    # Group references by subtopic
    by_subtopic: dict[str, list[Reference]] = {}
    for ref in references:
        for subtopic in ref.subtopics or ["Uncategorized"]:
            if subtopic not in by_subtopic:
                by_subtopic[subtopic] = []
            by_subtopic[subtopic].append(ref)

    for subtopic, refs in sorted(by_subtopic.items()):
        lines.append(f"## {subtopic}\n\n")

        for ref in sorted(refs, key=lambda r: r.priority.value if r.priority else "z"):
            # Reference header
            authors_str = ", ".join(a.name for a in ref.authors[:3])
            if len(ref.authors) > 3:
                authors_str += " et al."

            lines.append(f"### {ref.title}\n")
            if authors_str:
                lines.append(f"*{authors_str}*")
                if ref.year:
                    lines.append(f" ({ref.year})")
                lines.append("\n\n")

            # Links
            if ref.url:
                lines.append(f"- URL: {ref.url}\n")
            if ref.arxiv_id:
                lines.append(f"- arXiv: [{ref.arxiv_id}](https://arxiv.org/abs/{ref.arxiv_id})\n")
            if ref.doi:
                lines.append(f"- DOI: [{ref.doi}](https://doi.org/{ref.doi})\n")

            # Metadata
            lines.append(f"- Priority: {ref.priority}\n")
            lines.append(f"- Status: {ref.status}\n")
            if ref.tags:
                lines.append(f"- Tags: {', '.join(ref.tags)}\n")

            # Abstract
            if ref.abstract:
                lines.append(f"\n**Abstract:** {ref.abstract[:500]}...\n" if len(ref.abstract) > 500 else f"\n**Abstract:** {ref.abstract}\n")

            # Notes for this reference
            ref_notes = [n for n in notes if n.reference_id == ref.id]
            if ref_notes:
                lines.append("\n**Notes:**\n")
                for note in ref_notes:
                    lines.append(f"- {note.content}\n")
                    if note.quote:
                        lines.append(f"  > \"{note.quote}\"\n")

            lines.append("\n---\n\n")

    with open(output_path, "w") as f:
        f.writelines(lines)


def export_to_bibtex(references: list[Reference], output_path: Path) -> None:
    """Export references to BibTeX format.

    Args:
        references: List of references
        output_path: Path to output .bib file
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    entries = []
    for ref in references:
        # Generate citation key
        first_author = ref.authors[0].name.split()[-1] if ref.authors else "unknown"
        year = ref.year or "nd"
        title_word = ref.title.split()[0].lower() if ref.title else "untitled"
        cite_key = f"{first_author.lower()}{year}{title_word}"

        # Determine entry type
        entry_type = {
            "paper": "article",
            "preprint": "article",
            "book": "book",
            "book_chapter": "inbook",
            "thesis": "phdthesis",
            "article": "article",
        }.get(ref.ref_type, "misc")

        entry = [f"@{entry_type}{{{cite_key},"]
        entry.append(f'  title = {{{ref.title}}},')

        if ref.authors:
            authors = " and ".join(a.name for a in ref.authors)
            entry.append(f'  author = {{{authors}}},')

        if ref.year:
            entry.append(f'  year = {{{ref.year}}},')

        if ref.venue:
            entry.append(f'  journal = {{{ref.venue}}},')

        if ref.doi:
            entry.append(f'  doi = {{{ref.doi}}},')

        if ref.url:
            entry.append(f'  url = {{{ref.url}}},')

        if ref.arxiv_id:
            entry.append(f'  eprint = {{{ref.arxiv_id}}},')
            entry.append('  archivePrefix = {arXiv},')

        if ref.abstract:
            abstract = ref.abstract.replace('{', '\\{').replace('}', '\\}')
            entry.append(f'  abstract = {{{abstract}}},')

        entry.append("}")
        entries.append("\n".join(entry))

    with open(output_path, "w") as f:
        f.write("\n\n".join(entries))
