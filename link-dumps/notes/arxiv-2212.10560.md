# Self-Instruct: Aligning Language Models with Self-Generated Instructions

**arXiv:** https://arxiv.org/abs/2212.10560
**Authors:** Yizhong Wang, Yeganeh Kordi, Swaroop Mishra, Alisa Liu, Noah A. Smith, Daniel Khashabi, Hannaneh Hajishirzi (University of Washington, Allen AI)
**Date:** 2022-12
**Venue:** ACL 2023

## Abstract

Self-Instruct is a framework for improving the instruction-following capabilities of pretrained language models by bootstrapping off their own generations.

The method:
1. Uses a language model to generate instructions
2. Generates input-output pairs for those instructions
3. Filters low-quality examples
4. Fine-tunes the original model on the generated data

This approach reduces the reliance on human-annotated instruction data.

## Key Results

- Applying Self-Instruct to GPT-3 resulted in 33% improvement on Super-NaturalInstructions benchmark
- Performance approached InstructGPT-001 (trained with human feedback)
- Demonstrated that models can bootstrap their own instruction-following ability

## Claude Summary

Self-Instruct pioneered the idea of using LLMs to generate their own training data:

**Key insight**: LLMs can generate diverse, high-quality instruction-following examples that can be used to improve themselves.

**Pipeline**:
1. Seed with small set of human instructions
2. Generate new instructions
3. Generate inputs and outputs
4. Filter for quality
5. Fine-tune

**Impact**: Directly inspired:
- Stanford Alpaca (self-instruct on LLaMA)
- Many other synthetic data approaches
- The entire "open-source LLM" movement

## Relevance

Foundational for synthetic data generation in LLM training. Enabled the open-source instruction-tuned model ecosystem. Important for understanding how to efficiently create training data.
