# Self-Consistency Improves Chain of Thought Reasoning in Language Models

**arXiv:** [2203.11171](https://arxiv.org/abs/2203.11171)
**Authors:** Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, et al. (8 total)
**Date:** 2022-03-21
**Categories:** cs.CL, cs.AI

## Abstract

Chain-of-thought prompting combined with pre-trained large language models has achieved encouraging results on complex reasoning tasks. In this paper, we propose a new decoding strategy, self-consistency, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths instead of only taking the greedy one, and then selects the most consistent answer by marginalizing out the sampled reasoning paths. Self-consistency leverages the intuition that a complex reasoning problem typically admits multiple different ways of thinking leading to its unique correct answer. Our extensive empirical evaluation shows that self-consistency boosts the performance of chain-of-thought prompting with a striking margin on a range of popular arithmetic and commonsense reasoning benchmarks, including GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).

---
*Metadata fetched via arxiv API on 2025-12-31*
