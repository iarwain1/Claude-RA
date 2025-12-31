# Scalable MatMul-free Language Modeling

**arXiv:** [2406.02528](https://arxiv.org/abs/2406.02528)
**Authors:** Rui-Jie Zhu, Yu Zhang, Steven Abreu, Ethan Sifferman, Tyler Sheaves, et al. (10 total)
**Date:** 2024-06-04
**Categories:** cs.CL

## Abstract

Large Language Models (LLMs) have fundamentally altered how we approach scaling in machine learning. However, these models pose substantial computational and memory challenges, primarily due to the reliance on matrix multiplication (MatMul) within their attention and feed-forward (FFN) layers. We demonstrate that MatMul operations can be eliminated from LLMs while maintaining strong performance, even at billion-parameter scales. Our MatMul-free models, tested on models up to 2.7B parameters, are comparable to state-of-the-art pre-trained Transformers, and the performance gap narrows as model size increases. Our approach yields significant memory savings: a GPU-efficient implementation reduces memory consumption by up to 61% during training and over 10x during inference. When adapted for a multi-chip neuromorphic system, the model leverages asynchronous processing to achieve 4x higher throughput with 10x less energy than edge GPUs.

---
*Metadata fetched via arxiv API on 2025-12-31*
