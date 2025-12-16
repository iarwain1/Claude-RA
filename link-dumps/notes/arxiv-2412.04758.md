# Measuring Goal-Directedness

**arXiv:** https://arxiv.org/abs/2412.04758
**Authors:** Matt MacDermott, James Fox, Francesco Belardinelli, Tom Everitt
**Date:** 2024-12-06
**Venue:** NeurIPS 2024

## Abstract

The paper defines **Maximum Entropy Goal-directedness (MEG)**, a formal measure of goal-directedness in causal models and Markov decision processes, with algorithms for computing it.

## Why This Matters

**For AI safety:**
- Goal-directedness is central to many AI harm concerns
- Highly goal-directed agents may be more dangerous
- Need to measure it before we can reason about it

**For philosophy:**
- Goal-directedness is a key aspect of agency
- Dennett's idea: behavior is goal-directed if it's the rational choice for achieving goals

## Technical Approach

**Based on maximum causal entropy framework:**
- Adapted from inverse reinforcement learning
- Uses causal models (general enough for most ML frameworks)
- Behavior model derived from maximum entropy principle

**Three measurement modes:**
1. With respect to a known utility function
2. With respect to a hypothesis class of utility functions
3. With respect to a set of random variables

## Key Features

**Generality:**
- Works for single-decision tasks (prediction, classification, regression)
- Works for multi-decision MDPs
- Framework-agnostic

**Scalability potential:**
- Algorithms can use differentiable utility function classes
- May scale using deep neural networks

## Validation

MEG satisfies several formal desiderata. Demonstrated with small-scale experiments.

## Claude Summary

This paper provides rigorous foundations for measuring goal-directedness:

**The key question**: Is a system "trying" to achieve something, or just pattern-matching? MEG provides a formal answer based on how well behavior matches optimal goal-pursuit.

**Why maximum entropy?**: Among all behaviors consistent with outcomes, the least-assuming distribution helps identify how much behavior can be explained by goal-pursuit vs. other factors.

**Connection to AI safety**: If we can measure goal-directedness, we might:
- Identify when systems are becoming more agentic
- Distinguish tool-like from agent-like AI
- Detect emergence of concerning optimization behavior

**Limitations**: Small-scale experiments; scaling to large models is future work.

## Relevance

Important theoretical contribution to AI safety. Provides formal measure for a concept often discussed informally. From Everitt's group, which has done significant work on agent foundations. Published at NeurIPS 2024.
