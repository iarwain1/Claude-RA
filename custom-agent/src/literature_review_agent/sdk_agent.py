"""
Literature Review Agent using Claude Agent SDK.

This module provides the main agent implementation using the Claude Agent SDK,
with custom MCP tools for literature review operations.
"""

import json
from datetime import datetime
from pathlib import Path
from typing import AsyncIterator, Callable, Any

import anyio
from claude_code_sdk import (
    ClaudeCodeSDK,
    query,
    ClaudeCodeOptions,
    AssistantMessage,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
    ToolResultBlock,
)

from .sdk_tools.server import (
    create_literature_review_server,
    ALL_LITERATURE_REVIEW_TOOLS,
    BUILT_IN_TOOLS,
)
from .utils.config import Config, load_config
from .utils.logging import setup_logging, get_logger


# System prompt for the literature review agent
LITERATURE_REVIEW_SYSTEM_PROMPT = """You are an expert Literature Review Research Assistant. Your role is to help researchers conduct comprehensive literature reviews on academic topics.

## Your Capabilities

You have access to specialized tools for:

### Reference Collection
- **search_arxiv**: Search arXiv for preprints in AI, ML, CS, physics, etc.
- **search_semantic_scholar**: Search Semantic Scholar for published papers
- **get_paper_citations**: Find papers that cite a given paper (follow-up work)
- **get_paper_references**: Find papers cited by a given paper (foundational work)
- **get_recommendations**: Get AI-powered paper recommendations
- **process_url_file**: Process files containing URLs/bookmarks
- **process_blog_feed**: Extract content from blogs and newsletters
- **scan_local_folder**: Scan Obsidian vaults and local documents

### Reference Management
- **add_reference**: Manually add a reference
- **search_references**: Search your reference collection
- **update_reference_priority**: Set priority (critical/high/medium/low)
- **update_reference_status**: Track reading progress
- **get_reading_queue**: View prioritized reading list
- **get_reference_stats**: View collection statistics
- **assign_subtopic**: Organize references by topic

### Note Taking
- **create_note**: Record findings, quotes, questions while reading
- **get_notes_for_reference**: View notes for a specific paper
- **search_notes**: Search across all notes
- **get_key_findings**: List all key findings

### Organization
- **create_subtopic**: Create subtopics for organizing research
- **list_subtopics**: View all subtopics
- **add_subtopic_finding**: Record key findings for a subtopic
- **add_subtopic_question**: Record open questions

### Reporting
- **generate_progress_report**: Get current research status
- **export_references_bibtex**: Export for academic writing
- **export_references_markdown**: Export with notes

## Research Process

Follow this systematic approach:

1. **GATHER** - Collect references from multiple sources:
   - Search academic databases (arXiv, Semantic Scholar)
   - Process user's URL lists and bookmarks
   - Scan local notes and documents
   - Follow citation trails from key papers

2. **ORGANIZE** - Structure the literature:
   - Create subtopics based on themes you discover
   - Evaluate relevance and set priorities
   - Assign references to subtopics
   - Build a prioritized reading queue

3. **READ & ANALYZE** - Deep dive into key papers:
   - Read high-priority papers first
   - Take detailed notes (findings, methodology, quotes)
   - Identify connections between papers
   - Note questions and gaps in the literature

4. **FOLLOW LEADS** - Expand the search:
   - Get citations of important papers (who built on this?)
   - Get references from papers (what is this built on?)
   - Use recommendations for similar papers
   - Explore new subtopics that emerge

5. **SYNTHESIZE** - Create outputs:
   - Generate progress reports
   - Summarize findings by subtopic
   - Export references and notes

## Communication Guidelines

- **Be proactive**: Share interesting findings, potential connections, and insights as you discover them
- **Ask questions**: Clarify research scope, priorities, and preferences
- **Report progress**: Regularly update on what you've found and what's next
- **Be thorough**: Don't just find papers - analyze them and extract value
- **Stay organized**: Use subtopics and tags effectively

## Important Notes

- Always add discovered papers to the collection for tracking
- Prioritize quality over quantity - focus on highly relevant papers
- Look for survey papers and literature reviews on the topic
- Pay attention to "Related Work" sections for leads
- Consider publication venue and citation count as quality signals

You are the user's research partner. Be thorough, insightful, and communicative throughout the research process.
"""


class SDKLiteratureReviewAgent:
    """
    Literature Review Agent using Claude Agent SDK.

    This agent uses the SDK's agentic loop with custom MCP tools
    for comprehensive literature review capabilities.
    """

    def __init__(
        self,
        config: Config | None = None,
        data_dir: Path | None = None,
        output_dir: Path | None = None,
    ):
        """Initialize the SDK-based Literature Review Agent.

        Args:
            config: Configuration object
            data_dir: Directory for research data
            output_dir: Directory for output files
        """
        self.config = config or load_config()
        self.data_dir = data_dir or self.config.data_dir
        self.output_dir = output_dir or self.config.output_dir

        # Ensure directories exist
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        setup_logging(level=self.config.log_level)
        self.logger = get_logger("sdk_agent")

        # Create MCP server with all tools
        self.mcp_server = create_literature_review_server(
            data_dir=self.data_dir,
            output_dir=self.output_dir,
            arxiv_max_results=self.config.search.arxiv_max_results,
            semantic_scholar_max_results=self.config.search.semantic_scholar_max_results,
        )

        # Conversation history for context
        self._conversation_history: list[dict] = []

    def _get_allowed_tools(self) -> list[str]:
        """Get list of allowed tools for the agent."""
        return ALL_LITERATURE_REVIEW_TOOLS + BUILT_IN_TOOLS

    async def query(
        self,
        prompt: str,
        on_message: Callable[[str], None] | None = None,
        on_tool_use: Callable[[str, dict], None] | None = None,
    ) -> str:
        """
        Send a query to the agent and get a response.

        Args:
            prompt: The user's query or instruction
            on_message: Callback for text messages from the agent
            on_tool_use: Callback for tool usage (tool_name, args)

        Returns:
            The agent's final text response
        """
        self.logger.info(f"Query: {prompt[:100]}...")

        # Build options
        options = ClaudeCodeOptions(
            system_prompt=LITERATURE_REVIEW_SYSTEM_PROMPT,
            allowed_tools=self._get_allowed_tools(),
            mcp_servers={"literature-review": self.mcp_server},
            cwd=str(self.data_dir),
        )

        response_text = []

        try:
            async for message in query(prompt=prompt, options=options):
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            text = block.text
                            response_text.append(text)
                            if on_message:
                                on_message(text)
                        elif isinstance(block, ToolUseBlock):
                            if on_tool_use:
                                on_tool_use(block.name, block.input)
                            self.logger.debug(f"Tool: {block.name}")

                elif isinstance(message, ResultMessage):
                    self.logger.info(
                        f"Query complete. Tokens: {message.usage.input_tokens} in, "
                        f"{message.usage.output_tokens} out"
                    )

        except Exception as e:
            self.logger.error(f"Query error: {e}")
            raise

        return "\n".join(response_text)

    async def run_interactive(
        self,
        on_message: Callable[[str], None] | None = None,
        get_input: Callable[[str], str] | None = None,
    ) -> None:
        """
        Run the agent in interactive mode.

        Args:
            on_message: Callback for agent messages
            get_input: Callback for getting user input
        """
        # Default callbacks
        if on_message is None:
            on_message = lambda msg: print(f"\n{msg}")

        if get_input is None:
            get_input = lambda prompt: input(f"\n{prompt}: ")

        on_message("Welcome to the Literature Review Agent!")
        on_message(
            "I'll help you conduct a comprehensive literature review.\n"
            "Tell me about your research topic, or ask me to do something like:\n"
            "- 'Search arXiv for papers on transformer architectures'\n"
            "- 'Process my bookmarks file at ~/bookmarks.md'\n"
            "- 'Show me the reading queue'\n"
            "- 'Generate a progress report'\n"
            "\nType 'exit' or 'quit' to end the session."
        )

        while True:
            try:
                user_input = get_input("You")

                if user_input.lower() in ["exit", "quit", "q"]:
                    on_message("Goodbye! Your research data has been saved.")
                    break

                if not user_input.strip():
                    continue

                # Query the agent
                def handle_tool(name: str, args: dict):
                    print(f"  [Using: {name}]")

                response = await self.query(
                    prompt=user_input,
                    on_message=on_message,
                    on_tool_use=handle_tool,
                )

            except KeyboardInterrupt:
                on_message("\nInterrupted. Your research data has been saved.")
                break
            except Exception as e:
                on_message(f"Error: {e}")
                self.logger.error(f"Interactive error: {e}")

    async def gather_references(
        self,
        topic: str,
        sources: list[dict] | None = None,
        on_progress: Callable[[str], None] | None = None,
    ) -> int:
        """
        Gather references on a topic from various sources.

        Args:
            topic: Research topic description
            sources: List of source configs (optional)
            on_progress: Progress callback

        Returns:
            Number of references found
        """
        prompt = f"""Please gather references for a literature review on:

{topic}

Steps to follow:
1. Search arXiv for relevant preprints
2. Search Semantic Scholar for published papers
3. Process any provided sources
4. Report what you found

Focus on finding high-quality, relevant papers. Add all found papers to the collection.
"""

        if sources:
            source_details = "\n".join(
                f"- {s['type']}: {s.get('path') or s.get('url')}"
                for s in sources
            )
            prompt += f"\n\nAlso process these sources:\n{source_details}"

        await self.query(
            prompt=prompt,
            on_message=on_progress,
        )

        # Get count from reference stats
        from .sdk_tools.reference_tools import get_ref_manager
        manager = get_ref_manager()
        return len(manager.get_all())

    async def organize_references(
        self,
        on_progress: Callable[[str], None] | None = None,
    ) -> None:
        """
        Organize collected references by relevance and subtopics.

        Args:
            on_progress: Progress callback
        """
        prompt = """Please organize the collected references:

1. Review the current reference collection (use get_reference_stats)
2. Identify main themes and create appropriate subtopics
3. Assign high-priority papers to the reading queue
4. Provide a summary of the organization

Use the subtopic and reference management tools to organize everything properly.
"""

        await self.query(
            prompt=prompt,
            on_message=on_progress,
        )

    async def read_papers(
        self,
        count: int = 5,
        on_progress: Callable[[str], None] | None = None,
    ) -> int:
        """
        Read and analyze papers from the reading queue.

        Args:
            count: Number of papers to read
            on_progress: Progress callback

        Returns:
            Number of papers processed
        """
        prompt = f"""Please read and analyze the top {count} papers from the reading queue:

1. Get the reading queue (use get_reading_queue)
2. For each paper:
   - Fetch and read the content (use fetch_webpage_content or WebFetch)
   - Create detailed notes (key findings, methodology, quotes)
   - Update the reference status to 'completed'
   - Follow important citations if you find them
3. Summarize what you learned

Focus on extracting valuable insights and connections between papers.
"""

        await self.query(
            prompt=prompt,
            on_message=on_progress,
        )

        from .sdk_tools.reference_tools import get_ref_manager
        from .models import ReferenceStatus
        manager = get_ref_manager()
        completed = manager.get_by_status(ReferenceStatus.COMPLETED)
        return len(completed)

    async def generate_report(
        self,
        on_progress: Callable[[str], None] | None = None,
    ) -> Path:
        """
        Generate the literature review report.

        Args:
            on_progress: Progress callback

        Returns:
            Path to generated report
        """
        prompt = """Please generate a comprehensive literature review report:

1. Generate a progress report showing current status
2. For each subtopic, summarize the key findings
3. Export the references to markdown format
4. Create a BibTeX export for citations

Provide a high-level synthesis of what the literature shows.
"""

        await self.query(
            prompt=prompt,
            on_message=on_progress,
        )

        return self.output_dir / "literature_export.md"


async def run_sdk_agent_interactive(
    data_dir: Path | None = None,
    output_dir: Path | None = None,
) -> None:
    """
    Convenience function to run the SDK agent interactively.

    Args:
        data_dir: Data directory
        output_dir: Output directory
    """
    agent = SDKLiteratureReviewAgent(
        data_dir=data_dir,
        output_dir=output_dir,
    )
    await agent.run_interactive()


def main():
    """CLI entry point for interactive mode."""
    anyio.run(run_sdk_agent_interactive)


if __name__ == "__main__":
    main()
