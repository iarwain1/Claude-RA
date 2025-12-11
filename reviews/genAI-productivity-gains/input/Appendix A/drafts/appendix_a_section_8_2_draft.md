# Appendix A, Section 8.2: What Breaks for Generative AI

## Overview

This section identifies fundamental assumptions from traditional disciplines that fail for generative AI. Understanding these breaks is essential to avoid misapplying methods that won't work in AI contexts.

These aren't minor adjustments—they represent fundamental assumption violations that can lead established methods astray.

---

## Broken Assumptions

| Broken Assumption | Disciplines Affected | Reality for AI |
|-------------------|---------------------|----------------|
| **Determinism** | Software testing, reliability engineering | AI outputs are stochastic; same input produces different outputs |
| **Enumerable inputs/outputs** | Software testing, traditional ML | Input and output spaces are effectively unbounded |
| **Clear ground truth** | Traditional ML, psychometrics | Many AI tasks have no single "correct" answer |
| **Stable system under test** | All T&E disciplines | Models update continuously, sometimes without notice |
| **Stable traits/capabilities** | Psychometrics, I-O psychology | AI capabilities change rapidly |
| **Predictable failures** | Reliability engineering, safety | Failures occur unpredictably at jagged capability boundaries |
| **Observable processes** | Quality management, safety | AI processing is opaque |
| **Clear system boundaries** | Systems engineering | Where does AI end? (Model + prompt + context + user) |
| **Independent failures** | Reliability engineering, risk | AI failures may be correlated across applications |
| **Blinding** | Experimental design, clinical trials | Users typically know they're using AI |
| **Treatment stability** | Experimental design | AI changes during evaluation period |
| **Defined treatment** | Econometrics, program evaluation | "Using AI" is highly variable |
| **Historical data** | Risk analysis, reliability | Limited operating history for AI |
| **Population/norming** | Psychometrics | No natural reference population for AI |
| **Test security** | Psychometrics, educational measurement | Training may include benchmark items |

---

## Detailed Analysis of Key Breaks

### Determinism

**Traditional assumption**: Same inputs produce same outputs. Bugs are reproducible. Test results are deterministic.

**Reality for AI**: Generative AI is inherently stochastic. The same prompt can produce different outputs on different runs. Temperature settings control randomness but don't eliminate it. Even with temperature at zero, outputs may vary due to infrastructure factors.

**Implications**:
- Single test runs are insufficient
- Statistical approaches needed
- Reproducibility is approximate at best
- Version control is challenging

### Enumerable Inputs/Outputs

**Traditional assumption**: Inputs can be categorized. Outputs have defined formats. Test coverage can be systematically achieved.

**Reality for AI**: Natural language inputs are unbounded. Outputs can be essentially any text. The space of possible inputs and outputs is effectively infinite. "Coverage" of input space is impossible.

**Implications**:
- Can't test all inputs
- Sampling strategies essential
- Coverage is always incomplete
- Edge cases are unbounded

### Clear Ground Truth

**Traditional assumption**: There's a correct answer against which to evaluate. Classification has true labels. Regression has true values.

**Reality for AI**: Many generative AI tasks have no single correct answer. "Write an email" has many acceptable outputs. Quality is multidimensional and contextual. Expert judgments vary.

**Implications**:
- Human evaluation is necessary but subjective
- Inter-rater reliability is challenging
- "Accuracy" may not be meaningful
- Quality assessment is inherently fuzzy

### Stable System Under Test

**Traditional assumption**: Test the system, then deploy it. The tested system is the deployed system.

**Reality for AI**: Models update continuously. Providers may change models without notification. Fine-tuning, prompt engineering, and context continuously modify system behavior. The system evaluated may differ from the system deployed.

**Implications**:
- Point-in-time evaluation has limited validity
- Continuous monitoring is essential
- Version tracking is difficult
- Evaluation results decay over time

### Predictable Failures

**Traditional assumption**: Failure modes can be enumerated. Failures follow predictable patterns. Reliability can be predicted from components.

**Reality for AI**: Failures occur at unpredictable capability boundaries. Similar inputs may produce dramatically different performance. The jagged capability frontier means high capability adjacent to surprising failure.

**Implications**:
- Can't rely on reliability models
- More extensive testing needed
- Uncertainty bounds are wide
- Expect surprises

### Test Security / Benchmark Contamination

**Traditional assumption**: Test items are secure. Examinees haven't seen the test before. Scores reflect genuine capability.

**Reality for AI**: Training data may include benchmark items. Internet-scale training makes contamination pervasive. Scores may reflect memorization rather than capability. Contamination is hard to detect.

**Implications**:
- Benchmark scores may overstate capability
- Need novel evaluation approaches
- Held-out tests have value
- Deployment monitoring essential

---

## What to Do When Assumptions Break

When fundamental assumptions fail:

1. **Acknowledge the break** rather than pretending methods still work
2. **Adapt methods** where possible (see Section 8.3)
3. **Develop new approaches** where adaptation isn't sufficient (see Section 8.4)
4. **Increase uncertainty** in conclusions—less confidence is warranted
5. **Use multiple methods** to triangulate despite each method's limitations
6. **Monitor continuously** rather than relying on point-in-time evaluation

---

## Connections to Other Sections

Each individual discipline section (1.1-7.2) includes a "What Breaks for Generative AI" discussion specific to that discipline. This section synthesizes across disciplines to identify the most fundamental and cross-cutting assumption violations.

---

*[End of Section 8.2]*
