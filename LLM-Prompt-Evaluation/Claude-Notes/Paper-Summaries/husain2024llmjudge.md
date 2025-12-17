# Using LLM-as-a-Judge For Evaluation: A Complete Guide

**Authors:** Hamel Husain
**Year:** 2024
**URL:** https://hamel.dev/blog/posts/llm-judge/

## Key Contributions

1. **Binary classification paradigm** for LLM judges - reject Likert scales in favor of Pass/Fail with detailed critiques
2. **Validation methodology** using TPR/TNR metrics against human-labeled test sets
3. **"Criteria drift" concept** - evaluation criteria evolve through the process of grading outputs
4. **The "real value" insight** - building an LLM judge is a "hack" to force teams to look at their data carefully

## Methodology

Based on helping 30+ companies implement LLM-as-judge systems, including case studies like Honeycomb's Query Assistant. Combines practical experience with research insights (notably Shankar et al.'s "Who Validates the Validators?").

## Key Findings

### Common Mistakes Teams Make

| Mistake | Problem | Solution |
|---------|---------|----------|
| Too many metrics | Becomes unmanageable | Focus on scoped binary classifiers |
| Arbitrary scoring (1-5 scales) | "What makes a 3 vs a 4? Nobody knows" | Binary Pass/Fail only |
| Ignoring domain experts | Criteria miss real requirements | Involve domain experts in labeling |
| Skipping validation | Judge doesn't reflect quality criteria | Measure TPR/TNR on held-out set |

### Binary Classification + Critique

**Structure:** Binary Pass/Fail judgment + detailed critique explaining why

**Critique requirements:**
- Detailed enough for a "new employee to understand"
- Can serve as few-shot examples for the judge prompt
- Captures nuances that simple Pass/Fail misses

### Validation Process

1. Create labeled test set (100+ examples) with human judgments
2. Run LLM judge on same examples
3. Measure True Positive Rate (TPR) and True Negative Rate (TNR)
4. If alignment is poor, try different model or refine prompt
5. Use TPR/TNR to correct judge estimates for actual failure rates

**Key insight:** "Once you know your judge's True Positive and True Negative rates, you can correct its estimates to determine the actual failure rate in your system."

### Criteria Drift

From Shankar et al.: "To grade outputs, people need to externalize and define their evaluation criteria; however, the process of grading outputs helps them to define that very criteria."

**Implication:** You cannot write a good judge prompt until you've seen the data. Evaluation criteria emerge through iteration, not upfront specification.

### The Real Business Value

> "I would go as far as saying that creating a LLM judge is a nice 'hack' I use to trick people into carefully looking at their data! The real business value comes from looking at your data."

The LLM judge is a byproduct; the process of building it is what drives improvement.

### When to Use LLM-as-Judge

| Situation | Recommendation |
|-----------|----------------|
| Deterministic failures | Code-based evals (regex, structural) |
| Subjective qualities | LLM-as-judge |
| Trivially fixable issues | Don't build expensive evaluators |
| Persistent generalization failures | Worth the LLM-as-judge investment |

### Implementation Details

- **Temperature:** 0 for deterministic outputs
- **Multiple judges:** Consider for critical applications, monitor alignment
- **Fine-tuning judges:** Generally not recommended
- **Same model for task and eval:** Usually fine - different task context

## Relevance to Review

**Critical for prompt evaluation methodology.** Key insights:

1. **Prompt evaluation is inherently iterative** - can't specify criteria upfront
2. **Binary judgments scale better** than nuanced scoring for prompt quality assessment
3. **Validation is mandatory** - unvalidated judges may not reflect actual quality
4. **Domain expertise required** - generic LLM judges miss context-specific criteria

For evaluating prompts specifically:
- System prompts: LLM-as-judge good for subjective qualities (tone, helpfulness)
- User prompts: Error analysis + binary judges for common failure modes
- Agentic prompts: Need multi-step evaluation (separate topic)

## Citations to Follow

- **Shankar et al.** - "Who Validates the Validators? Aligning LLM-Assisted Evaluation of LLM Outputs with Human Preferences" - academic foundation for criteria drift
- **Honeycomb case study** - Query Assistant implementation example
- **Eugene Yan** - "Evaluating the Effectiveness of LLM-Evaluators" - complementary perspective

## Questions/Notes

- **Strength:** Concrete validation methodology (TPR/TNR) gives measurable targets
- **Strength:** "Criteria drift" explains why upfront eval design fails
- **Limitation:** 100+ labeled examples may not be feasible for rapid iteration
- **Gap:** Limited guidance on prompt-specific judges vs. output-specific judges
- **Practical insight:** The process matters more than the artifact - building the judge forces data examination
- **Currency:** 2024, remains highly relevant

## Evidence Quality

**Medium-High for practical guidance.** Strong methodology backed by extensive consulting experience. Cites academic research (Shankar et al.) but primarily practitioner-focused. Can cite for: binary judgment approach, validation methodology, criteria drift concept. Cannot cite for: controlled comparisons of scoring approaches.
