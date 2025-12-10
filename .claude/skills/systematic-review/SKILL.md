---
name: systematic-review
description: Comprehensive methodology for conducting systematic literature reviews. Use this skill when starting a new literature review, planning search strategies, or synthesizing findings across multiple papers. Provides structured workflows from planning through final synthesis.
---

# Systematic Literature Review Methodology

This skill guides you through a rigorous, reproducible literature review process adapted from PRISMA guidelines and systematic review best practices.

## When to Use This Skill

- Starting a new literature review
- Planning comprehensive search strategies
- Organizing and screening large numbers of papers
- Synthesizing findings across studies
- Ensuring methodological rigor

## The 7-Phase Review Process

### Phase 1: Planning & Scoping

Before searching, clearly define:

1. **Research Question(s)**
   - Use PICO framework for empirical questions:
     - **P**opulation: Who/what is being studied?
     - **I**ntervention/Interest: What is the focus?
     - **C**omparison: What alternatives exist?
     - **O**utcome: What results matter?
   - Or use PEO for qualitative reviews:
     - **P**opulation, **E**xposure, **O**utcome

2. **Inclusion/Exclusion Criteria**
   - Publication date range
   - Study types (empirical, theoretical, review)
   - Language restrictions
   - Quality thresholds

3. **Scope Boundaries**
   - What's in scope vs. adjacent topics
   - Depth vs. breadth tradeoffs

**Action**: Update `subtopics.yaml` with initial topic structure and `notes/questions.md` with research questions.

### Phase 2: Search Strategy

Execute systematic searches across multiple sources:

1. **Academic Databases** (via WebSearch)
   - `site:arxiv.org [topic] [year range]`
   - `site:semanticscholar.org [topic]`
   - `[topic] filetype:pdf site:edu`

2. **Search Term Development**
   - Start with key concepts from research questions
   - Identify synonyms and related terms
   - Use Boolean operators: AND, OR, NOT
   - Include both technical and common terminology

3. **Document Your Search**
   - Record exact queries used
   - Note date of each search
   - Track results per source

**Action**: Use `/search` command, document strategy in `notes/search-log.md`.

### Phase 3: Screening & Selection

Apply inclusion criteria systematically:

1. **Title/Abstract Screening**
   - Quick relevance assessment
   - Apply inclusion criteria
   - When uncertain, include for full review

2. **Full-Text Review**
   - Deeper relevance assessment
   - Quality evaluation
   - Document exclusion reasons

3. **Track Selection Flow**
   ```
   Records identified: N
   ├── Duplicates removed: N
   ├── Screened (title/abstract): N
   │   └── Excluded: N (reasons)
   ├── Full-text assessed: N
   │   └── Excluded: N (reasons)
   └── Included in review: N
   ```

**Action**: Update `references.yaml` with all candidates, use priority scores for screening.

### Phase 4: Data Extraction

For each included paper, systematically extract:

1. **Bibliographic Data**
   - Authors, year, venue
   - DOI/URL

2. **Study Characteristics**
   - Research design/methodology
   - Sample/dataset details
   - Key variables/constructs

3. **Key Findings**
   - Main results
   - Effect sizes (if applicable)
   - Limitations noted by authors

4. **Quality Indicators**
   - Methodological strengths/weaknesses
   - Potential biases
   - Generalizability

**Action**: Create detailed notes in `notes/paper-summaries/` using the paper-analysis skill.

### Phase 5: Quality Assessment

Evaluate methodological rigor:

1. **For Empirical Studies**
   - Sample adequacy
   - Measurement validity
   - Analysis appropriateness
   - Bias controls

2. **For Theoretical Papers**
   - Logical coherence
   - Evidence support
   - Novel contribution

3. **For Reviews**
   - Systematic methodology
   - Comprehensiveness
   - Synthesis quality

**Action**: Add quality notes to paper summaries, flag concerns in `subtopics.yaml`.

### Phase 6: Synthesis

Integrate findings across papers:

1. **Thematic Analysis**
   - Identify recurring themes
   - Note convergences and divergences
   - Track evidence strength per theme

2. **Gap Analysis**
   - What questions remain unanswered?
   - Where is evidence weak?
   - What methodologies are missing?

3. **Conceptual Framework**
   - How do findings relate?
   - What models or frameworks emerge?
   - How does this advance understanding?

**Action**: Update `notes/themes/` with cross-paper synthesis, maintain `subtopics.yaml`.

### Phase 7: Reporting

Generate comprehensive documentation:

1. **Methodology Section**
   - Search strategy
   - Selection process
   - Quality assessment approach

2. **Findings by Theme**
   - Synthesized results
   - Evidence quality
   - Confidence levels

3. **Discussion**
   - Implications
   - Limitations
   - Future directions

**Action**: Use `/synthesize` command to generate `reports/literature-review.md`.

## Quality Checklist

Before finalizing, verify:

- [ ] Search strategy documented and reproducible
- [ ] Inclusion/exclusion criteria applied consistently
- [ ] All included papers have quality assessment
- [ ] Themes supported by multiple sources
- [ ] Gaps and limitations acknowledged
- [ ] Citations accurate and complete

## Tips for Rigor

1. **Be Systematic**: Follow the same process for each paper
2. **Document Everything**: Decisions, exclusions, uncertainties
3. **Stay Current**: Re-run searches periodically for updates
4. **Acknowledge Limits**: No review is exhaustive
5. **Iterate**: Refine scope as understanding develops

---

*Adapted from K-Dense-AI/claude-scientific-writer (MIT License) and PRISMA guidelines.*
