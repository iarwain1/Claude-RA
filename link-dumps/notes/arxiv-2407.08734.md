# Transformer Circuit Faithfulness Metrics are not Robust

**arXiv:** [2407.08734](https://arxiv.org/abs/2407.08734)
**Authors:** Joseph Miller, Bilal Chughtai, William Saunders
**Date:** 2024-07-11
**Categories:** cs.LG, cs.AI, cs.CL

## Abstract

Mechanistic interpretability work attempts to reverse engineer the learned algorithms present inside neural networks. One focus of this work has been to discover 'circuits' -- subgraphs of the full model that explain behaviour on specific tasks. But how do we measure the performance of such circuits? Prior work has attempted to measure circuit 'faithfulness' -- the degree to which the circuit replicates the performance of the full model. In this work, we survey many considerations for designing experiments that measure circuit faithfulness by ablating portions of the model's computation. Concerningly, we find existing methods are highly sensitive to seemingly insignificant changes in the ablation methodology. We conclude that existing circuit faithfulness scores reflect both the methodological choices of researchers as well as the actual components of the circuit - the task a circuit is required to perform depends on the ablation used to test it. The ultimate goal of mechanistic interpretability work is to understand neural networks, so we emphasize the need for more clarity in the precise claims being made about circuits. We open source a library at https://github.com/UFO-101/auto-circuit that includes highly efficient implementations of a wide range of ablation methodologies and circuit discovery algorithms.

---
*Metadata fetched via arxiv API on 2025-12-31*
