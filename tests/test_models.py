"""Tests for data models."""

import pytest
from datetime import datetime

from literature_review_agent.models import (
    Reference,
    Note,
    SubTopic,
    Author,
    ReferenceType,
    ReferenceStatus,
    Priority,
)


class TestReference:
    """Tests for Reference model."""

    def test_create_basic_reference(self):
        """Test creating a basic reference."""
        ref = Reference(
            id="test123",
            title="Test Paper",
        )
        assert ref.id == "test123"
        assert ref.title == "Test Paper"
        assert ref.status == ReferenceStatus.DISCOVERED
        assert ref.priority == Priority.UNKNOWN

    def test_reference_with_authors(self):
        """Test creating a reference with authors."""
        authors = [
            Author(name="John Doe", affiliation="MIT"),
            Author(name="Jane Smith"),
        ]
        ref = Reference(
            id="test456",
            title="Collaborative Research",
            authors=authors,
            year=2024,
        )
        assert len(ref.authors) == 2
        assert ref.authors[0].name == "John Doe"
        assert ref.year == 2024

    def test_reference_with_identifiers(self):
        """Test reference with various identifiers."""
        ref = Reference(
            id="test789",
            title="Paper with IDs",
            arxiv_id="2301.07041",
            doi="10.1234/example",
            url="https://example.com/paper",
        )
        assert ref.arxiv_id == "2301.07041"
        assert ref.doi == "10.1234/example"
        assert ref.url == "https://example.com/paper"

    def test_reference_tags_and_subtopics(self):
        """Test reference organization features."""
        ref = Reference(
            id="testorg",
            title="Organized Paper",
            tags=["ml", "nlp", "transformers"],
            subtopics=["Language Models", "Attention"],
        )
        assert "ml" in ref.tags
        assert "Language Models" in ref.subtopics


class TestNote:
    """Tests for Note model."""

    def test_create_note(self):
        """Test creating a basic note."""
        note = Note(
            id="note1",
            reference_id="ref1",
            content="This is an important finding.",
        )
        assert note.id == "note1"
        assert note.reference_id == "ref1"
        assert note.content == "This is an important finding."

    def test_note_with_quote(self):
        """Test note with a quote."""
        note = Note(
            id="note2",
            reference_id="ref1",
            content="Key claim about transformers",
            quote="Attention is all you need",
            page_number=3,
            section="Introduction",
        )
        assert note.quote == "Attention is all you need"
        assert note.page_number == 3


class TestSubTopic:
    """Tests for SubTopic model."""

    def test_create_subtopic(self):
        """Test creating a subtopic."""
        subtopic = SubTopic(
            id="st1",
            name="Attention Mechanisms",
            description="Research on attention in neural networks",
        )
        assert subtopic.name == "Attention Mechanisms"
        assert subtopic.priority == Priority.MEDIUM

    def test_subtopic_with_findings(self):
        """Test subtopic with key findings."""
        subtopic = SubTopic(
            id="st2",
            name="Scaling Laws",
            description="Research on model scaling",
            key_findings=[
                "Larger models perform better",
                "Compute-optimal training exists",
            ],
            open_questions=[
                "What are the limits of scaling?",
            ],
        )
        assert len(subtopic.key_findings) == 2
        assert len(subtopic.open_questions) == 1
