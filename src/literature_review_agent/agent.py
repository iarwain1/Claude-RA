"""
Main Literature Review Agent - orchestrates the entire research process.

This agent coordinates:
1. Gathering references from various sources
2. Organizing and prioritizing references
3. Reading and analyzing documents
4. Taking notes and following citation trails
5. Synthesizing findings into reports
6. Communicating with the user throughout
"""

import asyncio
from datetime import datetime
from pathlib import Path
from typing import Optional, Callable, Any
import uuid

from anthropic import Anthropic

from .models import (
    Reference,
    ResearchProject,
    ResearchTopic,
    SourceConfig,
    SubTopic,
    ReferenceStatus,
    Priority,
    AgentMessage,
)
from .collectors import (
    URLCollector,
    ArxivCollector,
    SemanticScholarCollector,
    WebCollector,
    BlogCollector,
    LocalFileCollector,
)
from .managers import ReferenceManager, NoteManager, SubtopicManager
from .processors import DocumentReader, DocumentAnalyzer, ReportGenerator
from .utils.config import Config, load_config
from .utils.logging import setup_logging, get_logger
from .utils.persistence import save_project, load_project


class LiteratureReviewAgent:
    """
    Main agent for conducting comprehensive literature reviews.

    This agent acts as an AI-powered research assistant, helping users:
    - Discover relevant references from multiple sources
    - Organize literature by topics and subtopics
    - Read and analyze papers, taking detailed notes
    - Follow citation trails to find related work
    - Synthesize findings into comprehensive reports

    The agent communicates extensively with the user throughout the process,
    asking questions, providing updates, and seeking feedback.
    """

    def __init__(
        self,
        config: Optional[Config] = None,
        message_callback: Optional[Callable[[AgentMessage], None]] = None,
        input_callback: Optional[Callable[[str, list[str] | None], str]] = None,
    ):
        """Initialize the Literature Review Agent.

        Args:
            config: Configuration object (loads defaults if not provided)
            message_callback: Callback for agent messages to user
            input_callback: Callback for getting user input (prompt, options) -> response
        """
        self.config = config or load_config()
        self.config.setup_directories()

        setup_logging(level=self.config.log_level)
        self.logger = get_logger("agent")

        # Communication callbacks
        self._message_callback = message_callback
        self._input_callback = input_callback

        # Initialize components
        self._init_collectors()
        self._init_managers()
        self._init_processors()

        # Current project state
        self.project: Optional[ResearchProject] = None

    def _init_collectors(self) -> None:
        """Initialize source collectors."""
        self.url_collector = URLCollector()
        self.arxiv_collector = ArxivCollector(
            max_results=self.config.search.arxiv_max_results
        )
        self.semantic_scholar = SemanticScholarCollector(
            max_results=self.config.search.semantic_scholar_max_results
        )
        self.web_collector = WebCollector()
        self.blog_collector = BlogCollector()
        self.local_collector = LocalFileCollector()

    def _init_managers(self) -> None:
        """Initialize data managers."""
        self.ref_manager = ReferenceManager(self.config.data_dir)
        self.note_manager = NoteManager(self.config.data_dir)
        self.subtopic_manager = SubtopicManager(self.config.data_dir)

    def _init_processors(self) -> None:
        """Initialize document processors."""
        if not self.config.llm.api_key:
            self.logger.warning("No API key configured - analysis features disabled")
            self.doc_reader = DocumentReader(cache_dir=self.config.data_dir / "pdfs")
            self.analyzer = None
            self.report_gen = None
        else:
            self.doc_reader = DocumentReader(cache_dir=self.config.data_dir / "pdfs")
            self.analyzer = DocumentAnalyzer(
                api_key=self.config.llm.api_key,
                model=self.config.llm.model,
            )
            self.report_gen = ReportGenerator(
                api_key=self.config.llm.api_key,
                model=self.config.llm.model,
            )

    # ==================== Communication Methods ====================

    def _send_message(
        self,
        content: str,
        message_type: str = "update",
        requires_response: bool = False,
        options: list[str] | None = None,
    ) -> None:
        """Send a message to the user.

        Args:
            content: Message content
            message_type: Type of message
            requires_response: Whether response is required
            options: Multiple choice options if applicable
        """
        message = AgentMessage(
            message_type=message_type,
            content=content,
            requires_response=requires_response,
            options=options,
        )

        if self._message_callback:
            self._message_callback(message)
        else:
            # Default: print to console
            prefix = {
                "update": "[Update]",
                "question": "[Question]",
                "insight": "[Insight]",
                "request_feedback": "[Feedback Request]",
                "summary": "[Summary]",
            }.get(message_type, "[Agent]")
            print(f"\n{prefix} {content}")

    def _get_input(
        self,
        prompt: str,
        options: list[str] | None = None,
    ) -> str:
        """Get input from the user.

        Args:
            prompt: Prompt to display
            options: Multiple choice options

        Returns:
            User's response
        """
        if self._input_callback:
            return self._input_callback(prompt, options)
        else:
            # Default: use standard input
            if options:
                print(f"\n{prompt}")
                for i, opt in enumerate(options, 1):
                    print(f"  {i}. {opt}")
                response = input("Enter choice (number or text): ").strip()
                # Handle numeric selection
                try:
                    idx = int(response) - 1
                    if 0 <= idx < len(options):
                        return options[idx]
                except ValueError:
                    pass
                return response
            else:
                return input(f"\n{prompt}: ").strip()

    def _ask_confirmation(self, question: str) -> bool:
        """Ask for yes/no confirmation.

        Args:
            question: Question to ask

        Returns:
            True if confirmed
        """
        response = self._get_input(question, options=["Yes", "No"])
        return response.lower() in ["yes", "y", "1"]

    # ==================== Project Management ====================

    async def start_new_project(
        self,
        topic_name: str,
        topic_description: str,
        key_questions: list[str] | None = None,
        key_terms: list[str] | None = None,
    ) -> ResearchProject:
        """Start a new literature review project.

        Args:
            topic_name: Name of the research topic
            topic_description: Detailed description
            key_questions: Key research questions to address
            key_terms: Key search terms

        Returns:
            Created ResearchProject
        """
        self._send_message(
            f"Starting new literature review project: {topic_name}",
            message_type="update"
        )

        topic = ResearchTopic(
            name=topic_name,
            description=topic_description,
            key_questions=key_questions or [],
            key_terms=key_terms or [],
        )

        self.project = ResearchProject(
            id=str(uuid.uuid4())[:8],
            name=topic_name,
            topic=topic,
            phase="initialization",
        )

        # Save project
        save_project(self.project, self.config.data_dir / "project")

        self._send_message(
            "Project initialized. Let me know about your sources:\n"
            "- Do you have URL lists or bookmarks to process?\n"
            "- Any blogs or newsletters to search?\n"
            "- Local notes or documents (e.g., Obsidian vault)?",
            message_type="question",
            requires_response=True,
        )

        return self.project

    async def load_existing_project(self, project_dir: Path) -> Optional[ResearchProject]:
        """Load an existing project.

        Args:
            project_dir: Directory containing project data

        Returns:
            Loaded project or None
        """
        project = load_project(project_dir)
        if project:
            self.project = project
            self._send_message(
                f"Loaded project: {project.name}\n"
                f"Phase: {project.phase}\n"
                f"References: {len(self.ref_manager.get_all())}",
                message_type="update"
            )
        return project

    # ==================== Source Collection ====================

    async def add_source(self, source: SourceConfig) -> None:
        """Add a source configuration to the project.

        Args:
            source: Source configuration
        """
        if self.project:
            self.project.sources.append(source)
            save_project(self.project, self.config.data_dir / "project")
            self._send_message(f"Added source: {source.name}", message_type="update")

    async def gather_references(self) -> int:
        """Gather references from all configured sources.

        Returns:
            Number of new references found
        """
        if not self.project:
            self._send_message("No project loaded. Start a new project first.", message_type="update")
            return 0

        self._send_message(
            "Starting reference gathering phase...",
            message_type="update"
        )

        self.project.phase = "gathering"
        total_new = 0

        # Process each source
        for source in self.project.sources:
            self._send_message(f"Processing source: {source.name}", message_type="update")

            try:
                if source.source_type == "url_list":
                    result = await self.url_collector.collect(
                        file_paths=[Path(source.path)] if source.path else None,
                        urls=[source.url] if source.url else None,
                    )
                elif source.source_type == "blog":
                    result = await self.blog_collector.collect(
                        feed_urls=[source.rss_feed] if source.rss_feed else None,
                        blog_urls=[source.url] if source.url else None,
                    )
                elif source.source_type == "notes_folder":
                    result = await self.local_collector.collect(
                        paths=[Path(source.path)] if source.path else None,
                    )
                else:
                    self._send_message(f"Unknown source type: {source.source_type}", message_type="update")
                    continue

                new, updated = self.ref_manager.add_batch(result.references)
                total_new += new

                self._send_message(
                    f"  Found {len(result.references)} references ({new} new, {updated} updated)",
                    message_type="update"
                )

                if result.errors:
                    for error in result.errors[:3]:
                        self._send_message(f"  Warning: {error}", message_type="update")

            except Exception as e:
                self._send_message(f"Error processing {source.name}: {e}", message_type="update")

        # Search academic databases
        if self.config.search.arxiv_enabled:
            await self._search_arxiv()

        if self.config.search.semantic_scholar_enabled:
            await self._search_semantic_scholar()

        total_refs = len(self.ref_manager.get_all())
        self._send_message(
            f"\nReference gathering complete!\n"
            f"Total references: {total_refs}\n"
            f"New references added: {total_new}",
            message_type="summary"
        )

        return total_new

    async def _search_arxiv(self) -> None:
        """Search arXiv for relevant papers."""
        if not self.project:
            return

        self._send_message("Searching arXiv...", message_type="update")

        # Build search queries from topic and key terms
        queries = [self.project.topic.name]
        queries.extend(self.project.topic.key_terms[:3])

        for query in queries:
            try:
                result = await self.arxiv_collector.search(
                    query=query,
                    max_results=self.config.search.arxiv_max_results // len(queries),
                )
                new, _ = self.ref_manager.add_batch(result.references)
                self._send_message(f"  arXiv '{query}': {new} new references", message_type="update")
            except Exception as e:
                self._send_message(f"  arXiv search error: {e}", message_type="update")

    async def _search_semantic_scholar(self) -> None:
        """Search Semantic Scholar for relevant papers."""
        if not self.project:
            return

        self._send_message("Searching Semantic Scholar...", message_type="update")

        try:
            result = await self.semantic_scholar.search(
                query=self.project.topic.name,
                max_results=self.config.search.semantic_scholar_max_results,
            )
            new, _ = self.ref_manager.add_batch(result.references)
            self._send_message(f"  Semantic Scholar: {new} new references", message_type="update")
        except Exception as e:
            self._send_message(f"  Semantic Scholar search error: {e}", message_type="update")

    # ==================== Organization ====================

    async def organize_references(self) -> None:
        """Organize references by relevance and subtopics."""
        if not self.project:
            return

        self._send_message(
            "Organizing references by relevance and subtopics...",
            message_type="update"
        )

        self.project.phase = "organizing"
        references = self.ref_manager.get_all()

        # Evaluate relevance for unprocessed references
        unprocessed = [r for r in references if r.priority == Priority.UNKNOWN]

        if unprocessed and self.analyzer:
            self._send_message(
                f"Evaluating relevance of {len(unprocessed)} references...",
                message_type="update"
            )

            for i, ref in enumerate(unprocessed):
                if i % 10 == 0:
                    self._send_message(f"  Progress: {i}/{len(unprocessed)}", message_type="update")

                try:
                    priority, score, explanation = await self.analyzer.evaluate_relevance(
                        ref,
                        self.project.topic.description,
                        self.project.topic.key_questions,
                    )
                    self.ref_manager.update_priority(ref.id, priority, explanation)
                except Exception as e:
                    self.logger.warning(f"Error evaluating {ref.id}: {e}")

        # Suggest subtopics
        if self.analyzer:
            await self._suggest_subtopics()

        # Queue high-priority references for reading
        high_priority = self.ref_manager.get_by_priority(Priority.CRITICAL)
        high_priority.extend(self.ref_manager.get_by_priority(Priority.HIGH))

        for ref in high_priority:
            if ref.status == ReferenceStatus.DISCOVERED:
                self.ref_manager.update_status(ref.id, ReferenceStatus.QUEUED)

        queue_size = len(self.ref_manager.get_reading_queue())
        self._send_message(
            f"Organization complete!\n"
            f"Reading queue: {queue_size} papers",
            message_type="summary"
        )

    async def _suggest_subtopics(self) -> None:
        """Use LLM to suggest subtopics."""
        if not self.analyzer or not self.project:
            return

        self._send_message("Analyzing references to suggest subtopics...", message_type="update")

        references = self.ref_manager.get_all()
        existing = [st.name for st in self.subtopic_manager.get_all()]

        try:
            suggestions = await self.analyzer.suggest_subtopics(
                references,
                self.project.topic.description,
                existing,
            )

            if suggestions:
                self._send_message(
                    "Suggested subtopics based on the literature:",
                    message_type="insight"
                )

                for sugg in suggestions:
                    self._send_message(
                        f"  - {sugg['name']}: {sugg['description']}",
                        message_type="update"
                    )

                if self._ask_confirmation("Would you like me to create these subtopics?"):
                    for sugg in suggestions:
                        self.subtopic_manager.create(
                            name=sugg["name"],
                            description=sugg["description"],
                            tags=sugg.get("key_terms", []),
                        )
                    self._send_message(
                        f"Created {len(suggestions)} subtopics",
                        message_type="update"
                    )

        except Exception as e:
            self._send_message(f"Error suggesting subtopics: {e}", message_type="update")

    # ==================== Reading & Analysis ====================

    async def read_papers(self, max_papers: int = 10) -> int:
        """Read and analyze papers from the queue.

        Args:
            max_papers: Maximum papers to read in this session

        Returns:
            Number of papers processed
        """
        if not self.project:
            return 0

        self._send_message(
            f"Starting reading session (up to {max_papers} papers)...",
            message_type="update"
        )

        self.project.phase = "reading"
        queue = self.ref_manager.get_reading_queue()[:max_papers]

        if not queue:
            self._send_message("Reading queue is empty!", message_type="update")
            return 0

        processed = 0

        for ref in queue:
            self._send_message(f"\nReading: {ref.title}", message_type="update")
            self.ref_manager.update_status(ref.id, ReferenceStatus.READING)

            try:
                # Read the document
                text = await self.doc_reader.read(ref)

                if not text:
                    self._send_message("  Could not access full text", message_type="update")
                    self.ref_manager.update_status(ref.id, ReferenceStatus.UNAVAILABLE)
                    continue

                # Analyze and take notes
                if self.analyzer:
                    await self._analyze_paper(ref, text)

                # Mark as completed
                self.ref_manager.update_status(ref.id, ReferenceStatus.COMPLETED)
                processed += 1

                # Check for new leads
                if self.config.processing.extract_citations:
                    await self._follow_citations(ref, text)

            except Exception as e:
                self._send_message(f"  Error reading paper: {e}", message_type="update")

        self._send_message(
            f"\nReading session complete!\n"
            f"Papers processed: {processed}",
            message_type="summary"
        )

        return processed

    async def _analyze_paper(self, ref: Reference, text: str) -> None:
        """Analyze a paper and generate notes.

        Args:
            ref: Reference being analyzed
            text: Document text
        """
        if not self.analyzer:
            return

        self._send_message("  Analyzing content...", message_type="update")

        try:
            # Extract key points
            key_points = await self.analyzer.extract_key_points(
                text,
                ref,
                self.project.topic.description if self.project else "",
            )

            # Generate notes
            existing_notes = self.note_manager.get_for_reference(ref.id)
            note_dicts = await self.analyzer.generate_notes(
                text,
                ref,
                self.project.topic.description if self.project else "",
                existing_notes,
            )

            for note_dict in note_dicts:
                self.note_manager.create(
                    reference_id=ref.id,
                    content=note_dict.get("content", ""),
                    quote=note_dict.get("quote"),
                    section=note_dict.get("section"),
                    note_type=note_dict.get("note_type", "general"),
                )

            # Report key findings
            if key_points and "key_findings" in key_points:
                self._send_message(
                    f"  Key findings: {len(key_points['key_findings'])}",
                    message_type="insight"
                )
                for finding in key_points["key_findings"][:2]:
                    self._send_message(f"    - {finding}", message_type="update")

        except Exception as e:
            self._send_message(f"  Analysis error: {e}", message_type="update")

    async def _follow_citations(self, ref: Reference, text: str) -> None:
        """Follow citations to find new references.

        Args:
            ref: Reference being analyzed
            text: Document text
        """
        if not self.analyzer:
            return

        self._send_message("  Extracting citations...", message_type="update")

        try:
            citations = await self.analyzer.identify_citations(text, ref)

            if citations:
                high_importance = [c for c in citations if c.get("importance") == "high"]

                if high_importance:
                    self._send_message(
                        f"  Found {len(high_importance)} potentially important citations",
                        message_type="insight"
                    )

                    # Try to find these papers
                    for cit in high_importance[:5]:
                        title = cit.get("title", "")
                        if title:
                            # Search for the paper
                            result = await self.semantic_scholar.search(
                                query=title,
                                max_results=1,
                            )
                            if result.references:
                                new_ref = result.references[0]
                                new_ref.discovered_from = f"cited_in:{ref.id}"
                                _, was_new = self.ref_manager.add(new_ref)
                                if was_new:
                                    self._send_message(
                                        f"    Added: {new_ref.title[:60]}...",
                                        message_type="update"
                                    )

        except Exception as e:
            self._send_message(f"  Citation extraction error: {e}", message_type="update")

    # ==================== Report Generation ====================

    async def generate_report(
        self,
        output_path: Optional[Path] = None,
    ) -> str:
        """Generate the literature review report.

        Args:
            output_path: Path to save the report

        Returns:
            Report text
        """
        if not self.project:
            return "No project loaded"

        self._send_message(
            "Generating literature review report...",
            message_type="update"
        )

        self.project.phase = "synthesis"

        if not output_path:
            output_path = self.config.output_dir / "reports" / f"{self.project.name}_review.md"

        if self.report_gen:
            report = await self.report_gen.generate_full_report(
                project=self.project,
                subtopics=self.subtopic_manager.get_all(),
                references=self.ref_manager.get_all(),
                notes=self.note_manager.get_all(),
                output_path=output_path,
            )
        else:
            report = self._generate_basic_report(output_path)

        self._send_message(
            f"Report generated: {output_path}",
            message_type="summary"
        )

        return report

    def _generate_basic_report(self, output_path: Path) -> str:
        """Generate a basic report without LLM.

        Args:
            output_path: Path to save report

        Returns:
            Report text
        """
        references = self.ref_manager.get_all()
        notes = self.note_manager.get_all()

        lines = [
            f"# Literature Review: {self.project.name}\n",
            f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n\n",
            f"## Overview\n\n{self.project.topic.description}\n\n",
            f"## References ({len(references)} total)\n\n",
        ]

        for ref in references:
            lines.append(f"### {ref.title}\n")
            if ref.authors:
                lines.append(f"*{', '.join(a.name for a in ref.authors[:3])}*\n")
            if ref.abstract:
                lines.append(f"\n{ref.abstract[:300]}...\n")

            ref_notes = self.note_manager.get_for_reference(ref.id)
            if ref_notes:
                lines.append("\n**Notes:**\n")
                for note in ref_notes:
                    lines.append(f"- {note.content}\n")

            lines.append("\n---\n\n")

        report = "".join(lines)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(report)
        return report

    # ==================== Interactive Research Loop ====================

    async def run_interactive(self) -> None:
        """Run the agent in interactive mode."""
        self._send_message(
            "Welcome to the Literature Review Agent!\n"
            "I'll help you conduct a comprehensive literature review.\n"
            "Let's start by setting up your research project.",
            message_type="update"
        )

        # Get topic from user
        topic_name = self._get_input("What is your research topic?")
        topic_desc = self._get_input(
            "Please describe your research focus in detail.\n"
            "Include key aspects, scope, and any specific areas of interest"
        )

        questions_input = self._get_input(
            "What are your key research questions?\n"
            "(Enter each question on a new line, or 'skip' to continue)"
        )
        key_questions = [q.strip() for q in questions_input.split("\n") if q.strip() and q.lower() != "skip"]

        # Create project
        await self.start_new_project(
            topic_name=topic_name,
            topic_description=topic_desc,
            key_questions=key_questions,
        )

        # Main loop
        while True:
            action = self._get_input(
                "What would you like to do?",
                options=[
                    "Add sources",
                    "Gather references",
                    "Organize references",
                    "Read papers",
                    "Generate report",
                    "View statistics",
                    "Exit",
                ]
            )

            if "add" in action.lower():
                await self._interactive_add_sources()
            elif "gather" in action.lower():
                await self.gather_references()
            elif "organize" in action.lower():
                await self.organize_references()
            elif "read" in action.lower():
                count = self._get_input("How many papers to read?")
                try:
                    await self.read_papers(max_papers=int(count))
                except ValueError:
                    await self.read_papers()
            elif "report" in action.lower():
                await self.generate_report()
            elif "stat" in action.lower():
                self._show_statistics()
            elif "exit" in action.lower():
                self._send_message("Goodbye! Your project has been saved.", message_type="update")
                break

    async def _interactive_add_sources(self) -> None:
        """Interactive source addition."""
        source_type = self._get_input(
            "What type of source?",
            options=[
                "URL list file",
                "Blog/Newsletter",
                "Local notes folder",
                "Cancel",
            ]
        )

        if "cancel" in source_type.lower():
            return

        name = self._get_input("Name for this source:")

        if "url" in source_type.lower():
            path = self._get_input("Path to URL list file:")
            await self.add_source(SourceConfig(
                name=name,
                source_type="url_list",
                path=path,
            ))
        elif "blog" in source_type.lower():
            url = self._get_input("Blog URL or RSS feed URL:")
            await self.add_source(SourceConfig(
                name=name,
                source_type="blog",
                url=url,
                rss_feed=url if "rss" in url.lower() or "feed" in url.lower() else None,
            ))
        elif "notes" in source_type.lower() or "local" in source_type.lower():
            path = self._get_input("Path to notes folder:")
            await self.add_source(SourceConfig(
                name=name,
                source_type="notes_folder",
                path=path,
            ))

    def _show_statistics(self) -> None:
        """Display project statistics."""
        ref_stats = self.ref_manager.get_statistics()
        note_stats = self.note_manager.get_statistics()
        subtopic_stats = self.subtopic_manager.get_statistics()

        self._send_message(
            f"Project Statistics:\n"
            f"\nReferences:\n"
            f"  Total: {ref_stats['total']}\n"
            f"  By status: {ref_stats['by_status']}\n"
            f"  By priority: {ref_stats['by_priority']}\n"
            f"\nNotes:\n"
            f"  Total: {note_stats['total']}\n"
            f"  By type: {note_stats['by_type']}\n"
            f"\nSubtopics:\n"
            f"  Total: {subtopic_stats['total']}\n"
            f"  Key findings: {subtopic_stats['total_findings']}\n"
            f"  Open questions: {subtopic_stats['total_questions']}",
            message_type="summary"
        )

    # ==================== Cleanup ====================

    async def close(self) -> None:
        """Clean up resources."""
        await self.url_collector.close()
        await self.web_collector.close()
        await self.blog_collector.close()
        await self.doc_reader.close()

        if self.project:
            save_project(self.project, self.config.data_dir / "project")
