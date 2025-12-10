# Synthesize Literature Review

Generate a comprehensive literature review report.

## Steps

1. Confirm which review you're working on.

2. Read all relevant files:
   - `references.yaml` - all references
   - `subtopics.yaml` - organization and findings
   - All files in `notes/paper-summaries/`
   - All files in `notes/themes/`
   - `notes/questions.md`

3. Generate `reviews/<review-name>/reports/literature-review.md`:

   ```markdown
   # Literature Review: <Topic>

   **Generated:** <date>
   **Papers Reviewed:** <count>

   ## Executive Summary
   <2-3 paragraph overview of the field and key findings>

   ## Introduction
   <background and motivation>
   <research questions addressed>
   <scope and methodology of this review>

   ## <Subtopic 1>
   ### Overview
   <what this subtopic covers>

   ### Key Papers
   <discussion of most important papers>

   ### Findings
   <synthesized findings, not just paper-by-paper>

   ### Open Questions
   <unresolved issues>

   ## <Subtopic 2>
   ...

   ## Cross-cutting Themes
   <patterns that span subtopics>

   ## Gaps in the Literature
   <what's missing or underexplored>

   ## Future Directions
   <promising research directions>

   ## Conclusion
   <summary and implications>

   ## References
   <formatted reference list>
   ```

4. Ask the user:
   - What citation style do they prefer?
   - Any specific sections to emphasize?
   - Target audience?

5. Generate `reviews/<review-name>/reports/references.bib` (BibTeX format)

6. Commit the reports

7. Present a summary of the report and offer to:
   - Expand any section
   - Adjust the focus
   - Generate alternative formats (shorter summary, presentation outline, etc.)
