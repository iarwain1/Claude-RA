# Benchmarks as Microscopes: A Call for Model Metrology

**arXiv:** https://arxiv.org/abs/2407.16711
**Authors:** Michael Saxon, Ari Holtzman, Peter West, William Yang Wang, Naomi Saphra
**Date:** 2024-07-22 (v1), revised 2024-07-30 (v2)
**Venue:** COLM 2024

## Abstract

Modern language models pose new challenges in capability assessment. Static benchmarks inevitably saturate without providing confidence in deployment tolerances. Yet developers claim generalized traits (reasoning, understanding) based on flawed metrics.

**Thesis**: We need a new discipline of **model metrology** - one focused on generating benchmarks that predict performance under deployment.

## Historical Analogy

Galileo built one of the first optical telescopes in 1609. Turned around, it became a microscope. For centuries, the same scientists built and used these tools for discoveries.

Similarly, model metrology requires:
- Building benchmarks as scientific instruments
- Using them to make rigorous discoveries about models
- Continuous refinement of measurement approaches

## Problems with Current Benchmarks

- Not scalable (saturate quickly)
- Not relevant (don't predict deployment performance)
- Not durable (quickly gamed or outdated)
- Engineering and policy decisions rest on unreliable metrics
- Even experts disagree about actual capabilities

## Vision for Model Metrology

Model metrologists would:
- Bridge scientists, practitioners, and users
- Build benchmarks meeting rigorous desiderata
- Share techniques, tooling, and theory
- Enable critique and auditing of others' work

## Claude Summary

This paper articulates what's wrong with how we measure LLMs:

**Core problem**: We use benchmarks as if they're measuring general capabilities, but they're not. A model beating MMLU doesn't mean it can "reason" - it means it can do MMLU.

**The metrology solution**: Treat benchmarking as a science, not a leaderboard sport. Focus on what benchmarks actually measure and whether that predicts real-world use.

**Why this matters**: Bad metrics lead to bad decisions. If benchmarks don't predict deployment, companies and regulators are flying blind.

**Call to action**: Build a discipline around measurement, not just capability claims.

## Relevance

Essential reading for anyone working with LLM benchmarks. Articulates fundamental problems with current evaluation practices. Provides framework for thinking about what good benchmarks should do.
