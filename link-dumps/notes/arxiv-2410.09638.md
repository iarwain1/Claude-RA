# On Goodhart's Law, with an Application to Value Alignment

**arXiv:** https://arxiv.org/abs/2410.09638
**Authors:** El-Mahdi El-Mhamdi, Lê-Nguyên Hoang
**Date:** 2024-10-12

## Abstract

This paper investigates Goodhart's law formally, proving it critically depends on the tail distribution of the discrepancy between the true goal and the optimized measure.

## Key Distinctions

**Weak Goodhart's law:**
- Over-optimizing the metric is *useless* for the true goal
- Correlation goes to zero
- Still not actively harmful

**Strong Goodhart's law:**
- Over-optimizing the metric is *harmful* for the true goal
- Negative correlation emerges
- Active counter-production

## Technical Results

**Normal distributions → Weak Goodhart:**
- Correlation goes to zero extremely slowly
- Over-optimization is wasteful but not harmful

**Subexponential/power law distributions → Strong Goodhart:**
- If discrepancy has thicker power law than goal
- Negative correlation emerges
- Optimization becomes counter-productive

## Key Finding

Discrepancies with **long-tail distributions** favor strong Goodhart's law.

## Implications

**For algorithms in complex environments:**
- Strong Goodhart may apply to any algorithm (even without ML)
- Environments modified by the algorithm create dynamics
- Testing on fixed datasets misses these effects

**User-algorithm simulation:**
- Recommendations affect user preferences
- Nonlinear dynamics expose algorithms to strong Goodhart
- Lab performance ≠ deployment performance

## Claude Summary

This paper puts mathematical foundations under Goodhart's law:

**Why formalization matters**: "When a measure becomes a target, it ceases to be a good measure" is folklore. This paper shows exactly when and why it happens.

**Key insight**: The shape of the distribution matters. Normal discrepancies → weak Goodhart (wasteful). Long-tailed discrepancies → strong Goodhart (harmful).

**For AI alignment**: Value alignment involves optimizing proxies for human values. If the proxy-value discrepancy has long tails (plausible for complex values), strong Goodhart is a real risk.

**Practical implication**: Testing on fixed datasets can't detect strong Goodhart. Need to account for how the system changes its environment.

## Relevance

Foundational for understanding optimization failures in AI. Mathematical precision on a concept often invoked informally. Important for value alignment research and reward modeling.
