# Language Models (Mostly) Know What They Know

**URL:** https://www.anthropic.com/news/language-models-mostly-know-what-they-know
**Date:** July 11, 2022
**Type:** Research Announcement

## Abstract

This research demonstrates that larger language models exhibit strong calibration on diverse multiple-choice and true/false questions when presented appropriately. The study introduces methodology where models first generate answers, then evaluate the probability "P(True)" that their responses are correct.

## Key Findings

### Model Calibration (P(True))
The team showed encouraging performance, calibration, and scaling for P(True) on a diverse array of tasks. Models can assess the probability that their generated answers are correct with reasonable accuracy.

### Knowledge Prediction (P(IK))
The second phase investigates models' ability to predict "P(IK)"—the probability that they possess knowledge to answer questions—without referencing specific proposed answers. Models performed well at predicting P(IK) and demonstrated partial generalization across different tasks.

### Limitations
Calibration challenges emerged when applying this approach to entirely new tasks. The findings suggest promise for developing more transparent models but indicate that perfect generalization remains difficult.

## Implications

This work is foundational for understanding model uncertainty and truthfulness. It demonstrates that language models have some capacity for introspection about their own knowledge, which is critical for:
- Reducing hallucinations
- Building more reliable AI systems
- Developing truthful AI that can express uncertainty appropriately

## Relevance

**Critical for AI safety research.** Early work on model calibration and uncertainty quantification. Foundational for later research on truthfulness, hallucination reduction, and reliable AI systems.

---
*Metadata fetched via WebFetch on 2025-12-31*
