# QLoRA: Efficient Finetuning of Quantized LLMs

**arXiv:** https://arxiv.org/abs/2305.14992
**Authors:** Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer (University of Washington)
**Date:** 2023-05
**Venue:** NeurIPS 2023

## Abstract

QLoRA (Quantized Low-Rank Adaptation) enables fine-tuning of large language models with dramatically reduced memory requirements while preserving full 16-bit fine-tuning performance.

## Key Innovations

1. **4-bit NormalFloat (NF4)**: New data type that is information-theoretically optimal for normally distributed weights
2. **Double Quantization**: Quantizing the quantization constants to save additional memory
3. **Paged Optimizers**: Using NVIDIA unified memory to handle memory spikes during gradient checkpointing

## Key Results

- Fine-tune a 65B parameter model on a single 48GB GPU
- Matches full fine-tuning performance on benchmarks
- Introduced the Guanaco family of models

## Claude Summary

QLoRA democratized LLM fine-tuning by making it accessible on consumer hardware:

**Problem**: Fine-tuning large models requires prohibitive memory (65B model needs ~780GB for full fine-tuning)

**Solution**: Combine 4-bit quantization with LoRA adapters
- Base model stored in 4-bit
- Adapters trained in higher precision
- Memory reduced by ~4x

**Impact**: Enabled researchers without large GPU clusters to fine-tune frontier-scale models. The Guanaco models showed QLoRA could match ChatGPT performance on some benchmarks.

## Relevance

Essential for efficient fine-tuning. Democratized access to LLM customization. Important for understanding memory-efficient training techniques.
