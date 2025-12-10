"""Subtopic manager for organizing research by topics."""

from datetime import datetime
from pathlib import Path
from typing import Optional
import json
import uuid

from ..models import SubTopic, Priority
from ..utils.logging import get_logger


class SubtopicManager:
    """Manages research subtopics."""

    def __init__(self, data_dir: Path):
        """Initialize the subtopic manager.

        Args:
            data_dir: Directory for storing subtopic data
        """
        self.data_dir = data_dir
        self.subtopics_file = data_dir / "subtopics.json"
        self.logger = get_logger("subtopic_manager")

        self._subtopics: dict[str, SubTopic] = {}
        self._by_parent: dict[str, list[str]] = {}  # parent_id -> child_ids

        self._load()

    def _load(self) -> None:
        """Load subtopics from disk."""
        if self.subtopics_file.exists():
            with open(self.subtopics_file) as f:
                data = json.load(f)
            for item in data:
                subtopic = SubTopic(**item)
                self._add_to_indices(subtopic)
        self.logger.info(f"Loaded {len(self._subtopics)} subtopics")

    def _save(self) -> None:
        """Save subtopics to disk."""
        self.subtopics_file.parent.mkdir(parents=True, exist_ok=True)
        data = [st.model_dump(mode="json") for st in self._subtopics.values()]
        with open(self.subtopics_file, "w") as f:
            json.dump(data, f, indent=2, default=str)

    def _add_to_indices(self, subtopic: SubTopic) -> None:
        """Add a subtopic to indices.

        Args:
            subtopic: Subtopic to index
        """
        self._subtopics[subtopic.id] = subtopic

        parent_id = subtopic.parent_id or "root"
        if parent_id not in self._by_parent:
            self._by_parent[parent_id] = []
        if subtopic.id not in self._by_parent[parent_id]:
            self._by_parent[parent_id].append(subtopic.id)

    def create(
        self,
        name: str,
        description: str,
        parent_id: Optional[str] = None,
        tags: Optional[list[str]] = None,
        priority: Priority = Priority.MEDIUM,
    ) -> SubTopic:
        """Create a new subtopic.

        Args:
            name: Subtopic name
            description: Subtopic description
            parent_id: Parent subtopic ID for nesting
            tags: Tags for the subtopic
            priority: Priority level

        Returns:
            Created subtopic
        """
        subtopic = SubTopic(
            id=str(uuid.uuid4())[:8],
            name=name,
            description=description,
            parent_id=parent_id,
            tags=tags or [],
            priority=priority,
        )

        self._add_to_indices(subtopic)
        self._save()
        self.logger.info(f"Created subtopic: {name}")
        return subtopic

    def get(self, subtopic_id: str) -> Optional[SubTopic]:
        """Get a subtopic by ID.

        Args:
            subtopic_id: Subtopic ID

        Returns:
            Subtopic or None
        """
        return self._subtopics.get(subtopic_id)

    def get_by_name(self, name: str) -> Optional[SubTopic]:
        """Get a subtopic by name.

        Args:
            name: Subtopic name

        Returns:
            Subtopic or None
        """
        name_lower = name.lower()
        for st in self._subtopics.values():
            if st.name.lower() == name_lower:
                return st
        return None

    def get_all(self) -> list[SubTopic]:
        """Get all subtopics.

        Returns:
            List of all subtopics
        """
        return list(self._subtopics.values())

    def get_root_subtopics(self) -> list[SubTopic]:
        """Get all top-level subtopics.

        Returns:
            List of root subtopics
        """
        return [st for st in self._subtopics.values() if st.parent_id is None]

    def get_children(self, parent_id: str) -> list[SubTopic]:
        """Get child subtopics.

        Args:
            parent_id: Parent subtopic ID

        Returns:
            List of child subtopics
        """
        child_ids = self._by_parent.get(parent_id, [])
        return [self._subtopics[cid] for cid in child_ids if cid in self._subtopics]

    def update(self, subtopic: SubTopic) -> None:
        """Update a subtopic.

        Args:
            subtopic: Updated subtopic
        """
        if subtopic.id in self._subtopics:
            self._subtopics[subtopic.id] = subtopic
            self._save()

    def add_reference(self, subtopic_id: str, reference_id: str) -> Optional[SubTopic]:
        """Add a reference to a subtopic.

        Args:
            subtopic_id: Subtopic ID
            reference_id: Reference ID to add

        Returns:
            Updated subtopic or None
        """
        subtopic = self.get(subtopic_id)
        if subtopic:
            if reference_id not in subtopic.reference_ids:
                new_refs = subtopic.reference_ids + [reference_id]
                updated = subtopic.model_copy(update={"reference_ids": new_refs})
                self.update(updated)
                return updated
        return subtopic

    def remove_reference(self, subtopic_id: str, reference_id: str) -> Optional[SubTopic]:
        """Remove a reference from a subtopic.

        Args:
            subtopic_id: Subtopic ID
            reference_id: Reference ID to remove

        Returns:
            Updated subtopic or None
        """
        subtopic = self.get(subtopic_id)
        if subtopic:
            new_refs = [rid for rid in subtopic.reference_ids if rid != reference_id]
            updated = subtopic.model_copy(update={"reference_ids": new_refs})
            self.update(updated)
            return updated
        return None

    def add_key_finding(self, subtopic_id: str, finding: str) -> Optional[SubTopic]:
        """Add a key finding to a subtopic.

        Args:
            subtopic_id: Subtopic ID
            finding: Key finding to add

        Returns:
            Updated subtopic or None
        """
        subtopic = self.get(subtopic_id)
        if subtopic:
            new_findings = subtopic.key_findings + [finding]
            updated = subtopic.model_copy(update={"key_findings": new_findings})
            self.update(updated)
            return updated
        return None

    def add_question(self, subtopic_id: str, question: str) -> Optional[SubTopic]:
        """Add an open question to a subtopic.

        Args:
            subtopic_id: Subtopic ID
            question: Question to add

        Returns:
            Updated subtopic or None
        """
        subtopic = self.get(subtopic_id)
        if subtopic:
            new_questions = subtopic.open_questions + [question]
            updated = subtopic.model_copy(update={"open_questions": new_questions})
            self.update(updated)
            return updated
        return None

    def set_summary(self, subtopic_id: str, summary: str) -> Optional[SubTopic]:
        """Set the summary for a subtopic.

        Args:
            subtopic_id: Subtopic ID
            summary: Summary text

        Returns:
            Updated subtopic or None
        """
        subtopic = self.get(subtopic_id)
        if subtopic:
            updated = subtopic.model_copy(update={"summary": summary})
            self.update(updated)
            return updated
        return None

    def get_hierarchy(self) -> dict:
        """Get the full subtopic hierarchy.

        Returns:
            Nested dictionary of subtopics
        """
        def build_tree(parent_id: Optional[str] = None) -> list[dict]:
            children = []
            child_ids = self._by_parent.get(parent_id or "root", [])

            for child_id in child_ids:
                subtopic = self._subtopics.get(child_id)
                if subtopic:
                    children.append({
                        "subtopic": subtopic,
                        "children": build_tree(child_id),
                    })

            return children

        return {"root": build_tree()}

    def delete(self, subtopic_id: str, recursive: bool = False) -> bool:
        """Delete a subtopic.

        Args:
            subtopic_id: Subtopic ID to delete
            recursive: Also delete children

        Returns:
            True if deleted, False if not found
        """
        if subtopic_id not in self._subtopics:
            return False

        if recursive:
            # Delete all children first
            for child in self.get_children(subtopic_id):
                self.delete(child.id, recursive=True)

        subtopic = self._subtopics[subtopic_id]

        # Remove from indices
        del self._subtopics[subtopic_id]

        parent_id = subtopic.parent_id or "root"
        if parent_id in self._by_parent:
            self._by_parent[parent_id] = [
                sid for sid in self._by_parent[parent_id]
                if sid != subtopic_id
            ]

        self._save()
        return True

    def get_statistics(self) -> dict:
        """Get statistics about subtopics.

        Returns:
            Statistics dictionary
        """
        subtopics = list(self._subtopics.values())

        return {
            "total": len(subtopics),
            "root_count": len(self.get_root_subtopics()),
            "with_summary": len([st for st in subtopics if st.summary]),
            "total_references": sum(len(st.reference_ids) for st in subtopics),
            "total_findings": sum(len(st.key_findings) for st in subtopics),
            "total_questions": sum(len(st.open_questions) for st in subtopics),
        }
