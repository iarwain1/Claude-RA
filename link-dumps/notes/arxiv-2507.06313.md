# ETT: Expanding the Long Context Understanding Capability of LLMs at Test-Time

**arXiv:** [2507.06313](https://arxiv.org/abs/2507.06313)
**Authors:** Kiarash Zahirnia, Zahra Golpayegani, Walid Ahmed, Yang Liu
**Date:** 2025-07-08
**Categories:** cs.CL

## Abstract

Transformer-based Language Models' computation and memory overhead increase quadratically as a function of sequence length. The quadratic cost poses challenges when employing LLMs for processing long sequences. In this work, we introduce \ourmodelacronym~(Extend at Test-Time), method for extending the context length of short context Transformer-based LLMs, with constant memory requirement and linear computation overhead. ETT enable the extension of the context length at test-time by efficient fine-tuning the model's parameters on the input context, chunked into overlapping small subsequences. We evaluate ETT on LongBench by extending the context length of GPT-Large and Phi-2 up to 32 times, increasing from 1k to 32k tokens. This results in up to a 30 percent improvement in the model's accuracy. We also study how context can be stored in LLM's weights effectively and efficiently. Through a detailed ablation study, we examine which Transformer modules are most beneficial to fine-tune at test-time. Interestingly, we find that fine-tuning the second layer of the FFNs is more effective than full fine-tuning, leading to a further improvement in the models' accuracy.

---
*Metadata fetched via arxiv API on 2025-12-31*
