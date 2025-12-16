# Verification Methods for International AI Agreements

**arXiv:** https://arxiv.org/abs/2408.16074
**Authors:** Akash R. Wasil, Tom Reed, Jack William Miller, Peter Barnett
**Date:** 2024-08-28 (v1), revised 2024-11-04 (v2)

## Abstract

**Research Question:** What techniques can be used to verify compliance with international agreements about advanced AI development?

The paper examines 10 verification methods that could detect:
1. Unauthorized AI training (e.g., above certain FLOP thresholds)
2. Unauthorized data centers

## Three Categories of Verification Methods

**(a) National technical means** - Methods requiring minimal access:
- Remote sensing
- Whistleblowers
- Energy monitoring
- Customs data analysis
- Financial intelligence

**(b) Access-dependent methods** - Require approval from suspected nation:
- Data center inspections
- Semiconductor manufacturing facility inspections
- AI developer inspections

**(c) Hardware-dependent methods** - Require rules around advanced hardware:
- Chip location tracking
- Chip-based reporting

## Hardware-Dependent Approach

Modifying chips used in training/inference to:
- Locate them (preventing smuggling or secret data centers)
- Record what they're used for
- Block unauthorized large training runs
- Enable government registry of chip activities

## Historical Precedents

For each method, the paper provides historical precedents and possible evasion techniques, drawing on experience from arms control and other domains.

## Claude Summary

This paper provides a practical toolkit for international AI governance:

**Why this matters**: International agreements are only as good as verification. Without verification, agreements lack teeth and are subject to defection.

**Key insight**: Many verification techniques exist from other domains (nuclear, biological, chemical weapons) that can be adapted for AI.

**Hardware approaches are key**: Compute is physical and trackable. Chip-level controls offer strong verification potential, though implementation is complex.

**Challenges**: Many methods can be evaded; multiple overlapping methods likely needed. Political/economic barriers may be larger than technical ones.

## Relevance

Essential for AI governance and policy research. Provides concrete technical options for international AI agreements. From researchers thinking seriously about implementation, not just principles.
