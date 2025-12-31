# Automating Thought of Search: A Journey Towards Soundness and Completeness

**arXiv:** [2408.11326](https://arxiv.org/abs/2408.11326)
**Authors:** Daniel Cao, Michael Katz, Harsha Kokel, Kavitha Srinivas, Shirin Sohrabi
**Date:** 2024-08-21
**Categories:** cs.AI

## Abstract

Large language models (LLMs) are being used to solve planning problems that require search. Most of the literature uses LLMs as world models to define the search space, forgoing soundness for the sake of flexibility. A recent work, Thought of Search (ToS), proposed defining the search space with code, having LLMs produce that code. ToS requires a human in the loop, collaboratively producing a sound successor function and goal test. The result, however, is worth the effort: all the tested datasets were solved with 100% accuracy. Consequently, there is great potential to automate the ToS process. We take a first major step towards automating ToS (AutoToS), taking the human out of the loop of interactions with the language model. AutoToS guides the language model step by step towards the generation of sound and complete search components, through feedback from both generic and domain specific unit tests. We show that AutoToS is able to achieve 100% accuracy on all the evaluated domains with a small number of LLM calls.

---
*Metadata fetched via arxiv API on 2025-12-31*
