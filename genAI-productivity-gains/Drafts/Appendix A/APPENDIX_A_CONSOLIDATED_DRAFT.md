# Appendix A: Cross-Disciplinary Foundations for AI Evaluation

## Consolidated Draft Version

---

## Executive Summary

This appendix surveys the disciplines and fields that inform AI evaluation, identifying what transfers directly, what breaks, and what is genuinely novel about evaluating generative AI. The goal is to help readers connect their existing expertise to AI evaluation challenges and understand what established methods offer versus where new approaches are needed.

### Key Takeaways

**What Transfers Directly:**
- **Verification vs. Validation distinction** (Software/Systems T&E): Benchmarks are verification; operational pilots are validation
- **Risk-based prioritization** (Risk Analysis): Focus evaluation resources on highest-risk applications
- **Adversarial evaluation** (Cybersecurity): Red teaming and threat modeling
- **Trust calibration** (Human Factors): Users should be appropriately skeptical, not over- or under-trusting
- **Validity framework** (Experimental Design): Internal, external, and construct validity
- **Structured evaluation** (I-O Psychology): Structure reduces noise and bias
- **Implementation fidelity** (Program Evaluation): Check if AI is actually being used

**What Breaks:**
- **Determinism**: AI is stochastic; same input produces different outputs
- **Bounded outputs**: AI output space is essentially unlimited
- **Clear ground truth**: Many tasks have no single correct answer
- **Stable system**: Models update continuously
- **Predictable failures**: Failures occur at unpredictable jagged boundaries
- **Test security**: Training data may include benchmark items

**What's Genuinely New:**
- Evaluating unbounded output spaces (no prior field has done this)
- The jagged capability frontier (high capability adjacent to surprising failure)
- Specification depth problem (valuable tasks are hard to specify)
- Skill amplification (same system produces vastly different outcomes for different users)
- The "vibes" quality problem (experts recognize quality but struggle to articulate criteria)

### How to Use This Appendix

| If you have background in... | Start with... | Then explore... |
|------------------------------|---------------|-----------------|
| T&E / Defense acquisition | Sections 1, 4, 6 | Section 2 (experimental rigor) |
| Research / Statistics | Sections 2, 6 | Section 7.1 (metrology) |
| Management / Acquisition | Sections 3, 4.4, 7 | Section 5.3 (organizational factors) |
| Human factors | Section 5 | Section 1.3 (autonomous systems) |
| AI Safety | Sections 6.1, 4.5, 1.5 | All sections (this work bridges fields) |

---

## Section Structure

Each discipline section follows a common structure:

1. **Overview**: What the field studies and its relevance to AI evaluation
2. **Core Concepts**: Key ideas and methods
3. **What Transfers**: Approaches that apply directly to AI evaluation
4. **What Breaks**: Where assumptions fail for generative AI
5. **What Can Be Adapted**: Approaches that work with modification
6. **Implications for AI Evaluation**: Practical takeaways
7. **Key References**: Entry points to the literature
8. **Connections**: Links to other sections

---

## Table of Contents

**Section 1: Testing and Evaluation Traditions**
- 1.1 Software Testing and Quality Assurance
- 1.2 Systems Engineering and Hardware T&E
- 1.3 Autonomous Systems Testing and Evaluation
- 1.4 Traditional Machine Learning Evaluation
- 1.5 Cybersecurity Testing and Red Teaming

**Section 2: Experimental and Statistical Methods**
- 2.1 Experimental Design and Analysis
- 2.2 Psychometrics and Measurement Theory
- 2.3 Econometrics and Causal Inference
- 2.4 Qualitative Research Methods
- 2.5 Survey Methodology

**Section 3: Economics and Productivity**
- 3.1 Information Systems Economics
- 3.2 Productivity Measurement and Economics
- 3.3 Cost Analysis and Investment Evaluation

**Section 4: Risk, Quality, and Assurance**
- 4.1 Risk Analysis and Management
- 4.2 Reliability Engineering
- 4.3 Quality Management
- 4.4 Audit and Assurance
- 4.5 Safety Engineering

**Section 5: Human and Organizational Factors**
- 5.1 Human-Computer Interaction and UX Research
- 5.2 Human Factors and Human-Machine Systems
- 5.3 Organizational Behavior and Change Management
- 5.4 Judgment and Decision Making
- 5.5 Industrial-Organizational Psychology

**Section 6: Evaluation and Assessment Traditions**
- 6.1 AI Safety Evaluation (Emerging)
- 6.2 Program Evaluation
- 6.3 Educational Measurement
- 6.4 Clinical Trial Methodology

**Section 7: Standards and Governance**
- 7.1 Metrology (Science of Measurement)
- 7.2 Standards Development and Governance

**Section 8: Synthesis and Crosswalks**
- 8.1 What Transfers Directly
- 8.2 What Breaks for Generative AI
- 8.3 What Requires Adaptation
- 8.4 What's Genuinely New
- 8.5 Terminology Crosswalk
- 8.6 Synthesis: What AI Evaluation Requires
- 8.7 Reader Guide

---

## Cross-Disciplinary Terminology Crosswalk

Different disciplines use different terms for related concepts. This crosswalk helps readers translate between fields:

### Core Evaluation Concepts

| Concept | Software Testing | Systems T&E | Psychometrics | Clinical Trials | AI Evaluation |
|---------|------------------|-------------|---------------|-----------------|---------------|
| "Does it work correctly?" | Verification | DT | - | Efficacy | Benchmark performance |
| "Does it serve the purpose?" | Validation | OT | Criterion validity | Effectiveness | Operational effectiveness |
| "Can I trust the result?" | Test coverage | Confidence level | Reliability | Statistical power | Evaluation confidence |
| "Will it work elsewhere?" | - | External validity | Generalizability | Generalizability | Benchmark-to-real gap |
| "Technical parameter" | Test result | MOP | Score | Endpoint | Benchmark score |
| "Mission outcome" | User acceptance | MOE | Criterion | Clinical benefit | Real-world utility |

### Error and Quality

| Concept | Software | ML | Psychometrics | Quality Mgmt | AI |
|---------|----------|-------|---------------|--------------|-----|
| Wrong output | Defect, Bug | Error | Measurement error | Defect | Hallucination, Error |
| Consistent results | Deterministic | Low variance | Reliable | Capable process | - (AI is stochastic) |
| Unexpected failure | Bug | Out-of-distribution | - | Special cause | Jagged frontier failure |

### Human-AI Interaction

| Concept | Human Factors | JDM | I-O Psych | AI Context |
|---------|---------------|-----|-----------|------------|
| Using AI uncritically | Complacency, Automation bias | Algorithm appreciation | - | Overreliance |
| Not using AI when helpful | Disuse | Algorithm aversion | - | Underutilization |
| Appropriate use | Trust calibration | Calibrated advice-taking | - | Calibrated AI use |
| Skill loss from AI | Skill degradation | - | - | Deskilling |

### Risk and Safety

| Concept | Risk Analysis | Safety Eng | Cybersecurity | AI Context |
|---------|---------------|------------|---------------|------------|
| What could cause harm | Hazard | Hazard | Vulnerability | Harmful capability |
| Likelihood × Consequence | Risk | Risk | Risk | AI risk |
| Who might cause harm | - | - | Threat | Adversarial user |
| Seeking failures | Risk identification | Hazard analysis | Penetration testing | Red teaming |

---

## Key Themes Across Disciplines

### Theme 1: Verification vs. Validation

Nearly every discipline distinguishes between:
- **Technical correctness**: Does it meet specifications? (Software: verification; Systems T&E: DT; Psychometrics: construct validity)
- **Fitness for purpose**: Does it serve users' needs? (Software: validation; Systems T&E: OT; Psychometrics: criterion validity)

For AI, benchmarks primarily address technical correctness. Operational pilots address fitness for purpose. Both are necessary; neither is sufficient.

### Theme 2: Structure Reduces Error

Multiple disciplines find that structured approaches outperform unstructured ones:
- I-O Psychology: Structured interviews beat unstructured
- JDM: Decision hygiene reduces noise
- Audit: Structured evidence gathering improves reliability
- Psychometrics: Standardized tests are more reliable

For AI evaluation: Structured rubrics, defined criteria, and systematic procedures beat "vibes."

### Theme 3: Independence Matters

Disciplines handling consequential judgments emphasize evaluator independence:
- Audit: Auditor independence is fundamental
- Systems T&E: Independent operational testing
- Clinical trials: Independent data monitoring
- Cybersecurity: External red teams find what internal teams miss

For AI: Developer/vendor self-evaluation is insufficient for high-stakes decisions.

### Theme 4: Expect Selection Effects

Social science disciplines warn about selection:
- Econometrics: Who adopts is not random
- Program evaluation: Participants differ from non-participants
- Survey methodology: Responders differ from non-responders

For AI: Who adopts AI, who participates in pilots, who responds to surveys—none are random. Selection threatens causal interpretation.

### Theme 5: Time Matters

Multiple disciplines recognize that effects evolve over time:
- IS Economics: IT productivity paradox—gains take years
- Economics: Learning curves—performance improves with experience
- Human factors: Skill degradation—skills atrophy without use
- Clinical trials: Post-market surveillance catches long-term effects

For AI: Short-term evaluation may miss long-term effects (positive or negative).

### Theme 6: Context Matters

Disciplines emphasize context-dependence:
- HCI: Situated action—behavior is always situated
- Program evaluation: Realist evaluation—what works, for whom, when
- OB: Implementation depends on organizational context
- Human factors: Trust calibration depends on reliability in context

For AI: Context (organization, user, task, stakes) affects outcomes. Average effects may mislead when effects vary by context.

---

## Consolidated Implications for AI Evaluation

Drawing across all disciplines, effective AI evaluation should:

### Before Evaluation: Planning
1. **Define what "good" means** (criterion problem from I-O psych)
2. **Develop a logic model** (program evaluation)—how is AI supposed to create value?
3. **Apply threat modeling** (cybersecurity)—what could go wrong?
4. **Use risk-based prioritization** (risk analysis)—focus on highest-risk areas
5. **Plan comparison conditions** (experimental design)—relative to what?

### During Evaluation: Execution
6. **Use structured approaches** (I-O psych, audit)—reduce noise and bias
7. **Include adversarial evaluation** (cybersecurity)—red team
8. **Test realistic scenarios** (systems T&E)—not just benchmarks
9. **Assess implementation fidelity** (program evaluation)—is AI actually being used?
10. **Evaluate the human-AI team** (human factors)—not just AI capability
11. **Check trust calibration** (human factors)—appropriate reliance?
12. **Apply qualitative methods** (qual research)—understand how and why

### After Evaluation: Interpretation
13. **Quantify uncertainty** (metrology, statistics)—report confidence intervals
14. **Analyze heterogeneity** (econometrics)—who benefits, who doesn't?
15. **Consider selection** (econometrics, survey)—who participated is not random
16. **Acknowledge residual risk** (risk analysis)—evaluation reduces but doesn't eliminate risk
17. **Plan post-deployment monitoring** (clinical trials, quality mgmt)—evaluation doesn't end at deployment

### Cross-Cutting
18. **Maintain independence** (audit, systems T&E)—separate evaluator from developer
19. **Expect evolution** (novel to AI)—systems change during and after evaluation
20. **Recognize criterion validity gap** (psychometrics)—benchmarks may not predict real-world value

---

## Quick Reference: Which Discipline for Which Question?

| Question | Relevant Disciplines | Key Concept |
|----------|---------------------|-------------|
| "Does it work technically?" | Software testing, Traditional ML | Verification, Benchmarks |
| "Does it serve the mission?" | Systems T&E, Program evaluation | Validation, Effectiveness |
| "Can we trust these results?" | Psychometrics, Experimental design | Reliability, Validity |
| "Will results generalize?" | Experimental design, Psychometrics | External validity, Criterion validity |
| "What's the causal effect?" | Econometrics, Experimental design | RCT, Quasi-experiments |
| "Why does it work (or not)?" | Qualitative methods, HCI | Contextual inquiry |
| "How do users experience it?" | HCI, Human factors | Usability, Trust |
| "Is it safe?" | Safety engineering, AI safety | Hazard analysis, Safety cases |
| "What could go wrong?" | Risk analysis, Cybersecurity | Threat modeling, Red teaming |
| "Is quality maintained?" | Quality management | SPC, Control charts |
| "Is evaluation independent?" | Audit | Independence |
| "What's the ROI?" | Economics | CBA, TCO |
| "Will the org adopt it?" | Organizational behavior | TAM, Change management |
| "Are we measuring real capability?" | Metrology, Psychometrics | Traceability, Construct validity |

---

## Individual Section Drafts

All drafts are located in the `drafts/` folder. Each section has separate subsection files following the pattern used in Section 1:

**Section 1: Testing and Evaluation Traditions**
- `appendix_a_section_1_1_draft.md` - Software Testing and Quality Assurance
- `appendix_a_section_1_2_draft.md` - Systems Engineering and Hardware T&E
- `appendix_a_section_1_3_draft.md` - Autonomous Systems Testing and Evaluation
- `appendix_a_section_1_4_draft.md` - Traditional Machine Learning Evaluation
- `appendix_a_section_1_5_draft.md` - Cybersecurity Testing and Red Teaming

**Section 2: Experimental and Statistical Methods**
- `appendix_a_section_2_1_draft.md` - Experimental Design and Analysis
- `appendix_a_section_2_2_draft.md` - Psychometrics and Measurement Theory
- `appendix_a_section_2_3_draft.md` - Econometrics and Causal Inference
- `appendix_a_section_2_4_draft.md` - Qualitative Research Methods
- `appendix_a_section_2_5_draft.md` - Survey Methodology

**Section 3: Economics and Productivity**
- `appendix_a_section_3_1_draft.md` - Information Systems Economics
- `appendix_a_section_3_2_draft.md` - Productivity Measurement and Economics
- `appendix_a_section_3_3_draft.md` - Cost Analysis and Investment Evaluation

**Section 4: Risk, Quality, and Assurance**
- `appendix_a_section_4_1_draft.md` - Risk Analysis and Management
- `appendix_a_section_4_2_draft.md` - Reliability Engineering
- `appendix_a_section_4_3_draft.md` - Quality Management
- `appendix_a_section_4_4_draft.md` - Audit and Assurance
- `appendix_a_section_4_5_draft.md` - Safety Engineering

**Section 5: Human and Organizational Factors**
- `appendix_a_section_5_1_draft.md` - Human-Computer Interaction and UX Research
- `appendix_a_section_5_2_draft.md` - Human Factors and Human-Machine Systems
- `appendix_a_section_5_3_draft.md` - Organizational Behavior and Change Management
- `appendix_a_section_5_4_draft.md` - Judgment and Decision Making
- `appendix_a_section_5_5_draft.md` - Industrial-Organizational Psychology

**Section 6: Evaluation and Assessment Traditions**
- `appendix_a_section_6_1_draft.md` - AI Safety Evaluation (Emerging)
- `appendix_a_section_6_2_draft.md` - Program Evaluation
- `appendix_a_section_6_3_draft.md` - Educational Measurement
- `appendix_a_section_6_4_draft.md` - Clinical Trial Methodology

**Section 7: Standards and Governance**
- `appendix_a_section_7_1_draft.md` - Metrology (Science of Measurement)
- `appendix_a_section_7_2_draft.md` - Standards Development and Governance

**Section 8: Synthesis and Crosswalks**
- `appendix_a_section_8_1_draft.md` - What Transfers Directly
- `appendix_a_section_8_2_draft.md` - What Breaks for Generative AI
- `appendix_a_section_8_3_draft.md` - What Requires Adaptation
- `appendix_a_section_8_4_draft.md` - What's Genuinely New
- `appendix_a_section_8_5_draft.md` - Terminology Crosswalk
- `appendix_a_section_8_6_draft.md` - Synthesis: What AI Evaluation Requires
- `appendix_a_section_8_7_draft.md` - Reader Guide

**Legacy combined drafts** (retained for reference):
- `appendix_a_section_2_draft.md` through `appendix_a_section_8_draft.md`

---

## Complete Bibliography (to be compiled)

References from all sections should be compiled into a master bibliography for the final version.

---

*Draft version - December 2025 (updated)*
*Individual subsection drafts now available for all sections (1-8)*
