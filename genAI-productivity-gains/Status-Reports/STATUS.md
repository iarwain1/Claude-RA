# GenAI Productivity Gains Literature Review - Status

## Overview

**Topic**: Evaluating AI Productivity for Defense Acquisition: From Benchmarks to Operational Effectiveness

**Primary Audience**: Military acquisition decision-makers
**Secondary Audience**: Testing & Evaluation (T&E) experts for military systems

**Start Date**: 2025-12-10
**Current Phase**: Literature review development
**Last Updated**: 2025-12-31

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
| **Cross-Disciplinary Background** | **(formerly Appendix A)** | ✅ **COMPLETE** (~70KB consolidated) |
| Other Appendices | Glossary, Study Summaries, Checklists, Resources | Not started |

### Input Materials

Located in `User-Input/`:

- `handoff_document_v2.md` - Comprehensive project state from previous conversations
- `paper_outline_v3.md` - Detailed paper outline (~1600 lines)

### Cross-Disciplinary Background - ✅ COMPLETE

**Location**: `Drafts/Cross-Disciplinary-Background/Cross-Disciplinary-Background.md`

**Status**: Fully drafted and consolidated (~70KB, comprehensive coverage of all 8 sections)

**Sections Completed:**
1. **Testing & Evaluation Traditions** (5 subsections)
   - Software Testing, Systems Engineering, Autonomous Systems, Traditional ML, Cybersecurity/Red Team
2. **Economics & Organizational Theory** (5 subsections)
   - Technology Adoption, Productivity Measurement, Organizational Learning, Labor Economics, Innovation Economics
3. **Human Factors & Cognitive Science** (3 subsections)
   - Human-AI Interaction, Decision Support Systems, Skill Acquisition & Expertise
4. **Risk & Safety Engineering** (5 subsections)
   - Safety Engineering, Reliability Engineering, Security Engineering, Adversarial Robustness, Ethical AI
5. **Statistics & Experimental Design** (5 subsections)
   - Experimental Design, Observational Studies, Measurement Theory, Statistical Modeling, Meta-Analysis
6. **Machine Learning & AI** (4 subsections)
   - ML Fundamentals, LLM Architecture, Evaluation Methods, Deployment & MLOps
7. **Standards & Governance** (2 subsections)
   - Standards Development, Regulatory Frameworks
8. **Synthesis** (7 subsections)
   - Conceptual Integration, Methodological Synthesis, Common Challenges, Best Practices, Framework Integration, Research Gaps, Future Directions

**Archive**: 45 individual section drafts moved to `archives/` subdirectory

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
| **BCG/Wharton Jagged Frontier** | 2023 | **40% quality boost** but homogeneous outputs |
| **Brynjolfsson Customer Service** | 2023 | **34% gain for novices**, quality DECLINE for experts |
| **Noy & Zhang (Science)** | 2023 | **40% faster, 18% better quality** in writing tasks |
| **MIT 95% Pilot Failure** | 2025 | Only **5% of AI pilots** achieve P&L impact |

### References Status

See `references.yaml` for full list (**80 entries** with detailed metadata).

**By Priority:**
- Priority 10 (Essential): 10 references
- Priority 9 (Very important): 14 references
- Priority 8 (Important): 24 references
- Priority 7 (Useful): 20 references
- Priority 6 (Background): 12 references

**By Category (Batch 3 additions):**
- Military/Defense AI: 6 new sources (FAS, Scale/DoD, NDAA, USAF, UNIDIR, CNAS)
- Productivity Studies: 5 new sources (Fed Reserve, PwC, OECD, McKinsey, Dallas Fed)
- Training Interventions: 4 new sources (Science journal RCT, Stanford/MIT, MIT Sloan, Inc)
- Agent Evaluation: 4 new sources (AgentBench, τ-bench, IBM Research, Deloitte)
- Trust/Overreliance: 5 new sources (CHB experiment, CSET bias, ACM review, Springer, false-confidence)
- NIST Standards: 3 new sources (ARIA, Zero Drafts, GenAI pilot)
- Post-Deployment: 1 new source (Ada Lovelace)

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
1. ~~Continue Appendix A drafting~~ ✅ COMPLETED (now Cross-Disciplinary Background)
2. Synthesize findings by subtopic
3. Refine framework based on literature
4. Begin drafting main report sections (Parts 1, 3, 4)

---

## File Locations

```
genAI-productivity-gains/
├── Status-Reports/
│   └── STATUS.md                           # This file
├── References/
│   ├── references.yaml                     # All references with metadata (79 entries)
│   ├── reading-queue.yaml                  # Prioritized reading list
│   └── subtopics.yaml                      # Topic organization (11 subtopics)
├── User-Input/                             # User's starting materials
│   ├── handoff_document_v2.md
│   └── paper_outline_v3.md
├── Claude-Notes/
│   └── Paper-Summaries/                    # Individual paper notes (21 summaries)
└── Drafts/
    └── Cross-Disciplinary-Background/
        ├── Cross-Disciplinary-Background.md  # ✅ COMPLETE (~70KB)
        └── archives/                         # 45 individual section drafts
```

---
*Last updated: 2025-12-31*
