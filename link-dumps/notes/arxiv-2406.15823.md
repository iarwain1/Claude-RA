# CaT-BENCH: Benchmarking Language Model Understanding of Causal and Temporal Dependencies in Plans

**arXiv:** [2406.15823](https://arxiv.org/abs/2406.15823)
**Authors:** Yash Kumar Lal, Vanya Cohen, Nathanael Chambers, Niranjan Balasubramanian, Raymond Mooney
**Date:** 2024-06-22
**Categories:** cs.CL

## Abstract

Understanding the abilities of LLMs to reason about natural language plans, such as instructional text and recipes, is critical to reliably using them in decision-making systems. A fundamental aspect of plans is the temporal order in which their steps needs to be executed, which reflects the underlying causal dependencies between them. We introduce CaT-Bench, a benchmark of Step Order Prediction questions, which test whether a step must necessarily occur before or after another in cooking recipe plans. We use this to evaluate how well frontier LLMs understand causal and temporal dependencies. We find that SOTA LLMs are underwhelming (best zero-shot is only 0.59 in F1), and are biased towards predicting dependence more often, perhaps relying on temporal order of steps as a heuristic. While prompting for explanations and using few-shot examples improve performance, the best F1 result is only 0.73. Further, human evaluation of explanations along with answer correctness show that, on average, humans do not agree with model reasoning. Surprisingly, we also find that explaining after answering leads to better performance than normal chain-of-thought prompting, and LLM answers are not consistent across questions about the same step pairs. Overall, results show that LLMs' ability to detect dependence between steps has significant room for improvement.

---
*Metadata fetched via arxiv API on 2025-12-31*
