# Use Our Prompt Improver to Optimize Your Prompts

**Authors:** Anthropic
**Year:** 2024-2025
**URL:** https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/prompt-improver

## Key Contributions

1. **Automatic prompt refinement** in developer console
2. **Five core techniques:** Chain-of-thought, example standardization, example enrichment, prompt rewriting, prefill addition
3. **Structured output:** XML tags, standardized examples, strategic prefills
4. **Performance improvements:** 30% accuracy increase demonstrated for multilabel classification

## Overview

Claude can automatically refine prompts in the developer console using advanced prompt engineering techniques. Ideal for adapting prompts from other AI models and optimizing hand-written prompts.

## Five Core Techniques

| Technique | Description |
|-----------|-------------|
| **Chain-of-Thought Reasoning** | Adds structured reasoning section for systematic problem-solving |
| **Example Standardization** | Converts examples to consistent XML format |
| **Example Enrichment** | Augments examples with chain-of-thought reasoning |
| **Prompt Rewriting** | Improves clarity, structure, grammar, spelling |
| **Prefill Addition** | Guides responses toward specific actions/formats |

## Improved Prompt Structure

### What Improved Prompts Include

1. **Detailed chain-of-thought instructions** - Guide Claude's reasoning process
2. **Clear XML organization** - Separate different components
3. **Standardized example formatting** - Demonstrate step-by-step reasoning
4. **Strategic prefills** - Guide initial responses

### XML Tag Organization

Examples:
```xml
<input>...</input>
<reasoning>...</reasoning>
<output>...</output>
```

## Performance Results

| Task | Improvement |
|------|-------------|
| Multilabel classification (Haiku) | **30% accuracy increase** |
| Word count adherence | **100% compliance** |

> "Claude 3 Haiku's accuracy increased by 30% in comparison to the original prompt in a multilabel classification task."

> "Given ten Wikipedia articles, Claude's adherence to an instruction to write summaries within a specific word count range was 100% after running through the prompt improver."

## Additional Features

### Example Generation
> "If your prompt doesn't have examples, you can add them with Claude-driven example generation. Claude can automatically create synthetic example inputs and draft outputs."

### Prompt Evaluator
> "The prompt evaluator lets you test your prompts under different scenarios. An optional 'ideal output' column is added in the Evaluations tab to benchmark and improve performance."

## Tradeoffs and Troubleshooting

### Important Tradeoff

> "The prompt improver creates templates that produce longer, more thorough, but slower responses."

| Consideration | Recommendation |
|---------------|----------------|
| Latency-sensitive | Consider simpler prompts |
| Cost-sensitive | Consider simpler prompts |
| Quality-focused | Use improved prompts |

### Common Issues

| Issue | Solution |
|-------|----------|
| Examples not appearing | Check XML formatting at start of first user message |
| CoT too verbose | Add length/detail instructions |
| Reasoning steps mismatch | Modify steps section for use case |

## Relevance to Review

**Directly relevant for automated prompt optimization.** Key insights:

### For Prompt Evaluation

1. **Baseline comparison:** Compare original vs. improved prompts
2. **Technique effectiveness:** Test individual technique contributions
3. **Tradeoff measurement:** Quantify quality vs. latency/cost
4. **Synthetic example quality:** Evaluate auto-generated examples

### Evaluation Workflow Integration

| Prompt Improver Feature | Evaluation Application |
|-------------------------|----------------------|
| Chain-of-thought addition | Test reasoning quality improvement |
| XML structure | Test format compliance |
| Example enrichment | Test few-shot effectiveness |
| Prefills | Test response guidance accuracy |

### Connections to Other Guidance

| Prompt Improver | Related Concept |
|-----------------|-----------------|
| CoT addition | Claude 4 thinking capabilities |
| XML structure | Husain binary Pass/Fail (structured output) |
| Auto-generated examples | Husain synthetic data guidance |
| Prompt evaluation | Anthropic Console eval tool |

## Citations to Follow

- Anthropic Workbench documentation
- Chain-of-thought research literature
- XML prompting best practices

## Questions/Notes

- **Strength:** Automatic application of best practices
- **Strength:** Quantified improvements (30%, 100%)
- **Strength:** Integrated evaluation workflow
- **Practical insight:** Improved prompts produce longer, slower responses
- **Practical insight:** Can auto-generate examples when none exist
- **Limitation:** May over-engineer simple prompts
- **Limitation:** Tradeoff with latency/cost not always acceptable
- **Gap:** Limited guidance on when NOT to use improver
- **Connects to:** anthropic2025evaltool (evaluation integration), prompt-optimization subtopic
- **Currency:** 2024-2025, actively maintained

## Evidence Quality

**Medium for tool documentation.** Provides specific performance claims (30%, 100%) but limited methodology detail. Strong for understanding tooling; weaker for independent validation.
