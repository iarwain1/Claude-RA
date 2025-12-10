"""Document analyzer using LLM for intelligent analysis."""

from typing import Optional
import json

from anthropic import Anthropic

from ..models import Reference, Note, Priority
from ..utils.logging import get_logger
from ..utils.text import truncate_text, count_tokens


class DocumentAnalyzer:
    """Analyzes documents using Claude for intelligent insights."""

    def __init__(
        self,
        api_key: str,
        model: str = "claude-sonnet-4-20250514",
    ):
        """Initialize the analyzer.

        Args:
            api_key: Anthropic API key
            model: Model to use for analysis
        """
        self.logger = get_logger("document_analyzer")
        self.client = Anthropic(api_key=api_key)
        self.model = model

    async def evaluate_relevance(
        self,
        reference: Reference,
        research_topic: str,
        research_questions: list[str],
    ) -> tuple[Priority, float, str]:
        """Evaluate how relevant a reference is to the research topic.

        Args:
            reference: Reference to evaluate
            research_topic: Main research topic description
            research_questions: Key research questions

        Returns:
            Tuple of (priority, relevance_score, explanation)
        """
        # Build context about the reference
        ref_info = f"Title: {reference.title}\n"
        if reference.authors:
            ref_info += f"Authors: {', '.join(a.name for a in reference.authors[:5])}\n"
        if reference.year:
            ref_info += f"Year: {reference.year}\n"
        if reference.abstract:
            ref_info += f"Abstract: {reference.abstract}\n"
        if reference.tags:
            ref_info += f"Tags: {', '.join(reference.tags)}\n"

        questions_str = "\n".join(f"- {q}" for q in research_questions)

        prompt = f"""Evaluate the relevance of this reference to the research topic.

RESEARCH TOPIC:
{research_topic}

KEY RESEARCH QUESTIONS:
{questions_str}

REFERENCE:
{ref_info}

Please evaluate:
1. How relevant is this reference to the research topic? (0.0 to 1.0)
2. What priority should it have for reading? (critical, high, medium, low)
3. Brief explanation of why (2-3 sentences)

Respond in JSON format:
{{
    "relevance_score": 0.0-1.0,
    "priority": "critical|high|medium|low",
    "explanation": "..."
}}"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=500,
                messages=[{"role": "user", "content": prompt}],
            )

            result_text = response.content[0].text

            # Extract JSON from response
            start = result_text.find("{")
            end = result_text.rfind("}") + 1
            if start >= 0 and end > start:
                result = json.loads(result_text[start:end])
                priority_map = {
                    "critical": Priority.CRITICAL,
                    "high": Priority.HIGH,
                    "medium": Priority.MEDIUM,
                    "low": Priority.LOW,
                }
                return (
                    priority_map.get(result["priority"], Priority.MEDIUM),
                    float(result["relevance_score"]),
                    result["explanation"],
                )

        except Exception as e:
            self.logger.error(f"Error evaluating relevance: {e}")

        return Priority.UNKNOWN, 0.0, "Could not evaluate relevance"

    async def extract_key_points(
        self,
        text: str,
        reference: Reference,
        research_topic: str,
    ) -> list[dict]:
        """Extract key points from document text.

        Args:
            text: Document text
            reference: Reference being analyzed
            research_topic: Research topic for context

        Returns:
            List of key point dictionaries
        """
        # Truncate text if too long
        text = truncate_text(text, 30000)  # ~30k tokens max

        prompt = f"""Analyze this document and extract key points relevant to the research topic.

RESEARCH TOPIC: {research_topic}

DOCUMENT TITLE: {reference.title}

DOCUMENT TEXT:
{text}

Extract:
1. Key findings (3-5 most important findings)
2. Methodology highlights (if applicable)
3. Relevant quotes (2-3 important quotes with page references if available)
4. Connections to the research topic
5. Potential follow-up leads (other papers mentioned, open questions)

Respond in JSON format:
{{
    "key_findings": ["finding1", "finding2", ...],
    "methodology": ["method1", "method2", ...],
    "quotes": [{{"text": "...", "context": "..."}}],
    "connections": ["connection1", ...],
    "follow_up_leads": ["lead1", ...]
}}"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}],
            )

            result_text = response.content[0].text

            start = result_text.find("{")
            end = result_text.rfind("}") + 1
            if start >= 0 and end > start:
                return json.loads(result_text[start:end])

        except Exception as e:
            self.logger.error(f"Error extracting key points: {e}")

        return {}

    async def generate_notes(
        self,
        text: str,
        reference: Reference,
        research_topic: str,
        existing_notes: list[Note] = None,
    ) -> list[dict]:
        """Generate research notes from document.

        Args:
            text: Document text
            reference: Reference being analyzed
            research_topic: Research topic
            existing_notes: Existing notes to avoid duplication

        Returns:
            List of note dictionaries
        """
        text = truncate_text(text, 25000)

        existing_content = ""
        if existing_notes:
            existing_content = "\n".join(f"- {n.content}" for n in existing_notes[:10])
            existing_content = f"\n\nEXISTING NOTES (avoid duplicating):\n{existing_content}"

        prompt = f"""Generate detailed research notes from this document.

RESEARCH TOPIC: {research_topic}

DOCUMENT: {reference.title}

TEXT:
{text}
{existing_content}

Generate comprehensive notes in the following categories:
- key_finding: Important discoveries or claims
- methodology: Research methods used
- critique: Potential weaknesses or limitations
- connection: Links to other work or concepts
- question: Questions raised by the content
- quote: Important direct quotes

For each note, include:
- content: The note content
- note_type: Category from above
- quote: Relevant quote from the text (if applicable)
- section: Which section it's from (if identifiable)

Respond as JSON array:
[{{"content": "...", "note_type": "...", "quote": "...", "section": "..."}}]"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=3000,
                messages=[{"role": "user", "content": prompt}],
            )

            result_text = response.content[0].text

            start = result_text.find("[")
            end = result_text.rfind("]") + 1
            if start >= 0 and end > start:
                return json.loads(result_text[start:end])

        except Exception as e:
            self.logger.error(f"Error generating notes: {e}")

        return []

    async def identify_citations(
        self,
        text: str,
        reference: Reference,
    ) -> list[dict]:
        """Identify and extract citation information from text.

        Args:
            text: Document text
            reference: Reference being analyzed

        Returns:
            List of citation dictionaries
        """
        # Focus on Related Work and References sections
        text_lower = text.lower()

        # Find Related Work section
        related_start = text_lower.find("related work")
        if related_start == -1:
            related_start = text_lower.find("background")

        # Find References section
        refs_start = text_lower.find("\nreferences\n")
        if refs_start == -1:
            refs_start = text_lower.find("\nbibliography\n")

        # Extract relevant portions
        relevant_text = ""
        if related_start > 0:
            end = refs_start if refs_start > related_start else min(related_start + 10000, len(text))
            relevant_text = text[related_start:end]

        if not relevant_text:
            relevant_text = truncate_text(text, 15000)

        prompt = f"""Extract cited papers from this text that might be relevant for further research.

Focus on:
1. Papers mentioned in Related Work sections
2. Foundational papers that are frequently cited
3. Recent papers that extend or build on this work

TEXT:
{relevant_text}

For each citation found, extract what you can:
- title: Paper title (if mentioned)
- authors: Author names (if mentioned)
- year: Publication year (if mentioned)
- context: Why this paper is cited (1 sentence)
- importance: How important does this seem? (high/medium/low)

Respond as JSON array:
[{{"title": "...", "authors": "...", "year": null, "context": "...", "importance": "..."}}]"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=2000,
                messages=[{"role": "user", "content": prompt}],
            )

            result_text = response.content[0].text

            start = result_text.find("[")
            end = result_text.rfind("]") + 1
            if start >= 0 and end > start:
                return json.loads(result_text[start:end])

        except Exception as e:
            self.logger.error(f"Error identifying citations: {e}")

        return []

    async def suggest_subtopics(
        self,
        references: list[Reference],
        research_topic: str,
        existing_subtopics: list[str] = None,
    ) -> list[dict]:
        """Suggest subtopics based on collected references.

        Args:
            references: Collected references
            research_topic: Main research topic
            existing_subtopics: Already identified subtopics

        Returns:
            List of subtopic suggestions
        """
        # Build summary of references
        ref_summaries = []
        for ref in references[:30]:  # Limit for context
            summary = f"- {ref.title}"
            if ref.tags:
                summary += f" [Tags: {', '.join(ref.tags[:3])}]"
            ref_summaries.append(summary)

        refs_text = "\n".join(ref_summaries)

        existing_text = ""
        if existing_subtopics:
            existing_text = f"\n\nEXISTING SUBTOPICS:\n" + "\n".join(f"- {st}" for st in existing_subtopics)

        prompt = f"""Based on these references, suggest subtopics for organizing the literature review.

RESEARCH TOPIC: {research_topic}

COLLECTED REFERENCES:
{refs_text}
{existing_text}

Suggest 3-7 subtopics that would help organize this literature. For each:
- name: Short subtopic name
- description: What this subtopic covers (1-2 sentences)
- key_terms: Keywords for this subtopic

Respond as JSON array:
[{{"name": "...", "description": "...", "key_terms": ["...", "..."]}}]"""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1500,
                messages=[{"role": "user", "content": prompt}],
            )

            result_text = response.content[0].text

            start = result_text.find("[")
            end = result_text.rfind("]") + 1
            if start >= 0 and end > start:
                return json.loads(result_text[start:end])

        except Exception as e:
            self.logger.error(f"Error suggesting subtopics: {e}")

        return []

    async def summarize_reference(
        self,
        text: str,
        reference: Reference,
        max_length: int = 500,
    ) -> str:
        """Generate a summary of a reference.

        Args:
            text: Document text
            reference: Reference to summarize
            max_length: Maximum summary length in words

        Returns:
            Summary text
        """
        text = truncate_text(text, 20000)

        prompt = f"""Summarize this academic paper/article in {max_length} words or less.

TITLE: {reference.title}

TEXT:
{text}

Provide a concise summary that covers:
1. Main contribution or thesis
2. Key methodology (if applicable)
3. Main findings
4. Significance

Write the summary directly without preamble."""

        try:
            response = self.client.messages.create(
                model=self.model,
                max_tokens=1000,
                messages=[{"role": "user", "content": prompt}],
            )

            return response.content[0].text.strip()

        except Exception as e:
            self.logger.error(f"Error summarizing: {e}")
            return ""
