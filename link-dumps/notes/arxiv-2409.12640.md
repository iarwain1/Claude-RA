# Michelangelo: Long Context Evaluations Beyond Haystacks via Latent Structure Queries

**arXiv:** [2409.12640](https://arxiv.org/abs/2409.12640)
**Authors:** Kiran Vodrahalli, Santiago Ontanon, Nilesh Tripuraneni, Kelvin Xu, Sanil Jain, et al. (24 total)
**Date:** 2024-09-19
**Categories:** cs.CL, cs.LG

## Abstract

We introduce Michelangelo: a minimal, synthetic, and unleaked long-context reasoning evaluation for large language models which is also easy to automatically score. This evaluation is derived via a novel, unifying framework for evaluations over arbitrarily long contexts which measure the model's ability to do more than retrieve a single piece of information from its context. The central idea of the Latent Structure Queries framework (LSQ) is to construct tasks which require a model to ``chisel away'' the irrelevant information in the context, revealing a latent structure in the context. To verify a model's understanding of this latent structure, we query the model for details of the structure. Using LSQ, we produce three diagnostic long-context evaluations across code and natural-language domains intended to provide a stronger signal of long-context language model capabilities. We perform evaluations on several state-of-the-art models and demonstrate both that a) the proposed evaluations are high-signal and b) that there is significant room for improvement in synthesizing long-context information.

---
*Metadata fetched via arxiv API on 2025-12-31*
