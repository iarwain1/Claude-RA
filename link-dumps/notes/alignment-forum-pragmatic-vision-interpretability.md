# A Pragmatic Vision for Interpretability

**URL:** https://www.alignmentforum.org/posts/StENzDcD3kpfGJssR/a-pragmatic-vision-for-interpretability
**Authors:** Neel Nanda, Josh Engels, Arthur Conmy, Senthooran Rajamanoharan, bilalchughtai, CallumMcDougall, János Kramár, Lewis Smith (Google DeepMind Mechanistic Interpretability Team)
**Date:** 2025-12-01

## Claude Summary

The Google DeepMind mechanistic interpretability team announces a strategic pivot from "ambitious reverse-engineering" to "pragmatic interpretability" - focusing on problems on the critical path to AGI safety with measurable progress.

### Key Insights

1. **Disappointment with ambitious mech interp**: Existing techniques struggle with today's important behaviors involving large models, complex environments, agentic behavior, and long chains of thought.

2. **Proxy tasks are essential**: Easy to fool oneself in research. Need ways to tell if actually making progress. Key criterion: "if you succeeded on it, would you actually update toward believing you'd made progress on your North Star?"

3. **Examples of good proxy tasks**:
   - Interpreting the hidden goal of a model organism
   - Stopping emergent misalignment without changing training data
   - Predicting what prompt changes will stop undesired behavior

4. **Method minimalism**: Start with simplest methods (prompting, steering, probing, reading CoT). Add complexity only when baselines fail.

5. **SAE lessons learned**: Much of 2024 spent on sparse autoencoders. In hindsight, made tactical errors - progress was slower than it could have been by measuring via proxy tasks rather than reconstruction error.

### Relevance

Major strategic statement from leading interpretability team. Shifts focus from understanding models comprehensively to solving specific safety-relevant problems. Influential for interpretability research direction in AI safety community.
