"""Note manager for organizing research notes."""

from datetime import datetime
from pathlib import Path
from typing import Optional
import uuid

from ..models import Note
from ..utils.logging import get_logger
from ..utils.persistence import save_notes, load_notes


class NoteManager:
    """Manages research notes."""

    def __init__(self, data_dir: Path):
        """Initialize the note manager.

        Args:
            data_dir: Directory for storing notes
        """
        self.data_dir = data_dir
        self.notes_dir = data_dir / "notes"
        self.notes_file = self.notes_dir / "notes.json"
        self.logger = get_logger("note_manager")

        self._notes: dict[str, Note] = {}
        self._by_reference: dict[str, list[str]] = {}  # ref_id -> note_ids
        self._by_tag: dict[str, list[str]] = {}  # tag -> note_ids

        self._load()

    def _load(self) -> None:
        """Load notes from disk."""
        notes = load_notes(self.notes_file)
        for note in notes:
            self._add_to_indices(note)
        self.logger.info(f"Loaded {len(self._notes)} notes")

    def _save(self) -> None:
        """Save notes to disk."""
        save_notes(list(self._notes.values()), self.notes_file)

    def _add_to_indices(self, note: Note) -> None:
        """Add a note to all indices.

        Args:
            note: Note to index
        """
        self._notes[note.id] = note

        if note.reference_id not in self._by_reference:
            self._by_reference[note.reference_id] = []
        if note.id not in self._by_reference[note.reference_id]:
            self._by_reference[note.reference_id].append(note.id)

        for tag in note.tags:
            if tag not in self._by_tag:
                self._by_tag[tag] = []
            if note.id not in self._by_tag[tag]:
                self._by_tag[tag].append(note.id)

    def create(
        self,
        reference_id: str,
        content: str,
        quote: Optional[str] = None,
        page_number: Optional[int] = None,
        section: Optional[str] = None,
        tags: Optional[list[str]] = None,
        note_type: str = "general",
    ) -> Note:
        """Create a new note.

        Args:
            reference_id: ID of the reference this note is about
            content: Note content
            quote: Direct quote from the source
            page_number: Page number if applicable
            section: Section name if applicable
            tags: Tags for the note
            note_type: Type of note

        Returns:
            Created note
        """
        note = Note(
            id=str(uuid.uuid4())[:8],
            reference_id=reference_id,
            content=content,
            quote=quote,
            page_number=page_number,
            section=section,
            tags=tags or [],
            note_type=note_type,
        )

        self._add_to_indices(note)
        self._save()
        self.logger.debug(f"Created note for reference {reference_id}")
        return note

    def get(self, note_id: str) -> Optional[Note]:
        """Get a note by ID.

        Args:
            note_id: Note ID

        Returns:
            Note or None
        """
        return self._notes.get(note_id)

    def get_all(self) -> list[Note]:
        """Get all notes.

        Returns:
            List of all notes
        """
        return list(self._notes.values())

    def get_for_reference(self, reference_id: str) -> list[Note]:
        """Get all notes for a reference.

        Args:
            reference_id: Reference ID

        Returns:
            List of notes for the reference
        """
        note_ids = self._by_reference.get(reference_id, [])
        return [self._notes[nid] for nid in note_ids if nid in self._notes]

    def get_by_tag(self, tag: str) -> list[Note]:
        """Get notes by tag.

        Args:
            tag: Tag to filter by

        Returns:
            List of notes with the tag
        """
        note_ids = self._by_tag.get(tag, [])
        return [self._notes[nid] for nid in note_ids if nid in self._notes]

    def get_by_type(self, note_type: str) -> list[Note]:
        """Get notes by type.

        Args:
            note_type: Note type to filter by

        Returns:
            List of notes of the type
        """
        return [n for n in self._notes.values() if n.note_type == note_type]

    def update(self, note: Note) -> None:
        """Update an existing note.

        Args:
            note: Updated note
        """
        if note.id in self._notes:
            note = note.model_copy(update={"updated_at": datetime.now()})
            self._add_to_indices(note)
            self._save()

    def delete(self, note_id: str) -> bool:
        """Delete a note.

        Args:
            note_id: Note ID to delete

        Returns:
            True if deleted, False if not found
        """
        if note_id in self._notes:
            note = self._notes[note_id]

            # Remove from indices
            del self._notes[note_id]

            if note.reference_id in self._by_reference:
                self._by_reference[note.reference_id] = [
                    nid for nid in self._by_reference[note.reference_id]
                    if nid != note_id
                ]

            for tag in note.tags:
                if tag in self._by_tag:
                    self._by_tag[tag] = [
                        nid for nid in self._by_tag[tag]
                        if nid != note_id
                    ]

            self._save()
            return True
        return False

    def add_tags(self, note_id: str, tags: list[str]) -> Optional[Note]:
        """Add tags to a note.

        Args:
            note_id: Note ID
            tags: Tags to add

        Returns:
            Updated note or None
        """
        note = self.get(note_id)
        if note:
            new_tags = list(set(note.tags + tags))
            updated = note.model_copy(update={"tags": new_tags})
            self.update(updated)
            return updated
        return None

    def search(self, query: str) -> list[Note]:
        """Search notes by content.

        Args:
            query: Search query

        Returns:
            List of matching notes
        """
        query_lower = query.lower()
        matches = []

        for note in self._notes.values():
            searchable = f"{note.content} {note.quote or ''}"
            if query_lower in searchable.lower():
                matches.append(note)

        return matches

    def get_key_findings(self) -> list[Note]:
        """Get all key finding notes.

        Returns:
            List of key finding notes
        """
        return self.get_by_type("key_finding")

    def get_questions(self) -> list[Note]:
        """Get all question notes.

        Returns:
            List of question notes
        """
        return self.get_by_type("question")

    def get_statistics(self) -> dict:
        """Get statistics about notes.

        Returns:
            Statistics dictionary
        """
        notes = list(self._notes.values())

        type_counts = {}
        for note in notes:
            type_counts[note.note_type] = type_counts.get(note.note_type, 0) + 1

        return {
            "total": len(notes),
            "by_type": type_counts,
            "references_with_notes": len(self._by_reference),
            "unique_tags": len(self._by_tag),
        }

    def export_for_reference(
        self,
        reference_id: str,
        format: str = "markdown",
    ) -> str:
        """Export notes for a reference.

        Args:
            reference_id: Reference ID
            format: Export format ("markdown" or "text")

        Returns:
            Formatted notes string
        """
        notes = self.get_for_reference(reference_id)
        if not notes:
            return ""

        if format == "markdown":
            lines = [f"## Notes\n"]
            for note in notes:
                lines.append(f"### {note.note_type.replace('_', ' ').title()}")
                if note.section:
                    lines.append(f"*Section: {note.section}*")
                if note.page_number:
                    lines.append(f"*Page: {note.page_number}*")
                lines.append("")
                lines.append(note.content)
                if note.quote:
                    lines.append(f"\n> \"{note.quote}\"")
                if note.tags:
                    lines.append(f"\nTags: {', '.join(note.tags)}")
                lines.append("\n---\n")
            return "\n".join(lines)
        else:
            lines = []
            for note in notes:
                lines.append(f"[{note.note_type}] {note.content}")
                if note.quote:
                    lines.append(f'  Quote: "{note.quote}"')
            return "\n".join(lines)
