"""Reference manager for organizing, tagging, and ranking references."""

from datetime import datetime
from pathlib import Path
from typing import Optional
import json

from ..models import Reference, ReferenceStatus, Priority, SubTopic
from ..utils.logging import get_logger
from ..utils.text import normalize_title
from ..utils.persistence import save_references, load_references


class ReferenceManager:
    """Manages the collection of references."""

    def __init__(self, data_dir: Path):
        """Initialize the reference manager.

        Args:
            data_dir: Directory for storing reference data
        """
        self.data_dir = data_dir
        self.references_file = data_dir / "references" / "references.json"
        self.logger = get_logger("reference_manager")

        self._references: dict[str, Reference] = {}
        self._title_index: dict[str, str] = {}  # normalized_title -> id
        self._url_index: dict[str, str] = {}  # url -> id
        self._arxiv_index: dict[str, str] = {}  # arxiv_id -> id
        self._doi_index: dict[str, str] = {}  # doi -> id

        self._load()

    def _load(self) -> None:
        """Load references from disk."""
        refs = load_references(self.references_file)
        for ref in refs:
            self._add_to_indices(ref)
        self.logger.info(f"Loaded {len(self._references)} references")

    def _save(self) -> None:
        """Save references to disk."""
        save_references(list(self._references.values()), self.references_file)

    def _add_to_indices(self, ref: Reference) -> None:
        """Add a reference to all indices.

        Args:
            ref: Reference to index
        """
        self._references[ref.id] = ref
        self._title_index[normalize_title(ref.title)] = ref.id
        if ref.url:
            self._url_index[ref.url] = ref.id
        if ref.arxiv_id:
            self._arxiv_index[ref.arxiv_id] = ref.id
        if ref.doi:
            self._doi_index[ref.doi] = ref.id

    def add(self, ref: Reference, deduplicate: bool = True) -> tuple[Reference, bool]:
        """Add a reference to the collection.

        Args:
            ref: Reference to add
            deduplicate: Check for duplicates

        Returns:
            Tuple of (reference, was_new)
        """
        if deduplicate:
            existing = self.find_duplicate(ref)
            if existing:
                # Merge new info into existing
                merged = self._merge_references(existing, ref)
                self._add_to_indices(merged)
                self._save()
                return merged, False

        self._add_to_indices(ref)
        self._save()
        self.logger.debug(f"Added reference: {ref.title[:50]}...")
        return ref, True

    def add_batch(
        self,
        refs: list[Reference],
        deduplicate: bool = True,
    ) -> tuple[int, int]:
        """Add multiple references.

        Args:
            refs: References to add
            deduplicate: Check for duplicates

        Returns:
            Tuple of (new_count, updated_count)
        """
        new_count = 0
        updated_count = 0

        for ref in refs:
            _, was_new = self.add(ref, deduplicate=deduplicate)
            if was_new:
                new_count += 1
            else:
                updated_count += 1

        self._save()
        self.logger.info(f"Added {new_count} new, updated {updated_count} references")
        return new_count, updated_count

    def get(self, ref_id: str) -> Optional[Reference]:
        """Get a reference by ID.

        Args:
            ref_id: Reference ID

        Returns:
            Reference or None
        """
        return self._references.get(ref_id)

    def get_all(self) -> list[Reference]:
        """Get all references.

        Returns:
            List of all references
        """
        return list(self._references.values())

    def find_duplicate(self, ref: Reference) -> Optional[Reference]:
        """Find a duplicate of the given reference.

        Args:
            ref: Reference to check

        Returns:
            Existing duplicate or None
        """
        # Check by arXiv ID
        if ref.arxiv_id and ref.arxiv_id in self._arxiv_index:
            return self._references[self._arxiv_index[ref.arxiv_id]]

        # Check by DOI
        if ref.doi and ref.doi in self._doi_index:
            return self._references[self._doi_index[ref.doi]]

        # Check by URL
        if ref.url and ref.url in self._url_index:
            return self._references[self._url_index[ref.url]]

        # Check by normalized title
        norm_title = normalize_title(ref.title)
        if norm_title in self._title_index:
            return self._references[self._title_index[norm_title]]

        return None

    def _merge_references(
        self,
        existing: Reference,
        new: Reference,
    ) -> Reference:
        """Merge new reference info into existing.

        Args:
            existing: Existing reference
            new: New reference with potentially new info

        Returns:
            Merged reference
        """
        # Update with new info where existing is missing
        updates = {}

        if not existing.abstract and new.abstract:
            updates["abstract"] = new.abstract
        if not existing.arxiv_id and new.arxiv_id:
            updates["arxiv_id"] = new.arxiv_id
        if not existing.doi and new.doi:
            updates["doi"] = new.doi
        if not existing.pdf_url and new.pdf_url:
            updates["pdf_url"] = new.pdf_url
        if not existing.year and new.year:
            updates["year"] = new.year
        if not existing.authors and new.authors:
            updates["authors"] = new.authors

        # Merge tags and subtopics
        if new.tags:
            updates["tags"] = list(set(existing.tags + new.tags))
        if new.subtopics:
            updates["subtopics"] = list(set(existing.subtopics + new.subtopics))

        if updates:
            return existing.model_copy(update=updates)
        return existing

    def update(self, ref: Reference) -> None:
        """Update an existing reference.

        Args:
            ref: Updated reference
        """
        if ref.id in self._references:
            self._add_to_indices(ref)
            self._save()

    def update_status(
        self,
        ref_id: str,
        status: ReferenceStatus,
    ) -> Optional[Reference]:
        """Update reference status.

        Args:
            ref_id: Reference ID
            status: New status

        Returns:
            Updated reference or None
        """
        ref = self.get(ref_id)
        if ref:
            updated = ref.model_copy(update={
                "status": status,
                "processed_at": datetime.now() if status == ReferenceStatus.COMPLETED else None,
            })
            self.update(updated)
            return updated
        return None

    def update_priority(
        self,
        ref_id: str,
        priority: Priority,
        explanation: Optional[str] = None,
    ) -> Optional[Reference]:
        """Update reference priority.

        Args:
            ref_id: Reference ID
            priority: New priority
            explanation: Explanation for the priority

        Returns:
            Updated reference or None
        """
        ref = self.get(ref_id)
        if ref:
            updates = {"priority": priority}
            if explanation:
                updates["relevance_explanation"] = explanation
            updated = ref.model_copy(update=updates)
            self.update(updated)
            return updated
        return None

    def add_tags(self, ref_id: str, tags: list[str]) -> Optional[Reference]:
        """Add tags to a reference.

        Args:
            ref_id: Reference ID
            tags: Tags to add

        Returns:
            Updated reference or None
        """
        ref = self.get(ref_id)
        if ref:
            new_tags = list(set(ref.tags + tags))
            updated = ref.model_copy(update={"tags": new_tags})
            self.update(updated)
            return updated
        return None

    def add_subtopic(
        self,
        ref_id: str,
        subtopic: str,
    ) -> Optional[Reference]:
        """Add a subtopic to a reference.

        Args:
            ref_id: Reference ID
            subtopic: Subtopic to add

        Returns:
            Updated reference or None
        """
        ref = self.get(ref_id)
        if ref:
            new_subtopics = list(set(ref.subtopics + [subtopic]))
            updated = ref.model_copy(update={"subtopics": new_subtopics})
            self.update(updated)
            return updated
        return None

    def get_by_status(self, status: ReferenceStatus) -> list[Reference]:
        """Get references by status.

        Args:
            status: Status to filter by

        Returns:
            List of matching references
        """
        return [r for r in self._references.values() if r.status == status]

    def get_by_priority(self, priority: Priority) -> list[Reference]:
        """Get references by priority.

        Args:
            priority: Priority to filter by

        Returns:
            List of matching references
        """
        return [r for r in self._references.values() if r.priority == priority]

    def get_by_subtopic(self, subtopic: str) -> list[Reference]:
        """Get references by subtopic.

        Args:
            subtopic: Subtopic to filter by

        Returns:
            List of matching references
        """
        return [r for r in self._references.values() if subtopic in r.subtopics]

    def get_by_tag(self, tag: str) -> list[Reference]:
        """Get references by tag.

        Args:
            tag: Tag to filter by

        Returns:
            List of matching references
        """
        return [r for r in self._references.values() if tag in r.tags]

    def get_reading_queue(self) -> list[Reference]:
        """Get references in reading queue, sorted by priority.

        Returns:
            List of references to read
        """
        queued = self.get_by_status(ReferenceStatus.QUEUED)
        priority_order = {
            Priority.CRITICAL: 0,
            Priority.HIGH: 1,
            Priority.MEDIUM: 2,
            Priority.LOW: 3,
            Priority.UNKNOWN: 4,
        }
        return sorted(queued, key=lambda r: priority_order.get(r.priority, 5))

    def get_statistics(self) -> dict:
        """Get statistics about the reference collection.

        Returns:
            Statistics dictionary
        """
        refs = list(self._references.values())

        status_counts = {}
        for status in ReferenceStatus:
            status_counts[status.value] = len([r for r in refs if r.status == status])

        priority_counts = {}
        for priority in Priority:
            priority_counts[priority.value] = len([r for r in refs if r.priority == priority])

        subtopic_counts = {}
        for ref in refs:
            for subtopic in ref.subtopics:
                subtopic_counts[subtopic] = subtopic_counts.get(subtopic, 0) + 1

        return {
            "total": len(refs),
            "by_status": status_counts,
            "by_priority": priority_counts,
            "by_subtopic": subtopic_counts,
            "with_abstract": len([r for r in refs if r.abstract]),
            "with_pdf": len([r for r in refs if r.pdf_url or r.local_pdf_path]),
        }

    def search(
        self,
        query: str,
        in_title: bool = True,
        in_abstract: bool = True,
        in_tags: bool = True,
    ) -> list[Reference]:
        """Search references.

        Args:
            query: Search query
            in_title: Search in titles
            in_abstract: Search in abstracts
            in_tags: Search in tags

        Returns:
            List of matching references
        """
        query_lower = query.lower()
        matches = []

        for ref in self._references.values():
            searchable_parts = []
            if in_title:
                searchable_parts.append(ref.title.lower())
            if in_abstract and ref.abstract:
                searchable_parts.append(ref.abstract.lower())
            if in_tags:
                searchable_parts.extend(tag.lower() for tag in ref.tags)

            searchable = " ".join(searchable_parts)
            if query_lower in searchable:
                matches.append(ref)

        return matches
