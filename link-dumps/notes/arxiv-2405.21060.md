# Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality

**arXiv:** https://arxiv.org/abs/2405.21060
**Authors:** Tri Dao, Albert Gu
**Date:** 2024-05-31
**Venue:** ICML 2024

## Abstract

While Transformers have been the main architecture behind deep learning's success in language modeling, state-space models (SSMs) such as Mamba have recently been shown to match or outperform Transformers at small to medium scale.

This paper shows that these families of models are actually quite closely related, developing a rich framework of theoretical connections between SSMs and variants of attention.

## Key Contributions

**State Space Duality (SSD) Framework**: Connects SSMs and attention through various decompositions of structured semiseparable matrices.

**Mamba-2 Architecture**: A refinement of Mamba's selective SSM that is:
- 2-8x faster than Mamba-1
- Competitive with Transformers on language modeling
- Larger internal state (16 → 256)
- Simpler code (~30 lines for core layer)

## Technical Details

- Shows masked attention and state-space models can be unified under the SSD framework
- Enables efficient algorithms for both families
- Provides pretrained models: mamba2-130m, mamba2-370m, mamba2-780m, mamba2-2.7b

## Claude Summary

This paper establishes deep theoretical connections between two major architecture families:

**Key insight**: Transformers and SSMs are not fundamentally different - they're related through structured semiseparable matrices. This unification opens new research directions.

**Practical impact**:
- Mamba-2 is significantly faster while maintaining performance
- Simpler implementation reduces engineering complexity
- Larger state enables better long-range dependencies

**Why this matters**:
- Transformers' quadratic complexity in sequence length is a major bottleneck
- SSMs offer linear complexity, but adoption has been slow due to perceived differences
- This work bridges the gap, potentially enabling SSM adoption in more applications

## Relevance

Foundational for understanding alternative architectures to Transformers. Important for anyone working on efficient inference, long-context models, or architecture research. The Mamba line of work represents the most serious alternative to attention-based models.
