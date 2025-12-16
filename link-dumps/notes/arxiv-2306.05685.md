# Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena

**arXiv:** https://arxiv.org/abs/2306.05685
**Authors:** Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E. Gonzalez, Ion Stoica (UC Berkeley, LMSYS)
**Date:** 2023-06-09 (v1), revised 2023-12-24 (v4)

## Abstract

Evaluating large language model (LLM) based chat assistants is challenging due to their broad capabilities and the inadequacy of existing benchmarks in measuring human preferences. To address this, the authors explore using strong LLMs as judges to evaluate these models on more open-ended questions.

They examine the usage and limitations of LLM-as-a-judge, including:
- Position bias
- Verbosity bias
- Self-enhancement bias
- Limited reasoning ability

They verify the agreement between LLM judges and human preferences by introducing two benchmarks:
1. **MT-bench**: Multi-turn question set
2. **Chatbot Arena**: Crowdsourced battle platform

Results reveal that strong LLM judges like GPT-4 can match both controlled and crowdsourced human preferences well, achieving over 80% agreement.

## Claude Summary

This paper introduced the influential MT-Bench and Chatbot Arena evaluation frameworks that have become standard for LLM evaluation:

**MT-Bench**: Structured multi-turn conversations testing specific capabilities
**Chatbot Arena**: Crowdsourced head-to-head comparisons with ELO ratings

**Key contribution**: Validated that LLM judges (like GPT-4) can approximate human preferences with ~80% agreement, enabling scalable evaluation.

**Identified biases** in LLM-as-judge:
- Position bias (first response preferred)
- Verbosity bias (longer = better)
- Self-enhancement (models prefer own outputs)

This work is foundational for the LLM-as-judge paradigm now widely used.

## Relevance

Essential for AI evaluation methodology. Introduced benchmarks (MT-Bench, Chatbot Arena) now standard in the field. Important for understanding LLM-as-judge limitations.
