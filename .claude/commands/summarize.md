# Summarize Specific Paper

Summarize the paper with key "$ARGUMENTS".

## Steps

1. Confirm which review you're working on.

2. Look up the paper in `reviews/<review-name>/references.yaml` by key.

3. If not found, search by partial title match. If still not found, ask the user for clarification.

4. Fetch the paper content using WebFetch.

5. Create a detailed summary note at `reviews/<review-name>/notes/paper-summaries/<key>.md`:

   ```markdown
   # <Title>

   **Authors:** <authors>
   **Year:** <year>
   **URL:** <url>
   **DOI:** <doi if available>

   ## Abstract
   <original abstract>

   ## Key Contributions
   - <main contribution 1>
   - <main contribution 2>

   ## Methodology
   <detailed methodology>

   ## Key Findings
   - <finding 1>
   - <finding 2>

   ## Strengths
   - <strength 1>

   ## Limitations
   - <limitation 1>

   ## Relevance to Review
   <detailed relevance assessment>

   ## Related Work Mentioned
   - <paper 1> - <why interesting>
   - <paper 2> - <why interesting>

   ## Quotes
   > "<notable quote>" (p. X)

   ## Questions/Notes
   - <observations>
   ```

6. Update `references.yaml`: set `read: true`, `notes_file`

7. If in reading queue, mark as done

8. Add notable citations to the reading queue

9. Update relevant subtopics

10. Commit changes

11. Present the summary to the user and ask:
    - Should any citations be prioritized?
    - Does this change the review direction?
    - Which subtopic does this most inform?
