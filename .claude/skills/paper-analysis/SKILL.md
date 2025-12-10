---
name: paper-analysis
description: Critical analysis framework for evaluating research papers. Use this skill when reading and summarizing papers to ensure rigorous, consistent evaluation of methodology, findings, and quality. Combines scientific critical thinking with structured note-taking.
---

# Paper Analysis Framework

This skill provides a systematic approach to critically reading and evaluating research papers, ensuring consistent and rigorous assessment across your literature review.

## When to Use This Skill

- Reading papers from the queue (`/read-next`)
- Evaluating paper quality for inclusion decisions
- Creating detailed paper summaries
- Assessing evidence strength for synthesis

## The Analysis Framework

### 1. First Pass: Overview (5-10 minutes)

Quick assessment to understand scope and relevance:

1. **Read in Order**:
   - Title, abstract, keywords
   - Section headings
   - Figures and tables (with captions)
   - Conclusion

2. **Answer**:
   - What type of paper? (empirical, theoretical, review, position)
   - What is the main contribution?
   - Is it relevant to my review?
   - Should I read in detail?

3. **Decision**: Continue to detailed analysis or move to next paper.

### 2. Second Pass: Detailed Reading (30-60 minutes)

Thorough examination with critical eye:

#### A. Introduction & Background
- What problem is addressed?
- What gap in knowledge is claimed?
- Are claims about prior work accurate?
- Is the research question clear and focused?

#### B. Methodology Assessment

**For Empirical Studies**:
| Aspect | Questions to Ask |
|--------|------------------|
| Design | Is the design appropriate for the question? |
| Sample | Size adequate? Selection bias? Representativeness? |
| Measures | Valid? Reliable? Operationalized correctly? |
| Procedures | Reproducible? Controlled appropriately? |
| Analysis | Statistical tests appropriate? Assumptions met? |

**For Theoretical Papers**:
| Aspect | Questions to Ask |
|--------|------------------|
| Framework | Internally consistent? Well-defined concepts? |
| Arguments | Logical flow? Evidence-supported? |
| Novelty | Genuine advance over prior work? |
| Scope | Clear boundaries? Overgeneralization? |

**For Review Papers**:
| Aspect | Questions to Ask |
|--------|------------------|
| Coverage | Systematic? Comprehensive? Current? |
| Synthesis | Beyond summarization? New insights? |
| Bias | Balanced representation? Cherry-picking? |

#### C. Results Evaluation
- Do results actually support the claims?
- Are effect sizes meaningful, not just significant?
- Are limitations acknowledged?
- Alternative explanations considered?

#### D. Discussion & Conclusions
- Conclusions follow from evidence?
- Appropriate hedging/confidence?
- Implications reasonable?
- Future directions sensible?

### 3. Critical Thinking Checklist

#### Bias Detection
- [ ] **Selection bias**: Non-representative samples
- [ ] **Confirmation bias**: Seeking supporting evidence only
- [ ] **Publication bias**: Only positive results published
- [ ] **Measurement bias**: Instruments favor certain outcomes
- [ ] **Researcher bias**: Expectations influence results
- [ ] **Survivorship bias**: Only successful cases analyzed

#### Statistical Red Flags
- [ ] p-hacking (multiple comparisons without correction)
- [ ] Small sample with large claims
- [ ] Missing effect sizes
- [ ] Inappropriate statistical tests
- [ ] Overfitting (too many variables for sample)
- [ ] HARKing (hypothesizing after results known)

#### Logical Fallacies
- [ ] Correlation ≠ Causation
- [ ] Appeal to authority without evidence
- [ ] Straw man of competing views
- [ ] Moving goalposts
- [ ] Cherry-picking evidence
- [ ] Ecological fallacy (group → individual)

### 4. Evidence Quality Rating

Rate overall quality on a scale:

| Rating | Criteria |
|--------|----------|
| **High** | Rigorous methodology, appropriate analysis, limitations acknowledged, reproducible |
| **Medium** | Generally sound but some methodological concerns or limitations |
| **Low** | Significant methodological issues, limited generalizability, or major gaps |
| **Very Low** | Fundamental flaws that undermine conclusions |

Consider using GRADE criteria for empirical work:
- Risk of bias
- Inconsistency across studies
- Indirectness of evidence
- Imprecision of results
- Publication bias likelihood

### 5. Note Template

When creating paper summaries in `notes/paper-summaries/`, include:

```markdown
# [Paper Title]

**Authors:** [names]
**Year:** [year]
**Venue:** [journal/conference]
**URL:** [link]

## Paper Type
[Empirical/Theoretical/Review/Position]

## Summary
[2-3 sentence overview]

## Key Contributions
1. [Main contribution]
2. [Secondary contributions]

## Methodology
- **Design**: [approach]
- **Sample/Data**: [details]
- **Analysis**: [methods]

## Key Findings
1. [Finding 1]
2. [Finding 2]

## Critical Assessment

### Strengths
- [Strength 1]
- [Strength 2]

### Limitations
- [Limitation 1]
- [Limitation 2]

### Quality Rating
[High/Medium/Low] - [brief justification]

## Relevance to My Review
[How this connects to your research questions]

## Connections to Other Papers
- Supports: [paper keys]
- Contradicts: [paper keys]
- Extends: [paper keys]

## Citations to Follow
- [Interesting reference 1] - [why]
- [Interesting reference 2] - [why]

## Questions/Notes
- [Open questions]
- [Personal observations]
```

## Quick Reference: Question Battery

When uncertain about a paper, ask:

1. **So what?** - Why does this matter?
2. **Who says?** - What's the evidence?
3. **What's missing?** - What wasn't studied?
4. **What if?** - Alternative explanations?
5. **Who benefits?** - Potential conflicts of interest?

## Constructive Criticism

Remember: The goal is understanding, not demolition.

- Distinguish fatal flaws from minor issues
- Acknowledge what was done well
- Consider constraints authors faced
- Note how limitations affect your use of findings
- A flawed paper may still have valuable insights

---

*Adapted from K-Dense-AI/claude-scientific-writer scientific-critical-thinking and peer-review skills (MIT License).*
