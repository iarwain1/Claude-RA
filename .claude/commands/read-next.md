# Read Next Paper in Queue

Read and summarize the next paper in the reading queue.

## Steps

1. Confirm which review you're working on.

2. Read `<review-name>/References/reading-queue.yaml` to find the highest-priority pending paper.

3. If no papers in queue, inform the user and suggest running `/search`.

4. Get the paper details from `References/references.yaml`.

5. Fetch the paper content:
   - Use WebFetch to get the abstract/content
   - If it's a PDF, ask the user to upload it
   - Look for HTML versions when available

6. Create a summary note at `<review-name>/Claude-Notes/Paper-Summaries/<key>.md` using this template:

   ```markdown
   # <Title>

   **Authors:** <authors>
   **Year:** <year>
   **URL:** <url>

   ## Key Contributions
   - <main contribution 1>
   - <main contribution 2>

   ## Methodology
   <methodology summary>

   ## Key Findings
   - <finding 1>
   - <finding 2>

   ## Relevance to Review
   <how this relates to the review topic>

   ## Citations to Follow
   - <interesting reference to add to queue>

   ## Questions/Notes
   - <observations, critiques, questions>
   ```

7. Update `References/references.yaml`: set `read: true` and `notes_file` path

8. Update `References/reading-queue.yaml`: set status to `done`

9. Add any interesting citations to the reading queue

10. Update relevant subtopics in `References/subtopics.yaml` with findings

11. Commit changes

12. Report:
    - Summary of the paper
    - Key findings relevant to the review
    - New citations added to queue
    - Suggested next paper to read
