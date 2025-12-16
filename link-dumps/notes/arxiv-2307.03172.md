# Lost in the Middle: How Language Models Use Long Contexts

**arXiv:** https://arxiv.org/abs/2307.03172
**Authors:** Nelson F. Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, Percy Liang
**Date:** 2023-07-06 (v1), revised 2023-11-20 (v3)

## Abstract

While recent language models have the ability to take long contexts as input, relatively little is known about how well they use longer context. The authors analyze the performance of language models on two tasks that require identifying relevant information in their input contexts: multi-document question answering and key-value retrieval.

They find that performance can degrade significantly when changing the position of relevant information, indicating that current language models do not robustly make use of information in long input contexts.

In particular, they observe that performance is often highest when relevant information occurs at the beginning or end of the input context, and significantly degrades when models must access relevant information in the middle of long contexts, even for explicitly long-context models.

## Claude Summary

"Lost in the Middle" is a highly influential paper revealing a critical limitation of long-context LLMs:

**The U-shaped curve**: Models perform best when relevant information is at the beginning or end of context, worst in the middle.

**Implications**:
- Long context windows don't guarantee effective use of context
- Position of information matters more than expected
- Affects RAG systems, multi-document QA, agents with long histories

**Practical consequences**:
- Document ordering strategies matter
- May need redundancy or repositioning of key information
- Implications for prompt engineering

This finding has influenced how practitioners design prompts and RAG systems.

## Relevance

Essential for understanding LLM limitations. Directly relevant to agent design (long action histories), RAG systems, and prompt engineering best practices.
