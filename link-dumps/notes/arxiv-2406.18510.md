# WildTeaming at Scale: From In-the-Wild Jailbreaks to (Adversarially) Safer Language Models

**arXiv:** https://arxiv.org/abs/2406.18510
**Authors:** Liwei Jiang, Kavel Rao, Seungju Han, Allyson Ettinger, Faeze Brahman, Sachin Kumar, Niloofar Mireshghallah, Ximing Lu, Maarten Sap, Yejin Choi, Nouha Dziri (AI2)
**Date:** 2024-06-26
**Venue:** NeurIPS 2024
**GitHub:** https://github.com/allenai/wildteaming

## Abstract

WildTeaming is an automatic LLM safety red-teaming framework that:
1. Mines in-the-wild user-chatbot interactions
2. Discovers 5.7K unique clusters of novel jailbreak tactics
3. Composes multiple tactics for systematic exploration of novel jailbreaks

Unlike prior work using human workers, gradient optimization, or LLM revision, this work investigates jailbreaks from real chatbot users who weren't specifically trying to break the system.

## Key Results

- Up to 4.6x more diverse and successful adversarial attacks vs. SOTA jailbreak methods
- Reveals previously unidentified vulnerabilities in frontier LLMs

## WildJailbreak Dataset

Large-scale synthetic safety dataset with 262K prompt-response pairs:
- Vanilla (direct request) and adversarial (complex jailbreak) pairs
- **Contrastive types**: Harmful queries AND benign queries that resemble harmful ones
- Designed to mitigate exaggerated safety (over-refusal)

## Safety Training Properties Identified

Ideal balance requires:
- Appropriate safeguarding without over-refusal
- Effective handling of both vanilla and adversarial queries
- Minimal decrease in general capabilities

## Claude Summary

WildTeaming makes a crucial methodological contribution to LLM safety:

**Key insight**: Mining real user interactions reveals jailbreak tactics that researchers wouldn't think to try. Users in the wild are creative adversaries.

**Why contrastive data matters**:
- Harmful queries teach models what to refuse
- Benign lookalikes teach what NOT to refuse
- Both are needed to avoid exaggerated safety

**Practical value**:
- Dataset can improve model safety training
- Framework enables ongoing red-teaming
- Taxonomy of tactics useful for defense research

## Relevance

Important companion to WildGuard (same team). Provides both offense (red-teaming) and defense (safety training) tools. The contrastive dataset approach is particularly valuable for addressing over-refusal, which degrades user experience.
