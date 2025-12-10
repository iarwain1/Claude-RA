"""Report generator for synthesizing literature review findings."""

from datetime import datetime
from pathlib import Path
from typing import Optional

from anthropic import Anthropic

from ..models import Reference, Note, SubTopic, ResearchProject
from ..utils.logging import get_logger
from ..utils.text import truncate_text


class ReportGenerator:
    """Generates literature review reports and syntheses."""

    def __init__(
        self,
        api_key: str,
        model: str = "claude-sonnet-4-20250514",
    ):
        """Initialize the report generator.

        Args:
            api_key: Anthropic API key
            model: Model to use for generation
        """
        self.logger = get_logger("report_generator")
        self.client = Anthropic(api_key=api_key)
        self.model = model

    async def generate_subtopic_summary(
        self,
        subtopic: SubTopic,
        references: list[Reference],
        notes: list[Note],
    ) -> str:
        """Generate a summary for a subtopic.

        Args:
            subtopic: Subtopic to summarize
            references: References in this subtopic
            notes: Notes related to this subtopic

        Returns:
            Summary text
        """
        # Build context
        refs_text = []
        for ref in references[:15]:
            ref_info = f"- {ref.title}"
            if ref.year:
                ref_info += f" ({ref.year})"
            if ref.abstract:
                ref_info += f"\n  Abstract: {ref.abstract[:300]}..."
            refs_text.append(ref_info)

        notes_text = []
        for note in notes[:20]:
            notes_text.append(f"- [{note.note_type}] {note.content}")
            if note.quote:
                notes_text.append(f'  > "{note.quote[:200]}..."')

        prompt = f"""Write a comprehensive summary for this subtopic of a literature review.

SUBTOPIC: {subtopic.name}
DESCRIPTION: {subtopic.description}

KEY REFERENCES ({len(references)} total):
{chr(10).join(refs_text)}

RESEARCH NOTES:
{chr(10).join(notes_text)}

KEY FINDINGS IDENTIFIED:
{chr(10).join('- ' + f for f in subtopic.key_findings) if subtopic.key_findings else 'None yet'}

OPEN QUESTIONS:
{chr(10).join('- ' + q for q in subtopic.open_questions) if subtopic.open_questions else 'None yet'}

Write a well-organized summary (400-600 words) that:
1. Introduces the subtopic and its relevance
2. Synthesizes the main themes and findings from the literature
3. Highlights key debates or areas of disagreement
4. Identifies gaps in the current research
5. Notes important methodological approaches

Use academic writing style. Reference specific papers when making claims."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}],
            )

            return response.content[0].text.strip()

        except Exception as e:
            self.logger.error(f"Error generating subtopic summary: {e}")
            return ""

    async def generate_full_report(
        self,
        project: ResearchProject,
        subtopics: list[SubTopic],
        references: list[Reference],
        notes: list[Note],
        output_path: Optional[Path] = None,
    ) -> str:
        """Generate a full literature review report.

        Args:
            project: Research project
            subtopics: All subtopics
            references: All references
            notes: All notes
            output_path: Path to save report (optional)

        Returns:
            Report text
        """
        report_parts = []

        # Title and metadata
        report_parts.append(f"# Literature Review: {project.topic.name}\n")
        report_parts.append(f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
        report_parts.append(f"*Total References: {len(references)}*\n\n")

        # Research overview
        report_parts.append("## Research Overview\n\n")
        report_parts.append(f"{project.topic.description}\n\n")

        if project.topic.key_questions:
            report_parts.append("### Key Research Questions\n\n")
            for q in project.topic.key_questions:
                report_parts.append(f"- {q}\n")
            report_parts.append("\n")

        # Executive summary
        exec_summary = await self._generate_executive_summary(
            project, subtopics, references, notes
        )
        report_parts.append("## Executive Summary\n\n")
        report_parts.append(f"{exec_summary}\n\n")

        # Subtopic sections
        for subtopic in subtopics:
            if subtopic.parent_id is None:  # Root subtopics only
                report_parts.append(f"## {subtopic.name}\n\n")

                # Get references and notes for this subtopic
                subtopic_refs = [r for r in references if subtopic.id in r.subtopics or subtopic.name in r.subtopics]
                subtopic_notes = [n for n in notes if n.reference_id in [r.id for r in subtopic_refs]]

                # Generate or use existing summary
                if subtopic.summary:
                    report_parts.append(f"{subtopic.summary}\n\n")
                else:
                    summary = await self.generate_subtopic_summary(
                        subtopic, subtopic_refs, subtopic_notes
                    )
                    report_parts.append(f"{summary}\n\n")

                # Key findings
                if subtopic.key_findings:
                    report_parts.append("### Key Findings\n\n")
                    for finding in subtopic.key_findings:
                        report_parts.append(f"- {finding}\n")
                    report_parts.append("\n")

                # Key references
                if subtopic_refs:
                    report_parts.append("### Key References\n\n")
                    for ref in sorted(subtopic_refs, key=lambda r: r.priority.value if r.priority else "z")[:10]:
                        authors = ", ".join(a.name for a in ref.authors[:3]) if ref.authors else "Unknown"
                        year = f" ({ref.year})" if ref.year else ""
                        report_parts.append(f"- **{ref.title}** - {authors}{year}\n")
                    report_parts.append("\n")

        # Open questions and future directions
        all_questions = []
        for subtopic in subtopics:
            all_questions.extend(subtopic.open_questions)

        if all_questions:
            report_parts.append("## Open Questions and Future Directions\n\n")
            for q in all_questions:
                report_parts.append(f"- {q}\n")
            report_parts.append("\n")

        # Bibliography
        report_parts.append("## Bibliography\n\n")
        for ref in sorted(references, key=lambda r: (r.authors[0].name if r.authors else "ZZZ", r.year or 9999)):
            citation = self._format_citation(ref)
            report_parts.append(f"- {citation}\n")

        report = "".join(report_parts)

        # Save if path provided
        if output_path:
            output_path.parent.mkdir(parents=True, exist_ok=True)
            output_path.write_text(report)
            self.logger.info(f"Report saved to {output_path}")

        return report

    async def _generate_executive_summary(
        self,
        project: ResearchProject,
        subtopics: list[SubTopic],
        references: list[Reference],
        notes: list[Note],
    ) -> str:
        """Generate executive summary.

        Args:
            project: Research project
            subtopics: Subtopics
            references: References
            notes: Notes

        Returns:
            Executive summary text
        """
        # Collect key findings across all subtopics
        all_findings = []
        for st in subtopics:
            all_findings.extend(st.key_findings)

        # Get key finding notes
        key_notes = [n for n in notes if n.note_type == "key_finding"][:20]

        subtopics_text = "\n".join(f"- {st.name}: {st.description}" for st in subtopics[:10])
        findings_text = "\n".join(f"- {f}" for f in all_findings[:15])
        notes_text = "\n".join(f"- {n.content}" for n in key_notes)

        prompt = f"""Write an executive summary for this literature review.

RESEARCH TOPIC: {project.topic.name}
DESCRIPTION: {project.topic.description}

SUBTOPICS COVERED:
{subtopics_text}

KEY FINDINGS FROM RESEARCH:
{findings_text}

KEY NOTES:
{notes_text}

STATISTICS:
- Total references reviewed: {len(references)}
- Subtopics identified: {len(subtopics)}
- Notes taken: {len(notes)}

Write a concise executive summary (200-300 words) that:
1. States the purpose and scope of the review
2. Summarizes the main themes discovered
3. Highlights the most significant findings
4. Notes any major gaps or contradictions in the literature
5. Briefly indicates implications for future research"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=800,
                messages=[{"role": "user", "content": prompt}],
            )

            return response.content[0].text.strip()

        except Exception as e:
            self.logger.error(f"Error generating executive summary: {e}")
            return "Executive summary generation failed."

    def _format_citation(self, ref: Reference) -> str:
        """Format a reference as a citation.

        Args:
            ref: Reference to format

        Returns:
            Formatted citation string
        """
        parts = []

        # Authors
        if ref.authors:
            if len(ref.authors) == 1:
                parts.append(ref.authors[0].name)
            elif len(ref.authors) == 2:
                parts.append(f"{ref.authors[0].name} & {ref.authors[1].name}")
            else:
                parts.append(f"{ref.authors[0].name} et al.")

        # Year
        if ref.year:
            parts.append(f"({ref.year})")

        # Title
        parts.append(f"*{ref.title}*")

        # Venue
        if ref.venue:
            parts.append(f"{ref.venue}")

        # URL/DOI
        if ref.doi:
            parts.append(f"https://doi.org/{ref.doi}")
        elif ref.url:
            parts.append(ref.url)

        return ". ".join(parts)

    async def generate_progress_report(
        self,
        project: ResearchProject,
        references: list[Reference],
        notes: list[Note],
    ) -> str:
        """Generate a progress report for the research.

        Args:
            project: Research project
            references: Current references
            notes: Current notes

        Returns:
            Progress report text
        """
        from ..models import ReferenceStatus, Priority

        # Calculate statistics
        total_refs = len(references)
        by_status = {}
        for status in ReferenceStatus:
            by_status[status.value] = len([r for r in references if r.status == status])

        by_priority = {}
        for priority in Priority:
            by_priority[priority.value] = len([r for r in references if r.priority == priority])

        report = f"""# Progress Report: {project.topic.name}

*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*

## Current Phase: {project.phase}

## Reference Statistics

- **Total References**: {total_refs}
- Discovered: {by_status.get('discovered', 0)}
- Queued for reading: {by_status.get('queued', 0)}
- Currently reading: {by_status.get('reading', 0)}
- Completed: {by_status.get('completed', 0)}
- Skipped: {by_status.get('skipped', 0)}

## Priority Distribution

- Critical: {by_priority.get('critical', 0)}
- High: {by_priority.get('high', 0)}
- Medium: {by_priority.get('medium', 0)}
- Low: {by_priority.get('low', 0)}

## Notes Taken

- Total notes: {len(notes)}
- Key findings: {len([n for n in notes if n.note_type == 'key_finding'])}
- Questions: {len([n for n in notes if n.note_type == 'question'])}

## Recent Activity

"""

        # Add recent references
        recent_refs = sorted(references, key=lambda r: r.discovered_at, reverse=True)[:5]
        report += "### Recently Added References\n\n"
        for ref in recent_refs:
            report += f"- {ref.title}\n"

        # Add notes from agent
        if project.notes_to_user:
            report += "\n### Agent Notes\n\n"
            for note in project.notes_to_user[-5:]:
                report += f"- {note}\n"

        return report
