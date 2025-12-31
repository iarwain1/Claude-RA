# Analyzing Probabilistic Methods for Evaluating Agent Capabilities

**arXiv:** [2409.16125](https://arxiv.org/abs/2409.16125)
**Authors:** Axel Højmark, Govind Pimpale, Arjun Panickssery, Marius Hobbhahn, Jérémy Scheurer
**Date:** 2024-09-24
**Categories:** cs.AI

## Abstract

To mitigate risks from AI systems, we need to assess their capabilities accurately. This is especially difficult in cases where capabilities are only rarely displayed. Phuong et al. propose two methods that aim to obtain better estimates of the probability of an AI agent successfully completing a given task. The milestone method decomposes tasks into subtasks, aiming to improve overall success rate estimation, while the expert best-of-N method leverages human guidance as a proxy for the model's independent performance.
  Our analysis of these methods as Monte Carlo estimators reveals that while both effectively reduce variance compared to naive Monte Carlo sampling, they also introduce bias. Experimental results demonstrate that the milestone method underestimates true solve rates for many real-world tasks due to its constraining assumptions. The expert best-of-N method exhibits even more severe underestimation across all tasks, attributed to an inherently flawed re-weighting factor. To enhance the accuracy of capability estimates of AI agents on difficult tasks, we suggest future work should leverage the rich literature on Monte Carlo Estimators.

---
*Metadata fetched via arxiv API on 2025-12-31*
