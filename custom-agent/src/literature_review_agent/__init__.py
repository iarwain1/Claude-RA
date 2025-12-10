"""
Literature Review Agent - An AI-powered research assistant for comprehensive literature reviews.

This agent helps researchers:
- Gather references from URLs, blogs, newsletters, and academic databases
- Organize and tag references by subtopic
- Read and analyze papers, taking detailed notes
- Follow citation trails to discover new sources
- Synthesize findings into comprehensive reports

The agent uses the Claude Agent SDK for intelligent, tool-based research automation.
"""

__version__ = "0.2.0"

# Legacy agent (direct API calls)
from .agent import LiteratureReviewAgent

# New SDK-based agent (recommended)
from .sdk_agent import SDKLiteratureReviewAgent, run_sdk_agent_interactive

# Data models
from .models import (
    Reference,
    Note,
    ResearchTopic,
    ResearchProject,
    SubTopic,
    Author,
    ReferenceType,
    ReferenceStatus,
    Priority,
)

# Hooks
from .hooks import AgentHooks, create_logging_hook, create_interactive_hooks

__all__ = [
    # Agents
    "LiteratureReviewAgent",  # Legacy
    "SDKLiteratureReviewAgent",  # Recommended
    "run_sdk_agent_interactive",
    # Models
    "Reference",
    "Note",
    "ResearchTopic",
    "ResearchProject",
    "SubTopic",
    "Author",
    "ReferenceType",
    "ReferenceStatus",
    "Priority",
    # Hooks
    "AgentHooks",
    "create_logging_hook",
    "create_interactive_hooks",
]
