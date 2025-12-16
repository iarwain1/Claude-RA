# Games for AI Control: Models of Safety Evaluations of AI Deployment Protocols

**arXiv:** https://arxiv.org/abs/2409.07985
**Authors:** Charlie Griffin, Louis Thomson, Buck Shlegeris, Alessandro Abate
**Date:** 2024-09-12

## Abstract

To evaluate the safety and usefulness of deployment protocols for untrusted AIs, AI Control uses red-teaming exercises between a protocol designer and an adversary.

This paper introduces **AI-Control Games**: a formal decision-making model of the red-teaming exercise as a multi-objective, partially observable, stochastic game.

## Key Contributions

1. **Formal framework**: AI-Control Games model the strategic interaction between protocol designers and potential attackers

2. **Methods for finding optimal protocols**: Reduce to zero-sum partially observable stochastic games

3. **Application**: Model, evaluate, and synthesize protocols for deploying untrusted LLMs as programming assistants

## Focus: Trusted Monitoring Protocols

The paper focuses on protocols that use:
- Weaker language models (as monitors)
- Limited human assistance
- To oversee potentially untrusted stronger models

## Key Findings

- Formal analysis can improve over empirical studies
- Can evaluate protocols in new settings
- Modeling assumptions significantly affect safety/usefulness trade-offs

## Claude Summary

This paper provides rigorous game-theoretic foundations for AI Control:

**Why formalism matters**: Ad-hoc evaluation of control protocols may miss important attack vectors or overestimate safety. Formal analysis can find optimal strategies for both sides.

**Connection to AI Control literature**: Extends the empirical work on AI Control (Greenblatt et al. 2024) with theoretical grounding.

**Key insight**: The safety-usefulness trade-off in deployment protocols can be precisely characterized using game theory. This enables principled comparison of different approaches.

**Practical value**: Can synthesize protocols that are provably optimal within the model, and identify when empirical evaluations may be misleading.

## Relevance

Important theoretical contribution to AI Control. Provides mathematical foundations for evaluating deployment protocols. Useful for researchers working on trusted monitoring and deployment safety.
