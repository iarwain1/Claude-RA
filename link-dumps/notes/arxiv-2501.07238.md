# Lessons From Red Teaming 100 Generative AI Products

**arXiv:** https://arxiv.org/abs/2501.07238
**Authors:** Blake Bullwinkel et al. (26 authors, Microsoft AI Red Team)
**Date:** 2025-01

## Abstract

Based on Microsoft's experience red teaming over 100 generative AI products, this paper presents their internal threat model ontology and eight main lessons learned.

## The Eight Lessons

1. **Understand what the system can do and where it is applied**
2. **You don't have to compute gradients to break an AI system**
3. **AI red teaming is not safety benchmarking**
4. **Automation can help cover more of the risk landscape**
5. **The human element of AI red teaming is crucial**
6. **Responsible AI harms are pervasive but difficult to measure**
7. **LLMs amplify existing security risks and introduce new ones**
8. **The work of securing AI systems will never be complete**

## Background

**Microsoft AI Red Team (AIRT):**
- Established 2018
- Initially focused on traditional security vulnerabilities and evasion attacks
- Expanded scope as AI systems gained new capabilities
- Developed PyRIT framework for automated testing

## Key Insights

**Red teaming ≠ Benchmarking:**
- Benchmarks measure known risks
- Red teaming discovers unknown risks
- Both are necessary but serve different purposes

**Human + Automation:**
- Automation scales coverage
- Humans find novel attack vectors
- Combined approach is most effective

## Claude Summary

This paper distills hard-won operational experience:

**Why 100 products matters**: Not theoretical - based on actually securing deployed systems. The lessons reflect real-world constraints.

**Key takeaways for practitioners**:
- Context matters: understand the specific application
- Black-box attacks work: don't assume gradient access is needed
- Continuous process: security is never "done"

**For the field**: Establishes that AI red teaming is a distinct discipline from benchmarking, requiring different skills and processes.

## Relevance

**Essential reading for AI security practitioners.** From the team that literally wrote the book (and framework - PyRIT) on AI red teaming. Provides operational wisdom not found in academic papers.
