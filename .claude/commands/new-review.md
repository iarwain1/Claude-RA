# Create New Literature Review

Create a new literature review project named "$ARGUMENTS".

## Steps

1. Create the directory structure at `reviews/$ARGUMENTS/`:
   - Copy `templates/references.yaml` to `reviews/$ARGUMENTS/references.yaml`
   - Copy `templates/reading-queue.yaml` to `reviews/$ARGUMENTS/reading-queue.yaml`
   - Copy `templates/subtopics.yaml` to `reviews/$ARGUMENTS/subtopics.yaml`
   - Copy `templates/notes/questions.md` to `reviews/$ARGUMENTS/notes/questions.md`
   - Create `reviews/$ARGUMENTS/notes/paper-summaries/.gitkeep`
   - Create `reviews/$ARGUMENTS/notes/themes/.gitkeep`
   - Create `reviews/$ARGUMENTS/reports/.gitkeep`

2. Update the metadata in each YAML file:
   - Set `review_name` to "$ARGUMENTS"
   - Set `created` and `last_updated` to today's date

3. Ask the user:
   - What is the main topic/research question for this review?
   - Are there any initial papers or sources to add?
   - What subtopics do they expect to explore?

4. Update `references.yaml` with the topic and any initial sources

5. Create an initial commit for the new review

Report the created structure and ask for the topic and initial sources.
