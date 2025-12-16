# How to evaluate control measures for LLM agents? A trajectory from today to superintelligence

**arXiv:** [2504.05259](https://arxiv.org/abs/2504.05259)
**Authors:** Tomek Korbak, Mikita Balesni, Buck Shlegeris, Geoffrey Irving
**Date:** 2025-04-07
**Organizations:** UK AI Security Institute, Apollo Research, Redwood Research

## Abstract

As LLM agents grow more capable of causing harm autonomously, AI developers will rely on increasingly sophisticated control measures to prevent possibly misaligned agents from causing harm.

AI developers could demonstrate that their control measures are sufficient by running control evaluations: testing exercises in which a red team produces agents that try to subvert control measures.

To ensure control evaluations accurately capture misalignment risks, the affordances granted to this red team should be adapted to the capability profiles of the agents to be deployed under control measures.

In this paper they propose a systematic framework for adapting affordances of red teams to advancing AI capabilities. Rather than assuming that agents will always execute the best attack strategies known to humans, the authors demonstrate how knowledge of an agent's actual capability profile can inform proportional control evaluations, resulting in more practical and cost-effective control measures.

## Claude Summary

This paper provides a roadmap for how to evaluate AI control measures as capabilities increase toward superintelligence. The key insight is that red team affordances should scale with model capabilities rather than always assuming worst-case attack strategies.

**Key contributions:**
- Framework for proportional control evaluations based on capability profiles
- Practical guidance for cost-effective control measures
- Trajectory from current systems to superintelligent ones

**Relevance:** Essential reading for anyone designing or evaluating AI safety measures for agentic systems. Provides concrete methodology for scaling safety evaluations.
