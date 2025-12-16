# ReAct: Synergizing Reasoning and Acting in Language Models

**arXiv:** https://arxiv.org/abs/2210.03629
**Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao (Princeton, Google)
**Date:** 2022-10-06 (v1), revised 2023-03-10 (v3)
**Venue:** ICLR 2023

## Abstract

While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g., chain-of-thought prompting) and acting (e.g., action plan generation) have primarily been studied as separate topics.

This paper explores the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two:
- Reasoning traces help the model induce, track, and update action plans as well as handle exceptions
- Actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information

## Key Results

- **HotpotQA & Fever**: ReAct overcomes hallucination and error propagation by interacting with Wikipedia API
- **ALFWorld**: 34% absolute improvement over imitation/RL methods
- **WebShop**: 10% absolute improvement
- Achieves this with only 1-2 in-context examples

## Claude Summary

ReAct is a **foundational paper for LLM agents**, introducing the interleaved reasoning+acting paradigm that underlies most modern agent architectures.

**Key insight**: Separating reasoning (chain-of-thought) from acting (tool use) is suboptimal. Interleaving them allows:
- Reasoning to inform action selection
- Action results to update reasoning
- Better handling of exceptions and errors

**Pattern**: Think → Act → Observe → Think → Act → ...

This paper essentially created the template that frameworks like LangChain, AutoGPT, and others build upon.

## Relevance

**Foundational for agent research.** The ReAct pattern is now ubiquitous in LLM agent design. Essential reading for understanding modern agent architectures.

## Resources

- Project page: https://react-lm.github.io/
