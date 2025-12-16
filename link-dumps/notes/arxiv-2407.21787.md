# Large Language Monkeys: Scaling Inference Compute with Repeated Sampling

**arXiv:** https://arxiv.org/abs/2407.21787
**Authors:** Bradley Brown, Jordan Juravsky, Ryan Ehrlich, Ronald Clark, Quoc V. Le, Christopher Ré, Azalia Mirhoseini
**Date:** 2024-07-31 (v1), revised 2024-12-30 (v3)

## Abstract

Scaling the amount of compute used to train language models has dramatically improved their capabilities. However, when it comes to inference, we often limit models to making only one attempt at a problem. The authors explore inference compute as another axis for scaling, using the simple technique of repeatedly sampling candidate solutions from a model.

Across multiple tasks and models, they observe that coverage -- the fraction of problems that are solved by any generated sample -- scales with the number of samples over four orders of magnitude. Interestingly, the relationship between coverage and the number of samples is often log-linear and can be modelled with an exponentiated power law, suggesting the existence of inference-time scaling laws.

In domains like coding and formal proofs, where answers can be automatically verified, these increases in coverage directly translate into improved performance.

## Claude Summary

This paper establishes "inference-time scaling laws" - showing that simply sampling multiple solutions from an LLM and selecting the best one (via verifier) yields predictable, log-linear improvements in problem coverage. Key insight: inference compute can be scaled independently of training compute.

The methodology is straightforward: generate many candidate solutions at positive temperature, then use domain-specific verifiers (unit tests for code, proof checkers for math) to select correct answers. This works especially well in verifiable domains.

Implications for AI safety: this technique could amplify both capabilities and potential misuse. Models that seem limited by single-sample performance may be much more capable with repeated sampling + verification.

## Relevance

Important for understanding AI capability scaling beyond training. Directly relevant to AI evaluations - single-attempt benchmarks may underestimate true model capabilities. Also relevant to AI safety discussions about capability elicitation.
