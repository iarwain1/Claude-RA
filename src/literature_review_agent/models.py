"""
Core data models for the Literature Review Agent.
"""

from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class ReferenceType(str, Enum):
    """Type of reference source."""
    PAPER = "paper"
    ARTICLE = "article"
    BLOG_POST = "blog_post"
    BOOK = "book"
    BOOK_CHAPTER = "book_chapter"
    PREPRINT = "preprint"
    THESIS = "thesis"
    REPORT = "report"
    WEBPAGE = "webpage"
    VIDEO = "video"
    PODCAST = "podcast"
    NEWSLETTER = "newsletter"
    UNKNOWN = "unknown"


class ReferenceStatus(str, Enum):
    """Processing status of a reference."""
    DISCOVERED = "discovered"  # Found but not yet evaluated
    QUEUED = "queued"  # In queue for reading
    READING = "reading"  # Currently being read/analyzed
    COMPLETED = "completed"  # Fully processed with notes
    SKIPPED = "skipped"  # Deemed not relevant
    UNAVAILABLE = "unavailable"  # Could not access content


class Priority(str, Enum):
    """Priority level for reading."""
    CRITICAL = "critical"  # Must read - foundational
    HIGH = "high"  # Very relevant, should read
    MEDIUM = "medium"  # Relevant, read if time permits
    LOW = "low"  # Tangentially relevant
    UNKNOWN = "unknown"  # Not yet evaluated


class Author(BaseModel):
    """Author information."""
    name: str
    affiliation: Optional[str] = None
    email: Optional[str] = None
    orcid: Optional[str] = None


class Reference(BaseModel):
    """A reference (paper, article, blog post, etc.) in the literature review."""
    id: str = Field(description="Unique identifier for the reference")
    title: str
    authors: list[Author] = Field(default_factory=list)
    year: Optional[int] = None

    # Source information
    url: Optional[str] = None
    doi: Optional[str] = None
    arxiv_id: Optional[str] = None
    semantic_scholar_id: Optional[str] = None
    pdf_url: Optional[str] = None
    local_pdf_path: Optional[str] = None

    # Metadata
    ref_type: ReferenceType = ReferenceType.UNKNOWN
    abstract: Optional[str] = None
    venue: Optional[str] = None  # Journal, conference, blog name, etc.

    # Organization
    tags: list[str] = Field(default_factory=list)
    subtopics: list[str] = Field(default_factory=list)

    # Evaluation
    status: ReferenceStatus = ReferenceStatus.DISCOVERED
    priority: Priority = Priority.UNKNOWN
    relevance_score: Optional[float] = Field(default=None, ge=0.0, le=1.0)
    relevance_explanation: Optional[str] = None

    # Relations
    cited_by: list[str] = Field(default_factory=list, description="IDs of refs that cite this")
    cites: list[str] = Field(default_factory=list, description="IDs of refs this cites")
    related_refs: list[str] = Field(default_factory=list, description="IDs of related refs")
    discovered_from: Optional[str] = Field(default=None, description="How this ref was found")

    # Timestamps
    discovered_at: datetime = Field(default_factory=datetime.now)
    processed_at: Optional[datetime] = None

    # Content
    full_text: Optional[str] = None

    class Config:
        use_enum_values = True


class Note(BaseModel):
    """A note taken while reading a reference."""
    id: str
    reference_id: str

    # Content
    content: str
    quote: Optional[str] = None  # Direct quote from the source
    page_number: Optional[int] = None
    section: Optional[str] = None

    # Organization
    tags: list[str] = Field(default_factory=list)
    note_type: str = "general"  # e.g., "key_finding", "methodology", "question", "critique"

    # Timestamps
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)


class SubTopic(BaseModel):
    """A subtopic within the research project."""
    id: str
    name: str
    description: str
    parent_id: Optional[str] = None  # For nested subtopics

    # References
    reference_ids: list[str] = Field(default_factory=list)

    # Organization
    tags: list[str] = Field(default_factory=list)
    priority: Priority = Priority.MEDIUM

    # Notes
    summary: Optional[str] = None
    key_findings: list[str] = Field(default_factory=list)
    open_questions: list[str] = Field(default_factory=list)

    created_at: datetime = Field(default_factory=datetime.now)


class ResearchTopic(BaseModel):
    """The main research topic configuration."""
    name: str
    description: str
    key_questions: list[str] = Field(default_factory=list)
    key_terms: list[str] = Field(default_factory=list)
    exclusion_criteria: list[str] = Field(default_factory=list)
    date_range: Optional[tuple[int, int]] = None  # Year range


class SourceConfig(BaseModel):
    """Configuration for a source of references."""
    name: str
    source_type: str  # "url_list", "blog", "newsletter", "notes_folder"
    path: Optional[str] = None  # File or folder path
    url: Optional[str] = None
    rss_feed: Optional[str] = None
    search_depth: int = 1  # How many levels of links to follow


class ResearchProject(BaseModel):
    """The overall research project state."""
    id: str
    name: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)

    # Configuration
    topic: ResearchTopic
    sources: list[SourceConfig] = Field(default_factory=list)

    # Data
    subtopics: list[SubTopic] = Field(default_factory=list)

    # Progress tracking
    phase: str = "initialization"  # Current phase of research
    notes_to_user: list[str] = Field(default_factory=list)


class AgentMessage(BaseModel):
    """A message from the agent to the user."""
    message_type: str  # "update", "question", "insight", "request_feedback", "summary"
    content: str
    requires_response: bool = False
    options: Optional[list[str]] = None  # For multiple choice questions
    context: Optional[dict] = None
    timestamp: datetime = Field(default_factory=datetime.now)


class UserResponse(BaseModel):
    """A response from the user to the agent."""
    content: str
    in_reply_to: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.now)
