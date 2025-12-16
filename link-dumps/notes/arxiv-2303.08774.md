# GPT-4 Technical Report

**arXiv:** https://arxiv.org/abs/2303.08774
**Authors:** OpenAI (279+ contributors)
**Date:** 2023-03-15 (v1), revised 2024-03-04 (v6)

## Abstract

The paper reports the development of GPT-4, a large-scale, multimodal model which can accept image and text inputs and produce text outputs. While less capable than humans in many real-world scenarios, GPT-4 exhibits human-level performance on various professional and academic benchmarks, including passing a simulated bar exam with a score around the top 10% of test takers.

GPT-4 is a Transformer-based model pre-trained to predict the next token in a document. The post-training alignment process results in improved performance on measures of factuality and adherence to desired behavior.

A core component of this project was developing infrastructure and optimization methods that behave predictably across a wide range of scales. This allowed them to accurately predict some aspects of GPT-4's performance based on models trained with no more than 1/1,000th the compute of GPT-4.

## Key Features

- **Multimodal**: Accepts both image and text inputs
- **Benchmark performance**: Human-level on many professional exams
- **Predictable scaling**: Performance predictable from smaller models
- **Extensive system card**: Detailed safety analysis

## Claude Summary

The GPT-4 technical report is notable for what it **doesn't** reveal (architecture, training data, compute) as much as what it does:

**What's disclosed**:
- Benchmark results across academic/professional exams
- Safety evaluation methodology
- Predictable scaling laws for loss prediction
- Extensive system card on risks

**What's hidden**:
- Model size
- Architecture details
- Training data composition
- Training compute

This report marked OpenAI's shift toward less transparency, citing competitive and safety concerns.

## Relevance

Important for understanding GPT-4 capabilities and OpenAI's safety approach. The system card is valuable for AI risk evaluation methodology.
