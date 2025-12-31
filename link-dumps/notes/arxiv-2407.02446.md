# Predicting vs. Acting: A Trade-off Between World Modeling & Agent Modeling

**arXiv:** [2407.02446](https://arxiv.org/abs/2407.02446)
**Authors:** Margaret Li, Weijia Shi, Artidoro Pagnoni, Peter West, Ari Holtzman
**Date:** 2024-07-02
**Categories:** cs.CL, cs.AI

## Abstract

RLHF-aligned LMs have shown unprecedented ability on both benchmarks and long-form text generation, yet they struggle with one foundational task: next-token prediction. As RLHF models become agent models aimed at interacting with humans, they seem to lose their world modeling -- the ability to predict what comes next in arbitrary documents, which is the foundational training objective of the Base LMs that RLHF adapts.
  Besides empirically demonstrating this trade-off, we propose a potential explanation: to perform coherent long-form generation, RLHF models restrict randomness via implicit blueprints. In particular, RLHF models concentrate probability on sets of anchor spans that co-occur across multiple generations for the same prompt, serving as textual scaffolding but also limiting a model's ability to generate documents that do not include these spans. We study this trade-off on the most effective current agent models, those aligned with RLHF, while exploring why this may remain a fundamental trade-off between models that act and those that predict, even as alignment techniques improve.

---
*Metadata fetched via arxiv API on 2025-12-31*
