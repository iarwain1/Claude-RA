# A Practical Approach to Verifying Code at Scale

**URL:** https://alignment.openai.com/scaling-code-verification/
**Authors:** Maja Trębacz, Sam Arnesen, Albin Cassirer, Max Johnson, Xin Lin, Thibault Sottiaux, and the Codex team
**Date:** December 1, 2025
**Type:** Research Article

## Abstract

This research demonstrates that automated code review systems must prioritize precision over comprehensive coverage when deployed in real engineering environments. The authors found that "defenses often fail not because they are technically wrong, but because they are so impractical that the user chooses not to use them," establishing precision-recall tradeoffs as essential for adoption.

The study reveals that repository-wide access and code execution capabilities substantially improve reviewer effectiveness. Models equipped with these tools identified critical issues while producing significantly fewer false positives compared to diff-only approaches, resulting in higher developer trust and actionable feedback rates.

## Key Findings

### Precision Over Recall
- Automated reviewers must minimize false positives to maintain developer trust
- High false alarm rates lead to tool abandonment regardless of technical correctness
- Precision-recall tradeoffs are critical for real-world deployment

### Tool Access Improves Performance
- Repository-wide context access significantly reduces false positives
- Code execution capabilities improve bug detection
- Diff-only approaches generate more false alarms

### Verification Scales Efficiently
- Crucial insight: Verification requires substantially fewer computational resources than code generation
- Reviewer recovered most previously identified issues at modest inference budgets
- Suggests that oversight scales cost-effectively alongside increasingly capable code generators

## Technical Contributions

1. **Demonstration of repo-scale context benefits** - Repository access and execution reduce false alarms while maintaining bug detection

2. **Specialized training insights** - Dedicated training for code review differs meaningfully from training reward models for generation

3. **Practical deployment framework** - Shows 52.7% author adoption of reviewer suggestions across 100,000+ daily external pull requests

4. **Verification-generation inference gap** - Quantifies that verifiers operate efficiently at fractional generator budgets

## Relevance

**Critical for AI safety and scalable oversight.** Demonstrates that verification can scale more efficiently than generation, supporting alignment approaches based on oversight. Real-world deployment data provides evidence for practical AI safety mechanisms in production systems.

---
*Metadata fetched via WebFetch on 2025-12-31*
