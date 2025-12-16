# AgentDojo: A Dynamic Environment to Evaluate Attacks and Defenses for LLM Agents

**arXiv:** https://arxiv.org/abs/2406.13352
**Authors:** Edoardo Debenedetti, Jie Zhang, Mislav Balunović, Luca Beurer-Kellner, Marc Fischer, Florian Tramèr (ETH Zürich)
**Date:** 2024-06
**GitHub:** https://github.com/ethz-spylab/agentdojo

## Abstract

AgentDojo is a dynamic evaluation framework for testing security of LLM-based agents, with particular focus on prompt injection attacks.

## Key Features

**Benchmark Design:**
- Dynamic environment where agents complete realistic tasks
- Agents interact with tools and external data
- Tests resilience to adversarial content injection

**Attack Focus:**
- Prompt injection through data the agent processes
- Malicious content in emails, documents, web pages
- Indirect attacks through tool outputs

**Evaluation Dimensions:**
- Task completion (utility)
- Security against attacks
- Trade-off between security and utility

## Agent Tasks

Multiple domains where agents must:
- Use tools appropriately
- Process external data
- Complete user objectives
- Resist manipulation attempts

## Claude Summary

AgentDojo addresses a critical gap in LLM agent security research:

**Why this matters**:
- LLM agents are increasingly deployed with tool access
- Prompt injection through data is a major vulnerability
- Existing benchmarks don't capture this dynamic threat

**Key insight**: Security and utility are often in tension. Agents that are more cautious may be safer but less useful. This benchmark enables systematic exploration of this trade-off.

**Practical applications**:
- Evaluate agent architectures for security
- Test prompt injection defenses
- Compare attack strategies
- Guide deployment decisions

**Limitations to consider**: Synthetic benchmarks may not capture all real-world attack scenarios, but provide necessary controlled evaluation.

## Relevance

Essential for LLM agent security research. As agents gain more capabilities and tool access, security becomes increasingly critical. Provides systematic evaluation where ad-hoc testing is insufficient.
