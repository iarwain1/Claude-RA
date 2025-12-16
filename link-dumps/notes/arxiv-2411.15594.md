# A Survey on LLM-as-a-Judge

**arXiv:** https://arxiv.org/abs/2411.15594
**Authors:** Jiawei Gu, Xuhui Jiang, Zhichao Shi, Hexiang Tan, Xuehao Zhai, Chengjin Xu, Wei Li, Yinghan Shen, Shengjie Ma, Honghao Liu, Saizhuo Wang, Kun Zhang, Yuanzhuo Wang, Wen Gao, Lionel Ni, Jian Guo
**Date:** 2024-11-23 (multiple revisions through 2025-10)

## Abstract

Large Language Models (LLMs) have achieved remarkable success across diverse domains, leading to the emergence of "LLM-as-a-Judge," where LLMs are employed as evaluators for complex tasks. With their ability to process diverse data types and provide scalable, cost-effective, and consistent assessments, LLMs present a compelling alternative to traditional expert-driven evaluations.

This paper provides a comprehensive survey of LLM-as-a-Judge, addressing the core question: How can reliable LLM-as-a-Judge systems be built? The authors explore strategies to enhance reliability, including improving consistency, mitigating biases, and adapting to diverse assessment scenarios.

Additionally, the paper proposes methodologies for evaluating the reliability of LLM-as-a-Judge systems, supported by a novel benchmark designed for this purpose. It also discusses practical applications, challenges, and future directions.

## Claude Summary

This comprehensive survey covers the emerging paradigm of using LLMs as evaluators/judges for AI system outputs. Key topics include:

**Reliability Challenges:**
- Consistency across evaluations
- Bias mitigation (position bias, verbosity bias, self-preference)
- Adaptation to different assessment scenarios

**Building Reliable Systems:**
- Prompt engineering for evaluation
- Calibration techniques
- Multi-judge approaches

**Meta-Evaluation:**
- How to evaluate the evaluators
- Benchmark for LLM-as-a-Judge reliability

This is increasingly important as human evaluation becomes prohibitively expensive and LLM judges are used in training (RLHF), evaluation, and deployment.

## Relevance

Essential for AI evaluation methodology. Directly relevant to understanding evaluation validity and the recursive problem of evaluating AI with AI. Important for AI governance discussions about scalable oversight.

## Resources

- GitHub: https://github.com/IDEA-FinAI/LLM-as-Evaluator
