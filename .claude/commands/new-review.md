# Create New Literature Review

Create a new literature review project named "$ARGUMENTS".

## Steps

1. Create the directory structure at `$ARGUMENTS/`:
   - Copy `Templates/References/references.yaml` to `$ARGUMENTS/References/references.yaml`
   - Copy `Templates/References/reading-queue.yaml` to `$ARGUMENTS/References/reading-queue.yaml`
   - Copy `Templates/References/subtopics.yaml` to `$ARGUMENTS/References/subtopics.yaml`
   - Copy `Templates/Claude-Notes/questions.md` to `$ARGUMENTS/Claude-Notes/questions.md`
   - Copy `Templates/User-Input/README.md` to `$ARGUMENTS/User-Input/README.md`
   - Create `$ARGUMENTS/Claude-Notes/Paper-Summaries/.gitkeep`
   - Create `$ARGUMENTS/Claude-Notes/Themes/.gitkeep`
   - Create `$ARGUMENTS/Drafts/.gitkeep`
   - Create `$ARGUMENTS/Status-Reports/.gitkeep`
   - Create `$ARGUMENTS/User-Input/References/.gitkeep`
   - Create `$ARGUMENTS/User-Input/Notes/.gitkeep`

2. Update the metadata in each YAML file:
   - Set `review_name` to "$ARGUMENTS"
   - Set `created` and `last_updated` to today's date

3. Check if the user has already placed input materials in the review folder:
   - Look for project_description.md, outline.md, or similar in User-Input/
   - Check for User-Input/References/ or User-Input/Notes/ with content
   - If found, acknowledge them

4. Ask the user:
   - What is the main topic/research question for this review?
   - Do you have input materials to add to `User-Input/`? (project description, link dumps, notes)
   - What subtopics do you expect to explore?

5. If the user provides a project description or has one in User-Input/:
   - Read it to understand the topic
   - Extract initial research questions for `Claude-Notes/questions.md`
   - Suggest initial subtopics based on the description

6. Update `References/references.yaml` with the topic

7. Create an initial commit for the new review

8. Report what was created and suggest next steps:
   - "Add your input materials to `$ARGUMENTS/User-Input/`"
   - "Then run `/process-sources User-Input/References/` to extract relevant links"
   - "And `/scan-notes User-Input/Notes/` to find references in your notes"
   - "Or `/search <topic>` to start finding papers"
