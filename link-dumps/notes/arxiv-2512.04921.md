# The AI Consumer Index (ACE)

**arXiv:** https://arxiv.org/abs/2512.04921
**Authors:** Julien Benchek, Rohit Shetty, Benjamin Hunsberger, Ajay Arun, Zach Richards, Brendan Foody, Osvald Nitski, Bertie Vidgen
**Date:** 2025-12-04 (v1), revised 2025-12-09 (v3)

## Abstract

The paper introduces the first version of the AI Consumer Index (ACE), a benchmark for assessing whether frontier AI models can perform everyday consumer tasks. ACE contains a hidden heldout set of 400 test cases, split across four consumer activities: shopping, food, gaming, and DIY. The authors are also open sourcing 80 cases as a devset with a CC-BY license.

For the ACE leaderboard they evaluated 10 frontier models (with websearch turned on) using a novel grading methodology that dynamically checks whether relevant parts of the response are grounded in the retrieved web sources.

Key Results:
- GPT 5 (Thinking = High) is the top-performing model, scoring 56.1%
- o3 Pro (Thinking = On) at 55.2%
- GPT 5.1 (Thinking = High) at 55.1%
- Model scores differ across domains; in Shopping the top model scores under 50%

## Claude Summary

ACE fills an important gap in AI evaluation by focusing on practical consumer tasks rather than abstract reasoning or professional work. The benchmark tests real-world utility: can AI actually help people shop, find recipes, solve DIY problems, or navigate gaming questions?

The low scores (top model at 56.1%) reveal significant gaps between frontier model capabilities and practical consumer utility. The grounding-based evaluation methodology is notable - checking whether responses are actually grounded in retrieved sources rather than hallucinated.

The domain-specific variation (shopping under 50%) suggests uneven capability profiles that matter for deployment decisions.

## Relevance

Relevant for understanding practical AI deployment and capability gaps. Provides a different perspective from academic benchmarks focused on reasoning or professional tasks.
