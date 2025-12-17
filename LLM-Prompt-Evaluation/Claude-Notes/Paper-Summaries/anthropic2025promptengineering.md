# Prompt Engineering Overview (Anthropic Documentation)

**Authors:** Anthropic
**Year:** 2025
**URL:** https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview

## Key Contributions

1. **Success criteria framework:** Focus on what's controllable through prompting
2. **Prerequisites defined:** Clear success criteria, empirical testing methods, draft prompt
3. **Technique organization:** Ordered from broadly effective to specialized
4. **Prompting vs. finetuning comparison:** Resource efficiency, cost, maintainability

## Overview

Anthropic's official prompt engineering documentation emphasizing controllable success criteria and systematic iteration. Focuses on what can actually be improved through prompt design versus other factors.

## Key Findings

### Controllable vs. Non-Controllable Factors

> "The guide focuses on success criteria that are controllable through prompt engineering. Not every success criteria or failing eval is best solved by prompt engineering."

| Factor | Controllable via Prompting? | Alternative |
|--------|---------------------------|-------------|
| Output quality | Yes | - |
| Response format | Yes | - |
| Content relevance | Yes | - |
| Tone | Yes | - |
| Latency | Sometimes | Model selection |
| Cost | Sometimes | Model selection |

### Prerequisites for Effective Prompting

1. **Clear success criteria** - Know what you're optimizing for
2. **Empirical testing methods** - Ability to measure improvement
3. **Draft prompt to iterate on** - Starting point for optimization

### Prompting vs. Finetuning

| Dimension | Prompting | Finetuning |
|-----------|-----------|-----------|
| **Resource efficiency** | Text input only | High-end GPUs, large memory |
| **Cost** | Base model pricing | Significant training costs |
| **Model updates** | Automatically inherit | May need retraining |
| **Speed** | Fast iteration | Slow iteration cycles |

> "Prompt engineering is far faster than other methods of model behavior control, such as finetuning, and can often yield leaps in performance in far less time."

### Technique Organization

Techniques ordered by general effectiveness:
1. Start with broadly effective techniques
2. Move to specialized techniques if needed
3. Actual impact depends on use case
4. Try in order when troubleshooting

## Relevance to Review

**Directly relevant for understanding evaluation scope.** Key insights:

### For Prompt Evaluation

1. **Scope awareness:** Not all issues are prompting problems
2. **Prerequisites matter:** Success criteria needed before evaluation
3. **Iteration speed:** Prompting allows rapid experimentation
4. **Model selection interaction:** Latency/cost may require model changes, not prompt changes

### Implications for Evaluation Design

| Anthropic Principle | Evaluation Implication |
|--------------------|----------------------|
| Clear success criteria | Define before building evals |
| Controllable factors | Evaluate prompting-addressable issues separately |
| Empirical testing | Must have measurement capability |
| Technique ordering | Prioritize evaluation of high-impact techniques |

### Alignment with Practitioner Guidance

| Anthropic | Husain Guidance | Assessment |
|-----------|-----------------|-----------|
| Clear success criteria | Error analysis first | **Aligned** - define goals before evals |
| Empirical testing | Human-validated measurements | **Aligned** |
| Ordered techniques | Iterative improvement | **Aligned** |
| Model selection as alternative | "Does error analysis suggest model is the problem?" | **Strongly aligned** |

## Citations to Follow

- Anthropic Claude 4 best practices
- Anthropic prompt improver tool
- Technique-specific documentation pages

## Questions/Notes

- **Strength:** Official vendor documentation - authoritative for Claude
- **Strength:** Clear prerequisites framework
- **Strength:** Distinguishes controllable vs. non-controllable factors
- **Practical insight:** "Not every failing eval is best solved by prompt engineering"
- **Limitation:** Claude-specific, may not generalize to other models
- **Limitation:** Less depth on evaluation methodology
- **Gap:** No specific metrics or thresholds provided
- **Connects to:** husain2024evals (success criteria emphasis), anthropic2025evaltool (practical tooling)
- **Currency:** 2025, actively maintained

## Evidence Quality

**Medium for methodology guidance.** Vendor documentation provides authoritative Claude-specific guidance but limited empirical validation. Strong for "what to consider"; weaker for "how to measure."
