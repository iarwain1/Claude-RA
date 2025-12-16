# Link Dumps Changelog

All notable changes to the link dumps database will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [1.0.5] - 2025-12-16

### Added
- Major batch processing: 18 additional paper notes (total now 46):
  - `arxiv-2407.21787.md` - Large Language Monkeys: Inference-time scaling laws
  - `arxiv-2408.02479.md` - LLMs to LLM-based Agents for SE Survey
  - `arxiv-2409.03793.md` - Safeguarding AI Agents: Safety architectures
  - `arxiv-2410.05229.md` - GSM-Symbolic: Math reasoning limitations (ICLR 2025)
  - `arxiv-2410.07095.md` - MLE-bench: ML engineering agents (ICLR 2025)
  - `arxiv-2410.09024.md` - AgentHarm: Agent harmfulness benchmark (ICLR 2025)
  - `arxiv-2410.13787.md` - Looking Inward: LLM introspection capabilities
  - `arxiv-2411.00114.md` - Project Sid: Many-agent AI civilization simulations
  - `arxiv-2411.01114.md` - Infant Agent: 90x improvement on SWE-bench
  - `arxiv-2411.02306.md` - Targeted Manipulation in RLHF (deceptive targeting)
  - `arxiv-2411.04986.md` - Semantic Hub Hypothesis (ICLR 2025)
  - `arxiv-2411.10053.md` - That Chip Has Sailed: AlphaChip rebuttal
  - `arxiv-2411.15594.md` - LLM-as-a-Judge comprehensive survey
  - `arxiv-2412.09563.md` - Intermediate layer representations (LeCun)
  - `arxiv-2412.14093.md` - **Alignment Faking** (Anthropic) - CRITICAL SAFETY PAPER
  - `arxiv-2403.13793.md` - Evaluating Dangerous Capabilities (DeepMind)
  - `arxiv-2406.12442.md` - Abstraction-of-Thought reasoning
  - `arxiv-2405.00332.md` - GSM1k: Contamination detection benchmark

### Changed
- Updated `PROCESSING-STATUS.md` to reflect 46 processed links
- Processing now covers papers from March 2024 through December 2024

### Technical Notes
- WebSearch intermittently available; processed during availability windows
- ~572 links still pending full processing

## [1.0.4] - 2025-12-16

### Added
- Completed processing of all high-importance links (7 more notes):
  - `arxiv-2511.04703.md` - Construct Validity in LLM Benchmarks (very-high, 29 expert reviewers, 445 benchmarks)
  - `arxiv-2512.04123.md` - Measuring Agents in Production (very-high, 306 practitioners surveyed)
  - `nist-ai-measurement-science.md` - NIST CAISI Measurement Science (very-high, policy)
  - `arxiv-2512.00193.md` - A Rosetta Stone for AI Benchmarks (high, capability forecasting)
  - `arxiv-2512.04921.md` - AI Consumer Index ACE (high, consumer task benchmark)
  - `alignment-forum-pragmatic-vision-interpretability.md` - GDM Mech Interp Team's strategic pivot (high)
  - `langsmith-agent-builder.md` - LangChain no-code agent builder (high)

### Changed
- Updated `PROCESSING-STATUS.md` to reflect 28 processed links
- All high-importance links (> and >>) now have full notes
- Updated tags for processed entries to reflect content

### Technical Notes
- WebSearch continues to work as primary metadata retrieval method
- ~590 links still pending full processing

## [1.0.3] - 2025-12-16

### Added
- Extended notes collection to 21 papers with abstracts and metadata:
  - `arxiv-2407.09468.md` - AI Risk Management: Safety and Security
  - `arxiv-2406.02061.md` - MixEval: Deriving Wisdom of the Crowd (benchmarks)
  - `arxiv-2407.14937.md` - Sycophancy to Subterfuge (reward tampering)
  - `arxiv-2411.12820.md` - BALROG: Benchmarking Agentic LLM Reasoners
  - `arxiv-2411.08088.md` - SWE-bench+ and MB+ (improved benchmarks)
  - `arxiv-2407.07890.md` - Representation Engineering: Top-Down Approach
  - `arxiv-2401.03188.md` - V&V, T&E of Neurosymbolic AI Survey
  - `arxiv-2407.16216.md` - LLM Alignment Techniques Survey (RLHF, DPO)
  - `arxiv-2407.12784.md` - GenAI Paradox: Create vs Understand
  - `arxiv-2407.11969.md` - Internal Consistency and Self-Feedback
  - `arxiv-2412.02159.md` - Jailbreak Defense in Narrow Domain
  - `arxiv-2503.19887.md` - AI Threats via Incident Regime (policy)
  - `arxiv-2504.13839.md` - Audit Cards for AI Evaluations (governance)
  - `arxiv-2504.15585.md` - LLM Full Stack Safety Survey (800+ papers)

### Changed
- Updated `PROCESSING-STATUS.md` to reflect 21 processed links
- Added notes field references to all 21 processed database entries
- Updated titles and metadata for all processed papers

### Technical Notes
- arXiv API script written but blocked by network restrictions (403)
- Continued using WebSearch as workaround for metadata retrieval
- ~597 links still pending full processing

## [1.0.2] - 2025-12-16

### Added
- Created detailed notes for 7 key papers/articles in `notes/` directory:
  - `arxiv-2411.00640.md` - Adding Error Bars to Evals (methodology)
  - `arxiv-2405.19550.md` - Stress-Testing Capability Elicitation (sandbagging)
  - `arxiv-2406.04313.md` - Short Circuiting for Alignment (jailbreak defense)
  - `arxiv-2512.07810.md` - Auditing Games for Sandbagging (AISI)
  - `arxiv-2509.15541.md` - Deliberative Alignment Anti-Scheming (Apollo/AISI)
  - `arxiv-2504.05259.md` - Evaluating Control Measures (control evaluations)
  - `anthropic-how-ai-transforming-work.md` - AI productivity research
- Created `PROCESSING-STATUS.md` documenting progress and pending work
- Created `fetch_arxiv_metadata.py` script for batch arXiv processing

### Changed
- Updated titles for 10+ entries with proper paper/article titles
- Updated tags for processed entries to match content
- Added notes field references to 7 database entries

### Technical Notes
- WebFetch blocked on most sites (arXiv, Anthropic, OpenAI, LessWrong, etc.)
- Used WebSearch as workaround to retrieve metadata from search results
- ~600 links still need full processing (titles from URLs only)

## [1.0.1] - 2025-12-16

### Fixed
- Corrected interpretation of `>` and `>>` markers in source files
  - `>` now sets importance to `high` (was incorrectly used as title)
  - `>>` now sets importance to `very-high` (was incorrectly used as title)
- Updated 14 entries with proper titles and importance levels:
  - 4 entries set to `very-high` importance
  - 10 entries set to `high` importance
- Replaced placeholder titles with descriptive titles derived from URLs

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
