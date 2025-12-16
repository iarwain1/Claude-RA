# LLaMA: Open and Efficient Foundation Language Models

**arXiv:** https://arxiv.org/abs/2302.13971
**Authors:** Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, Aurelien Rodriguez, Armand Joulin, Edouard Grave, Guillaume Lample (Meta AI)
**Date:** 2023-02-27

## Abstract

The paper introduces LLaMA, a collection of foundation language models ranging from 7B to 65B parameters. The models are trained on trillions of tokens using only publicly available datasets, without resorting to proprietary data.

## Key Results

- **LLaMA-13B outperforms GPT-3 (175B)** on most benchmarks, despite being 10× smaller
- **LLaMA-65B** is competitive with Chinchilla-70B and PaLM-540B
- All models use only publicly available data
- Models released to research community

## Claude Summary

LLaMA is arguably the most impactful open-source AI release, catalyzing the entire open-source LLM ecosystem:

**Key insight**: Smaller, well-trained models can match larger models
- Follows Chinchilla scaling laws (more tokens, fewer parameters)
- 13B model beats 175B GPT-3

**Open-source impact**:
- Weights leaked shortly after release
- Spawned: Alpaca, Vicuna, Koala, WizardLM, etc.
- Enabled: QLoRA, GGML/llama.cpp, local LLM movement

**Training data** (publicly available):
- CommonCrawl, C4, Wikipedia
- GitHub, ArXiv, StackExchange
- Books (Gutenberg, Books3)

LLaMA democratized access to capable language models.

## Relevance

**Foundational for open-source AI.** Understanding LLaMA is essential for understanding the open-source LLM landscape. Led to LLaMA 2, LLaMA 3, and Meta's open model strategy.
