# Toolformer: Language Models Can Teach Themselves to Use Tools

**arXiv:** https://arxiv.org/abs/2302.04761
**Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom (Meta AI)
**Date:** 2023-02-09
**Venue:** NeurIPS 2023

## Abstract

Language models (LMs) exhibit remarkable abilities to solve new tasks from just a few examples or textual instructions, especially at scale. They also, paradoxically, struggle with basic functionality, such as arithmetic or factual lookup, where much simpler and smaller models excel.

This paper shows that LMs can teach themselves to use external tools via simple APIs and achieve the best of both worlds. Toolformer is a model trained to decide:
- Which APIs to call
- When to call them
- What arguments to pass
- How to incorporate results into future token prediction

This is done in a self-supervised way, requiring nothing more than a handful of demonstrations for each API.

## Tools Incorporated

- Calculator
- Q&A system
- Two search engines
- Translation system
- Calendar

## Key Results

Toolformer (based on 6.7B GPT-J) achieves substantially improved zero-shot performance, often competitive with much larger models like GPT-3, without sacrificing core language modeling abilities.

## Claude Summary

Toolformer is a landmark paper demonstrating that LLMs can learn to use tools through self-supervision rather than explicit training:

**Key insight**: Models can be trained to insert API calls into their outputs, learning when tools help and when they don't.

**Self-supervised approach**: Generate API call candidates → Filter by whether they improve predictions → Fine-tune on successful examples

This approach influenced subsequent work on tool-augmented LLMs and established that tool use can emerge from language modeling.

## Relevance

Foundational for tool-augmented LLMs. Demonstrates self-supervised tool learning approach. Important precursor to modern function-calling capabilities.
