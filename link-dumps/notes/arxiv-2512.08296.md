# Towards a Science of Scaling Agent Systems

**arXiv:** [2512.08296](https://arxiv.org/abs/2512.08296)
**Authors:** Yubin Kim, Ken Gu, Chanwoo Park, Chunjong Park, Samuel Schmidgall, A. Ali Heydari, Yao Yan, Zhihan Zhang, Yuchen Zhuang, Mark Malhotra, Paul Pu Liang, Hae Won Park, Yuzhe Yang, Xuhai Xu, Yilun Du, Shwetak Patel, Tim Althoff, Daniel McDuff, Xin Liu
**Date:** 2025-12-09 (revised 2025-12-17)
**Categories:** cs.AI, cs.MA

## Abstract

This research establishes quantitative scaling principles for language model-based agent systems. The team evaluated five agent architectures—including single-agent and four multi-agent variants—across multiple benchmarks and LLM families, conducting "a controlled evaluation spanning 180 configurations." They developed a predictive model using coordination metrics that achieved strong cross-validation performance.

## Key Findings

### Three Critical Effects

1. **Tool Usage vs. Multi-Agent Overhead Trade-off** - Under fixed budgets, there's a tension between tool usage and coordination overhead

2. **Diminishing Returns from Coordination** - Once single-agent performance reaches ~45%, coordination benefits plateau

3. **Topology-Dependent Error Propagation** - Error rates vary significantly based on coordination structure

### Performance Results

- **Centralized coordination:** 80.8% improvement on parallelizable tasks
- **Sequential reasoning tasks:** Performance degraded across all multi-agent variants
- **Predictive framework:** Successfully predicts optimal coordination strategies for most configurations

## Implications

Provides actionable guidance for scaling language model agents in real-world applications. Validates key principles on frontier models. Demonstrates that coordination architecture must match task characteristics.

## Relevance

**Critical for multi-agent systems research.** First systematic study of scaling laws for LLM agent coordination. Provides empirical foundation for architectural decisions in agent system design.

---
*Metadata fetched via WebFetch on 2025-12-31*
