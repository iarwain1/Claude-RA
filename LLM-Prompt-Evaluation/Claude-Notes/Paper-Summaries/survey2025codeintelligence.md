# From Code Foundation Models to Agents and Applications: A Comprehensive Survey and Practical Guide to Code Intelligence

**Authors:** Jian Yang et al. (70+ authors)
**Year:** 2025 (November)
**URL:** https://arxiv.org/abs/2511.18538

## Key Contributions

1. **Comprehensive survey** of code LLMs covering entire model lifecycle
2. **Unified taxonomy** tracing evolution from transformer models to instruction-tuned systems with emergent reasoning
3. **Six-stage evolution framework:** Manual coding → Tool-assisted → Framework-driven → AI-assisted (current) → AI-driven → AI-autonomous
4. **Systematic analysis** of data curation, pretraining, fine-tuning, prompting, and agent development

## Overview

Examines how LLMs have transformed automated software development, driving commercial adoption through tools like GitHub Copilot, Cursor, Trae, and Claude Code. Documents evolution from single-digit to 95%+ success rates on benchmarks like HumanEval.

## Key Findings

### Performance Evolution

| Era | Benchmark Performance |
|-----|----------------------|
| Early code models | Single-digit % on HumanEval |
| Current state-of-art | 95%+ on HumanEval |
| Repository-level | Still challenging (SWE-bench) |

### Advanced Techniques Covered

| Technique | Description |
|-----------|-------------|
| **Chain-of-thought prompting** | Multi-step reasoning for complex problems |
| **Few-shot learning** | Learning from examples in prompt |
| **RAG for code** | Retrieval-augmented generation approaches |
| **Autonomous agents** | Multi-step problem decomposition, planning, tool use |

### Evaluation Landscape

The survey critically evaluates benchmarks and evaluation methodologies:

- **HumanEval:** Function-level, 164 problems, may be saturated
- **SWE-bench:** Repository-level, 2,294 real GitHub issues, more realistic
- **Beyond binary correctness:** Quality, efficiency, maintainability metrics emerging

### Software Engineering Agents

> "The survey addresses how SWE Agents operate across lifecycles in software engineering."

Agent capabilities include:
- Multi-step problem decomposition
- Retrieval-augmented generation
- Tool integration
- Memory mechanisms

### Prompting Paradigms

| Paradigm | Application |
|----------|-------------|
| Instruction tuning | Following natural language commands |
| Chain-of-thought | Step-by-step reasoning |
| Few-shot | Example-based learning |
| RAG | Retrieval-augmented code generation |

## Relevance to Review

**Moderately relevant as supplementary context.** Key insights:

### For Prompt Evaluation

1. **Benchmark evolution matters:** HumanEval saturation suggests need for harder benchmarks
2. **Repository-level evaluation:** SWE-bench-style evals better reflect real-world complexity
3. **Agent evaluation:** Multi-step decomposition requires different evaluation approaches
4. **Beyond correctness:** Quality, efficiency, maintainability as additional metrics

### Mapping to Evaluation Subtopics

| Survey Topic | Evaluation Implication |
|--------------|----------------------|
| Prompting paradigms | Test effectiveness of CoT, few-shot, RAG |
| Agent systems | Two-level evaluation (end-to-end + step) |
| Benchmark evolution | Use repository-level for production relevance |
| Commercial tools | Study Copilot/Cursor/Claude Code patterns |

### Limitations for This Review

- **Code-focused:** May not generalize to non-coding prompts
- **Survey breadth:** Less depth on evaluation specifics
- **Benchmark-centric:** Less focus on production evaluation

## Citations to Follow

- SWE-bench paper and variants (SWE-bench Verified, SWE-bench Pro)
- BigCodeBench as HumanEval successor
- NaturalCodeBench for realistic user prompts
- Specific agent architectures (Devin, SWE-agent)

## Questions/Notes

- **Strength:** Comprehensive coverage of code LLM landscape
- **Strength:** Evolution timeline provides historical context
- **Strength:** Commercial tool analysis (Copilot, Cursor, Claude Code)
- **Gap:** Limited focus on prompt evaluation methodology specifically
- **Gap:** Benchmark limitations acknowledged but alternatives less clear
- **Connects to:** guo2025agentbenchmark (complementary survey), agentic-evaluation subtopic
- **Currency:** November 2025, very current

## Evidence Quality

**High for landscape overview.** 70+ authors, comprehensive coverage. Good for "what techniques exist"; weaker for "how to evaluate prompts" specifically. Survey of field rather than evaluation methodology guide.
