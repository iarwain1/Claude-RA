# On Speeding Up Language Model Evaluation

**arXiv:** [2407.06172](https://arxiv.org/abs/2407.06172)
**Authors:** Jin Peng Zhou, Christian K. Belardi, Ruihan Wu, Travis Zhang, Carla P. Gomes, et al. (7 total)
**Date:** 2024-07-08
**Categories:** cs.AI, cs.CL

## Abstract

Developing prompt-based methods with Large Language Models (LLMs) requires making numerous decisions, which give rise to a combinatorial search problem over hyper-parameters. This exhaustive evaluation can be time-consuming and costly. In this paper, we propose an $\textit{adaptive}$ approach to explore this space. We are exploiting the fact that often only few samples are needed to identify clearly superior or inferior settings, and that many evaluation tests are highly correlated. We lean on multi-armed bandits to sequentially identify the next (method, validation sample)-pair to evaluate and utilize low-rank matrix factorization to fill in missing evaluations. We carefully assess the efficacy of our approach on several competitive benchmark problems and show that it can identify the top-performing method using only 5-15% of the typical resources -- resulting in 85-95% LLM cost savings. Our code is available at https://github.com/kilian-group/banditeval.

---
*Metadata fetched via arxiv API on 2025-12-31*
