# OpenAI Evals Framework

**Authors:** OpenAI
**Year:** 2023-2025
**URL:** https://github.com/openai/evals

## Key Contributions

1. **Open-source eval framework** for LLMs and LLM systems
2. **Registry of benchmarks** for testing model capabilities
3. **Multiple eval templates:** Basic, model-graded, custom
4. **No-code eval creation** via YAML configuration

## Overview

OpenAI Evals is a framework for evaluating LLMs with an open-source registry of benchmarks. Designed to enable both standardized benchmarking and custom use-case-specific evaluation.

## Architecture

### Eval Types

| Type | Use Case | Implementation |
|------|----------|----------------|
| **Basic evals** | Exact/fuzzy string matching | JSON data + YAML config |
| **Model-graded evals** | Open-ended responses | LLM judges LLM outputs |
| **Custom evals** | Domain-specific metrics | Python code (limited acceptance) |

### Model-Graded Evaluation

> "In cases where the desired model response can contain significant variation, such as answering an open-ended question, using the model to grade itself is a viable strategy for automated evaluation."

**Process:**
1. Get model completion to original prompt
2. Wrap completion in evaluation prompt
3. Get model completion to evaluation prompt (grade)

**Key design decision:** Evaluation model and evaluated model don't have to be the same.

### Pre-built Model-Graded Templates

- **fact** - Factual accuracy checking
- **closedqa** - Question answering evaluation
- **battle** - Comparative evaluation between responses

### Custom Model-Graded YAML

For use cases beyond pre-built templates:
- Create new YAML files in `evals/registry/modelgraded`
- Specify custom evaluation prompts
- Define grading criteria

### Building Evals Without Code

Following templates requires:
1. Data in JSON format
2. Eval parameters in YAML
3. No Python code needed

### OpenAI Evals API (2025)

Newer API supports:
- **Pass/Fail Grader:** LLM-based answer matching
- **Python Grader:** Programmatic behavior checking
- Combined graders for robust evaluation

## Relevance to Review

**Foundational reference for LLM evaluation infrastructure.** Key insights:

### Alignment with Best Practices

| OpenAI Evals | Husain Guidance | Assessment |
|--------------|-----------------|------------|
| Model-graded evals | LLM-as-judge | **Aligned** - but Husain emphasizes human validation |
| JSON/YAML config | Low-code iteration | **Aligned** - enables domain expert involvement |
| Multiple grader types | Objective + subjective split | **Aligned** |
| Open-source registry | Standardized benchmarks | Useful for comparison |

### Gaps vs. Recommended Practice

1. **No TPR/TNR validation:** Framework doesn't enforce human agreement measurement
2. **No criteria drift tracking:** Missing workflow for evolving criteria
3. **Benchmark focus:** More suited to standardized testing than production monitoring
4. **Limited agentic support:** Primary focus on single-turn evaluation

### Framework Comparison

| Feature | OpenAI Evals | Husain Recommendations |
|---------|--------------|----------------------|
| Judge validation | Optional | **Required** (100+ labels) |
| Grading scale | Configurable | Binary preferred |
| Error analysis | Not built-in | Foundation of process |
| Iteration workflow | Manual | Structured cadence |

### Practical Use Cases

1. **Baseline benchmarking** - Compare model versions
2. **Regression testing** - Detect capability changes
3. **Custom domain evals** - Task-specific evaluation
4. **Comparative evaluation** - A/B testing prompts

## Citations to Follow

- OpenAI Cookbook evaluation examples
- simple-evals repository (reference implementations)
- MCP evaluation notebook

## Questions/Notes

- **Strength:** Open-source, widely adopted
- **Strength:** Low-code eval creation lowers barrier
- **Strength:** Model-graded templates for common patterns
- **Limitation:** simple-evals no longer updated (as of July 2025)
- **Limitation:** Not accepting custom code submissions
- **Gap:** Limited production monitoring focus
- **Gap:** No built-in human validation workflow
- **Connects to:** husain2024llmjudge (model-graded methodology), automated-metrics subtopic
- **Currency:** Actively maintained, though simple-evals deprecated

## Evidence Quality

**High for framework documentation.** Well-documented, widely used open-source tool. Strong for understanding available infrastructure; weaker for best practice guidance (framework is neutral on methodology).
