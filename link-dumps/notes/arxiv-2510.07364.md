# Base Models Know How to Reason, Thinking Models Learn When

**arXiv:** [2510.07364](https://arxiv.org/abs/2510.07364)
**Authors:** Constantin Venhoff, Iván Arcuschin, Philip Torr, Arthur Conmy, Neel Nanda
**Date:** 2025-10-08
**Categories:** cs.AI, cs.LG

## Abstract

Why do thinking language models like DeepSeek R1 outperform their base counterparts? Despite consistent performance gains, it remains unclear to what extent thinking models learn entirely new reasoning capabilities or repurpose pre-existing base model ones. In this work, we propose a hybrid model where we activate reasoning mechanisms in base models at the right time to elicit thinking-model-level reasoning chains, implying that thinking models exploit already existing capabilities. To ground our analysis, we introduce an unsupervised, bottom-up approach for uncovering human-interpretable reasoning behaviors in thinking models. This approach provides an unbiased method to discover reasoning behaviors without imposing manual or LLM-derived assumptions. Across three base and four thinking models, using GSM8K and MATH500, our hybrid model recovers up to 91% of the performance gap to thinking models without any weight updates while steering only 12% of tokens. Concretely, our empirical setup provides a simple, causal way to test the effectiveness of existing reasoning mechanisms in base models by invoking them directly and measuring the resulting task performance. More broadly, these results reframe our understanding of how thinking models are trained: pre-training is when models acquire most of their reasoning mechanisms, and post-training teaches efficient deployment of these mechanisms at the right time, enabling efficient use of their inference-time compute.

---
*Metadata fetched via arxiv API on 2025-12-31*
