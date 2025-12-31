# Benchmarking World-Model Learning

**arXiv:** [2510.19788](https://arxiv.org/abs/2510.19788)
**Authors:** Archana Warrier, Dat Nguyen, Michelangelo Naim, Moksh Jain, Yichao Liang, et al. (11 total)
**Date:** 2025-10-22
**Categories:** cs.AI, cs.LG

## Abstract

Model-learning agents should gather information to learn world models that support many downstream tasks and inferences, such as predicting unobserved states, estimating near- and far-term consequences of actions, planning action sequences, and detecting changes in dynamics. Current methods for learning and evaluating world models diverge from this goal: training and evaluation are anchored to next-frame prediction, and success is scored by reward maximization in the same environment. We propose WorldTest, a protocol to evaluate model-learning agents that separates reward-free interaction from a scored test phase in a different but related environment. WorldTest is open-ended $\unicode{x2014}$ models should support many different tasks unknown ahead of time $\unicode{x2014}$ and agnostic to model representation, allowing comparison across approaches. We instantiated WorldTest with AutumnBench, a suite of 43 interactive grid-world environments and 129 tasks across three families: masked-frame prediction, planning, and predicting changes to the causal dynamics. We compared 517 human participants and three frontier models on AutumnBench. We found that humans outperform the models, and scaling compute improves performance only in some environments but not others. WorldTest provides a novel template $\unicode{x2014}$ reward-free exploration, derived tests, and behavior-based scoring $\unicode{x2014}$ to evaluate what agents learn about environment dynamics, and AutumnBench exposes significant headroom in world-model learning.

---
*Metadata fetched via arxiv API on 2025-12-31*
