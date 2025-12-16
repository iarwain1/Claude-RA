# Distilling System 2 into System 1

**arXiv:** https://arxiv.org/abs/2407.06023
**Date:** 2024-07

## Abstract

This paper explores distilling the reasoning capabilities of "System 2" thinking (slow, deliberate, step-by-step reasoning) into "System 1" behavior (fast, automatic, intuitive responses) in large language models.

## The Core Problem

**System 2 approaches (e.g., Chain-of-Thought):**
- Improve LLM performance
- Computationally expensive
- Higher latency (more tokens generated)

**System 1 responses:**
- Fast and efficient
- May lack quality of deliberate reasoning
- Preferable for deployment if quality can be maintained

## The Solution

**Distillation approach:**
- Train models to produce high-quality answers directly (System 1 style)
- Learn from System 2 reasoning traces
- Essentially "compile" slow thinking into fast intuition

## Connection to Cognitive Science

The terminology comes from Kahneman's dual-process theory:
- **System 1**: Fast, automatic, intuitive
- **System 2**: Slow, deliberate, analytical

The paper applies this framework to LLM inference efficiency.

## Claude Summary

This paper addresses a practical trade-off in LLM deployment:

**The tension**: CoT and similar reasoning techniques work well but are expensive. Can we get the benefits without the cost?

**The approach**: Use System 2 reasoning as training signal, but at inference time operate in System 1 mode. The reasoning capability gets "baked in" rather than explicit.

**Practical implications**:
- Cheaper inference for production systems
- Lower latency responses
- May enable reasoning in resource-constrained settings

**Limitations**:
- Distillation is lossy - may not capture all reasoning benefits
- May reduce interpretability (no visible reasoning steps)
- Trade-off between efficiency and transparency

## Relevance

Important for practical LLM deployment. Shows how training-time compute can substitute for inference-time compute. Relevant to discussions of reasoning in LLMs and the role of chain-of-thought.
