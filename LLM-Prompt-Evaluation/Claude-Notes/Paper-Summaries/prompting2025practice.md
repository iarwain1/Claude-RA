# Prompting in Practice: Investigating Software Developers' Use of Generative AI Tools

**Authors:** Daniel Otten, Trevor Stalnaker, Nathan Wintersgill, Oscar Chaparro, Denys Poshyvanyk
**Year:** 2025 (October)
**URL:** https://arxiv.org/abs/2510.06000

## Key Contributions

1. **Large-scale empirical study** of 91 software engineers (72 active GenAI users)
2. **14 key findings** on prompting strategies, conversation patterns, reliability
3. **Task-specific reliability assessment** across 6 SE activities
4. **Strategy effectiveness data** on real-world prompting patterns

## Methodology

Survey-based study examining:
- Prompting strategies used by developers
- Conversation patterns (single-shot vs. iterative)
- Reliability perceptions by task type
- Common failure modes

## Key Findings

### Usage Patterns

| Task | Usage Rate | Reliability |
|------|------------|-------------|
| Code generation | Near-universal | Medium |
| Documentation | High | **Highest** |
| Debugging | Moderate (proficiency-correlated) | Low |
| Code review | Moderate (proficiency-correlated) | Low |
| Testing | Moderate | Medium |
| Refactoring | Lower | Medium |

**Key insight:** Proficiency correlates with using AI for more nuanced tasks (debugging, code review).

### Prompting Strategy Effectiveness

| Strategy | Usage Rate (among familiar users) |
|----------|----------------------------------|
| Output Style | 82% |
| Few-Shot Learning | 75% |
| Persona | 68% |
| Condition Check | 65% |

**Context inclusion patterns:**
- 76% include example inputs/expected outputs for code generation
- 53% include library instructions
- Many include codebase descriptions

### Conversation Patterns

> "Every developer reported needing at least multiple exchanges. Those with the highest self-reported proficiency often use 10+ back-and-forth exchanges."

**Critical finding:** Iterative multi-turn conversations preferred over single-shot prompting.

**Correlation:** Lengthier interaction correlates with greater perceived productivity gains.

### Reliability by Task Complexity

| Task Complexity | Reliability Score |
|-----------------|------------------|
| Documentation | Highest |
| Simple code generation | Medium-High |
| Complex code generation | Medium-Low |
| Debugging | Low |
| Architectural changes | **Lowest** |
| Advanced refactoring | **Lowest** |
| Non-functional requirements | **Lowest** |

### Common Failure Modes

1. Unintended behavior changes
2. Incomplete transformations
3. Incorrect compatibility
4. AI hallucinations/false positives

## Relevance to Review

**Highly relevant for understanding real-world prompt evaluation needs.** Key implications:

### For Prompt Evaluation Design

1. **Multi-turn evaluation needed:** Single-shot evaluation misses real usage patterns
2. **Task-specific metrics:** Different reliability profiles require different evaluation approaches
3. **Iterative improvement:** Evaluations should support conversation refinement, not just single prompts
4. **Complexity stratification:** Separate simple from complex tasks in evaluation

### Mapping to Evaluation Approaches

| Finding | Evaluation Implication |
|---------|----------------------|
| 10+ turns common | Need conversation-level evaluation |
| Documentation most reliable | Lower evaluation investment needed |
| Complex reasoning least reliable | Prioritize evaluation here |
| Few-shot commonly used | Test with/without examples |

### Strategy Testing Priorities

Based on usage rates, evaluations should test:
1. Output style instructions (82% usage)
2. Few-shot examples (75% usage)
3. Persona prompting (68% usage)
4. Condition checks (65% usage)

### Human Evaluation Baseline

Study provides empirical data on:
- What developers actually prompt for
- How they iterate on prompts
- Which tasks they trust AI with
- Common failure patterns they observe

## Citations to Follow

- Individual prompting strategy papers referenced
- SE task taxonomy sources
- Related developer productivity studies

## Questions/Notes

- **Strength:** Empirical data on real developer behavior
- **Strength:** Quantitative strategy usage rates
- **Strength:** Task-specific reliability assessments
- **Practical insight:** Multi-turn is the norm, not exception
- **Practical insight:** Proficiency enables more sophisticated AI use
- **Gap:** Self-reported data, may not reflect actual behavior
- **Gap:** No objective measures of prompt quality
- **Limitation:** SE-specific findings may not generalize to other domains
- **Currency:** October 2025, very current
- **Connects to:** husain2024evals (error analysis patterns), human-evaluation subtopic

## Evidence Quality

**Medium-high for descriptive findings.** Survey methodology with reasonable sample size (91 engineers, 72 active users). Good for "what developers do" patterns; weaker for causal claims about what works. Self-reported data has known limitations.
