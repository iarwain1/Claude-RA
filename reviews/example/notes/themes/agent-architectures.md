# Agent Architectures

## Overview
This subtopic covers the core architectural patterns used in LLM-based agents, including how they perceive, plan, and act in environments.

## Key Architectural Components

### 1. Perception/Input Processing
- How agents receive and process information from the environment
- Includes parsing observations, handling multimodal input

### 2. Memory Systems
- **Short-term memory**: Current context window
- **Long-term memory**: Vector stores, retrieval systems
- **Working memory**: Scratchpad for intermediate reasoning

### 3. Planning
- Task decomposition (breaking complex tasks into steps)
- With feedback: iterative refinement based on results
- Without feedback: generate full plan upfront

### 4. Action/Execution
- Tool use and API calls
- Code generation and execution
- Communication with users or other agents

## Patterns Identified

### ReAct Pattern
Interleave reasoning ("Thought") with actions. Most common pattern.
- Pros: Interpretable, recovers from errors
- Cons: Can be verbose, may overthink

### Plan-then-Execute
Generate full plan first, then execute.
- Pros: More coherent for complex tasks
- Cons: Harder to adapt mid-execution

### Reflexion/Self-Correction
Agent reflects on failures and adjusts approach.
- Pros: Learns from mistakes
- Cons: Requires good self-evaluation

## Open Questions
- What's the optimal memory architecture for different task types?
- How should agents handle uncertainty in their plans?
- Can we combine patterns adaptively?

## Key Papers
- wang2024survey - Comprehensive taxonomy
- yao2023react - Introduced ReAct pattern
