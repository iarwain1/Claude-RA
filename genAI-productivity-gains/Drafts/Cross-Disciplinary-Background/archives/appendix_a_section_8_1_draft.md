# Appendix A, Section 8.1: What Transfers Directly

## Overview

This section identifies concepts from established disciplines that transfer directly to AI evaluation with minimal modification. These are proven approaches that can be applied to AI essentially as-is.

The value of direct transfer is efficiency: we don't need to reinvent what already works. These concepts have been refined through decades of practice in their home disciplines.

---

## Direct Transfers by Discipline

### From Testing Traditions

| Discipline | Transferable Concept | Application to AI Evaluation |
|------------|---------------------|------------------------------|
| **Software Testing** | Verification vs. Validation distinction | Benchmarks are closer to verification; operational testing is validation |
| | Test planning discipline | Systematic identification of what to test |
| | Regression mindset | Track performance over time to detect degradation |
| **Systems T&E** | DT/OT paradigm | Lab testing (DT) precedes operational pilots (OT) |
| | MOPs vs. MOEs | Technical metrics ≠ mission effectiveness |
| | Independent evaluation | Separate evaluator from developer for credibility |
| **Autonomous Systems** | Sim-to-real gap awareness | Benchmark-to-real gap is analogous |
| | Scenario-based testing | Systematic scenario design and prioritization |
| | Safety case methodology | Structured safety argumentation |
| **Cybersecurity** | Adversarial mindset | Actively try to make AI fail |
| | Red teaming methodology | Structured adversarial evaluation |
| | Threat modeling | Prioritize evaluation based on threat analysis |
| | Defense in depth | Multiple protections, not reliance on single measure |

### From Statistical Methods

| Discipline | Transferable Concept | Application to AI Evaluation |
|------------|---------------------|------------------------------|
| **Experimental Design** | Validity framework | Internal, external, construct validity |
| | Control conditions | What's the comparison? Relative to what? |
| | Bias awareness | Selection, attrition, experimenter bias |
| | Pre-registration | Commit to analysis plans |
| **Psychometrics** | Reliability concepts | Consistency of measurement |
| | Construct validity | Does benchmark measure what we intend? |
| | Criterion validity | Does benchmark predict real-world performance? |
| | Inter-rater reliability | Agreement across human evaluators |
| **Econometrics** | Counterfactual thinking | What would have happened without AI? |
| | Selection bias awareness | Who adopts AI is not random |
| | Heterogeneity analysis | Effects vary across users/contexts |
| **Qualitative Methods** | Understanding "why" | How and why does AI help (or not)? |
| | Contextual inquiry | Observe AI use in natural settings |
| | User perspective | Understand experience from user point of view |
| **Survey Methods** | Questionnaire design | Careful item wording, validated scales |
| | Non-response awareness | Who responds is not random |

### From Risk, Quality, and Assurance

| Discipline | Transferable Concept | Application to AI Evaluation |
|------------|---------------------|------------------------------|
| **Risk Analysis** | Risk-based prioritization | Focus evaluation resources on highest-risk areas |
| | Residual risk | Evaluation reduces but doesn't eliminate risk |
| | Risk monitoring | Ongoing tracking, not just point-in-time |
| **Reliability Engineering** | Failure mode thinking | FMEA adapted for AI |
| | Monitoring over time | Track for degradation |
| | Common cause awareness | AI may have correlated failures |
| **Quality Management** | SPC for monitoring | Control charts for AI metrics over time |
| | Continuous improvement | Iterative improvement of AI use |
| | Root cause orientation | Understand why failures occur |
| **Audit** | Independence principle | Separate evaluator from developer |
| | Evidence standards | Rigor in gathering and assessing evidence |
| | Materiality | Focus on what matters for decisions |
| **Safety Engineering** | Hazard analysis | Systematically identify how AI can cause harm |
| | STPA | System-theoretic analysis of human-AI teams |
| | Safety cases | Structured safety argumentation |

### From Human and Organizational Factors

| Discipline | Transferable Concept | Application to AI Evaluation |
|------------|---------------------|------------------------------|
| **HCI** | Usability methods | Evaluate AI interfaces and interactions |
| | Contextual inquiry | Observe AI use in natural settings |
| | Mental models | Do users understand AI capabilities? |
| **Human Factors** | Trust calibration | Are users appropriately trusting/skeptical? |
| | Automation surprises | AI surprises users frequently |
| | Situation awareness | Human awareness in human-AI teams |
| **Organizational Behavior** | Adoption models | Predict adoption patterns |
| | Absorptive capacity | Organizational ability to learn from AI |
| | Change management | AI deployment as organizational change |
| **JDM** | Bias awareness | Both users and evaluators are biased |
| | Calibration | Do users know when to trust AI? |
| | Decision hygiene | Structure reduces bias and noise |
| **I-O Psychology** | Job analysis | Define what AI should do before evaluating |
| | Structured evaluation | Structure reduces noise and bias |
| | Criterion problem | Defining "good performance" is hard |
| | Work sample testing | Evaluate on realistic tasks |

### From Evaluation and Assessment Traditions

| Discipline | Transferable Concept | Application to AI Evaluation |
|------------|---------------------|------------------------------|
| **Program Evaluation** | Logic models | Make explicit how AI creates value |
| | Implementation fidelity | Is AI actually being used? How? |
| | Developmental evaluation | Appropriate for emerging AI use |
| | Formative evaluation | Focus on learning and improvement |
| **Educational Measurement** | Test security | Benchmark contamination matters |
| | Campbell's Law | Metrics become targets |
| | Standard setting | Determining thresholds requires judgment |
| **Clinical Trials** | Phased approach | Start small, expand based on results |
| | Post-market surveillance | Monitor after deployment |
| | Adaptive designs | Modify based on interim findings |

---

## Principles That Transfer Across Disciplines

Several principles recur across multiple disciplines:

**Structure reduces error**: Structured approaches outperform unstructured across I-O psychology, JDM, audit, and experimental design. Apply structure to AI evaluation.

**Independence matters**: Multiple disciplines emphasize evaluator independence—audit, systems T&E, cybersecurity. Independent AI evaluation is essential for high-stakes decisions.

**Context matters**: HCI, program evaluation, and organizational behavior all emphasize context-dependence. AI effects depend on context.

**Time matters**: IS economics, clinical trials, and human factors recognize temporal dynamics. Short-term and long-term effects may differ.

**Selection biases threaten causal claims**: Econometrics, program evaluation, and survey methods all warn about selection. Who uses AI is not random.

---

## How to Apply Direct Transfers

1. **Identify relevant disciplines** for your evaluation question
2. **Understand the concept** in its home discipline
3. **Apply with minimal modification** to AI context
4. **Document the application** for transparency
5. **Watch for where assumptions strain** (see Section 8.2)

---

*[End of Section 8.1]*
