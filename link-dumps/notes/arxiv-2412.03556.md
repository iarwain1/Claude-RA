# Best-of-N Jailbreaking

**arXiv:** https://arxiv.org/abs/2412.03556
**Date:** 2024-12

## Abstract

Best-of-N Jailbreaking is a technique for testing the robustness of language model safety measures by generating multiple prompt variations and selecting those most likely to bypass safety filters.

## Key Concept

**The approach:**
- Generate N variations of an adversarial prompt
- Select the best (most effective) variation
- Exploit statistical properties of model responses

**Why it works:**
- Safety measures have variance across similar inputs
- With enough samples, likely to find one that bypasses filters
- No model modification needed, pure black-box attack

## Connection to Inference-Time Compute

Related to findings about inference scaling:
- More compute at inference can improve capabilities
- Similarly, more attempts can find jailbreaks
- The defense must be robust across ALL variations, not just most

## Implications

**For safety evaluation:**
- Single-sample evaluation underestimates vulnerability
- Need to consider multi-attempt adversaries
- Report ASR@N metrics (success rate given N attempts)

**For defense:**
- Must achieve low vulnerability across sample space
- Cannot rely on "usually safe" being good enough
- May need different defense paradigms

## Claude Summary

Best-of-N jailbreaking highlights a fundamental challenge:

**The asymmetry**: Defenders must block ALL attacks; attackers only need ONE success. With multiple attempts, attackers have an advantage.

**Practical implication**: If adversaries can make many queries (which they usually can), safety measures need much higher per-query robustness than often assumed.

**Connection to AI safety**: This is another example of the attacker-defender asymmetry that pervades security. Evaluations must account for adversaries with multiple attempts.

## Relevance

Important for understanding jailbreak attack surfaces. Highlights need for multi-sample evaluation. Relevant for anyone designing or evaluating LLM safety measures.
