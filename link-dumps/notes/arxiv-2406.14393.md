# Jailbreaking as a Reward Misspecification Problem

**arXiv:** [2406.14393](https://arxiv.org/abs/2406.14393)
**Authors:** Zhihui Xie, Jiahui Gao, Lei Li, Zhenguo Li, Qi Liu, et al. (6 total)
**Date:** 2024-06-20
**Categories:** cs.LG, cs.CL

## Abstract

The widespread adoption of large language models (LLMs) has raised concerns about their safety and reliability, particularly regarding their vulnerability to adversarial attacks. In this paper, we propose a novel perspective that attributes this vulnerability to reward misspecification during the alignment process. This misspecification occurs when the reward function fails to accurately capture the intended behavior, leading to misaligned model outputs. We introduce a metric ReGap to quantify the extent of reward misspecification and demonstrate its effectiveness and robustness in detecting harmful backdoor prompts. Building upon these insights, we present ReMiss, a system for automated red teaming that generates adversarial prompts in a reward-misspecified space. ReMiss achieves state-of-the-art attack success rates on the AdvBench benchmark against various target aligned LLMs while preserving the human readability of the generated prompts. Furthermore, these attacks on open-source models demonstrate high transferability to closed-source models like GPT-4o and out-of-distribution tasks from HarmBench. Detailed analysis highlights the unique advantages of the proposed reward misspecification objective compared to previous methods, offering new insights for improving LLM safety and robustness.

---
*Metadata fetched via arxiv API on 2025-12-31*
