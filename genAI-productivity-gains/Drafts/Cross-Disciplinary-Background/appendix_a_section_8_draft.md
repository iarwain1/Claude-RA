# Appendix A, Section 8: Synthesis and Crosswalks

## Overview

This section synthesizes insights across the disciplines covered in this appendix, identifies what transfers to AI evaluation, what breaks, and what is genuinely new. It also provides "crosswalks"—mappings of equivalent or related concepts across disciplines that may help readers connect familiar concepts to new ones.

---

## Section 8.1: What Transfers Directly

The following concepts transfer directly from existing disciplines to AI evaluation and should be applied with minimal modification:

| Discipline | Key Transferable Concepts | Application to AI Evaluation |
|------------|--------------------------|------------------------------|
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
| **Risk Analysis** | Risk-based prioritization | Focus evaluation on highest-risk areas |
| | Residual risk | Evaluation reduces but doesn't eliminate risk |
| **Quality Management** | SPC for monitoring | Control charts for AI metrics over time |
| | Continuous improvement | Iterative improvement of AI use |
| **Audit** | Independence principle | Separate evaluator from developer |
| | Evidence standards | Rigor in gathering and assessing evidence |
| **Safety Engineering** | Hazard analysis | Systematically identify how AI can cause harm |
| | STPA | System-theoretic analysis of human-AI teams |
| **Human Factors** | Trust calibration | Are users appropriately trusting/skeptical? |
| | Automation surprises | AI surprises users frequently |
| | Situation awareness | Human awareness in human-AI teams |
| **I-O Psychology** | Structured evaluation | Structure reduces noise and bias |
| | Criterion problem | "Good performance" is hard to define |
| | Work sample testing | Evaluate on realistic tasks |
| **Program Evaluation** | Logic models | Make explicit how AI creates value |
| | Implementation fidelity | Is AI actually being used? How? |
| | Developmental evaluation | Appropriate for emerging AI use |
| **Clinical Trials** | Phased approach | Start small, expand based on results |
| | Post-market surveillance | Monitor after deployment |

---

## Section 8.2: What Breaks for Generative AI

Fundamental assumptions from traditional disciplines that fail for generative AI:

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

## Section 8.3: What Requires Adaptation

Concepts that transfer with significant modification:

| Original Concept | Discipline | Required Adaptation |
|-----------------|------------|---------------------|
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

---

## Section 8.4: What's Genuinely New

Some AI evaluation challenges don't have good precedents from existing disciplines:

### 1. Unbounded Output Evaluation

No prior field has evaluated systems that produce outputs from an essentially unlimited space. Classification has k classes; regression has one number; traditional software has specified output formats. Language models produce arbitrary text. The entire machinery of enumerable-output evaluation (confusion matrices, classification metrics, output verification) doesn't apply.

### 2. Jagged Capability Frontier

The pattern of high capability immediately adjacent to surprising failure is unprecedented. Traditional systems have understood capability boundaries—they work within specification and don't work outside it. AI exhibits high capability on some instances while failing on nearly identical instances. This "jaggedness" means evaluation must cover capability more densely than previous approaches assumed.

### 3. Specification Depth Problem

Much of AI's value lies in handling tasks that couldn't be specified precisely enough to automate traditionally. But if we could specify the task precisely, we could automate it without AI. This creates a fundamental tension: the tasks where AI is most valuable are the tasks hardest to specify—and therefore hardest to evaluate.

### 4. Benchmark Contamination Via Training

Traditional test security prevents examinees from seeing test items in advance. AI training may include benchmark items in training corpora—not through intentional cheating but through internet-scale data collection. This "data contamination" inflates benchmark performance in ways that don't reflect true capability, creating a novel threat to evaluation validity that doesn't have direct precedent.

### 5. Continuous Evolution During Deployment

Most evaluation paradigms assume a stable system: test it, then deploy it. AI systems may change continuously—through model updates, fine-tuning, or prompt engineering—without clear version boundaries. The entity evaluated may differ from the entity deployed, and the entity deployed today may differ from the entity deployed tomorrow.

### 6. Skill Amplification

The same AI system produces dramatically different outcomes for different users. A novice may barely use AI capability; an expert may achieve remarkable results. This "skill amplification" means system capability is entangled with user skill in ways that complicate evaluation. Traditional automation provides more uniform augmentation.

### 7. The "Vibes" Quality Problem

For many AI tasks, experts recognize quality when they see it but struggle to articulate criteria precisely enough for reliable measurement. This isn't unique to AI, but the breadth of AI applications (writing, coding, analysis, conversation) across so many quality dimensions makes it particularly acute. How do you systematically evaluate something when "you know it when you see it" is the best quality criterion available?

---

## Section 8.5: Terminology Crosswalk

Different disciplines use different terms for similar or related concepts. This crosswalk maps common concepts across disciplines to help readers connect familiar terminology to unfamiliar fields:

### Accuracy and Error

| Discipline | Term | Meaning |
|------------|------|---------|
| Traditional ML | Accuracy | Proportion of correct predictions |
| Traditional ML | Error rate | Proportion of incorrect predictions |
| Metrology | Accuracy | Closeness to true value (combining trueness and precision) |
| Metrology | Trueness | Systematic closeness to true value |
| Metrology | Precision | Repeatability of measurements |
| Software Testing | Defect | Software behavior contrary to specification |
| Quality Management | Defect | Unit that doesn't conform to specifications |

### Reliability and Consistency

| Discipline | Term | Meaning |
|------------|------|---------|
| Psychometrics | Reliability | Consistency of measurement across occasions, raters, items |
| Reliability Engineering | Reliability | Probability of successful operation over time |
| Software | Reliability | Probability of failure-free operation |
| Quality Management | Consistency | Producing similar outputs over time |

### Validity and Effectiveness

| Discipline | Term | Meaning |
|------------|------|---------|
| Psychometrics | Validity | Whether measure assesses intended construct |
| Experimental Design | Validity | Whether conclusions are warranted (internal, external, construct) |
| Systems T&E | Effectiveness | Degree to which system accomplishes mission |
| Psychometrics | Criterion validity | Whether measure predicts relevant outcomes |
| Systems T&E | MOE | Measure of Effectiveness—mission outcome metrics |

### Performance and Capability

| Discipline | Term | Meaning |
|------------|------|---------|
| Systems T&E | Performance | Technical parameter values (speed, accuracy, etc.) |
| Systems T&E | MOP | Measure of Performance—technical parameters |
| I-O Psychology | Performance | Work output quality and quantity |
| AI Safety | Capability | What the model can do (including dangerous capabilities) |
| AI Evaluation | Benchmark score | Performance on standardized evaluation |

### Testing Types

| Discipline | Term | Meaning |
|------------|------|---------|
| Software Testing | Unit testing | Testing individual components |
| Software Testing | Integration testing | Testing component interactions |
| Software Testing | System testing | Testing complete system |
| Systems T&E | Developmental testing (DT) | Testing during development |
| Systems T&E | Operational testing (OT) | Testing under realistic conditions |
| Clinical Trials | Phase I, II, III | Staged testing with increasing scale and rigor |

### Risk and Hazard

| Discipline | Term | Meaning |
|------------|------|---------|
| Risk Analysis | Risk | Probability × Consequence |
| Risk Analysis | Hazard | Condition that could cause harm |
| Safety Engineering | Hazard | Condition that could lead to accident |
| Safety Engineering | Risk | Function of hazard, exposure, and consequence |
| Cybersecurity | Threat | Potential source of harm |
| Cybersecurity | Vulnerability | Weakness that can be exploited |

### Independence and Separation

| Discipline | Term | Meaning |
|------------|------|---------|
| Audit | Independence | Auditor separate from entity being audited |
| Systems T&E | Independent evaluation | Evaluation by party independent of developer |
| Experimental Design | Random assignment | Unpredictable assignment to conditions |
| Experimental Design | Blinding | Hiding condition assignment from participants/researchers |

### Quality and Assurance

| Discipline | Term | Meaning |
|------------|------|---------|
| Quality Management | Quality | Conformance to requirements |
| Quality Management | Assurance | Confidence that quality requirements will be met |
| Audit | Assurance | Confidence that claims are accurate |
| Safety Engineering | Safety case | Structured argument that system is safe |
| AI Safety | Safety case | Structured argument for AI safety |

### Human-AI Concepts

| Discipline | Term | Meaning |
|------------|------|---------|
| Human Factors | Trust calibration | Matching trust to actual system reliability |
| Human Factors | Automation bias | Uncritical acceptance of automation |
| JDM | Algorithm aversion | Resistance to algorithmic advice |
| JDM | Algorithm appreciation | Over-reliance on algorithmic advice |
| Human Factors | Complacency | Inappropriate trust in automation |
| Human Factors | Situation awareness | Understanding of current state and future trajectory |

### Evaluation Approaches

| Discipline | Term | Meaning |
|------------|------|---------|
| Program Evaluation | Formative evaluation | Evaluation to improve during implementation |
| Program Evaluation | Summative evaluation | Evaluation to judge overall effectiveness |
| Program Evaluation | Process evaluation | Did intervention occur as planned? |
| Program Evaluation | Outcome evaluation | Did desired effects occur? |
| Clinical Trials | Efficacy | Effect under ideal conditions |
| Clinical Trials | Effectiveness | Effect under real-world conditions |

---

## Section 8.6: Synthesis: What AI Evaluation Requires

Drawing across all disciplines, effective AI evaluation requires:

### From Testing Traditions
- **Systematic approach**: Planned, comprehensive evaluation rather than ad hoc probing
- **V&V distinction**: Separate technical verification from fitness-for-purpose validation
- **DT/OT paradigm**: Lab evaluation precedes and differs from operational evaluation
- **Adversarial orientation**: Actively try to find failures, not just confirm successes
- **Scenario-based coverage**: Systematic scenario coverage since input space is unbounded

### From Statistical Methods
- **Validity framework**: Rigorous attention to internal, external, construct validity
- **Appropriate comparison**: Clear baseline/control conditions
- **Causal discipline**: Distinguish correlation from causation
- **Heterogeneity awareness**: Average effects may mask important variation
- **Qualitative complement**: Numbers need qualitative understanding of how and why

### From Economics
- **Productivity paradox awareness**: Don't expect immediate measured gains
- **Complementary investments**: AI benefits require organizational change
- **Full cost accounting**: Include hidden and indirect costs
- **Time horizons**: Short-run may differ from long-run

### From Risk and Quality
- **Risk-based prioritization**: Focus resources on highest-risk applications
- **Continuous monitoring**: Don't rely solely on pre-deployment evaluation
- **Residual risk acceptance**: Evaluation reduces but doesn't eliminate risk
- **Independence**: Separate evaluator from developer for high stakes

### From Human and Organizational Factors
- **Human-AI team evaluation**: Assess the team, not just the AI
- **Trust calibration**: Evaluate whether users trust appropriately
- **Organizational context**: Evaluation results depend on organizational factors
- **Implementation fidelity**: Check whether AI is actually being used

### From Evaluation Traditions
- **Logic models**: Make explicit how AI is supposed to create value
- **Developmental approach**: Appropriate when learning what works
- **Post-deployment surveillance**: Continue evaluation after deployment

### Novel Requirements for AI
- **Benchmark integrity**: Protect against contamination
- **Capability coverage**: Dense coverage of jagged frontier
- **Output evaluation**: Methods for unbounded, open-ended outputs
- **Evolution accommodation**: Evaluation design that handles system change
- **Skill interaction**: Understanding how user skill affects outcomes
- **Quality articulation**: Methods for the "vibes" problem

---

## Section 8.7: Reader Guide

**For T&E Professionals**:
Start with Sections 1 (Testing Traditions), 4 (Risk, Quality, Assurance), and 6 (Evaluation Traditions). These connect most directly to T&E backgrounds. Then explore Section 2 (Experimental Methods) for statistical rigor.

**For Researchers/Methodologists**:
Start with Section 2 (Experimental and Statistical Methods) and Section 6 (Evaluation Traditions). Then explore Section 7.1 (Metrology) for measurement foundations.

**For Acquisition/Management Professionals**:
Start with Section 3 (Economics and Productivity), Section 4.4 (Audit), and Section 7.2 (Standards). Then explore Section 5.3 (Organizational Behavior) for implementation factors.

**For Human Factors Specialists**:
Start with Section 5 (Human and Organizational Factors) and Section 5.1-5.2 (HCI and Human Factors). Then explore Section 1.3 (Autonomous Systems) for AI-specific human factors.

**For AI Safety Researchers**:
Start with Section 6.1 (AI Safety Evaluation), Section 4.5 (Safety Engineering), and Section 1.5 (Cybersecurity). Much of this work is building the bridges covered throughout this appendix.

---

*[End of Section 8]*
