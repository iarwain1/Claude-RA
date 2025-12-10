# Organize References by Subtopics

Analyze and organize the current references into subtopics.

## Steps

1. Confirm which review you're working on.

2. Read `reviews/<review-name>/references.yaml` to get all references.

3. Read `reviews/<review-name>/subtopics.yaml` for existing organization.

4. Analyze the references:
   - Group by themes, methodologies, or research questions
   - Identify clusters of related papers
   - Look for gaps between clusters

5. Propose subtopic organization:
   - List proposed subtopics with descriptions
   - Show which papers belong to each
   - Identify papers that span multiple subtopics
   - Note any papers that don't fit well

6. Ask the user:
   - Does this organization make sense?
   - Should any subtopics be merged or split?
   - Are there missing subtopics to add?
   - How should multi-subtopic papers be handled?

7. After confirmation, update:
   - `subtopics.yaml` with the new organization
   - `references.yaml` with subtopic tags for each reference
   - Create theme notes in `notes/themes/` for each subtopic

8. Commit changes

9. Report the final organization and suggest:
   - Which subtopics need more papers
   - Which subtopics are well-covered
   - Searches to fill gaps
