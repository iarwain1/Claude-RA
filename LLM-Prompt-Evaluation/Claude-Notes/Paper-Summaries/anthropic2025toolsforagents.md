# Writing Tools for Agents

**Authors:** Anthropic Engineering
**Year:** 2025
**URL:** https://www.anthropic.com/engineering/writing-tools-for-agents

## Key Contributions

1. **Evaluation-driven tool development:** Systematic measurement of tool performance
2. **Real-world data emphasis:** Avoid sandbox simplicity; use realistic complexity
3. **Iterative improvement loop:** Evaluate → improve → re-evaluate
4. **Multi-metric evaluation:** Accuracy, runtime, token consumption, tool errors

## Overview

Anthropic's engineering guidance on building effective tools for LLM agents, with emphasis on evaluation methodology. Key thesis: "Agents are only as effective as the tools we give them."

## Key Findings

### Evaluation Approach

**Start with comprehensive evaluation tasks:**
- Grounded in real-world uses
- Require multiple tool calls (potentially dozens)
- Test sufficient complexity

**Metrics to collect:**
- Accuracy (task completion)
- Runtime performance
- Token consumption
- Tool error rates

### Realistic vs. Sandbox Environments

> "Prompts should be inspired by real-world uses and be based on realistic data sources and services (for example, internal knowledge bases and microservices). Avoid overly simplistic or superficial 'sandbox' environments that don't stress-test your tools with sufficient complexity."

**Key insight:** Sandbox environments give false confidence. Tools need to be tested against real-world complexity.

### Iterative Improvement Process

1. **Prototype:** Stand up quick version, test locally
2. **Evaluate:** Run comprehensive evaluation to baseline
3. **Improve:** Work alongside agents to enhance tools
4. **Re-evaluate:** Measure impact of changes
5. **Repeat:** Until strong real-world performance

### Agent Reasoning Analysis

> "Analyze agent reasoning to identify improvement areas."

Don't just measure outcomes—understand *how* the agent is using tools to identify systematic issues.

### Model Context Protocol (MCP) Integration

Tools can be provided via MCP, enabling agents to access potentially hundreds of tools. Evaluation becomes more critical as tool count increases.

## Relevance to Review

**Directly relevant for agentic prompt/tool evaluation.** Key insights:

### Mapping to Two-Level Evaluation

| Anthropic Guidance | husain2025evalsfaq Alignment |
|-------------------|------------------------------|
| Multi-tool task evaluation | End-to-end task success |
| Token consumption, tool errors | Step-level diagnostics |
| Analyze agent reasoning | Process metrics |
| Real-world data sources | Avoid "sandbox" test data |

### Implications for Tool Prompts

1. **Tool descriptions are prompts** that need evaluation
2. **Verifiable responses:** Each evaluation task should have clear success criteria
3. **Complexity matters:** Simple tools may work in sandbox, fail in production
4. **Multiple calls:** Single-tool tests miss coordination issues

### Best Practices Extracted

| Practice | Rationale |
|----------|-----------|
| Use realistic data | Sandbox gives false confidence |
| Multi-call evaluations | Tests tool coordination |
| Collect multiple metrics | Accuracy alone insufficient |
| Analyze reasoning | Understand failure modes |
| Iterate with agents | Agents can help improve tools |

## Citations to Follow

- Model Context Protocol (MCP) documentation
- Anthropic effective context engineering post
- Specific tool optimization case studies

## Questions/Notes

- **Strength:** Practical engineering guidance from production experience
- **Strength:** Emphasis on realistic complexity over sandbox simplicity
- **Strength:** Multi-metric approach beyond just accuracy
- **Practical insight:** "Work alongside agents to improve tools" - agents as collaborators in tool development
- **Gap:** Limited specifics on threshold setting for metrics
- **Gap:** No discussion of human-in-the-loop validation
- **Connects to:** husain2025evalsfaq (agentic evaluation), guo2025agentbenchmark (agent-based solutions)
- **Currency:** 2025, very current

## Evidence Quality

**Medium-high for engineering guidance.** Based on Anthropic's production experience building Claude-based agents. Strong for practical recommendations; limited formal methodology description.
