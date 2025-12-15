# Link Dumps Changelog

All notable changes to the link dumps database will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.0] - 2025-12-15

### Added
- Initial database creation with three core files:
  - `links.yaml` - Main link database with 618 unique entries
  - `tags.yaml` - Hierarchical tag taxonomy with 80+ tags across 3 facets
  - `research-notes.md` - Documentation of tag system design decisions

- **Database Schema** (`links.yaml`):
  - Title, authors, affiliations
  - URL and alternate URLs
  - Publication/update dates
  - BibTeX citation field
  - Hierarchical tags (multiple allowed)
  - Importance levels: low, normal, high, very-high
  - Key figures/tables with image paths and descriptions
  - Notes (inline or file references)
  - Related links with relationship types
  - Source tracking (which dump file, date added)

- **Tag Taxonomy** (`tags.yaml`):
  - Three facets: Domain, Content Type, Source
  - Domain facet with polyhierarchical structure:
    - AI Capabilities (models, benchmarks, agents, reasoning, multimodal)
    - AI Safety (alignment, interpretability, evaluations, red-teaming, deception)
    - Governance (policy, regulation, standards, international)
    - Risk (existential, misuse, systemic)
    - Forecasting (timelines, economics)
    - Technical (theory, architecture, training)
    - Practical (coding, prompting, tools, applications)
    - Security (cybersecurity, privacy)
    - Meta (methodology, industry, open-source)
  - Content Type facet: paper, blog-post, report, tool, dataset, etc.
  - Source facet: arxiv, github, lesswrong, anthropic, openai, etc.

- **Supporting structure**:
  - `figures/` directory for storing key figures and tables
  - `notes/` directory for detailed reading notes
  - Relationship types for linking entries (blog-version, rebuttal, extends, etc.)

### Processed
- Imported and deduplicated 2,670 link entries from 12 source files
- Resulted in 618 unique URLs
- Mapped original categories to standardized tag taxonomy
- Source files processed:
  - Aryeh_s AI Link Dumps 4_21_25.docx
  - Aryeh_s AI Link Dumps 4_24.docx
  - Aryeh's AI Link Dumps_ 7_25_24.docx
  - Link Dump 11-17-25.docx
  - Link Dump 11-19-25.docx
  - Link Dump 11-24-25.docx
  - Link dump 12-09-25.docx
  - Link dump Nov _ Dec 2024.docx
  - Link dumps (OneNote export June 2024 - Dec 2025).docx
  - Link superdump 11-7-25.docx
  - Link superdump 9-18.docx
  - Links - AI Boosted Productivity.docx

### Research
- Documented tag system best practices from:
  - [Synaptica - On Polyhierarchy](https://synaptica.com/on-polyhierarchy/)
  - [NN/Group - Polyhierarchy](https://www.nngroup.com/articles/polyhierarchy/)
  - [Hedden - Polyhierarchy in Taxonomies](https://www.hedden-information.com/polyhierarchy-in-taxonomies/)
  - [Forte Labs - PKM Tagging Guide](https://fortelabs.com/blog/a-complete-guide-to-tagging-for-personal-knowledge-management/)
- Key design decisions recorded in `research-notes.md`

---

## Template for Future Entries

```
## [X.Y.Z] - YYYY-MM-DD

### Added
- New links added (count and sources)
- New tags added to taxonomy

### Changed
- Tags renamed or restructured
- Schema changes

### Fixed
- Duplicate removals
- Broken link fixes
- Tag corrections

### Processed
- Source files processed
```
