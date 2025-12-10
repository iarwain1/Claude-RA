"""Configuration management for the Literature Review Agent."""

import os
from pathlib import Path
from typing import Optional

import yaml
from pydantic import BaseModel, Field
from dotenv import load_dotenv


class LLMConfig(BaseModel):
    """Configuration for the LLM."""
    model: str = "claude-sonnet-4-20250514"
    max_tokens: int = 4096
    temperature: float = 0.7
    api_key: Optional[str] = None  # Will be loaded from env


class SearchConfig(BaseModel):
    """Configuration for search sources."""
    arxiv_enabled: bool = True
    arxiv_max_results: int = 50
    semantic_scholar_enabled: bool = True
    semantic_scholar_max_results: int = 50
    web_search_enabled: bool = True


class ProcessingConfig(BaseModel):
    """Configuration for document processing."""
    max_pdf_pages: int = 100
    chunk_size: int = 4000  # tokens
    chunk_overlap: int = 200
    extract_citations: bool = True
    follow_citations_depth: int = 1


class CommunicationConfig(BaseModel):
    """Configuration for agent-user communication."""
    update_frequency: str = "regular"  # "minimal", "regular", "verbose"
    ask_before_major_actions: bool = True
    show_progress_bar: bool = True
    auto_save_interval: int = 60  # seconds


class Config(BaseModel):
    """Main configuration for the Literature Review Agent."""
    # Project paths
    project_dir: Path = Field(default_factory=lambda: Path.cwd())
    data_dir: Path = Field(default_factory=lambda: Path.cwd() / "data")
    output_dir: Path = Field(default_factory=lambda: Path.cwd() / "output")

    # Sub-configurations
    llm: LLMConfig = Field(default_factory=LLMConfig)
    search: SearchConfig = Field(default_factory=SearchConfig)
    processing: ProcessingConfig = Field(default_factory=ProcessingConfig)
    communication: CommunicationConfig = Field(default_factory=CommunicationConfig)

    # Runtime settings
    debug: bool = False
    log_level: str = "INFO"

    class Config:
        arbitrary_types_allowed = True

    def setup_directories(self) -> None:
        """Create necessary directories."""
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        (self.data_dir / "references").mkdir(exist_ok=True)
        (self.data_dir / "notes").mkdir(exist_ok=True)
        (self.data_dir / "pdfs").mkdir(exist_ok=True)
        (self.output_dir / "reports").mkdir(exist_ok=True)


def load_config(config_path: Path | None = None) -> Config:
    """Load configuration from file and environment.

    Args:
        config_path: Optional path to YAML config file

    Returns:
        Config instance
    """
    # Load environment variables
    load_dotenv()

    config_data = {}

    # Load from YAML if provided
    if config_path and config_path.exists():
        with open(config_path) as f:
            config_data = yaml.safe_load(f) or {}

    # Create config
    config = Config(**config_data)

    # Override LLM API key from environment
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if api_key:
        config.llm.api_key = api_key

    return config


def save_config(config: Config, path: Path) -> None:
    """Save configuration to YAML file.

    Args:
        config: Config instance to save
        path: Path to save to
    """
    config_dict = config.model_dump(mode="json")
    # Remove sensitive data
    if "llm" in config_dict and "api_key" in config_dict["llm"]:
        config_dict["llm"]["api_key"] = None

    with open(path, "w") as f:
        yaml.safe_dump(config_dict, f, default_flow_style=False)
