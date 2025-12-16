# WildGuard: Open One-Stop Moderation Tools for Safety Risks, Jailbreaks, and Refusals of LLMs

**arXiv:** https://arxiv.org/abs/2406.18495
**Authors:** Seungju Han, Kavel Rao, Allyson Ettinger, Liwei Jiang, Bill Yuchen Lin, Nathan Lambert, Yejin Choi, Nouha Dziri (AI2)
**Date:** 2024-06-26 (v1), revised 2024-12-09 (v3)
**GitHub:** https://github.com/allenai/wildguard

## Abstract

WildGuard is an open, lightweight moderation tool for LLM safety that achieves three goals:
1. Identifying malicious intent in user prompts
2. Detecting safety risks of model responses
3. Determining model refusal rate

Together, WildGuard provides a one-stop tool with enhanced accuracy across 13 risk categories.

## Motivation

Existing tools like Llama-Guard2 have significant limitations:
- Much less effective at discerning harm in adversarial prompts (jailbreaks) vs. vanilla queries
- Fall far behind GPT-4 on both types
- Cannot independently assess refusal (needed for detecting exaggerated safety)

## WildGuardMix Dataset

- 92K labeled examples covering 13 risk categories
- Largest multi-task safety dataset to date
- Includes WildGuardTrain (training) and WildGuardTest (5K human-annotated test set)

## Key Results

- State-of-the-art in open-source safety moderation across all three tasks
- Up to 26.4% improvement on refusal detection vs. existing models
- Matches/exceeds GPT-4 (up to 3.9% improvement on prompt harmfulness)
- Reduces jailbreak attack success rate from 79.8% to 2.4% when used as moderator

## Claude Summary

WildGuard represents a significant advance in open-source safety tooling:

**Why three tasks matter**:
- Prompt harm: Is the user trying to elicit harmful content?
- Response harm: Did the model produce harmful output?
- Refusal detection: Did the model refuse? (Critical for detecting over-refusal)

**Practical impact**:
- Open alternative to proprietary moderation
- Can be used as input/output filter for any LLM
- Enables evaluation of safety properties at scale

**Novel contribution**: The refusal detection task is underappreciated - distinguishing between appropriate refusal, over-refusal, and harmful compliance requires understanding the full context.

## Relevance

Important tool for LLM deployment safety. Enables systematic evaluation of safety properties. The dataset is also valuable for training safer models. From AI2, a respected non-profit AI research org.
