# Prompt-to-Leaderboard

**arXiv:** [2502.14855](https://arxiv.org/abs/2502.14855)
**Authors:** Evan Frick, Connor Chen, Joseph Tennyson, Tianle Li, Wei-Lin Chiang, et al. (7 total)
**Date:** 2025-02-20
**Categories:** cs.LG, cs.CL

## Abstract

Large language model (LLM) evaluations typically rely on aggregated metrics like accuracy or human preference, averaging across users and prompts. This averaging obscures user- and prompt-specific variations in model performance. To address this, we propose Prompt-to-Leaderboard (P2L), a method that produces leaderboards specific to a prompt. The core idea is to train an LLM taking natural language prompts as input to output a vector of Bradley-Terry coefficients which are then used to predict the human preference vote. The resulting prompt-dependent leaderboards allow for unsupervised task-specific evaluation, optimal routing of queries to models, personalization, and automated evaluation of model strengths and weaknesses. Data from Chatbot Arena suggest that P2L better captures the nuanced landscape of language model performance than the averaged leaderboard. Furthermore, our findings suggest that P2L's ability to produce prompt-specific evaluations follows a power law scaling similar to that observed in LLMs themselves. In January 2025, the router we trained based on this methodology achieved the #1 spot on the Chatbot Arena leaderboard. Our code is available on GitHub at https://github.com/lmarena/p2l.

---
*Metadata fetched via arxiv API on 2025-12-31*
