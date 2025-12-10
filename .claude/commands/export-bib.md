# Export BibTeX References

Export all references as a BibTeX file.

## Steps

1. Confirm which review you're working on.

2. Read `reviews/<review-name>/references.yaml`

3. Convert each reference to BibTeX format:

   ```bibtex
   @article{key,
     title = {<title>},
     author = {<authors, formatted>},
     year = {<year>},
     url = {<url>},
     doi = {<doi if available>},
     abstract = {<abstract>},
     keywords = {<subtopics as keywords>}
   }
   ```

   Use appropriate entry types:
   - `@article` for journal papers
   - `@inproceedings` for conference papers
   - `@misc` for arXiv preprints and web sources
   - `@online` for blogs and websites

4. Write to `reviews/<review-name>/reports/references.bib`

5. Report:
   - Number of references exported
   - File location
   - Any references that couldn't be properly formatted

6. Offer to:
   - Export subset by subtopic
   - Export in other formats (RIS, EndNote)
   - Copy to clipboard
