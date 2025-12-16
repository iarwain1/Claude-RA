# Infant Agent: A Tool-Integrated, Logic-Driven Agent with Cost-Effective API Usage

**arXiv:** https://arxiv.org/abs/2411.01114
**Authors:** Bin Lei, Yuchen Li, Yiming Zeng, Tao Ren, Yi Luo, Tianyu Shi, Zitian Gao, Zeyu Hu, Weitai Kang, Qiuwu Chen
**Date:** 2024-11-02

## Abstract

The paper addresses two primary limitations of large language models (LLMs): (1) They struggle to autonomously solve real-world engineering problems, and (2) They remain challenged in reasoning through complex logic problems. To address these challenges, the authors developed the Infant Agent, integrating task-aware functions, operators, a hierarchical management system, and a memory retrieval mechanism.

Together, these components enable large language models to sustain extended reasoning processes and handle complex, multi-step tasks efficiently, all while significantly reducing API costs.

## Key Results

- GPT-4o accuracy on SWE-bench-lite: **0.33% → 30%** (90x improvement)
- GPT-4o accuracy on AIME-2024: **13.3% → 37%** (2.8x improvement)

## Claude Summary

Infant Agent is an agent scaffolding framework that dramatically improves LLM performance on complex tasks through:
1. Task-aware function integration
2. Hierarchical management system
3. Memory retrieval mechanism

The results are striking - a 90x improvement on SWE-bench-lite suggests that much of the gap between raw LLM capability and agent performance lies in scaffolding design, not base model capability.

The cost-effectiveness focus is practically important for real-world deployment.

## Relevance

Demonstrates the power of agent scaffolding for capability amplification. Relevant for understanding true AI capabilities (base vs. scaffolded) and for AI safety considerations around capability elicitation.
