# Measuring Agents in Production

**Paper Key:** pan2025agents
**Authors:** Pan, Melissa Z., Arabzadeh, Negar, Cogo, Riccardo, et al. (25 total authors from UC Berkeley, Databricks, MIT)
**Date:** December 2, 2025
**arXiv:** https://arxiv.org/abs/2512.04123
**Priority:** 10 (Essential)

---

## Summary

First large-scale systematic study of AI agents in production environments across 26 domains. Surveys 306 practitioners and conducts 20 in-depth case studies to understand why organizations build agents, how they build them, how they evaluate them, and top development challenges. **Reveals massive gap between research prototypes (long-horizon autonomous agents) and production reality (short chains with heavy human oversight).**

---

## Key Contribution

**Empirical reality check for AI agent research.** Provides first comprehensive data on what actually works in production vs. what's published in research. **Critical for bridging research-practice gap** in Part 4 (Practical Guidance).

---

## Methodology

**Two-pronged approach:**

1. **Large-scale survey:** 306 practitioners
2. **Deep case studies:** 20 in-depth interviews across 26 domains

**Domains covered:** Customer support, software engineering, content generation, data analysis, research assistance, sales, recruiting, legal, healthcare, finance, education, marketing, operations, security, and more.

---

## Main Findings

### Production Agent Characteristics (vs. Research Prototypes)

| Dimension | Production Reality | Research Focus | Gap |
|-----------|-------------------|----------------|-----|
| **Steps before human** | 68% execute ≤10 steps | Long-horizon (100s-1000s) | Massive |
| **Model approach** | 70% use prompting only | Fine-tuning, RL, custom training | Controllability > performance |
| **Evaluation method** | 74% rely on human eval | Automated metrics, benchmarks | Automation insufficient |
| **Architecture** | Simple, controllable | Complex, sophisticated | Simplicity wins |

### Critical Statistics

**Step Counts:**
- **68% execute at most 10 steps** before requiring human intervention
- Short action chains dominate
- Human-in-the-loop is norm, not exception

**Model Approach:**
- **70% rely on prompting off-the-shelf models** vs fine-tuning
- **Rationale:** Controllability, interpretability, ease of iteration
- Fine-tuning used sparingly (30%) for specific high-value use cases

**Evaluation:**
- **74% depend primarily on human evaluation**
- Automated metrics insufficient for production requirements
- Quality, safety, reliability require human judgment

**Top Development Challenge:**
- **Reliability** is #1 concern
- Driven by difficulties in ensuring and evaluating correctness
- Gap between test performance and production behavior

---

## Why Production Differs from Research

### Constraints Driving Simplicity

1. **Reliability requirements**
   - Production demands consistent, predictable behavior
   - Long chains increase failure probability exponentially
   - Each step is potential failure point

2. **Debuggability needs**
   - Must understand and fix failures quickly
   - Simple architectures easier to diagnose
   - Human oversight enables rapid intervention

3. **Cost considerations**
   - Long-horizon agents expensive (many LLM calls)
   - ROI often doesn't justify complexity
   - Human intervention cheaper than perfect automation

4. **Deployment realities**
   - Integration with existing systems favors simplicity
   - Organizational trust builds gradually
   - Start simple, scale complexity as confidence grows

---

## Practical Implications

### For Acquisition Decision-Makers

**Don't expect research-grade autonomy in production:**
- Research demos show 100+ step autonomous agents
- Production reality: 68% need human at ≤10 steps
- **Plan for human-in-the-loop, not full automation**

**Evaluation must include human judgment:**
- 74% can't rely on automated metrics alone
- Build evaluation processes including domain experts
- Budget for ongoing human evaluation

**Prioritize reliability over sophistication:**
- Top concern is ensuring correctness
- Simple, reliable > complex, impressive
- Iterate from simple baseline, add complexity only when needed

### For Agent System Design

**Start simple:**
- Prompting-based agents sufficient for most use cases (70%)
- Reserve fine-tuning for high-value specialized tasks
- Controllability matters more than peak performance

**Design for failure:**
- Assume agent will need human intervention
- Make handoff graceful, informative
- Track where humans intervene to improve system

**Human evaluation is feature, not bug:**
- Accept that 74% need human eval
- Design systems making evaluation efficient
- Use human feedback to improve agents over time

---

## Relevance to GenAI Productivity Review

### Part 1: The Benchmark-Utility Gap

**Explains the gap empirically.** Benchmarks evaluate long-horizon autonomy. Production uses short chains with human oversight. **Benchmarks measure wrong capability.**

### Part 4: Practical Guidance for Acquisition Decision-Makers

**ESSENTIAL guidance on realistic expectations:**
- Don't procure based on research demos or benchmark scores
- Expect 68% probability system needs human at ≤10 steps
- Budget for human evaluation (74% depend on it)
- Prioritize reliability over autonomy metrics

### Part 5: T&E Considerations

**Informs evaluation approach:**
- Can't rely on automated testing alone
- Need operational T&E with human evaluators
- Test with realistic step constraints (≤10 typical)
- Evaluate human-agent handoff quality

---

## Connections to Other References

- **Validates:** scale2025remotelabor (2.5% automation) - explains why agents fail on complex work
- **Contrasts:** Research focus on SWE-bench (long-horizon coding) vs production reality
- **Supports:** upwork2025upbench finding that human+agent > agent alone
- **Complements:** anthropic2025workdec - both show human oversight essential

---

## Key Insights for DoD Context

### Acquisition Implications

1. **Procurement specifications should reflect production reality:**
   - Specify acceptable human intervention frequency
   - Require demonstration of reliability over autonomy
   - Include human evaluation in acceptance criteria

2. **Deployment planning must account for human-in-loop:**
   - Manning requirements include human oversight
   - Training programs for human-agent teaming
   - Workflows designed for graceful agent-human handoff

3. **Testing should match production constraints:**
   - Test with 10-step limits (68% reality)
   - Evaluate handoff quality
   - Measure reliability under operational conditions

---

## Critical Quotes

> "68% execute at most 10 steps before requiring human intervention"

> "70% rely on prompting off-the-shelf models instead of weight tuning"

> "74% depend primarily on human evaluation"

> "Reliability remains the top development challenge, driven by difficulties in ensuring and evaluating agent correctness."

> "Simple yet effective methods already enable agents to deliver impact across diverse industries."

---

## Research Questions Raised

1. What evaluation methods would reliably predict production agent performance?
2. How can we design benchmarks that test 10-step reliability rather than 100-step autonomy?
3. What human-agent teaming patterns work best in defense contexts?
4. Can we develop automated proxies for the human evaluation 74% depend on?

---

## Limitations

- Survey sample may skew toward successful deployments (survivorship bias)
- Self-reported data on step counts and evaluation methods
- Case studies from 26 domains - may miss domain-specific patterns
- Snapshot in time (Dec 2025) - production practices evolving

---

## Tags

`#agent-evaluation` `#production-reality` `#empirical-anchor` `#research-practice-gap` `#human-in-loop` `#reliability` `#key-reference`

---

## Reading Status

- **Status:** Pending full read
- **Added to queue:** 2025-12-31
- **Note file created:** 2025-12-31
- **Full paper access:** Available on arXiv

---

## Next Steps

1. **Read full paper** to extract domain-specific patterns
2. **Map findings** to military acquisition use cases
3. **Develop guidelines** for realistic agent system specifications
4. **Integrate into Part 4** practical guidance section
5. **Cross-reference** with METR, Scale, Upwork studies on human-AI teaming

---

*Summary created: 2025-12-31*
*Last updated: 2025-12-31*
