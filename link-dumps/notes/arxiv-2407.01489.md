# Agentless: Demystifying LLM-based Software Engineering Agents

**arXiv:** https://arxiv.org/abs/2407.01489
**Authors:** Chunqiu Steven Xia, Yinlin Deng, Soren Dunn, Lingming Zhang
**Date:** 2024-07-01 (v1), revised 2024-10-29 (v2)
**GitHub:** https://github.com/OpenAutoCoder/Agentless

## Abstract

Recent advancements in LLMs have significantly advanced automation of software development tasks. Researchers have developed autonomous LLM agents with tools, command execution, environment feedback, and planning.

**Key Question**: Do we really have to employ complex autonomous software agents?

## The Agentless Approach

Instead of complex agent-based approaches, Agentless employs a simplistic three-phase process:
1. **Localization**: Find the buggy parts of the program
2. **Repair**: Fix the faulty code
3. **Patch Validation**: Verify the solution

Uses combination of prompting-based and embedding-based retrieval methods.

## Key Findings

**Simplicity wins:**
- Two-phase, cost-efficient method
- Uses hierarchical localization and diff-based repair
- Outperforms agent-based systems

**Problems with complex agents:**
- Costly
- Difficult to control
- Prone to errors
- Stem from limitations of current AI models

## Claude Summary

Agentless provides an important counterpoint to the "more agentic is better" trend:

**Core insight**: Complex agent architectures may be premature given current LLM limitations. Simpler, more controlled approaches can outperform while being more reliable and cheaper.

**Why this matters**:
- Agent complexity introduces failure modes
- Simpler systems are easier to debug and improve
- Cost and reliability matter for production use

**Implications for agent design**:
- Don't add complexity unless it demonstrably helps
- Consider non-agentic baselines before going agentic
- Control and predictability have value

## Relevance

Important for anyone building LLM-powered software engineering tools. Provides empirical evidence that simpler approaches can win. Useful baseline for evaluating whether agent complexity is warranted.
