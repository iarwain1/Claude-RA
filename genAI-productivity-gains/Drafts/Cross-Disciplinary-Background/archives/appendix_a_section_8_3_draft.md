# Appendix A, Section 8.3: What Requires Adaptation

## Overview

Between concepts that transfer directly (Section 8.1) and fundamental breaks (Section 8.2) lies substantial middle ground—approaches that can be applied to AI evaluation but require significant modification.

This section identifies concepts that transfer with adaptation and describes the adaptations required.

---

## Concepts Requiring Adaptation

| Original Concept | Source Discipline | Required Adaptation |
|-----------------|-------------------|---------------------|
| **Test coverage** | Software testing | Coverage of capabilities/scenarios, not input space |
| **Regression testing** | Software testing | Continuous monitoring rather than re-running fixed tests |
| **Reliability prediction** | Reliability engineering | Scenario-based rather than component-based |
| **FMEA** | Reliability/safety | Failure modes are less enumerable; more emphasis on unknown unknowns |
| **Trust calibration** | Human factors | For systems with stochastic, jagged capabilities |
| **Implementation fidelity** | Program evaluation | "Use" is highly variable and hard to characterize |
| **IRT/psychometric methods** | Psychometrics | For benchmark design, not stable trait measurement |
| **Safety cases** | Safety engineering | New evidence types and argument structures needed |
| **Audit evidence** | Audit | New evidence types for opaque AI systems |
| **Control charts** | Quality management | For AI-specific metrics with different variability patterns |
| **Cost-benefit analysis** | Economics | Adapted for uncertain, intangible benefits |
| **RCT design** | Experimental design | Adapted for non-blinded, evolving treatments |
| **Usability testing** | HCI | Adapted for variable system behavior |
| **Job analysis** | I-O Psychology | Adapted for defining AI "jobs" |

---

## Detailed Adaptation Guidance

### Test Coverage → Capability/Scenario Coverage

**Original concept**: Test coverage measures what proportion of inputs, code paths, or requirements have been tested.

**Adaptation needed**: For AI, coverage of the input space is impossible (infinite space). Instead, focus on:
- Coverage of capability categories (reasoning, coding, knowledge domains)
- Coverage of difficulty levels within categories
- Coverage of scenario types (routine vs. edge cases)
- Sampling strategies that ensure diversity

**How to adapt**: Define capability dimensions and ensure evaluation samples across dimensions. Use stratified sampling rather than attempting exhaustive coverage.

### Regression Testing → Continuous Monitoring

**Original concept**: Re-run previous tests after changes to detect regressions.

**Adaptation needed**: AI systems change continuously; point-in-time regression testing is insufficient. Also, stochastic outputs mean exact reproduction isn't possible.

**How to adapt**: Implement continuous monitoring of performance metrics. Track statistical properties over time rather than exact outputs. Alert when metrics drift outside expected ranges.

### FMEA → AI Failure Mode Analysis

**Original concept**: Enumerate failure modes, assess occurrence/severity/detectability, compute Risk Priority Numbers.

**Adaptation needed**: AI failure modes are less enumerable than hardware failures. Unknown unknowns are more significant. Probability estimates are harder.

**How to adapt**: Use FMEA framework but:
- Accept incompleteness of failure mode list
- Emphasize unknown unknowns as a category
- Use qualitative rather than quantitative probability estimates
- Focus on high-consequence failures regardless of probability

### Trust Calibration → AI Trust Calibration

**Original concept**: Help operators calibrate trust to actual automation reliability.

**Adaptation needed**: AI reliability varies unpredictably across tasks (jagged frontier). Reliability in one context doesn't predict reliability in similar contexts.

**How to adapt**:
- Train users on specific reliability patterns, not global reliability
- Provide task-specific reliability information where possible
- Design for appropriate skepticism as default
- Create feedback mechanisms so users learn calibration

### IRT → AI Benchmark Design

**Original concept**: Item Response Theory models test items to measure latent traits.

**Adaptation needed**: AI doesn't have "stable traits" in the psychometric sense. But IRT concepts can improve benchmark design.

**How to adapt**: Use IRT concepts for:
- Selecting discriminating benchmark items
- Identifying item difficulty ranges
- Detecting anomalous patterns (contamination)
- Creating adaptive benchmarks

Don't use IRT for:
- Claiming to measure stable AI "traits"
- Making strong inferences about underlying constructs

### Safety Cases → AI Safety Cases

**Original concept**: Structured arguments with claims, evidence, and argument that a system is safe.

**Adaptation needed**: Evidence types for AI differ from traditional systems. Formal verification isn't available. Probabilistic reliability claims are difficult.

**How to adapt**: Use safety case structure but:
- Develop new evidence types (red teaming results, behavioral testing, monitoring data)
- Accept qualitative rather than quantitative claims
- Make assumptions and limitations explicit
- Plan for updating as AI evolves
- Include deployment monitoring in the case

### RCT Design → AI RCT Design

**Original concept**: Randomized controlled trials with blinding and clear treatment definition.

**Adaptation needed**: Can't blind users to AI. "Treatment" (AI use) is heterogeneous. AI may change during study.

**How to adapt**:
- Acknowledge lack of blinding as limitation
- Characterize treatment heterogeneity
- Control for treatment version
- Use hybrid designs combining RCT elements with other methods
- Measure how AI is used, not just whether

---

## General Principles for Adaptation

1. **Preserve the core insight** while relaxing assumptions
2. **Accept lower precision** than the original method provides
3. **Combine with other methods** to compensate for limitations
4. **Document adaptations** transparently
5. **Validate adapted methods** where possible
6. **Iterate adaptations** as understanding improves

---

## When Adaptation Isn't Enough

Some situations require genuinely new approaches rather than adaptation:
- When core assumptions are fundamentally violated
- When adaptation would distort the method beyond recognition
- When the problem structure is genuinely novel

See Section 8.4 for challenges that require new approaches.

---

*[End of Section 8.3]*
