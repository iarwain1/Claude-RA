# Multitask Mayhem: Unveiling and Mitigating Safety Gaps in LLMs Fine-tuning

**arXiv:** [2409.15361](https://arxiv.org/abs/2409.15361)
**Authors:** Essa Jan, Nouar AlDahoul, Moiz Ali, Faizan Ahmad, Fareed Zaffar, et al. (6 total)
**Date:** 2024-09-18
**Categories:** cs.CL, cs.AI, cs.LG

## Abstract

Recent breakthroughs in Large Language Models (LLMs) have led to their adoption across a wide range of tasks, ranging from code generation to machine translation and sentiment analysis, etc. Red teaming/Safety alignment efforts show that fine-tuning models on benign (non-harmful) data could compromise safety. However, it remains unclear to what extent this phenomenon is influenced by different variables, including fine-tuning task, model calibrations, etc. This paper explores the task-wise safety degradation due to fine-tuning on downstream tasks such as summarization, code generation, translation, and classification across various calibration. Our results reveal that: 1) Fine-tuning LLMs for code generation and translation leads to the highest degradation in safety guardrails. 2) LLMs generally have weaker guardrails for translation and classification, with 73-92% of harmful prompts answered, across baseline and other calibrations, falling into one of two concern categories. 3) Current solutions, including guards and safety tuning datasets, lack cross-task robustness. To address these issues, we developed a new multitask safety dataset effectively reducing attack success rates across a range of tasks without compromising the model's overall helpfulness. Our work underscores the need for generalized alignment measures to ensure safer and more robust models.

---
*Metadata fetched via arxiv API on 2025-12-31*
