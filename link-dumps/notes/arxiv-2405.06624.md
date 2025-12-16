# Towards Guaranteed Safe AI: A Framework for Ensuring Robust and Reliable AI Systems

**arXiv:** https://arxiv.org/abs/2405.06624
**Authors:** David "davidad" Dalrymple, Joar Skalse, Yoshua Bengio, Stuart Russell, Max Tegmark, Sanjit Seshia, Steve Omohundro, Christian Szegedy, Ben Goldhaber, Nora Ammann, Alessandro Abate, Joe Halpern, Clark Barrett, Ding Zhao, Tan Zhi-Xuan, Jeannette Wing, Joshua Tenenbaum
**Date:** 2024-05-10 (v1), revised 2024-07-08 (v3)

## Abstract

Ensuring that AI systems reliably and robustly avoid harmful or dangerous behaviours is a crucial challenge, especially for AI systems with a high degree of autonomy and general intelligence, or systems used in safety-critical contexts.

The paper introduces and defines a family of approaches to AI safety referred to as "guaranteed safe (GS) AI." The core feature of these approaches is that they aim to produce AI systems which are equipped with high-assurance quantitative safety guarantees.

This is achieved by the interplay of three core components:
1. **World model**: Mathematical description of how the AI system affects the outside world
2. **Safety specification**: Mathematical description of what effects are acceptable
3. **Verifier**: Provides an auditable proof certificate that the AI satisfies the safety specification relative to the world model

## Claude Summary

This is a major position paper from leading AI safety researchers (Bengio, Russell, Tegmark, etc.) advocating for "Guaranteed Safe AI" - systems with formal, verifiable safety guarantees rather than empirical testing alone.

The GS AI framework proposes moving beyond:
- "Hope and pray" approaches
- Empirical testing (which can miss edge cases)
- Behavioral constraints without formal verification

To a more rigorous paradigm where:
- Safety properties are mathematically specified
- World models capture relevant system dynamics
- Verifiers provide auditable proof certificates

This represents a more ambitious vision of AI safety, borrowing from formal methods, control theory, and program verification.

## Relevance

Foundational for AI safety research direction. Proposes a formal framework that could provide stronger safety guarantees than current approaches. Important for understanding the landscape of AI safety strategies.
