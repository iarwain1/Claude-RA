# Tree of Thoughts: Deliberate Problem Solving with Large Language Models

**arXiv:** https://arxiv.org/abs/2305.10601
**Authors:** Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran, Thomas L. Griffiths, Yuan Cao, Karthik Narasimhan (Princeton, Google DeepMind)
**Date:** 2023-05
**Venue:** NeurIPS 2023

## Abstract

Tree of Thoughts (ToT) is a framework that generalizes Chain of Thought prompting by enabling language models to explore multiple reasoning paths over coherent units of text ("thoughts") that serve as intermediate steps toward problem solving.

The framework allows LLMs to perform deliberate decision-making by:
- Considering multiple different reasoning paths
- Self-evaluating choices to decide next actions
- Using search algorithms (BFS, DFS) to systematically explore the thought space

## Key Results

Evaluated on tasks requiring non-trivial planning or search:
- Game of 24
- Creative Writing
- Mini Crosswords

Shows significant improvements over standard prompting methods.

## Claude Summary

Tree of Thoughts extends Chain-of-Thought from linear reasoning to tree-structured exploration:

**CoT limitation**: Single reasoning path, no backtracking
**ToT solution**: Explore multiple paths, evaluate, backtrack when needed

**Components**:
1. Thought decomposition (breaking problems into steps)
2. Thought generation (proposing multiple options)
3. State evaluation (assessing progress)
4. Search algorithm (BFS/DFS for exploration)

This enables solving problems that require look-ahead, backtracking, or exploring alternatives - capabilities missing from linear prompting.

## Relevance

Important for LLM reasoning research. Extends prompting paradigm beyond linear chains. Useful for understanding how to elicit more deliberate reasoning from LLMs.
