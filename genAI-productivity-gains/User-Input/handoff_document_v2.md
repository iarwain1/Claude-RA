# AI Productivity Evaluation Paper: Comprehensive Handoff Document (v2)

## Document Purpose

This handoff document captures the full state of the AI productivity evaluation paper project for continuation in a new chat. It consolidates information from the original handoff document plus all work and decisions made in the current conversation.

---

## Project Overview

### What This Is

A comprehensive report examining how to measure productivity gains from generative AI adoption within organizations. The work addresses the critical gap between AI benchmark performance and real-world utility—what we call the "benchmark-utility gap."

### Audiences

- **Primary**: Military acquisition decision-makers (including ongoing vendor interactions, internal hiring/training/resource planning for maintaining, testing, and further developing AI products)
- **Secondary**: Testing & Evaluation (T&E) experts for military systems, including experts on traditional software T&E, autonomous systems, human-machine teams, and human evaluation

### Key Framing Insight

The paper bridges familiar T&E concepts (MOPs vs. MOEs, DT vs. OT, Human Systems Integration) with AI-specific challenges. This serves both audiences: practitioners get actionable guidance; T&E experts see rigorous connections to established frameworks.

### The "Alien Intern" Metaphor

A recurring framing device: GenAI as an "alien intern"—extremely capable in some ways, bafflingly incompetent in others, requires supervision, eager to please (sometimes to a fault), doesn't know what it doesn't know. This metaphor helps bridge to personnel selection/evaluation literature and makes AI evaluation challenges intuitive.

---

## Current Report Structure

Based on our discussions, the project has evolved from a single paper into a **modular multi-part report**. Here is the agreed structure:

### Overall Report Title (Working)
"Evaluating AI for Defense Acquisition: From Benchmarks to Operational Effectiveness"

### Report Parts

| Part | Title | Status | Description |
|------|-------|--------|-------------|
| Front Matter | Executive Summaries + Reading Guide | Not started | Overall exec summary + part-level summaries |
| Part 1 | The Benchmark-Utility Gap | Outlined | Problem statement and motivation (~10-15 pages) |
| Part 2 | The State of the Field | Needs development | Literature review of last 6-18 months (~30-50 pages) |
| Part 3 | A Framework for AI Evaluation | Outlined | Conceptual framework (~40-50 pages) |
| Part 4 | Practical Guidance for Acquisition Decision-Makers | Outlined | Actionable recommendations (~40-50 pages) |
| Part 5 | T&E Considerations for GenAI-Based Systems | Needs development | Guidance for T&E practitioners (~30-40 pages) |
| Part 6 | Research Agenda and Investment Priorities | Partially outlined | Open problems and research recommendations (~20-30 pages) |
| Appendix A | Disciplinary Foundations | In progress | Survey of relevant fields (~40-60 pages) |
| Other Appendices | Glossary, Study Summaries, Checklists, Resources | Not started | Reference materials |

### Key Design Decisions

1. **Modular structure**: Each part can stand alone but designed to work together
2. **Appendix A moved from main text**: The disciplinary survey is valuable but works better as reference material
3. **Executive summaries at multiple levels**: Overall + per-part for different reader needs
4. **Part 2 (Literature Review) is the biggest gap**: Structure exists but content needs development

---

## Completed Artifacts

The following artifacts have been created and should be uploaded to the new chat:

### 1. Paper Outline v3 (paper_outline_v3.md)
- Comprehensive outline for the full report
- ~4,000 words
- Covers all main parts and sections
- Includes change log from earlier versions

### 2. Appendix A Detailed Outline (appendix_a_disciplinary_foundations.md)
- Detailed outline for all 26 subsections across 8 sections
- ~15,000 words
- Structured format for each discipline: Overview, Core Concepts, What Transfers, What Breaks, What Can Be Adapted, Implications, Key References, Connections
- Includes synthesis section (Section 8) with summary tables

### 3. Appendix A Section 1.1 Draft (appendix_a_section_1_1_draft.md)
- Software Testing and Quality Assurance
- ~3,200 words
- Rough draft, formal but engaging tone

### 4. Appendix A Section 1.2 Draft (appendix_a_section_1_2_draft.md)
- Systems Engineering and Hardware T&E
- ~3,400 words
- Acknowledges primary audience familiarity with T&E
- Emphasizes connections to AI evaluation

### 5. Appendix A Section 1.3 Draft (appendix_a_section_1_3_draft.md)
- Autonomous Systems Testing and Evaluation
- ~3,800 words
- Positioned as closest existing paradigm to GenAI
- Covers ODD, safety cases, sim-to-real gap, human supervisory control

### 6. Appendix A Section 1.4 Draft (appendix_a_section_1_4_draft.md)
- Traditional Machine Learning Evaluation
- ~3,500 words
- Bridges T&E traditions to AI-specific challenges
- Strong "what breaks" section showing why GenAI is different

### Appendix A Short Outline (appendix_a_short_outline.md)
- Just section/subsection titles
- Quick reference for structure

---

## Appendix A Structure (for reference)

### Section 1: Testing and Evaluation Traditions
- 1.1 Software Testing and Quality Assurance ✓ DRAFTED
- 1.2 Systems Engineering and Hardware T&E ✓ DRAFTED
- 1.3 Autonomous Systems Testing and Evaluation ✓ DRAFTED
- 1.4 Traditional Machine Learning Evaluation ✓ DRAFTED
- 1.5 Cybersecurity Testing and Red Teaming (not yet drafted)

### Section 2: Experimental and Statistical Methods
- 2.1 Experimental Design and Analysis
- 2.2 Psychometrics and Measurement Theory
- 2.3 Econometrics and Causal Inference
- 2.4 Qualitative Research Methods
- 2.5 Survey Methodology

### Section 3: Economics and Productivity
- 3.1 Information Systems Economics
- 3.2 Productivity Measurement and Economics
- 3.3 Cost Analysis and Investment Evaluation

### Section 4: Risk, Quality, and Assurance
- 4.1 Risk Analysis and Management
- 4.2 Reliability Engineering
- 4.3 Quality Management
- 4.4 Audit and Assurance
- 4.5 Safety Engineering

### Section 5: Human and Organizational Factors
- 5.1 Human-Computer Interaction and User Experience Research
- 5.2 Human Factors and Human-Machine Systems
- 5.3 Organizational Behavior and Change Management
- 5.4 Judgment and Decision Making (JDM)
- 5.5 Industrial-Organizational (I-O) Psychology

### Section 6: Evaluation and Assessment Traditions
- 6.1 AI Safety Evaluation (Emerging Field)
- 6.2 Program Evaluation
- 6.3 Educational Measurement
- 6.4 Clinical Trial Methodology

### Section 7: Standards and Governance
- 7.1 Metrology (Science of Measurement)
- 7.2 Standards Development and Governance

### Section 8: Synthesis and Summary
- 8.1 What Transfers Directly
- 8.2 What Breaks for GenAI
- 8.3 What Requires Adaptation
- 8.4 What's Genuinely New

---

## Writing Style and Tone

Based on the drafted sections, the established style is:

### Tone
- Formal but engaging and accessible
- Respectful of existing disciplines while clear about limitations for AI
- Concrete examples over abstract claims
- Not condescending to experts; not inaccessible to non-experts

### Structure (for Appendix A sections)
Each section follows this structure:
1. **Overview**: What the field is, why it matters for AI evaluation
2. **Core Concepts**: Key ideas explained with enough depth to be useful
3. **What Transfers**: Direct applications to AI evaluation
4. **What Breaks**: Where assumptions fail for GenAI
5. **What Can Be Adapted**: Middle ground requiring modification
6. **Implications for AI Evaluation**: Practical takeaways
7. **Key References**: Entry points to literature (organized by subtopic)
8. **Connections**: Links to other appendix sections

### Length
- Appendix A sections: ~3,000-4,000 words each
- At current pace, full Appendix A would be ~80,000-100,000 words
- May need to trim some sections or accept that it's a reference document readers consult selectively

### Formatting
- Use tables for comparisons
- Use bullet points sparingly, mainly in "What Transfers/Breaks" sections
- Narrative prose preferred for Core Concepts
- Clear section headers for navigation

---

## Key Conceptual Frameworks

### The Three-Level Measurement Structure

| Level | Examples | Validity Trade-off |
|-------|----------|-------------------|
| Level 1: Easy to measure | Benchmarks, standardized tests | High internal, low external |
| Level 2: Controlled conditions | Lab studies, RCTs | Medium both |
| Level 3: What we care about | Real-world productivity, ROI | Low internal, high external |

### Challenge Categories (from outline)

**A. Specification & Coverage Problems**
- Hard to articulate what "good" looks like (the "vibes" issue)
- Hard to get representative task coverage for general-purpose tools
- Jagged capability frontier makes edge cases unpredictable

**B. Measurement & Attribution Problems**
- Measuring productivity on tasks that are hard to quantify
- Attributing gains correctly to AI vs. other factors
- Defining what system you're even evaluating
- Defining appropriate baselines

**C. Temporal & Contextual Instability**
- Models change faster than studies can be conducted
- Systems improve post-deployment through iteration
- User skill varies widely and evolves over time
- Same model performs differently with different setups/prompts

**D. Generalization Gaps**
- Lab conditions ≠ real deployment
- Individual task performance ≠ workflow productivity
- Task productivity ≠ organizational productivity

### Key Distinctions That Transfer from T&E

| Traditional T&E Concept | AI Evaluation Application |
|------------------------|--------------------------|
| Verification vs. Validation | Benchmarks (verification) vs. operational evaluation (validation) |
| MOPs vs. MOEs | Benchmark scores (MOPs) vs. mission outcomes (MOEs) |
| DT vs. OT | Controlled studies (DT) vs. operational pilots (OT) |
| ODD (Operational Design Domain) | Bounded capability claims for AI |
| Sim-to-Real Gap | Benchmark-to-Real Gap |
| M&S Accreditation | "When can we trust this benchmark?" |

### What's Genuinely New (no good precedent)

1. Unbounded output evaluation
2. Jagged capability frontier (unpredictable failures on similar tasks)
3. Specification depth problem (value from handling unspecifiable tasks)
4. Benchmark contamination via training
5. Continuous improvement during deployment
6. Extreme skill amplification (user heterogeneity)
7. The "vibes" quality problem

---

## Key References Already Discussed

### Fetched and Read in Previous Conversation

**Ethan Mollick - "Giving Your AI a Job Interview" (One Useful Thing)**
- URL: https://www.oneusefulthing.org/p/giving-your-ai-a-job-interview
- Key points: Benchmarks have limitations; "vibes" matter but aren't rigorous; organizations need to "interview" AI for their specific context
- Relevant to: Sections on evaluation methods, the human analogy

**Anthropic - "Estimating AI productivity gains from Claude conversations" (Nov 2025)**
- URL: https://assets.anthropic.com/m/28fda2ad148e2bf5/original/Estimating-AI-productivity-gains-from-Claude-conversations.pdf
- Key points: Uses Claude to estimate task completion times from 100K real conversations; 80% estimated time savings; validated against JIRA tickets; acknowledges limitations
- Relevant to: Methodology discussion, productivity measurement

### Key Studies to Incorporate (from link dumps)

**Benchmark/Evaluation Methodology**
- METR - "Measuring AI Ability to Complete Long Tasks" (March 2025)
- METR - "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (July 2025)
- OpenAI - GDPval (Sep 2025)
- Scale + CAIS - Remote Labor Index (Oct 2025): ~2.5% task automation finding
- Upwork - UpBench (Nov 2025)
- Epoch AI analyses on benchmarks
- Various papers on benchmark gaming/cheating

**Jagged Frontier / Capability Limitations**
- Helen Toner - "Taking Jaggedness Seriously"
- Various capability limitation analyses

**Productivity & Economic Impact**
- NBER research agenda on economics of transformative AI
- Various productivity studies

**Agent Evaluation** (emerging)
- Holistic Agent Leaderboard
- Agent benchmarks and limitations

**Frameworks & Standards**
- NIST AI RMF
- CLTC AI Risk Management materials
- Safety case literature

### References from Drafted Appendix A Sections

Each drafted section (1.1-1.4) includes curated reference lists organized by subtopic. These should be preserved and expanded as needed.

---

## Research Plan (from original handoff)

### Phase 1: Landscape Mapping (Week 1)
**Claude's tasks (via Research mode)**:
- Broad surveys of AI evaluation methodology
- Software T&E literature review
- Psychometrics/human evaluation frameworks
- Economics of AI productivity measurement

**Deena's tasks**:
- Systematic link dump review
- Newsletter archive scanning
- Twitter/social media scan for recent developments
- Mining prior work and internal documents on military T&E frameworks

### Phase 2: Targeted Deep Dives (Week 2)
**Claude focuses on**:
- Software T&E literature
- Psychometrics and human evaluation
- Economics of AI and productivity measurement
- Specific benchmarks and evaluation frameworks

**Deena focuses on**:
- Military T&E frameworks (MOPs/MOEs, DT/OT, HSI)
- Cutting-edge/unpublished work from Twitter/newsletters
- Practitioner perspectives
- Organizational context for primary audience

### Phase 3: Synthesis and Gap-Filling (Week 3)
- Organize findings by paper section
- Identify gaps in coverage
- Targeted searches to fill gaps

### Phase 4: Final Research and Writing Support (Week 4)
- Fill final gaps
- Resolve contradictions
- Support writing with targeted lookups

---

## Immediate Next Steps

Based on where we left off, the logical next steps are:

### For Appendix A (continuing current work)
1. **Draft Section 1.5** (Cybersecurity Testing and Red Teaming) - completes Section 1
2. **Continue through remaining sections** as prioritized
3. Consider which sections need full treatment vs. shorter coverage

### For the Main Report
1. **Develop Part 2 (Literature Review)** - this is the biggest gap
   - Structure the review by topic area
   - Fetch and synthesize key sources from link dumps
   - Use Research mode for landscape mapping
2. **Refine Part 3 (Framework)** based on literature findings
3. **Develop Part 5 (T&E Guidance)** - currently underdeveloped

### Deena's Parallel Work (from original plan)
- Military T&E frameworks research
- Newsletter archive scanning
- Twitter/social media for cutting-edge work
- Link dump processing

---

## Important Context and Decisions

### Why Appendix A First
We chose to develop Appendix A (Disciplinary Foundations) before the main report because:
1. It provides the conceptual foundation for the framework
2. The "what transfers / what breaks" analysis informs how to present the framework
3. It can be developed somewhat independently
4. Deena wanted to see the approach before committing to full report

### Length Considerations
- Current Appendix A sections average ~3,500 words
- Full appendix at this depth would be substantial (~80,000+ words)
- Options discussed:
  - Full depth for high-priority sections, shorter for others
  - Accept it as a reference document (readers consult selectively)
  - Trim across the board later
- Decision: Continue at current depth for now; trim later if needed

### Report Format Options (discussed but not decided)
- **Option A**: Single large report with all parts (~200-250 pages)
- **Option B**: Report series (parts published separately)
- **Option C**: Tiered products (exec summary + main report + technical supplements)

Leaning toward Option A or C depending on publication venue.

---

## Link Dumps and Source Materials

The original handoff mentioned link dump documents in project files. These contain:

### Highly Relevant (prioritized for fetching)
- Benchmark/evaluation methodology papers
- Productivity/economics papers
- Jagged frontier and capability limitations
- Frameworks and standards
- Agent evaluation (emerging area)
- Military/security relevant papers

### Ambiguous (need to fetch to assess)
- Various papers that might be relevant based on title

### Processing Workflow
1. Deena shares link dump docs
2. Claude scans titles and flags probable relevance
3. Deena reviews flags
4. Claude fetches and reads flagged items
5. Claude provides summaries organized by paper section

---

## Practical Notes

### ArXiv Links
- Abstract links (arxiv.org/abs/XXXX) work fine for initial screening
- Can convert to PDF links (arxiv.org/pdf/XXXX) for deep reading
- HTML versions often more accessible than PDFs

### Research Mode
- Takes 5-15 minutes per query
- Best for broad landscape surveys
- Less good for very recent work or paywalled content
- Write specific prompts with time ranges and named sources

### File Handling
- User uploads available at /mnt/user-data/uploads
- Create working files in /home/claude
- Final outputs to /mnt/user-data/outputs for sharing

---

## Questions to Resolve

These questions came up but weren't definitively resolved:

1. **Publication venue**: Academic paper? Government report? Internal document? (Affects tone and length)

2. **Classification level**: Are there classified or sensitive considerations that need separate treatment?

3. **How much military-specific T&E terminology** should be explicit vs. kept in analogies?

4. **International/allied perspectives**: Should these be included?

5. **Specific contract language examples**: Would these be valuable in recommendations?

6. **Case studies**: Should we include specific vignettes/scenarios? If so, real or hypothetical?

---

## Summary of Current State

**What's done:**
- Overall report structure decided
- Appendix A fully outlined (26 subsections)
- 4 Appendix A sections drafted (1.1-1.4)
- Paper outline v3 complete
- Key conceptual frameworks established
- Writing style and tone established

**What's in progress:**
- Appendix A drafting (22 sections remaining)
- Literature gathering (sources identified but not yet systematically processed)

**What's not started:**
- Part 2 (Literature Review) content
- Part 5 (T&E Guidance) dedicated development
- Executive summaries
- Other appendices (glossary, checklists, etc.)
- Final integration and editing

---

*Document created: [current conversation]*
*Purpose: Comprehensive handoff for continuing AI productivity evaluation paper in new chat*
*Files to upload with this handoff: paper_outline_v3.md, appendix_a_disciplinary_foundations.md, appendix_a_section_1_1_draft.md, appendix_a_section_1_2_draft.md, appendix_a_section_1_3_draft.md, appendix_a_section_1_4_draft.md*
