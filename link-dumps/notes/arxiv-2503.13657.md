# Why Do Multi-Agent LLM Systems Fail?

**arXiv:** https://arxiv.org/abs/2503.13657
**Authors:** Mert Cemri, Melissa Z. Pan, Shuyi Yang, et al. (Berkeley, Stanford)
**Date:** 2025-03-17 (v1), revised 2025-10-26 (v3)
**GitHub:** https://github.com/multi-agent-systems-failure-taxonomy/MAST

## Abstract

Despite enthusiasm for Multi-Agent LLM Systems (MAS), performance gains on benchmarks are often minimal. This gap highlights a critical need to understand **why MAS fail**.

## MAST-Data

**Comprehensive dataset:**
- 1600+ annotated traces
- 7 popular MAS frameworks
- First multi-agent dataset to outline failure dynamics

## MAST Taxonomy

**First Multi-Agent System Failure Taxonomy:**
- 14 unique failure modes
- Developed through rigorous analysis of 150 traces
- High inter-annotator agreement (kappa = 0.88)

## Three Failure Categories

**1. Specification and System Design (44.2%)**
- Largest category
- Issues in how systems are designed

**2. Inter-Agent Misalignment (32.3%)**
- Agents don't coordinate properly
- Communication failures

**3. Task Verification and Termination (23.5%)**
- Agents don't know when they're done
- Verification failures

## Key Findings

**System design is the biggest problem:**
- Nearly half of failures are design issues
- Multi-agent adds complexity without proportional benefit

**Implications for practitioners:**
- Focus on system design before adding agents
- Simple systems may outperform complex MAS

## Claude Summary

This paper provides much-needed empirical grounding for multi-agent hype:

**The core finding**: MAS often fail, and the failures are systematic and classifiable. This is actionable for improvement.

**Why system design dominates**: The 44% figure suggests many MAS problems could be solved before involving multiple agents. The architecture matters more than having more agents.

**Practical value**: If you're building MAS, this taxonomy tells you what to watch for. Can inform debugging and design.

**For the field**: Helps move from "MAS are cool" to "here's how to make MAS actually work."

## Relevance

Important for anyone building or evaluating multi-agent systems. Provides systematic failure taxonomy. Helps explain why MAS underperform expectations.
