# A Rosetta Stone for AI Benchmarks

**arXiv:** https://arxiv.org/abs/2512.00193
**Authors:** Anson Ho, Jean-Stanislas Denain, David Atanasov, Samuel Albanie, Rohin Shah
**Date:** 2025-11-28

## Abstract

Most AI benchmarks saturate within years or even months after they are introduced, making it hard to study long-run trends in AI capabilities. To address this challenge, the authors build a statistical framework that stitches benchmarks together, putting model capabilities and benchmark difficulties on a single numerical scale.

This acts as a "Rosetta Stone", allowing comparison of models across a wide range of abilities and time, even if they are not evaluated on the same benchmarks. Moreover, this works without assuming how capabilities evolve across time or with training compute.

They demonstrate three applications of this framework:
1. Measure the speed of AI progress over time
2. Forecast future AI capabilities
3. Compare models across different benchmark families

## Claude Summary

This paper addresses a critical challenge in AI evaluation: benchmark saturation. As models improve rapidly, benchmarks quickly become saturated and lose discriminative power. This makes it difficult to track long-term capability trends.

The "Rosetta Stone" framework uses statistical methods (likely item response theory or similar) to calibrate benchmarks against each other, creating a unified capability scale. This enables:
- Cross-benchmark model comparisons
- Long-term trend analysis despite benchmark turnover
- Capability forecasting

The involvement of Rohin Shah (DeepMind AI safety) suggests connections to safety-relevant capability tracking.

## Relevance

Essential for AI forecasting and longitudinal capability assessment. Addresses a fundamental measurement challenge that affects our ability to track AI progress and anticipate future capabilities.
