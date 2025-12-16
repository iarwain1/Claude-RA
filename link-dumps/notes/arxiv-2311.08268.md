# A Wolf in Sheep's Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily

**arXiv:** https://arxiv.org/abs/2311.08268
**Authors:** Peng Ding, Jun Kuang, Dan Ma, Xuezhi Cao, Yunsen Xian, Jiajun Chen, Shujian Huang (Nanjing University, Meituan)
**Date:** 2023-11-14 (v1), revised 2024-04-07 (v4)
**Venue:** NAACL 2024

## Abstract

Large Language Models (LLMs), such as ChatGPT and GPT-4, are designed to provide useful and safe responses. However, adversarial prompts known as 'jailbreaks' can circumvent safeguards, leading LLMs to generate potentially harmful content.

Existing jailbreak methods suffer from:
- Intricate manual design, or
- Requiring optimization on white-box models (compromising generalization/efficiency)

This paper generalizes jailbreak prompt attacks into two aspects:
1. **Prompt Rewriting**
2. **Scenario Nesting**

Based on this, they propose **ReNeLLM**, an automatic framework that leverages LLMs themselves to generate effective jailbreak prompts.

## Key Results

- ReNeLLM significantly improves attack success rate
- Greatly reduces time cost compared to existing baselines
- Difficult to detect by existing defense methods
- Exhibits generalization and transferability across representative LLMs

## Claude Summary

ReNeLLM represents an important step in understanding jailbreak vulnerabilities:

**Key insight**: Jailbreaks can be decomposed into prompt rewriting (paraphrasing harmful requests) and scenario nesting (embedding requests in fictional contexts). This systematic framework allows automated generation of jailbreaks.

**Why it matters**:
- Shows that LLMs can be used to jailbreak themselves
- Demonstrates transferability across models
- Evades existing defenses

**For AI safety**: Understanding attack taxonomies is essential for building robust defenses. The prompt rewriting + scenario nesting decomposition provides a useful framework for thinking about jailbreak vulnerabilities.

## Relevance

Important for understanding the landscape of jailbreak attacks. Provides a systematic taxonomy that helps in thinking about defenses. The automated approach using LLMs to generate jailbreaks is particularly concerning for scalable attacks.
