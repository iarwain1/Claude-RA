# OLMES: A Standard for Language Model Evaluations

**arXiv:** [2406.08446](https://arxiv.org/abs/2406.08446)
**Authors:** Yuling Gu, Oyvind Tafjord, Bailey Kuehl, Dany Haddad, Jesse Dodge, et al. (6 total)
**Date:** 2024-06-12
**Categories:** cs.CL, cs.AI

## Abstract

Progress in AI is often demonstrated by new models claiming improved performance on tasks measuring model capabilities. Evaluating language models can be particularly challenging, as choices of how a model is evaluated on a task can lead to large changes in measured performance. There is no common standard setup, so different models are evaluated on the same tasks in different ways, leading to claims about which models perform best not being reproducible. We propose OLMES, a completely documented, practical, open standard for reproducible LLM evaluations. In developing this standard, we identify and review the varying factors in evaluation practices adopted by the community - such as details of prompt formatting, choice of in-context examples, probability normalizations, and task formulation. In particular, OLMES supports meaningful comparisons between smaller base models that require the unnatural "cloze" formulation of multiple-choice questions against larger models that can utilize the original formulation. OLMES includes well-considered, documented recommendations guided by results from existing literature as well as new experiments resolving open questions.

---
*Metadata fetched via arxiv API on 2025-12-31*
