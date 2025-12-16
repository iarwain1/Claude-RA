# HuggingGPT: Solving AI Tasks with ChatGPT and its Friends in Hugging Face

**arXiv:** https://arxiv.org/abs/2303.17580
**Authors:** Yongliang Shen, Kaitao Song, Xu Tan, Dongsheng Li, Weiming Lu, Yueting Zhuang (Microsoft, Zhejiang University)
**Date:** 2023-03-30 (v1), revised 2023-12-03 (v4)

## Abstract

Solving complicated AI tasks with different domains and modalities is a key step toward artificial general intelligence. While there are numerous AI models available for various domains and modalities, they cannot handle complicated AI tasks autonomously.

Considering large language models (LLMs) have exhibited exceptional abilities in language understanding, generation, interaction, and reasoning, the authors advocate that LLMs could act as a controller to manage existing AI models to solve complicated AI tasks, with language serving as a generic interface.

## Four-Stage Workflow

1. **Task Planning**: LLM parses user request into task list and determines execution order
2. **Model Selection**: LLM assigns appropriate models to tasks based on Hugging Face model descriptions
3. **Task Execution**: Expert models execute assigned tasks
4. **Response Generation**: LLM integrates inference results and generates summary

## Claude Summary

HuggingGPT (also known as JARVIS) introduced the "LLM as controller" paradigm:

**Key concept**: Use an LLM to orchestrate many specialized AI models (vision, audio, etc.) through Hugging Face's model hub.

**Architecture pattern**:
- LLM acts as planner/coordinator (brain)
- Specialized models act as tools (capabilities)
- Language serves as universal interface

This demonstrated that LLMs could serve as general-purpose AI orchestrators, composing capabilities from multiple models to solve complex multi-modal tasks.

**Influence**: Inspired many subsequent multi-agent and tool-orchestration systems.

## Relevance

Important for multi-modal agent design. Demonstrates LLM-as-controller pattern for orchestrating specialized models. Influential in agent architecture development.

## Resources

- GitHub: https://github.com/AI-Chef/HuggingGPT
