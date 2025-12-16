# Llama 2: Open Foundation and Fine-Tuned Chat Models

**arXiv:** https://arxiv.org/abs/2307.09288
**Authors:** Hugo Touvron, Louis Martin, Kevin Stone, et al. (68 authors, Meta AI)
**Date:** 2023-07-18

## Abstract

Llama 2 is a collection of pretrained and fine-tuned large language models ranging from 7B to 70B parameters. The fine-tuned LLMs, called Llama 2-Chat, are optimized for dialogue use cases.

Llama 2 achieves superior performance in dialogue tasks compared to open-source alternatives and offers safety enhancements. The paper provides detailed description of fine-tuning and safety improvements.

## Key Features

- Model sizes: 7B, 13B, 70B parameters
- Trained on 40% more data than LLaMA 1
- Context length: 4096 tokens (2x LLaMA 1)
- **Commercial license** (unlike LLaMA 1)
- Extensive safety fine-tuning

## Safety Approach

- RLHF for helpfulness and safety
- Red-teaming for adversarial testing
- Safety system prompts
- Detailed safety evaluation

## Claude Summary

Llama 2 was Meta's pivot to truly open-source AI with a commercial license:

**Improvements over LLaMA 1**:
- 40% more training data (2T tokens)
- 2x context length (4096)
- Group Query Attention for efficiency
- Commercial-friendly license

**Chat models**: Llama 2-Chat used RLHF similar to ChatGPT, with:
- Supervised fine-tuning on demonstrations
- Reward modeling on preferences
- PPO optimization

**Impact**: Became the standard open-source foundation model, enabling widespread commercial deployment.

## Relevance

Essential for understanding open-source LLM landscape. Documents Meta's RLHF approach. Important baseline for comparing open models.
