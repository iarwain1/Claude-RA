# A Sketch of an AI Control Safety Case

**arXiv:** https://arxiv.org/abs/2501.17315
**Authors:** Tomek Korbak, Joshua Clymer, Benjamin Hilton, Buck Shlegeris, Geoffrey Irving (UK AISI, Redwood Research)
**Date:** 2025-01-28
**LessWrong:** https://www.lesswrong.com/posts/vWYzSorAEWwoJnnXq/a-sketch-of-an-ai-control-safety-case

## Abstract

As LLM agents gain capacity to cause harm, developers might rely on control measures (e.g., monitoring) to justify safety. This paper sketches how to construct a **control safety case**: a structured argument that models are incapable of subverting control measures to cause unacceptable outcomes.

## Case Study

**Scenario:** LLM agent deployed internally at AI company
**Concern:** Prevent sensitive information exfiltration
**Approach:** Red team designs models to exfiltrate data in proxy environment

## Safety Case Structure

**Key claims:**
1. Red team adequately elicits model capabilities to exfiltrate data
2. Control measures remain at least as effective in deployment
3. Developers conservatively extrapolate model performance

## Methodology

**Phases:**
1. Red team constructs model substitutes trained to execute attack strategies
2. Blue team constructs inputs (e.g., "honeypots") to evaluate model substitutes
3. Blue team uses model substitutes to complete tasks, aiming to observe malign actions
4. Developer estimates frequency at which red team would succeed in larger deployment

## Claude Summary

This paper operationalizes AI Control into a deployable safety case:

**Why safety cases matter**: Regulators and stakeholders need structured arguments for safety, not just "we ran some evals." Safety cases provide that structure.

**Key contribution**: Concrete sketch of what a control safety case looks like - not just theory but something developers could actually build toward.

**The red team / blue team setup**: Makes the adversarial nature of control evaluations explicit. Safety depends on red team being good enough to find vulnerabilities.

**Connection to broader AI Control work**: Builds on Greenblatt et al. (2024) and related Redwood Research work. Part of maturing AI Control from research concept to deployment practice.

## Relevance

**Essential for AI Control practitioners.** Provides template for constructing safety cases based on control evaluations. From UK AISI and Redwood Research - leading groups in this space.
