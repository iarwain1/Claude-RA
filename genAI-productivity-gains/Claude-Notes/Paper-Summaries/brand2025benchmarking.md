# Why Benchmarking is Hard

**Authors:** Florian Brand, Jean-Stanislas Denain
**Affiliation:** Epoch AI
**Date:** December 23, 2025
**Type:** Research Article
**URL:** https://epoch.ai/gradient-updates/why-benchmarking-is-hard

## Key Contributions

1. **Quantified scaffold variance**: 11-15% variance on SWE-bench Verified from scaffolding choices alone
2. **Systematic documentation** of compounding evaluation variables across benchmark setup and API access
3. **Identified resource barrier** created by evaluation complexity for smaller organizations

## Methodology

Analysis of practical benchmarking challenges through:
- Empirical testing of scaffold variations on SWE-bench Verified
- Documentation of API provider differences and reliability issues
- Examination of multiple sources of variance in the evaluation stack

## Key Findings

### 1. Benchmark Setup Variables Create Substantial Variance

**Sources of variance:**
- **Prompts**: Different formulations yield different results
- **Sampling parameters**: Temperature, top-p significantly impact performance
- **Scaffolds**: 11-15% variance on SWE-bench Verified from scaffold choice alone
- **Execution environments**: Runtime conditions matter
- **Scoring methods**: Different approaches produce different scores

**Critical insight:** "Scaffolds have a huge impact on agentic benchmarks"

### 2. API Access Issues Compound Problems

**Provider-specific problems:**
- Rate-limit errors
- Truncated responses
- Hidden token limits
- Timeout issues
- Newly released models handled less reliably than established ones

**Impact:** Selecting different API providers yields noticeably divergent results for identical models

### 3. Variables Compound Across Evaluation Stack

Multiple sources of variance multiply together, causing final scores to diverge significantly from developer-reported numbers. This creates substantial reproducibility challenges.

### 4. Resource Barrier for Independent Evaluation

The complexity particularly burdens smaller organizations—academics and hobbyists lack resources to navigate multiple API implementations and troubleshoot provider-specific issues, creating evaluation barriers that slow independent assessment of model capabilities.

## Relevance to GenAI Productivity Review

### Part 1: The Benchmark-Utility Gap

**CRITICAL supporting evidence.** This paper provides concrete explanation for why benchmark results may not replicate and why independent evaluation is so difficult. The 11-15% variance from scaffolds alone demonstrates that even well-designed benchmarks have substantial measurement error.

**Connection to [bean2025construct](bean2025construct.md):** While Bean et al. focus on construct validity (whether benchmarks measure what they claim), Brand & Denain focus on measurement reliability (whether benchmarks give consistent results). Both undermine benchmark credibility from different angles.

### Part 3: A Framework for AI Evaluation

**Important for evaluation design guidance.** Acquisition decision-makers need to understand:
- Benchmark scores have substantial error bars (11-15%+ from setup alone)
- Reproducibility requires careful documentation of all parameters
- Small organizations may not be able to independently verify vendor claims
- Internal evaluations should control for these sources of variance

### Part 4: Practical Guidance for Acquisition Decision-Makers

**Key practical implications:**

1. **Don't trust single benchmark numbers**: Variance from setup choices alone can be 11-15%
2. **Require methodology transparency**: Vendors should document prompts, scaffolds, sampling parameters
3. **Be skeptical of exact score claims**: Multiple legitimate evaluation approaches exist
4. **Plan for evaluation capacity**: Independent assessment requires significant technical resources
5. **Use multiple evaluation approaches**: Single benchmark scores are unreliable

### Part 6: Research Agenda and Investment Priorities

**Highlights need for:**
- Standardized evaluation protocols to reduce variance
- Public evaluation infrastructure to reduce resource barriers
- Better documentation standards for benchmark methodology
- Research into robust evaluation methods that reduce sensitivity to setup choices

## Critical Assessment

**Strengths:**
- Quantifies previously anecdotal concerns about benchmark variance
- Practical focus on real-world evaluation challenges
- Clear documentation of specific problems (API issues, scaffold variance)

**Limitations:**
- Limited to one benchmark (SWE-bench Verified) for quantified variance claim
- Doesn't propose solutions, only documents problems
- Published in blog post format (Epoch AI "Gradient Updates"), not peer-reviewed venue

**Currency:** Excellent - December 2025, addresses current evaluation landscape

**Evidence Quality:** Medium-High. Provides concrete quantified example (11-15% variance) but limited to single benchmark. Anecdotal evidence for other claims (API issues) not systematically measured.

## Connections to Other References

**Directly supports:**
- [bean2025construct](bean2025construct.md): Construct validity (what benchmarks measure) + measurement reliability (consistency) = comprehensive critique
- [pan2025agents](pan2025agents.md): Pan et al. show production agents differ from benchmarks; Brand & Denain show why benchmark scores are unreliable
- **metr2025developer**: METR's 19% slowdown finding contradicts expectations partly because benchmark-based expectations are unreliable

**Relevant to:**
- **openai2025gdpval**: GDPval methodology includes careful scaffolding—Brand & Denain show why this matters
- **scale2025remotelabor**: Scale's 2.5% automation rate shows benchmark performance doesn't predict real-world success—Brand & Denain help explain the gap

## Questions/Notes

1. **How much of the benchmark-utility gap is measurement error vs. construct validity?**
   - Brand & Denain show 11-15% from scaffolds alone
   - But larger gaps (e.g., Scale's 97.5% failure rate) suggest construct validity is the bigger problem

2. **What are best practices for reducing scaffold variance?**
   - Paper doesn't propose solutions
   - Need research on robust evaluation protocols

3. **How should acquisition decision-makers handle benchmark uncertainty?**
   - Require error bars on all benchmark claims?
   - Demand multiple independent evaluations?
   - Focus on operational pilots instead?

4. **Does 11-15% variance generalize to other benchmarks?**
   - Only tested on SWE-bench Verified
   - Likely varies by benchmark type (multiple choice vs. code generation vs. long-horizon agents)

## Citation Guidance

**Appropriate uses:**
- Citing specific 11-15% variance figure for SWE-bench Verified
- Documenting scaffold sensitivity in agent benchmarks
- Explaining reproducibility challenges in AI evaluation
- Supporting claims about resource barriers for independent evaluation

**Inappropriate uses:**
- Claiming all benchmarks have 11-15% variance (only tested on one)
- Using to dismiss all benchmark results (measurement error ≠ uselessness)
- Citing as peer-reviewed research (blog post format)

**Citation note:** While published as blog post, authors are from Epoch AI (reputable AI research organization) and provide concrete quantified evidence, making it suitable for citing in technical reports with appropriate caveats about venue.
