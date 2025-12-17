# Your AI Product Needs Evals

**Authors:** Hamel Husain
**Year:** 2024
**URL:** https://hamel.dev/blog/posts/evals/

## Key Contributions

1. **Three-level evaluation framework** with cost/frequency tradeoffs: Level 1 (assertions) → Level 2 (LLM-as-judge) → Level 3 (A/B testing)
2. **Error analysis methodology** adapted from qualitative research (open coding, axial coding) as the foundation for eval design
3. **Practical guidance** on when to use each evaluation type based on whether failures are objective/rule-based vs. subjective/judgment-based
4. **Validation requirements** for LLM-as-judge: must measure agreement with human judgments through iterative calibration

## Methodology

The framework emerges from Husain's experience helping 30+ companies build LLM products, plus his earlier work leading the CodeSearchNet team (precursor to GitHub Copilot). The methodology is practitioner-focused rather than academic.

## Key Findings

### Three Levels of Evaluation

| Level | Type | Cost | Frequency | Use Case |
|-------|------|------|-----------|----------|
| **1** | Assertions/Unit Tests | Low | Every code change | Objective, rule-based failures (regex checks, format validation) |
| **2** | LLM-as-Judge | Medium | Set cadence | Subjective failures (tone, relevance, reasoning quality) |
| **3** | A/B Testing | High | After significant product changes | User behavior/outcome validation |

**Key insight:** Conquer Level 1 before moving to Level 2. Level 2 requires 100+ labeled examples and ongoing weekly maintenance.

### Error Analysis Methodology

1. **Open Coding (Journaling):** Read traces end-to-end, write one-sentence notes on every error. Stop at the *most upstream error* (the causal root).
2. **Axial Coding:** Group notes into a "failure taxonomy" - distinct categories of similar failures.
3. **Write Evals for Discovered Errors:** "Write evaluators for errors you discover, not errors you imagine."

**Critical:** Cannot outsource open coding to an LLM - it lacks your context and "tribal knowledge."

**Cadence:** Review 100+ fresh traces every 2-4 weeks, especially after prompt updates, model switches, or major features.

### LLM-as-Judge Best Practices

- **Binary Pass/Fail over Likert scales:** Forces clarity, reduces noise from subjective distinctions between "3" and "4"
- **Validation required:** Measure agreement between LLM judge and human through 3-4 iteration rounds with a few hundred labeled examples
- **Save for persistent generalization failures:** Not issues fixable trivially with assertions

### When to Use What

| Failure Type | Evaluation Tool |
|--------------|-----------------|
| Objective, rule-based | Code-based evaluators (assertions) |
| Subjective, requiring judgment | LLM-as-judge |
| User behavior/outcomes | A/B tests |

## Relevance to Review

**Highly relevant.** This is the foundational practitioner framework for prompt evaluation. Key insights for the review:

1. **Evaluation is hierarchical:** Different prompt types may warrant different evaluation levels
2. **Error analysis precedes eval design:** Don't start with metrics; start with understanding failures
3. **LLM-as-judge has prerequisites:** Requires validation against human judgment, 100+ examples, ongoing maintenance
4. **Objective vs. subjective distinction:** Maps to different prompt evaluation needs

## Citations to Follow

- **Shreya Shankar** - Co-author of evals course, likely has complementary research
- **Rechat case study** - Example of hundreds of unit tests for AI product
- **Lenny's Newsletter interview** - "Evals, error analysis, and better prompts" - more detailed discussion
- **Inspect AI** - OSS Python library for LLM evals mentioned by Husain

## Questions/Notes

- **Limitation:** Framework assumes you have user data to analyze. What about evaluating prompts *before* deployment?
- **Gap:** No explicit discussion of evaluating *system prompts* vs *user prompts* - treats all prompts similarly
- **Strength:** Practical, battle-tested across 30+ companies - this is production-validated advice
- **Currency:** 2024 guidance remains highly relevant; methodology is model-agnostic
- **Appropriate citation use:** Can cite for three-level framework, error analysis methodology, LLM-as-judge validation requirements. Cannot cite for rigorous empirical comparisons (this is practitioner guidance, not controlled study).

## Evidence Quality

**Medium-High for practical guidance.** Based on extensive consulting experience (30+ companies, 2000+ trained practitioners) but not controlled empirical study. Strongest for "what works in practice" claims; weaker for claims about why specific approaches work better.
