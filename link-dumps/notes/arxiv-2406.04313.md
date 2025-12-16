# Improving Alignment and Robustness with Short Circuiting

**arXiv:** [2406.04313](https://arxiv.org/abs/2406.04313)
**Authors:** Andy Zou, Long Phan, Justin Wang, Derek Duenas, Maxwell Lin, Maksym Andriushchenko, Rowan Wang, Zico Kolter, Matt Fredrikson, Dan Hendrycks
**Date:** 2024-06-06

## Abstract

Existing techniques aimed at improving alignment, such as refusal training, are often bypassed. The paper presents an approach, inspired by recent advances in representation engineering, that "short-circuits" models as they respond with harmful outputs.

The method introduces 'short-circuiting,' a novel approach to enhance alignment and robustness in AI models, particularly LLMs and multimodal systems, to resist adversarial attacks and prevent harmful outputs. Short-circuiting focuses on controlling internal representations within the AI models rather than countering specific attacks, using a training process that redirects harmful representations to an orthogonal space to interrupt harmful behaviors.

Extensive experimentation with models like Mistral-7B-Instruct-v2 and Llama-3-8B-Instruct demonstrated significant improvements in alignment and robustness, with marked reductions in attack success rates while maintaining model performance.

## Claude Summary

This paper introduces "circuit breakers" - a representation engineering approach to making models more robust against jailbreaks. Unlike refusal training which can be bypassed, this method operates at the representation level, redirecting harmful activations to an orthogonal space.

**Key contributions:**
- Novel defense mechanism that's more robust than safety fine-tuning
- Works across different model architectures
- Maintains general capabilities while improving safety

**Relevance:** Important for understanding modern approaches to jailbreak defense that go beyond prompt-level interventions.
