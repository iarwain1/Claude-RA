# GenAI Productivity Gains Literature Review - Status

## Overview

**Topic**: Evaluating AI Productivity for Defense Acquisition: From Benchmarks to Operational Effectiveness

**Primary Audience**: Military acquisition decision-makers
**Secondary Audience**: Testing & Evaluation (T&E) experts for military systems

**Start Date**: 2025-12-10
**Current Phase**: Project setup / Literature gathering

---

## Project Structure

### Report Parts (from paper_outline_v3.md)

| Part | Title | Status |
|------|-------|--------|
| Front Matter | Executive Summaries + Reading Guide | Not started |
| Part 1 | The Benchmark-Utility Gap | Outlined |
| Part 2 | The State of the Field (Literature Review) | **NEEDS DEVELOPMENT** |
| Part 3 | A Framework for AI Evaluation | Outlined |
| Part 4 | Practical Guidance for Acquisition Decision-Makers | Outlined |
| Part 5 | T&E Considerations for GenAI-Based Systems | Needs development |
| Part 6 | Research Agenda and Investment Priorities | Partially outlined |
| Appendix A | Disciplinary Foundations | In progress (4/26 sections drafted) |
| Other Appendices | Glossary, Study Summaries, Checklists, Resources | Not started |

### Input Materials

Located in `input/`:

- `handoff_document_v2.md` - Comprehensive project state from previous conversations
- `paper_outline_v3.md` - Detailed paper outline (~1600 lines)
- `Appendix A/` - Disciplinary foundations work (6 files)
  - Sections 1.1-1.4 drafted (~14,000 words total)
  - Full outline for all 26 sections
- `Link Dumps/` - 13 files of collected links to process

### Appendix A Progress

| Section | Subsection | Status |
|---------|------------|--------|
| 1. T&E Traditions | 1.1 Software Testing | DRAFTED |
| | 1.2 Systems Engineering | DRAFTED |
| | 1.3 Autonomous Systems | DRAFTED |
| | 1.4 Traditional ML | DRAFTED |
| | 1.5 Cybersecurity/Red Team | Not started |
| 2-7 | All remaining | Not started |
| 8 | Synthesis | Not started |

---

## Current Literature Review Status

### Link Dump Processing (Completed 2025-12-10)

- **Total links extracted**: 1,623 unique URLs from 13 dump files
- **Links with dates**: 640 (39%)
- **Tier 1 (Score 9-10)**: 11 links - processed and added to references
- **Tier 2 (Score 7-8)**: 343 links - to be reviewed
- **Tier 3 (Score 5-6)**: 586 links - background reading

### Key Empirical Studies Found (with summaries)

| Study | Date | Key Finding |
|-------|------|-------------|
| **METR Developer Study** | Jul 2025 | **19% SLOWER with AI** (contradicts 24% expected speedup) |
| **Scale Remote Labor Index** | Oct 2025 | **2.5% automation rate** (97.5% failure on professional work) |
| **OpenAI GDPval** | Sep 2025 | **100x faster/cheaper** but human-assisted only 1.4x faster |
| **Upwork UpBench** | Nov 2025 | **70% boost** with human+agent collaboration |
| **Anthropic Economic Index** | 2025 | **57% augmentation vs 43% automation** |

### References Status

See `references.yaml` for full list (24 entries with detailed metadata).

**Tier 1 Critical Papers (10):**
- METR 2025 Developer Study - arXiv:2507.09089
- Scale/CAIS Remote Labor Index - arXiv:2510.26787
- OpenAI GDPval - arXiv:2510.04374
- Upwork UpBench/HAPI
- Anthropic Economic Index
- Toner "Taking Jaggedness Seriously"
- Mollick "Giving Your AI a Job Interview" (read)
- Anthropic productivity estimation (read)
- METR time horizons research
- Epoch AI benchmark-economic gap analysis

**Already Read:**
- Mollick "Giving Your AI a Job Interview"
- Anthropic "Estimating AI productivity gains"

### Subtopics Defined

See `subtopics.yaml` for details:
1. Benchmarks and Automated Evaluation
2. AI Productivity Studies
3. Jagged Capability Frontier
4. Human-AI Teaming
5. Evaluation Methodology
6. Economic and Organizational Impact
7. Risk and Safety Evaluation
8. Agent Evaluation (Emerging)
9. Standards and Frameworks
10. Acquisition and Deployment Guidance
11. Disciplinary Foundations

---

## Next Steps

### Immediate (Current Session)
1. Process link dump files to extract relevant sources
2. Add extracted references to references.yaml
3. Prioritize reading queue

### Short-term
1. Find and fetch high-priority papers (METR, Scale, OpenAI studies)
2. Read and summarize key papers
3. Develop Part 2 (Literature Review) content

### Medium-term
1. Continue Appendix A drafting (Section 1.5 next)
2. Synthesize findings by subtopic
3. Refine framework based on literature

---

## File Locations

```
reviews/genAI-productivity-gains/
├── STATUS.md                    # This file
├── references.yaml              # All references with metadata
├── reading-queue.yaml           # Prioritized reading list
├── subtopics.yaml               # Topic organization
├── input/                       # User's starting materials
│   ├── handoff_document_v2.md
│   ├── paper_outline_v3.md
│   ├── Appendix A/              # Drafted content
│   └── Link Dumps/              # 13 files to process
├── notes/
│   ├── paper-summaries/         # Individual paper notes
│   ├── themes/                  # Cross-cutting themes
│   └── questions.md             # Open research questions
└── reports/                     # Generated outputs
```

---
*Last updated: 2025-12-10*
