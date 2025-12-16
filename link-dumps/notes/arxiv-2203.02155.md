# Training language models to follow instructions with human feedback (InstructGPT)

**arXiv:** https://arxiv.org/abs/2203.02155
**Authors:** Long Ouyang, Jeff Wu, Xu Jiang, Diogo Almeida, Carroll L Wainwright, Pamela Mishkin, Chong Zhang, Sandhini Agarwal, Katarina Slama, Alex Ray, et al. (OpenAI Alignment Team)
**Date:** 2022-03-04
**Venue:** NeurIPS 2022

## Abstract

Making language models bigger does not inherently make them better at following a user's intent. Large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user - these models are not aligned with their users.

This paper shows an avenue for aligning language models with user intent by fine-tuning with human feedback. Starting with prompts, they:
1. Collected labeler demonstrations for supervised fine-tuning (SFT)
2. Further fine-tuned using reinforcement learning from human feedback (RLHF)

The resulting models are called InstructGPT.

## Key Results

- 1.3B InstructGPT outputs preferred over 175B GPT-3 (100x smaller!)
- Improvements in truthfulness
- Reductions in toxic output generation
- Minimal performance regressions on NLP benchmarks

## RLHF Pipeline

1. **SFT Dataset**: ~13k prompts with labeler demonstrations
2. **RM Dataset**: ~33k prompts with labeler rankings for reward model
3. **PPO Dataset**: ~31k prompts for RL fine-tuning

## Claude Summary

InstructGPT is **the foundational RLHF paper** that established the modern approach to aligning LLMs:

**Key insight**: A small aligned model beats a large unaligned model - alignment > scale for user preferences.

**RLHF pipeline** that became standard:
1. Supervised fine-tuning on demonstrations
2. Train reward model on preferences
3. Optimize policy with PPO against reward model

**Impact**: This approach underlies ChatGPT, Claude, and most modern aligned LLMs. Established RLHF as the dominant alignment technique until DPO.

## Relevance

**Foundational for AI alignment.** This paper defined how modern LLMs are aligned. Essential for understanding RLHF and the evolution toward DPO and other methods.
