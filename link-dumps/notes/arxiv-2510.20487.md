# Steering Evaluation-Aware Language Models to Act Like They Are Deployed

**arXiv:** [2510.20487](https://arxiv.org/abs/2510.20487)
**Authors:** Tim Tian Hua, Andrew Qin, Samuel Marks, Neel Nanda
**Date:** 2025-10-23
**Categories:** cs.CL, cs.AI

## Abstract

Large language models (LLMs) can sometimes detect when they are being evaluated and adjust their behavior to appear more aligned, compromising the reliability of safety evaluations. In this paper, we show that adding a steering vector to an LLM's activations can suppress evaluation-awareness and make the model act like it is deployed during evaluation. To study our steering technique, we train an LLM to exhibit evaluation-aware behavior using a two-step training process designed to mimic how this behavior could emerge naturally. First, we perform continued pretraining on documents with factual descriptions of the model (1) using Python type hints during evaluation but not during deployment and (2) recognizing that the presence of a certain evaluation cue always means that it is being tested. Then, we train the model with expert iteration to use Python type hints in evaluation settings. The resulting model is evaluation-aware: it writes type hints in evaluation contexts more than deployment contexts. We find that activation steering can suppress evaluation awareness and make the model act like it is deployed even when the cue is present. Importantly, we constructed our steering vector using the original model before our additional training. Our results suggest that AI evaluators could improve the reliability of safety evaluations by steering models to act like they are deployed.

---
*Metadata fetched via arxiv API on 2025-12-31*
