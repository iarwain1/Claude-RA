# AI Control: Improving Safety Despite Intentional Subversion

**arXiv:** https://arxiv.org/abs/2312.06942
**Authors:** Ryan Greenblatt et al. (Redwood Research)
**Date:** 2023-12 (v1), ICML 2024
**Venue:** International Conference on Machine Learning 2024

## Abstract

The paper addresses the concern that in the future, when LLMs are more powerful and deployed more autonomously, they will increasingly have the opportunity and ability to take actions that might have significant bad outcomes. Therefore, the safety mechanisms in the pipelines around these models will become increasingly important.

Past research has not assessed whether safety pipelines remain effective even if LLMs intentionally attempt to bypass them. Intentional subversion of safety techniques could occur if AIs start pursuing objectives that don't align with their intended goals, or if their weights or training data are compromised by attackers.

## Key Concepts

- **Control evaluation**: An evaluation that estimates the safety of a protocol by replacing an AI that might be intentionally subverting safety measures with a red-team-provided attack policy
- **Trusted monitoring**: Using a trusted but less capable model (e.g., GPT-3.5) to monitor outputs from a more capable but untrusted model (GPT-4)
- **Audit**: The process of using high-quality labor to analyze a particular model output

## Claude Summary

This is the foundational "AI Control" paper from Redwood Research, introducing a new paradigm for AI safety that assumes models may be intentionally adversarial.

**Key insight**: Safety measures should be designed to work even if the AI is actively trying to subvert them - either due to misalignment or compromise.

**Methodology**: Red-team safety pipelines where the "attacker" controls the AI's strategy, evaluating whether blue-team protocols remain robust.

**Practical techniques**: Trusted monitoring, auditing, and other defense strategies that don't rely on the model being cooperative.

This represents a shift from "behavioral safety" to "control-based safety" - trusting the process rather than the model.

## Relevance

**Critical for AI safety.** Introduces the control paradigm that's now central to AI safety discussions. Foundational for understanding defense-in-depth approaches to AI deployment.
