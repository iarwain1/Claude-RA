# When is the consistent prediction likely to be a correct prediction?

**arXiv:** [2407.05778](https://arxiv.org/abs/2407.05778)
**Authors:** Alex Nguyen, Dheeraj Mekala, Chengyu Dong, Jingbo Shang
**Date:** 2024-07-08
**Categories:** cs.CL, cs.AI

## Abstract

Self-consistency (Wang et al., 2023) suggests that the most consistent answer obtained through large language models (LLMs) is more likely to be correct. In this paper, we challenge this argument and propose a nuanced correction. Our observations indicate that consistent answers derived through more computation i.e. longer reasoning texts, rather than simply the most consistent answer across all outputs, are more likely to be correct. This is predominantly because we demonstrate that LLMs can autonomously produce chain-of-thought (CoT) style reasoning with no custom prompts merely while generating longer responses, which lead to consistent predictions that are more accurate. In the zero-shot setting, by sampling Mixtral-8x7B model multiple times and considering longer responses, we achieve 86% of its self-consistency performance obtained through zero-shot CoT prompting on the GSM8K and MultiArith datasets. Finally, we demonstrate that the probability of LLMs generating a longer response is quite low, highlighting the need for decoding strategies conditioned on output length.

---
*Metadata fetched via arxiv API on 2025-12-31*
