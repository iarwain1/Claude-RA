# AgentBench: Evaluating LLMs as Agents

**arXiv:** https://arxiv.org/abs/2308.03688
**Authors:** Xiao Liu, Hao Yu, Hanchen Zhang, Yifan Xu, Xuanyu Lei, Hanyu Lai, Yu Gu, et al. (22 authors, Tsinghua University)
**Date:** 2023-08 (v1)
**Venue:** ICLR 2024

## Abstract

Large Language Models (LLMs) are becoming increasingly smart and autonomous, targeting real-world pragmatic missions beyond traditional NLP tasks. As a result, there has been an urgent need to evaluate LLMs as agents on challenging tasks in interactive environments.

AgentBench is a multi-dimensional evolving benchmark that currently consists of 8 distinct environments to assess LLM-as-Agent's reasoning and decision-making abilities in a multi-turn open-ended generation setting.

Extensive testing over 27 API-based and open-sourced LLMs shows that while top commercial LLMs present a strong ability of acting as agents in complex environments, there is a significant disparity in performance between them and OSS competitors.

## Key Findings

- Poor long-term reasoning, decision-making, and instruction following are main obstacles for usable LLM agents
- Improving instruction following and training on high-quality multi-round alignment data improves agent performance
- Training on code presents ambivalent impacts on different agent tasks

## Claude Summary

AgentBench is a foundational benchmark for evaluating LLMs as autonomous agents, published at ICLR 2024. It provides:

- 8 distinct interactive environments
- Multi-turn evaluation settings
- Comprehensive LLM comparison (27 models)

The finding that commercial LLMs significantly outperform open-source alternatives on agent tasks has important implications for AI deployment and capability gaps.

## Relevance

Essential benchmark for agent capabilities. Provides systematic framework for evaluating LLM autonomy. Important for understanding the commercial vs. open-source capability gap.

## Resources

- GitHub: https://github.com/THUDM/AgentBench
