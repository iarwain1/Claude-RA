# A Comprehensive Survey on Benchmarks and Solutions in Software Engineering of LLM-Empowered Agentic System

**Authors:** Jiale Guo, Suizhi Huang, Mei Li, Dong Huang, Xingsheng Chen, Regina Zhang, Zhijiang Guo, Han Yu, Siu-Ming Yiu, Pietro Lio, Kwok-Yan Lam
**Year:** 2025 (October)
**URL:** https://arxiv.org/abs/2510.09721

## Key Contributions

1. **First holistic analysis** bridging evaluation methodologies and solution approaches for LLM-powered SE
2. **Two-dimensional taxonomy:** Solutions (prompt-based, fine-tuning, agent-based) × Benchmarks (generation, translation, repair)
3. **150+ papers reviewed** with 50+ benchmarks mapped to solution strategies
4. **Evolution analysis:** From simple prompt engineering to sophisticated agentic systems with planning, reasoning, memory, and tools

## Methodology

Systematic literature review from top-tier venues (NeurIPS, ICML, ICLR, ACL, EMNLP, ICSE, FSE, ASE) plus journals (TSE, TOSEM) and preprints. GitHub repository maintained with continuous updates.

## Key Findings

### Solution Taxonomy

| Paradigm | Description | Characteristics |
|----------|-------------|-----------------|
| **Prompt-based** | In-context learning, few-shot, chain-of-thought | No model changes, rapid iteration |
| **Fine-tuning-based** | Parameter updates on domain data | Requires compute, data curation |
| **Agent-based** | Planning, reasoning, memory, tool use | Autonomous, complex workflows |

### Benchmark Taxonomy

| Task Type | Key Benchmarks | Metrics |
|-----------|----------------|---------|
| **Code Generation** | HumanEval (164 problems), MBPP, CodeXGLUE | Pass@k |
| **Program Repair** | SWE-bench (2,294 GitHub issues), HumanEvalFix, QuixBugs, BugsInPy | Patch correctness |
| **Code Translation** | CodeXGLUE (14 tasks) | Functional equivalence |

### Benchmark Evolution

**Early benchmarks (HumanEval, MBPP):**
- Function-level tasks
- Pass@k metric (correct solution in top-k outputs)
- Synthetic problems

**Modern benchmarks (SWE-bench, LiveCodeBench):**
- Repository-level, real GitHub issues
- Production code changes
- Assess maintainability, system integration, documentation
- "State-of-the-art models continue to struggle with real engineering tasks"

### HumanEval Details

- 164 Python problems, 9.6 test cases average
- HumanEval+ extends to 764.1 test cases average (better edge case coverage)

### SWE-bench Details

- 2,294 real GitHub issues across 12 Python repos
- Task: Given codebase + issue description → generate patch
- Variants: SWE-bench Lite, Verified, Java

### Agent Capabilities Evolution

Simple prompt engineering → Sophisticated agentic systems with:
- **Planning** - Multi-step task decomposition
- **Reasoning** - Chain-of-thought, self-reflection
- **Memory** - Context retention across steps
- **Tool augmentation** - External tool invocation

### Future Directions Identified

1. Multi-agent collaboration frameworks
2. Self-evolving code generation systems
3. Integration of formal verification with LLM methods

## Relevance to Review

**Directly relevant for understanding benchmark landscape.** Key insights for prompt evaluation:

1. **Three solution paradigms** map to different evaluation needs:
   - Prompt-based: Evaluate prompt design directly
   - Agent-based: Two-level evaluation (end-to-end + step-level) aligns with husain2025evalsfaq

2. **Benchmark evolution** shows shift from synthetic to real-world tasks - implications for prompt evaluation validity

3. **Pass@k metric** is standard for generation tasks - measures whether *any* of k attempts succeeds

4. **Gap between benchmarks and production:** Even good benchmark scores don't predict real-world success

### Mapping to Prompt Types

| Prompt Type | Relevant Benchmarks | Evaluation Approach |
|-------------|---------------------|---------------------|
| Code generation prompts | HumanEval, MBPP | Pass@k |
| Agentic/tool prompts | SWE-bench | End-to-end + step diagnostics |
| System prompts | Repository-level benchmarks | Multi-step workflow evaluation |

## Citations to Follow

- **SWE-bench paper** - Detailed methodology for repository-level evaluation
- **LiveCodeBench** - Dynamic benchmark with production code changes
- **HumanEval+** - Extended test cases for better coverage
- GitHub repository maintained by authors (continuously updated)

## Questions/Notes

- **Strength:** Comprehensive taxonomy connecting solutions to benchmarks
- **Strength:** Clear evolution narrative from prompts → agents
- **Practical insight:** 50+ benchmarks mapped to solutions helps choose evaluation approach
- **Limitation:** Focused on code/SE domain - may not generalize to other prompt types
- **Gap:** Limited discussion of how to evaluate prompt *design* vs. model *capability*
- **Currency:** October 2025, very current
- **Connects to:** husain2025evalsfaq (two-level agentic evaluation aligns with agent-based paradigm)

## Evidence Quality

**High for taxonomy and benchmark coverage.** Systematic literature review methodology. Strong for "what benchmarks exist" and "what solutions have been tried." Cannot directly cite for prompt evaluation methodology (that's not the focus).
