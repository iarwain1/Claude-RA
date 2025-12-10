"""Logging configuration for the Literature Review Agent."""

import logging
import sys
from pathlib import Path
from rich.logging import RichHandler
from rich.console import Console

console = Console()

_loggers: dict[str, logging.Logger] = {}


def setup_logging(
    level: str = "INFO",
    log_file: Path | None = None,
) -> None:
    """Set up logging configuration.

    Args:
        level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_file: Optional path to log file
    """
    log_level = getattr(logging, level.upper(), logging.INFO)

    # Configure root logger
    root_logger = logging.getLogger("literature_review_agent")
    root_logger.setLevel(log_level)

    # Clear any existing handlers
    root_logger.handlers.clear()

    # Rich console handler for pretty output
    rich_handler = RichHandler(
        console=console,
        show_time=True,
        show_path=False,
        rich_tracebacks=True,
    )
    rich_handler.setLevel(log_level)
    rich_handler.setFormatter(logging.Formatter("%(message)s"))
    root_logger.addHandler(rich_handler)

    # File handler if specified
    if log_file:
        log_file.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
        )
        root_logger.addHandler(file_handler)


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance.

    Args:
        name: Name for the logger (will be prefixed with 'literature_review_agent.')

    Returns:
        Logger instance
    """
    full_name = f"literature_review_agent.{name}"
    if full_name not in _loggers:
        _loggers[full_name] = logging.getLogger(full_name)
    return _loggers[full_name]
