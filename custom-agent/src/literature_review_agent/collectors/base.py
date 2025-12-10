"""Base collector class for all source collectors."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Optional

from ..models import Reference
from ..utils.logging import get_logger


@dataclass
class CollectorResult:
    """Result from a collector operation."""
    references: list[Reference] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    warnings: list[str] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)

    @property
    def success(self) -> bool:
        """Check if collection was successful (found at least some references)."""
        return len(self.references) > 0 or len(self.errors) == 0

    def merge(self, other: "CollectorResult") -> "CollectorResult":
        """Merge another result into this one."""
        return CollectorResult(
            references=self.references + other.references,
            errors=self.errors + other.errors,
            warnings=self.warnings + other.warnings,
            metadata={**self.metadata, **other.metadata},
        )


class BaseCollector(ABC):
    """Abstract base class for all source collectors."""

    def __init__(self, name: str):
        """Initialize the collector.

        Args:
            name: Name of the collector for logging
        """
        self.name = name
        self.logger = get_logger(f"collector.{name}")

    @abstractmethod
    async def collect(self, **kwargs) -> CollectorResult:
        """Collect references from the source.

        Returns:
            CollectorResult containing found references and any errors
        """
        pass

    @abstractmethod
    async def search(self, query: str, **kwargs) -> CollectorResult:
        """Search for references matching a query.

        Args:
            query: Search query string

        Returns:
            CollectorResult containing matching references
        """
        pass

    def _create_reference_id(self, *parts: str) -> str:
        """Create a unique reference ID from parts.

        Args:
            *parts: Parts to include in the ID

        Returns:
            Unique reference ID
        """
        import hashlib
        combined = "_".join(str(p) for p in parts if p)
        return hashlib.sha256(combined.encode()).hexdigest()[:12]

    def _log_progress(self, message: str, current: int = 0, total: int = 0) -> None:
        """Log progress message.

        Args:
            message: Progress message
            current: Current item number
            total: Total number of items
        """
        if total > 0:
            self.logger.info(f"[{current}/{total}] {message}")
        else:
            self.logger.info(message)
