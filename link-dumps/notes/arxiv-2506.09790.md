# ComfyUI-R1: Exploring Reasoning Models for Workflow Generation

**arXiv:** [2506.09790](https://arxiv.org/abs/2506.09790)
**Authors:** Zhenran Xu, Yiyu Wang, Xue Yang, Longyue Wang, Weihua Luo, et al. (8 total)
**Date:** 2025-06-11
**Categories:** cs.CL, cs.CV, cs.SE

## Abstract

AI-generated content has evolved from monolithic models to modular workflows, particularly on platforms like ComfyUI, enabling customization in creative pipelines. However, crafting effective workflows requires great expertise to orchestrate numerous specialized components, presenting a steep learning curve for users. To address this challenge, we introduce ComfyUI-R1, the first large reasoning model for automated workflow generation. Starting with our curated dataset of 4K workflows, we construct long chain-of-thought (CoT) reasoning data, including node selection, workflow planning, and code-level workflow representation. ComfyUI-R1 is trained through a two-stage framework: (1) CoT fine-tuning for cold start, adapting models to the ComfyUI domain; (2) reinforcement learning for incentivizing reasoning capability, guided by a fine-grained rule-metric hybrid reward, ensuring format validity, structural integrity, and node-level fidelity. Experiments show that our 7B-parameter model achieves a 97\% format validity rate, along with high pass rate, node-level and graph-level F1 scores, significantly surpassing prior state-of-the-art methods that employ leading closed-source models such as GPT-4o and Claude series. Further analysis highlights the critical role of the reasoning process and the advantage of transforming workflows into code. Qualitative comparison reveals our strength in synthesizing intricate workflows with diverse nodes, underscoring the potential of long CoT reasoning in AI art creation.

---
*Metadata fetched via arxiv API on 2025-12-31*
