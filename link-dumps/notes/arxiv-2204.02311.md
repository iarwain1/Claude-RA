# PaLM: Scaling Language Modeling with Pathways

**arXiv:** https://arxiv.org/abs/2204.02311
**Authors:** Aakanksha Chowdhery, Sharan Narang, Jacob Devlin, Maarten Bosma, et al. (67 authors, Google)
**Date:** 2022-04-05 (v1), revised 2022-10-05 (v5)

## Abstract

Large language models have been shown to achieve remarkable performance across a variety of natural language tasks using few-shot learning. To further understand the impact of scale, the authors trained a 540-billion parameter, densely activated, Transformer language model called Pathways Language Model (PaLM).

PaLM was trained on 6144 TPU v4 chips using Pathways, a new ML system which enables highly efficient training across multiple TPU Pods.

## Key Results

- State-of-the-art few-shot learning on hundreds of benchmarks
- Breakthrough performance on multi-step reasoning tasks
- Outperforms average human performance on BIG-bench
- Discontinuous improvements from scale on many tasks
- Strong multilingual and code generation capabilities

## Claude Summary

PaLM was Google's response to GPT-3, pushing scale to 540B parameters:

**Scale**: 540B parameters, trained on 6144 TPU v4s
**Training**: Used Pathways system for efficient multi-pod training

**Key findings**:
1. **Emergent abilities**: Many capabilities appear discontinuously at scale
2. **Reasoning**: Strong multi-step reasoning, especially with CoT
3. **BIG-bench**: First model to exceed average human performance

**Architecture improvements over GPT**:
- SwiGLU activation
- Parallel attention/FFN layers
- Multi-query attention
- RoPE embeddings
- No biases
- Vocabulary from SentencePiece

PaLM (and later PaLM 2) underlies Gemini and Google's AI products.

## Relevance

Important for understanding scale's impact on capabilities. Documents emergent abilities. Influential architecture choices adopted by later models.
