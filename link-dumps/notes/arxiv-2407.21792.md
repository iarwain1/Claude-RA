# Safetywashing: Do AI Safety Benchmarks Actually Measure Safety Progress?

**arXiv:** https://arxiv.org/abs/2407.21792
**Authors:** Richard Ren, Steven Basart, Adam Khoja, Alice Gatti, Long Phan, Xuwang Yin, Mantas Mazeika, Alexander Pan, Gabriel Mukobi, Ryan H. Kim, Stephen Fitz, Dan Hendrycks (CAIS)
**Date:** 2024-07-31 (v1), revised 2024-12-27 (v3)
**GitHub:** https://github.com/centerforaisafety/safetywashing

## Abstract

As AI systems grow more powerful, there has been increasing interest in "AI safety" research. However, the field remains poorly defined and inconsistently measured, leading to confusion about how researchers can contribute.

This paper conducts a comprehensive meta-analysis of AI safety benchmarks, analyzing their correlation with general capabilities across dozens of models.

## Key Problem: Safetywashing

Many safety benchmarks highly correlate with:
- Upstream model capabilities
- Training compute

This enables **safetywashing** - where capability improvements are misrepresented as safety advancements.

## Key Findings

**High correlation benchmarks:**
- ETHICS: High capabilities and compute correlation
- Many "safety" benchmarks improve just by training larger models

**Low correlation benchmarks:**
- MACHIAVELLI: Low capabilities/compute correlation
- These may measure genuinely distinct properties

**Distinction between knowledge vs. propensity:**
- ETHICS: Tests ability to *recognize* moral considerations
- MACHIAVELLI/Sycophancy: Tests behavioral *propensities*
- Knowledge benchmarks correlate with capabilities; propensities may not

**Counterexample - Sycophancy:**
- Gets *worse* with increased capabilities and compute
- Demonstrates that more capable ≠ more aligned

## Claude Summary

This paper provides crucial empirical clarity to AI safety research:

**Core insight**: If a "safety" benchmark improves just by scaling, it may not be measuring safety at all - just general capabilities. This makes it easy to claim safety progress without actually making models safer.

**Implications**:
- Need to be skeptical of safety claims backed only by capability-correlated benchmarks
- Propensity-based measures may be more valuable for safety
- Some problems (like sycophancy) get worse with scale

**Methodological contribution**: Framework for evaluating whether safety research is genuinely distinct from capabilities research.

## Relevance

**Critical for AI safety field definition.** Helps distinguish genuine safety research from capability research with safety branding. From CAIS (Center for AI Safety), a leading AI safety research organization.
