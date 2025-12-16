# The Semantic Hub Hypothesis: Language Models Share Semantic Representations Across Languages and Modalities

**arXiv:** https://arxiv.org/abs/2411.04986
**Date:** 2024-11
**Venue:** ICLR 2025

## Abstract

Modern language models can process inputs across diverse languages and modalities. We hypothesize that models acquire this capability through learning a shared representation space across heterogeneous data types (e.g., different languages and modalities), which places semantically similar inputs near one another, even if they are from different modalities/languages.

The authors term this "the semantic hub hypothesis," following the hub-and-spoke model from neuroscience (Patterson et al., 2007), which posits that semantic knowledge in the human brain is organized through a transmodal semantic "hub" that integrates information from various modality-specific "spokes" regions.

The paper shows that model representations for semantically equivalent inputs in different languages are similar in the intermediate layers, and that this space can be interpreted using the model's dominant pretraining language via the logit lens.

## Claude Summary

This paper proposes a neuroscience-inspired theory for how multimodal/multilingual models work internally. The "semantic hub" hypothesis suggests that:

1. Models develop a shared, language-agnostic semantic space in middle layers
2. This hub integrates information from modality/language-specific "spokes"
3. The hub can be interpreted via the dominant training language

This has important implications for:
- Interpretability research (where to look for semantic representations)
- Understanding transfer learning across languages
- Cross-modal alignment

Drawing on the hub-and-spoke model from cognitive neuroscience adds theoretical grounding.

## Relevance

Relevant for AI interpretability and understanding how models process multilingual/multimodal inputs. Useful for interpretability research aiming to understand model internals.
