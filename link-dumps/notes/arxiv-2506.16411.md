# When Does Divide and Conquer Work for Long Context LLM? A Noise Decomposition Framework

**arXiv:** [2506.16411](https://arxiv.org/abs/2506.16411)
**Authors:** Zhen Xu, Shang Zhu, Jue Wang, Junlin Wang, Ben Athiwaratkun, et al. (8 total)
**Date:** 2025-06-19
**Categories:** cs.CL, cs.LG

## Abstract

We investigate the challenge of applying Large Language Models (LLMs) to long texts. We propose a theoretical framework that distinguishes the failure modes of long context tasks into three categories: cross-chunk dependence (task noise), confusion that grows with context size (model noise), and the imperfect integration of partial results (aggregator noise). Under this view, we analyze when it is effective to use multi-agent chunking, i.e., dividing a length sequence into smaller chunks and aggregating the processed results of each chunk. Our experiments on tasks such as retrieval, question answering, and summarization confirm both the theoretical analysis and the conditions that favor multi-agent chunking. By exploring superlinear model noise growth with input length, we also explain why, for large inputs, a weaker model configured with chunk-based processing can surpass a more advanced model like GPT4o applied in a single shot. Overall, we present a principled understanding framework and our results highlight a direct pathway to handling long contexts in LLMs with carefully managed chunking and aggregator strategies.

---
*Metadata fetched via arxiv API on 2025-12-31*
