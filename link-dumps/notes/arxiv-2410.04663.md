# Debate, Deliberate, Decide (D3): A Cost-Aware Adversarial Framework for Reliable and Interpretable LLM Evaluation

**arXiv:** [2410.04663](https://arxiv.org/abs/2410.04663)
**Authors:** Chaithanya Bandi, Abir Harrasse
**Date:** 2024-10-07
**Categories:** cs.CL, cs.LG, cs.MA

## Abstract

The evaluation of Large Language Models (LLMs) remains challenging due to inconsistency, bias, and the absence of transparent decision criteria in automated judging. We present Debate, Deliberate, Decide (D3), a cost-aware, adversarial multi-agent framework that orchestrates structured debate among role-specialized agents (advocates, a judge, and an optional jury) to produce reliable and interpretable evaluations. D3 instantiates two complementary protocols: (1) Multi-Advocate One-Round Evaluation (MORE), which elicits k parallel defenses per answer to amplify signal via diverse advocacy, and (2) Single-Advocate Multi-Round Evaluation (SAMRE) with budgeted stopping, which iteratively refines arguments under an explicit token budget and convergence checks. We develop a probabilistic model of score gaps that (i) characterizes reliability and convergence under iterative debate and (ii) explains the separation gains from parallel advocacy. Under mild assumptions, the posterior distribution of the round-r gap concentrates around the true difference and the probability of mis-ranking vanishes; moreover, aggregating across k advocates provably increases expected score separation. We complement theory with a rigorous experimental suite across MT-Bench, AlignBench, and AUTO-J, showing state-of-the-art agreement with human judgments (accuracy and Cohen's kappa), reduced positional and verbosity biases via anonymization and role diversification, and a favorable cost-accuracy frontier enabled by budgeted stopping. Ablations and qualitative analyses isolate the contributions of debate, aggregation, and anonymity. Together, these results establish D3 as a principled, practical recipe for reliable, interpretable, and cost-aware LLM evaluation.

---
*Metadata fetched via arxiv API on 2025-12-31*
