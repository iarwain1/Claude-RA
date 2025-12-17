# Cross-Disciplinary Background: Measuring Productivity Gains From Generative AI

---

## Purpose and How to Use This Document

This document surveys disciplines that inform AI evaluation. It helps readers:

1. **Connect existing expertise** to AI evaluation challenges
2. **Find entry points** into unfamiliar fields
3. **Identify what's genuinely novel** about evaluating generative AI

### Structure

Each discipline section covers:
- **Overview**: What the field studies and its relevance to AI
- **Core Concepts**: Key ideas and methods
- **AI Applicability**: What transfers, what breaks, and what requires adaptation
- **Key References**: Entry points to the literature

### Reading Paths

| Your Background | Start With | Then Explore |
|-----------------|------------|--------------|
| T&E / Defense acquisition | Sections 1, 4, 6 | Section 2 (experimental rigor) |
| Research / Statistics | Sections 2, 6 | Section 7.1 (metrology) |
| Management / Acquisition | Sections 3, 4.4, 7 | Section 5.3 (organizational factors) |
| Human factors | Section 5 | Section 1.3 (autonomous systems) |
| AI Safety | Sections 6.1, 4.5, 1.5 | All sections |

---

## Table of Contents

**Section 1: Testing and Evaluation Traditions**
- 1.1 Software Testing and Quality Assurance
- 1.2 Systems Engineering and Hardware T&E
- 1.3 Autonomous Systems Testing
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
- 3.2 Productivity Measurement
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
- 8.6 Synthesis
- 8.7 Reader Guide

---

# Section 1: Testing and Evaluation Traditions

## 1.1 Software Testing and Quality Assurance

### Overview

Software testing systematically evaluates software to identify defects, verify requirements, and validate fitness for purpose. The field has grappled for decades with a challenge familiar to AI evaluation: achieving confidence in system behavior despite the impossibility of exhaustive testing.

### Core Concepts

**Verification vs. Validation**

- **Verification**: "Are we building it right?" Does implementation match specification?
- **Validation**: "Are we building the right thing?" Does the system meet user needs?

A system can pass all verification tests while failing validation. This distinction maps directly to AI evaluation: benchmarks are verification (checking performance on specified tasks), while the harder question is validation (does benchmark performance translate to real-world utility?). The benchmark-utility gap is fundamentally a verification-validation gap.

**Test Coverage**

Coverage metrics assess how thoroughly tests exercise code:
- **Statement coverage**: Every line executed at least once
- **Branch coverage**: Every decision point evaluated both ways
- **Path coverage**: Every execution path tested

For AI, there's no finite set of code paths to enumerate. Yet coverage thinking remains valuable: we should exercise systems across diverse conditions and worry about unexplored regions of capability space. The jagged capability frontier—where AI fails unexpectedly on tasks similar to ones it handles well—is precisely what coverage-oriented thinking should catch.

**Test Oracles**

A test oracle determines whether a test passed or failed. For some tests, oracles are simple (does the function return 42?). For others, they're complex (is this output "good"?).

AI evaluation faces the oracle problem in its most severe form. For open-ended tasks—writing, coding, question answering—there's no single correct output. The "vibes" problem (knowing good output when you see it but struggling to articulate criteria) is an oracle problem.

**Regression Testing**

Regression testing re-runs tests after changes to ensure previously working functionality still works. It assumes:
1. Determinism (same input → same output)
2. Stable definition of "correct"
3. Ability to detect meaningful changes

AI violates all three. Models are stochastic, providers update systems continuously, and determining whether output has meaningfully changed is itself difficult. Still, the regression mindset—monitoring for performance changes over time—remains valuable.

**Boundary Testing**

Testing at boundaries (edges of valid input ranges, state transitions, capacity limits) reveals defects efficiently. For AI, boundaries are less predictable—the jagged capability frontier means failures don't cluster at definable boundaries. But boundary thinking still applies: test edges of claimed capabilities, transitions between task types, and limits of context or complexity.

**Adversarial Testing**

Mutation testing and fault injection deliberately introduce problems to verify tests can detect them. The AI analog is red teaming: actively trying to make the system fail rather than confirming it works on expected inputs.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| Verification/validation distinction | Determinism assumption | Statistical regression testing (distribution shifts, not exact outputs) |
| Test planning discipline | Enumerable input/output spaces | Metamorphic testing (test relationships between outputs) |
| Coverage thinking (diversity) | Clear oracles | Property-based testing (outputs satisfy constraints) |
| Regression mindset | Fault isolation | Differential testing (compare across models/versions) |
| Adversarial orientation | System stability | |

### Key References

- Beizer, B. (1990). *Software Testing Techniques* (2nd ed.)
- Myers, G.J., et al. (2011). *The Art of Software Testing* (3rd ed.)
- Ammann, P., & Offutt, J. (2016). *Introduction to Software Testing* (2nd ed.)
- Segura, S., et al. (2016). "A Survey on Metamorphic Testing." *IEEE TSE*
- Ribeiro, M.T., et al. (2020). "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList." *ACL*

---

## 1.2 Systems Engineering and Hardware T&E

### Overview

Military T&E represents one of the most mature frameworks for assessing whether systems will perform as needed in operational conditions. The central insight: demonstrating capability in controlled conditions is not the same as demonstrating it will work in combat. This wisdom applies with full force to AI.

### Core Concepts

**Developmental Testing (DT) vs. Operational Testing (OT)**

- **DT**: Conducted during development by developers. Supports engineering decisions, verifies specifications, reduces technical risk. Controlled environments, expert operators.
- **OT**: Conducted later by independent organizations. Assesses effectiveness and suitability for representative users in realistic conditions.

The DT→OT progression embodies a crucial insight: performance in controlled conditions doesn't guarantee performance in the field. For AI, benchmarks are DT; operational evaluation with representative users doing genuine work is OT. The benchmark-utility gap exists because we too often stop at DT.

**Measures of Performance (MOPs) vs. Measures of Effectiveness (MOEs)**

- **MOPs**: Technical characteristics (speed, accuracy, capacity)
- **MOEs**: Mission accomplishment (probability of mission success, targets destroyed)

Good MOPs don't guarantee good MOEs. AI benchmarks are MOPs; the MOE for a coding assistant is whether developers actually produce better software faster, not its HumanEval score.

**Suitability**

Beyond effectiveness: Is the system usable, maintainable, supportable?
- **Reliability**: Consistent performance over time
- **Maintainability**: Can it be updated and serviced?
- **Human factors**: Can typical users operate it effectively?
- **Interoperability**: Does it work with existing systems?

For AI, suitability includes: reliability across varied conditions, maintainability as requirements evolve, supportability with available expertise, and human factors in human-AI teaming.

**Test and Evaluation Master Plan (TEMP)**

Major acquisitions require comprehensive test planning: what will be tested, how, when, and to what criteria. Most AI acquisitions lack anything resembling a TEMP—evaluation is ad hoc, relying on vendor benchmarks and brief demonstrations.

**M&S Accreditation**

Not everything can be tested live. Modeling and simulation accreditation determines whether a simulation is adequate for a specific purpose. AI benchmarks are simulations of real tasks. Accreditation thinking asks: For what purposes is this benchmark suitable? What decisions should it inform? What are its limitations?

**Independent Operational Test Organizations**

Independent evaluators (like DOT&E) are separate from developers because developers have natural incentives to present systems favorably. For AI, vendor-provided evidence should be supplemented with independent assessment.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| DT/OT paradigm | Stable system configuration | Continuous monitoring (systems change during deployment) |
| MOP/MOE distinction | Physical test environments | Information environment characterization |
| Suitability concept | Failure mode predictability | Scenario-based reliability assessment |
| Test planning discipline | Requirements stability | Agile evaluation for emergent capabilities |
| M&S accreditation thinking | Mature test infrastructure | New evaluation infrastructure |
| Independent evaluation | Reproducibility | Statistical evaluation evidence |

### Key References

- DoD Directive 5000.01 and DoDI 5000.02 (acquisition policy)
- DoDI 5000.89 (T&E policy)
- INCOSE Systems Engineering Handbook (4th ed., 2015)
- Blanchard, B.S., & Fabrycky, W.J. (2010). *Systems Engineering and Analysis* (5th ed.)
- NIST AI Risk Management Framework

---

## 1.3 Autonomous Systems Testing

### Overview

Autonomous systems—self-driving vehicles, autonomous drones, robots—represent the closest existing paradigm to generative AI evaluation. Both involve AI making decisions under uncertainty in conditions that can't be fully anticipated. But important differences exist: autonomous systems operate in physical space with observable failures, while generative AI operates in information space with subtle failures that propagate through human decisions.

### Core Concepts

**Levels of Autonomy**

SAE J3016 defines automation levels from 0 (no automation) to 5 (full automation). Different levels require different evaluation:
- Lower autonomy (human reviews suggestions): evaluate human oversight effectiveness
- Higher autonomy (minimal oversight): comprehensive capability testing
- Handoff points (automation ↔ human): specific evaluation attention

Generative AI doesn't map neatly to these levels—the same coding assistant might be "Level 2" for routine completion but "Level 4" for automated workflows. The underlying questions remain relevant: How much is the human in the loop? What happens when monitoring fails?

**Operational Design Domain (ODD)**

ODD defines conditions under which a system is designed to operate: geographic areas, weather, road types, speed ranges. Performance claims apply only within the ODD.

For AI, ODD thinking asks: What tasks, conditions, user populations, and use patterns is this AI designed for? Current AI deployments rarely make ODD-like specifications explicit. Making the operational envelope explicit—and acknowledging uncertainty outside it—would improve both evaluation and deployment.

**Sim-to-Real Gap**

Simulation performance doesn't guarantee real-world performance. The sim-to-real gap drives strategies like domain randomization, progressive testing, and scenario validation.

The AI analog is the benchmark-to-real gap. Benchmarks simplify and standardize diverse, contextual activities. Strategies for managing this: diverse testing conditions, progressive deployment (benchmarks → controlled studies → pilots), and validation against operational performance.

**Edge Cases and Scenario-Based Testing**

Testing for rare, challenging situations uses scenario libraries, systematic scenario generation, adversarial scenarios, and importance sampling (focus on high-risk scenarios).

For AI, the scenario space is infinite and continuous. Still, scenario-based thinking has value: test different task types and difficulty levels, probe capability boundaries, include adversarial inputs.

**Safety Cases**

A safety case is a structured argument, supported by evidence, that a system is acceptably safe:
- **Claims**: Specific assertions about safety
- **Evidence**: Data, test results, analysis
- **Argument**: Logic linking evidence to claims
- **Context**: Assumptions and limitations

Safety cases make reasoning explicit and contestable. They're increasingly being adapted for AI systems.

**Human Supervisory Control**

Even highly automated systems involve human oversight. Research has identified challenges:
- **Vigilance**: Humans are poor at sustained monitoring
- **Mode confusion**: Uncertainty about system state
- **Skill degradation**: Atrophied skills if automation fails
- **Automation surprises**: Unexpected system behavior
- **Trust calibration**: Appropriate trust given varying reliability

All directly relevant to human-AI teaming with generative AI.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| Levels of autonomy thinking | Physical vs. information environments | Autonomy levels for information tasks |
| ODD discipline | Definable operating envelopes | Approximate capability boundaries |
| Sim-to-real gap awareness | Observable failures | Subtle failure detection |
| Scenario-based testing | Failure mode predictability | Scenario libraries for AI |
| Safety case methodology | Formal verification scope | AI-specific safety arguments |
| Human supervisory control research | Physical control interfaces | Conversational oversight interfaces |
| Runtime monitoring | Development stability | Continuous monitoring infrastructure |

### Key References

- SAE J3016 (Driving Automation Taxonomy)
- Kalra, N., & Paddock, S.M. (2016). "Driving to Safety." *Transportation Research Part A*
- UL 4600 (Autonomous Products Safety)
- ISO 21448 (SOTIF)
- Endsley, M.R. (2017). "Autonomous Driving Systems: A Preliminary Naturalistic Study." *JCEDM*

---

## 1.4 Traditional Machine Learning Evaluation

### Overview

Before large language models, ML evaluation developed sophisticated methods for assessing predictive models—classification, regression, ranking. These methods assume tasks have clear correct answers, performance can be measured automatically, output spaces are bounded, and test data matches deployment distributions. When these assumptions hold, evaluation is precise and scalable. When they don't—as with generative AI—traditional approaches break down.

### Core Concepts

**The Hold-Out Principle**

Don't evaluate on training data. Partition into training, validation, and test sets. The test set remains untouched until final evaluation—if test performance influences modeling decisions, it becomes contaminated.

For AI, benchmark contamination (models trained on benchmark data) is the equivalent of evaluating on training data. It produces inflated scores that don't reflect genuine capability.

**Performance Metrics**

Classification metrics (accuracy, precision, recall, F1, AUC-ROC), regression metrics (MSE, MAE, R²), ranking metrics (Precision@k, MAP, NDCG). Choice of metric matters: a model can excel on one while failing on another.

For generative AI, the relationship between metrics and what matters is unclear. What's the "precision" of a language model?

**Confusion Matrices and Error Analysis**

Confusion matrices reveal how models err, not just how often. Error analysis examines individual failures for patterns. More important for generative AI (aggregate metrics are less informative) but also harder (determining whether output is an "error" requires judgment).

**Generalization and Overfitting**

The core concern: will the model perform on new data, not just training data? Overfitting means learning patterns specific to training data that don't generalize.

For AI, the benchmark-to-real gap is partly a generalization gap: models may perform well on benchmark-style tasks without acquiring capabilities that transfer to real use.

**Fairness and Bias**

Group fairness metrics (demographic parity, equalized odds, calibration), individual fairness, disparate impact analysis. Models can encode and amplify societal biases. These concerns apply with full force to generative AI—arguably more so, given breadth of applications.

**Distribution Shift**

Test data rarely matches training distribution perfectly. Covariate shift (input distribution changes), label shift (output distribution changes), concept drift (relationships change over time), domain shift (deployment differs from training).

For AI, distribution shift is pervasive: benchmarks don't match real-world task distributions.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| Hold-out principle (benchmark integrity) | Bounded output space | Output evaluation methods for unbounded space |
| Multiple metrics | Clear ground truth | Multi-dimensional quality assessment |
| Error analysis discipline | Automated evaluation | Human judgment integration |
| Baseline comparisons | Task specificity | General-purpose evaluation frameworks |
| Fairness evaluation | Static models | Continuous fairness monitoring |
| Distribution shift awareness | IID test data | Cross-distribution robustness testing |

### Key References

- Hastie, T., et al. (2009). *The Elements of Statistical Learning* (2nd ed.)
- Barocas, S., et al. (2019). *Fairness and Machine Learning* (fairmlbook.org)
- Liang, P., et al. (2022). "Holistic Evaluation of Language Models (HELM)"
- Mitchell, M., et al. (2019). "Model Cards for Model Reporting." *FAT*

---

## 1.5 Cybersecurity Testing and Red Teaming

### Overview

Cybersecurity testing has developed an adversarial evaluation culture: the goal is not confirming systems work under expected conditions but discovering how they can be made to fail. Red teaming, penetration testing, and threat modeling all embody this mindset—assume adversaries exist, assume you've missed something, design for resilience. For AI evaluation, cybersecurity provides both methods and mindset.

### Core Concepts

**Red Team / Blue Team / Purple Team**

- **Red teams**: Authorized attackers finding and exploiting vulnerabilities
- **Blue teams**: Defenders protecting systems
- **Purple teams**: Facilitating learning between red and blue

AI red teaming—adversarial probing for harmful outputs, jailbreaking, systematic exploration of failure modes—has been directly adopted from this model.

**Penetration Testing**

Structured methodology: scoping → reconnaissance → vulnerability identification → exploitation → post-exploitation → reporting. Bounded and authorized. The methodology offers a template for AI evaluation: scope what's being tested, understand the system, identify potential weaknesses, demonstrate failures, document findings.

**Threat Modeling**

Systematic threat identification before testing: Who might attack? What are their goals? What methods might they use? What needs protection?

For AI: Who might try to make AI behave badly? What might they try to achieve? Threat modeling prioritizes red team activities and evaluation resources.

**Bug Bounties and Responsible Disclosure**

External researchers find vulnerabilities for rewards. Responsible disclosure coordinates reporting to allow fixes before public disclosure.

Bug bounty models are emerging for AI, though defining what counts as an AI "vulnerability" is fuzzier than for security.

**Zero-Day Thinking**

Unknown vulnerabilities can't be defended against directly. Responses include defense in depth, anomaly detection, assume-breach design, and prioritizing resilience over prevention.

For AI, this is essential: the jagged capability frontier means unexpected failures are inevitable. Design for detection, containment, and recovery, not just prevention.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| Adversarial mindset | Clear vulnerability definitions | Fuzzy failure characterization |
| Red teaming methodology | Exploit reproducibility | Probabilistic failure analysis |
| Threat modeling | Patching vulnerabilities | Mitigation layers vs. fixes |
| Bug bounty models | Formal security properties | AI vulnerability taxonomies |
| Defense in depth | Clear attack surface | Assume-failure design |
| Zero-day awareness | | |

### Key References

- NIST SP 800-115 (Security Testing Guide)
- PTES (Penetration Testing Execution Standard)
- MITRE ATT&CK Framework
- Shostack, A. (2014). *Threat Modeling: Designing for Security*
- Ganguli, D., et al. (2022). "Red Teaming Language Models to Reduce Harms"

---

# Section 2: Experimental and Statistical Methods

## 2.1 Experimental Design and Analysis

### Overview

Experimental design structures studies to support valid causal inferences. "Does AI improve productivity?" is a causal question—observing that AI users perform better doesn't establish that AI caused the improvement. Rigorous experimental design provides frameworks for moving from correlation to causation.

### Core Concepts

**Randomized Controlled Trials (RCTs)**

Randomly assign units to treatment and control. Random assignment ensures groups are comparable on all characteristics—observed and unobserved—except the treatment. Differences in outcomes can be attributed to the treatment.

For AI: randomly assign workers to use AI versus traditional methods, then compare outcomes. Without randomization, selection bias (AI users differ from non-users), confounding, and reverse causation all remain plausible.

**Validity Types**

- **Internal validity**: Can we attribute effects to the treatment?
- **External validity**: Do findings generalize beyond the study?
- **Construct validity**: Are we measuring what we intend?
- **Statistical conclusion validity**: Are statistical inferences appropriate?

These often trade off: tight laboratory control may sacrifice external validity.

**Control Conditions**

- **No-treatment control**: AI vs. nothing
- **Active control**: AI vs. alternative tools
- **Placebo control**: AI vs. belief you're using AI (often impractical)
- **Within-subjects**: Same people in both conditions (order effects)
- **Between-subjects**: Different people (requires larger samples)

Comparison condition choice determines what claims can be supported.

**Confounding and Bias**

- **Selection bias**: Treatment groups differ systematically
- **Attrition bias**: Differential dropout
- **Experimenter effects**: Expectations influence outcomes
- **Demand characteristics**: Participants guess hypothesis
- **Hawthorne effects**: Being observed changes behavior

**Statistical Power**

Power analysis determines sample size needed to detect effects. Underpowered studies miss real effects; multiple comparisons find spurious ones. Pre-registration constrains researcher flexibility.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| Validity framework | Treatment stability (AI changes during study) | Shorter evaluation windows, version tracking |
| Control condition thinking | Blinding (users know they're using AI) | Active control comparisons |
| Bias awareness | Standardized treatment (AI use varies by user) | Characterize usage patterns |
| Power analysis | Stable outcomes (AI changes work itself) | Multi-dimensional outcome assessment |
| Pre-registration | Effect size stability | Exploratory → confirmatory phasing |

### Key References

- Shadish, W.R., et al. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*
- Gerber, A.S., & Green, D.P. (2012). *Field Experiments*
- Simmons, J.P., et al. (2011). "False-Positive Psychology." *Psychological Science*

---

## 2.2 Psychometrics and Measurement Theory

### Overview

Psychometrics asks what it means to measure unobservable constructs. AI "capability" is such a construct—we observe performance and infer capability. Psychometrics provides frameworks for understanding reliability (measurement consistency), validity (measuring what's intended), and the relationship between test items and underlying traits.

### Core Concepts

**Reliability**

Consistency of measurement:
- **Test-retest**: Same results over time (complicated for AI by stochasticity and updates)
- **Inter-rater**: Different evaluators agree
- **Internal consistency**: Different items measuring same construct correlate

**Validity (Expanded)**

- **Content validity**: Does the test sample the domain adequately?
- **Criterion validity**: Does the test predict relevant outcomes?
  - Concurrent: Correlates with current criteria
  - Predictive: Predicts future outcomes (key for AI benchmarks)
- **Construct validity**: Does the test measure the theoretical construct?
  - Convergent: Correlates with other measures of same construct
  - Discriminant: Doesn't correlate with measures of different constructs

Most AI benchmarks have unknown criterion validity—we don't know if benchmark performance predicts operational value.

**Classical Test Theory**

Observed Score = True Score + Error. Reliability = proportion of variance due to true score.

**Item Response Theory (IRT)**

Models probability of correct response as function of ability and item characteristics (difficulty, discrimination, guessing). Not all benchmark items are equally informative—IRT thinking suggests optimizing item selection.

**Generalizability Theory**

Partitions variance into components (persons, items, raters, occasions). Reveals which error sources dominate—if rater disagreement dominates, invest in clearer rubrics.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| Reliability concepts | Stable trait assumption | Capability snapshots, not stable traits |
| Validity framework | Population and norming | Benchmark-specific validity arguments |
| Criterion validity focus | Test security (training includes benchmarks) | Contamination detection |
| IRT for benchmark design | Individual differences framing | System-level evaluation |
| Inter-rater reliability | | |

### Key References

- Cronbach, L.J., & Meehl, P.E. (1955). "Construct Validity in Psychological Tests." *Psychological Bulletin*
- Messick, S. (1989). "Validity." In *Educational Measurement* (3rd ed.)
- Brennan, R.L. (2001). *Generalizability Theory*

---

## 2.3 Econometrics and Causal Inference

### Overview

Econometrics provides methods for estimating causal effects from observational data when randomized experiments aren't feasible. The fundamental problem: we can't observe counterfactuals—what would have happened to AI users if they hadn't used AI.

### Core Concepts

**Difference-in-Differences (DiD)**

Compare changes over time between treatment and control: Effect = (Treatment_After - Treatment_Before) - (Control_After - Control_Before). Assumes parallel trends absent treatment.

For AI: compare productivity changes in departments that adopted AI versus those that didn't.

**Regression Discontinuity (RD)**

Exploit sharp cutoffs in treatment assignment. Compare those just above and below a threshold. Provides credible local estimates.

**Instrumental Variables (IV)**

Use exogenous variation to isolate causal effects. An instrument affects treatment but affects outcome only through treatment. Valid instruments are hard to find.

**Propensity Score Methods**

Match treated and control units with similar probability of treatment. Assumes selection on observables—if unobserved factors influence selection, the method fails.

**Heterogeneous Treatment Effects**

Average effects mask variation. AI might help novices while not helping experts. Causal machine learning methods (causal forests) discover heterogeneity data-driven.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| Counterfactual thinking | SUTVA (interference between units) | Account for spillovers |
| Selection bias awareness | Treatment definition ("using AI" varies) | Usage characterization |
| DiD and related designs | Long pre-periods needed | Short pre-period methods |
| Heterogeneity analysis | | |

### Key References

- Angrist, J.D., & Pischke, J.S. (2009). *Mostly Harmless Econometrics*
- Cunningham, S. (2021). *Causal Inference: The Mixtape*
- Athey, S., & Imbens, G.W. (2017). "The State of Applied Econometrics." *JEP*

---

## 2.4 Qualitative Research Methods

### Overview

Qualitative methods understand phenomena through description, interpretation, and attention to context. Numbers tell you AI improves productivity by 15%; qualitative methods tell you how users experience this, what makes it work, where it fails. Essential for understanding the "why" behind quantitative findings.

### Core Concepts

**Ethnography and Observation**

Extended immersion in settings to understand practice from participants' perspectives. Reveals informal workarounds, unspoken norms, emergent practices.

**Interviews**

Structured (comparable data), semi-structured (key topics with flexibility), unstructured (maximum depth). Focus groups leverage group dynamics.

**Grounded Theory**

Build theory inductively from data rather than testing pre-specified hypotheses. Valuable when we don't know enough to specify hypotheses.

**Case Study Methodology**

Investigate bounded cases in depth using multiple sources. Supports analytic generalization to theory, not populations.

**Process Tracing**

Examine causal mechanisms—not just whether X affects Y, but how.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| Understanding "why" | Generalization limits | Purposive sampling |
| Exploratory power | Resource intensity | Targeted qualitative components |
| Context sensitivity | Credibility for some audiences | Mixed methods designs |
| User perspective | | |

### Key References

- Creswell, J.W., & Poth, C.N. (2018). *Qualitative Inquiry and Research Design* (4th ed.)
- Yin, R.K. (2018). *Case Study Research and Applications* (6th ed.)
- Suchman, L. (1987). *Plans and Situated Actions*

---

## 2.5 Survey Methodology

### Overview

Surveys collect self-report data about behaviors, experiences, and attitudes. Relatively easy and inexpensive at scale, but what people report may not match what they do, question wording biases responses, and respondents may not represent the population.

### Core Concepts

**Questionnaire Design**

Item wording, response options, question order, and social desirability all affect responses. Validated scales (TAM, UTAUT) provide established measures.

**Sampling**

Probability sampling enables population generalization; non-probability samples (most AI surveys) cannot. Non-response bias: if only 20% respond, they may differ systematically.

**Measurement Error**

Self-report accuracy is limited. Recall bias affects questions about past behavior. AI studies showing perceived productivity gains exceeding actual gains suggest self-report limitations.

### AI Applicability

| What Transfers | What Breaks | Required Adaptations |
|----------------|-------------|---------------------|
| Questionnaire design principles | Self-report accuracy for AI use | Validate against behavioral data |
| Non-response awareness | Rapidly changing context | Time-bounded surveys |
| Validated technology acceptance scales | | Experience sampling, diary methods |

### Key References

- Groves, R.M., et al. (2009). *Survey Methodology* (2nd ed.)
- Venkatesh, V., et al. (2003). "User Acceptance of Information Technology." *MIS Quarterly*
- Tourangeau, R., et al. (2000). *The Psychology of Survey Response*

---

# Section 3: Economics and Productivity

## 3.1 Information Systems Economics

### Overview

Information Systems economics has decades of experience with a puzzle relevant to AI: technology that seems transformative often fails to produce measurable productivity gains, at least initially. The "IT productivity paradox"—computers everywhere except in productivity statistics—provides crucial context for AI.

### Core Concepts

**The IT Productivity Paradox**

Robert Solow (1987): "You can see the computer age everywhere but in the productivity statistics." Resolution came through several insights:
1. **Measurement problems**: Statistics may not capture IT benefits
2. **Time lags**: Benefits require learning and reorganization
3. **Redistribution vs. creation**: Some gains are competitive redistribution
4. **Mismeasured quality**: Quality improvements not captured

For AI, expect similar patterns: don't expect immediate measured gains.

**Complementary Investments**

IT investments alone don't produce productivity gains. Required: organizational restructuring, human capital development, changed incentives, business process redesign. Organizations expecting AI benefits without complementary changes may be disappointed.

**Task-Technology Fit**

Performance depends on match between task characteristics and technology capabilities. AI may dramatically improve some tasks (routine knowledge work) while providing little benefit for others (tasks requiring judgment or tacit knowledge).

### AI Applicability

| What Transfers | What Breaks |
|----------------|-------------|
| Productivity paradox awareness | Slower IT change (AI faster) |
| Complementary investments | Clearer IT capabilities (AI more uncertain) |
| Task-technology fit | |
| Multi-level measurement | |

### Key References

- Brynjolfsson, E. (1993). "The Productivity Paradox of Information Technology." *CACM*
- Brynjolfsson, E., & Hitt, L. (2000). "Beyond Computation." *JEP*
- Melville, N., et al. (2004). "IT and Organizational Performance." *MIS Quarterly*

---

## 3.2 Productivity Measurement

### Overview

Productivity—output per input—sounds simple but becomes complex upon examination. What counts as output? How do you measure it for knowledge work? For AI's effect on knowledge work, these questions become harder still.

### Core Concepts

**Productivity Definitions**

- **Labor productivity**: Output per worker/hour (attributes all changes to labor)
- **Total Factor Productivity**: Output growth not explained by input growth
- **Task-level productivity**: Output for specific tasks (easier to measure, may miss important aspects)

**Output Measurement Challenges**

For knowledge work: What's the output of analysis? The document? The insights? The decisions informed? How do you count heterogeneous outputs? How do you adjust for quality?

Quality adjustment is particularly challenging. Simple output counts may increase while quality decreases—a spurious "productivity gain."

**Aggregation Issues**

- **Composition effects**: High-productivity workers adopting AI shifts the mix
- **Level of analysis**: Task gains may not aggregate to firm gains
- **Time horizons**: Short-run may differ from long-run

### Key References

- Syverson, C. (2011). "What Determines Productivity?" *Journal of Economic Literature*
- Brynjolfsson, E., et al. (2021). "The Productivity J-Curve." *AEJ: Macroeconomics*

---

## 3.3 Cost Analysis and Investment Evaluation

### Overview

Beyond productivity effects, organizations need to understand full costs, expected benefits, and risks. AI investments often have hidden costs and uncertain benefits.

### Core Concepts

**Total Cost of Ownership (TCO)**

All costs over lifetime: direct costs (licensing, compute, APIs), implementation costs, training costs, ongoing costs (maintenance, QA, oversight), hidden costs (fixing AI errors, learning curves).

AI TCO is often underestimated.

**Cost-Benefit Analysis**

Compare costs and benefits in common units. Net Present Value, benefit-cost ratio. Challenge: quantifying intangible benefits and risks.

**Real Options Analysis**

Investments create future options (expand, abandon, wait). In uncertain environments, flexibility has value beyond immediate returns. AI investments often have option value: pilot with option to expand.

**Learning Curves**

Costs decrease with experience. Early AI costs may not reflect steady-state costs.

### Key References

- Boardman, A.E., et al. (2017). *Cost-Benefit Analysis* (5th ed.)
- Dixit, A.K., & Pindyck, R.S. (1994). *Investment Under Uncertainty*

---

# Section 4: Risk, Quality, and Assurance

## 4.1 Risk Analysis and Management

### Overview

Risk frameworks inform evaluation prioritization—where should limited resources focus?—and help characterize residual uncertainty after evaluation.

### Core Concepts

**Risk Identification**

Hazard analysis, threat modeling, historical analysis, checklists. For AI: incorrect outputs accepted as correct, biased outputs, system unavailability, privacy violations, adversarial misuse.

**Risk Assessment**

Probability × Impact, qualitative assessment, risk matrices, scenario-based assessment. For AI, probability estimation is challenging with limited history.

**Risk Prioritization**

Expected value ranking, risk appetite, consequence-focused prioritization (for catastrophic outcomes).

**Risk Mitigation**

Avoid, transfer, mitigate, accept. For AI: output filtering, human review, usage restrictions, monitoring, fallback procedures.

**Residual Risk**

Risk management reduces but doesn't eliminate risk. Residual risk must be quantified, documented, accepted, and monitored.

### AI Applicability

| What Transfers | What Breaks |
|----------------|-------------|
| Structured risk identification | Probability estimation |
| Risk-based prioritization | Enumerable failures |
| Residual risk concept | Independence assumptions |
| Risk monitoring | |

### Key References

- ISO 31000 (Risk Management Guidelines)
- NIST AI Risk Management Framework
- Hubbard, D.W. (2020). *The Failure of Risk Management* (2nd ed.)

---

## 4.2 Reliability Engineering

### Overview

Reliability engineering ensures systems perform required functions over time. For AI, "failure" needs reinterpretation—AI doesn't crash like hardware but produces wrong, unhelpful, or harmful outputs.

### Core Concepts

**Reliability Metrics**

MTBF (Mean Time Between Failures), MTTF, Availability. For AI, "reliability" might mean consistency of quality or probability of meeting thresholds.

**Failure Modes and Effects Analysis (FMEA)**

Identify: How can each component fail? What happens? How likely? How severe? How detectable? Risk Priority Number guides prioritization.

For AI: How can outputs fail (incorrect, biased, harmful)? What are consequences? How detectable?

**Reliability Growth**

Systems become more reliable as failures are found and fixed. AI reliability might improve as edge cases are identified, users learn, and prompts are refined.

**Common Cause Failures**

Multiple components failing from the same cause defeats redundancy. For AI: same model across applications, same training data biases, same vulnerabilities.

### Key References

- O'Connor, P.D.T., & Kleyner, A. (2012). *Practical Reliability Engineering* (5th ed.)

---

## 4.3 Quality Management

### Overview

Quality management provides systematic approaches to ensuring and improving quality—relevant for continuous AI monitoring and improvement.

### Core Concepts

**Statistical Process Control (SPC)**

Monitor outputs over time using control charts. Control limits define expected variation. When metrics exceed limits, investigate. For AI: monitor quality metrics, response times, error rates over time.

**Process Capability**

Can the process consistently meet specifications? For AI: Can AI consistently meet quality requirements?

**Continuous Improvement (PDCA)**

Plan → Do → Check → Act. Iterative improvement. For AI: identify prompt improvements, test changes, measure effects, standardize successes.

**Root Cause Analysis**

5 Whys, fishbone diagrams. For AI, root cause is often obscure (training data? model architecture? prompt?).

### Key References

- Montgomery, D.C. (2019). *Introduction to Statistical Quality Control* (8th ed.)
- Wheeler, D.J. (2000). *Understanding Variation*

---

## 4.4 Audit and Assurance

### Overview

Audit provides independent assurance that claims are accurate. The audit profession has developed rigorous methods for evidence gathering and professional judgment applicable to AI evaluation governance.

### Core Concepts

**Assurance Levels**

Reasonable assurance (high confidence) vs. limited assurance. Audit opinions provide independent assessment of credibility.

**Independence and Objectivity**

Independence from entity being audited, no conflicts of interest, professional skepticism. For AI: evaluation by parties separate from developers.

**Materiality**

Focus on what matters for decisions, not exhaustive evaluation of everything.

**Evidence Standards**

Documentary, testimonial, observational, analytical evidence. Sufficient (enough) and appropriate (relevant and reliable).

**Three Lines of Defense**

First line (operational controls), second line (risk/compliance functions), third line (internal audit). For AI: operational teams monitoring, risk/compliance overseeing, internal audit independently assessing.

### Key References

- AICPA Audit Standards
- IIA Standards (Internal Auditing)
- Raji, I.D., et al. (2020). "Closing the AI Accountability Gap." *FAT*

---

## 4.5 Safety Engineering

### Overview

Safety engineering prevents hazards and ensures systems don't cause harm. For safety-critical AI applications, safety engineering methods provide frameworks for hazard analysis and structured safety argumentation.

### Core Concepts

**Hazard Analysis**

A hazard is a condition that could lead to harm. Identify hazards, triggers, and consequences. For AI: incorrect outputs leading to bad decisions, biased outputs causing discrimination, AI misuse.

**Fault Tree Analysis (FTA)**

Work top-down from undesired event to identify causes.

**System-Theoretic Process Analysis (STPA)**

Systems perspective: failures come from unsafe interactions, not just component failures. Focus on control structures and unsafe control actions. Particularly valuable for human-AI systems.

**Safety Cases**

Structured arguments for acceptable safety: claims, evidence, argument, context. Goal Structuring Notation (GSN) provides visual representation. Emerging for frontier AI systems.

### Key References

- Leveson, N.G. (2011). *Engineering a Safer World*
- IEC 61508 (Functional Safety)
- Clymer, J., et al. (2024). "Safety Cases: How to Justify the Safety of Advanced AI Systems"

---

# Section 5: Human and Organizational Factors

## 5.1 Human-Computer Interaction and UX Research

### Overview

HCI studies how people actually interact with technology—not how designers intend, but how they actually do in practice. For AI evaluation, HCI methods reveal user experience, emergent strategies, and friction points.

### Core Concepts

**Usability Dimensions**

Effectiveness, efficiency, satisfaction, learnability, error rates. For AI: Can users prompt effectively? Can they recognize errors? Is iteration consuming time?

**Evaluation Methods**

- **Heuristic evaluation**: Expert review against usability principles
- **Cognitive walkthrough**: Step through tasks from user perspective
- **Usability testing**: Observe real users on realistic tasks
- **Contextual inquiry**: Study work in natural context

**Task Analysis**

Hierarchical Task Analysis (HTA) breaks work into goals and operations. Cognitive Task Analysis examines cognitive demands. For AI: Which tasks might AI support? What judgment must remain human?

**Mental Models**

Users develop models of how systems work—often incomplete or inaccurate. For AI: Do users understand capabilities and limits? Mismatched mental models lead to misuse.

### Key References

- Nielsen, J. (1993). *Usability Engineering*
- Beyer, H., & Holtzblatt, K. (1998). *Contextual Design*
- Amershi, S., et al. (2019). "Guidelines for Human-AI Interaction." *CHI*

---

## 5.2 Human Factors and Human-Machine Systems

### Overview

Human factors studies how humans interact with systems, emphasizing capabilities and limitations. Directly applicable to human-AI teaming: trust, automation, workload, situation awareness.

### Core Concepts

**Workload**

Mental and physical demands on operators. AI might reduce task demands while adding monitoring demands. Managing AI output quality is itself work.

**Situation Awareness**

Endsley's three levels: perception, comprehension, projection. If AI handles tasks automatically, does the human lose awareness?

**Trust in Automation**

- **Overtrust (complacency)**: Accepting outputs uncritically
- **Undertrust (disuse)**: Not using when it would help
- **Calibrated trust**: Matching trust to actual reliability

The jagged capability frontier makes AI trust calibration particularly challenging.

**Automation Surprises**

"What's it doing?" "Why did it do that?" "What will it do next?" AI's unpredictable behavior generates frequent surprises.

**Skill Degradation**

When automation handles tasks, human skills may atrophy. If AI fails, can humans perform?

### Key References

- Parasuraman, R., & Riley, V. (1997). "Humans and Automation." *Human Factors*
- Lee, J.D., & See, K.A. (2004). "Trust in Automation." *Human Factors*
- Endsley, M.R. (2016). *Designing for Situation Awareness* (2nd ed.)

---

## 5.3 Organizational Behavior and Change Management

### Overview

AI adoption is organizational change—it affects roles, processes, skills, relationships. Organizational factors determine whether capable AI delivers benefits.

### Core Concepts

**Technology Adoption Models**

TAM: Perceived usefulness and ease of use drive adoption. Diffusion of Innovations: Innovators → early adopters → early majority → late majority → laggards. UTAUT adds social influence and facilitating conditions.

**Absorptive Capacity**

Organizations differ in ability to recognize, assimilate, and apply new knowledge. High absorptive capacity enables learning from AI; low absorptive capacity limits benefits.

**Change Management**

Lewin (Unfreeze → Change → Refreeze), Kotter's 8 steps. Technology deployment requires deliberate change management.

**Resistance to Change**

Arises from uncertainty, loss of control, perceived threats, poor communication. Resistance often reflects legitimate concerns.

**Implementation Research**

Was the intervention delivered as intended? Implementation success depends on more than AI capability.

### Key References

- Rogers, E.M. (2003). *Diffusion of Innovations* (5th ed.)
- Kotter, J.P. (2012). *Leading Change*
- Venkatesh, V., et al. (2003). "User Acceptance of Information Technology." *MIS Quarterly*

---

## 5.4 Judgment and Decision Making

### Overview

JDM research studies how people make judgments, including systematic biases. Directly relevant to how humans use (and misuse) AI advice—and how human evaluators may be biased.

### Core Concepts

**Heuristics and Biases**

- **Availability**: Judging likelihood by ease of recall (dramatic AI successes more memorable)
- **Anchoring**: Initial values influence estimates (AI suggestions anchor judgment)
- **Representativeness**: Judging by similarity to stereotypes (output that "sounds right")
- **Confirmation bias**: Seeking confirming information

**Algorithm Aversion and Appreciation**

- **Aversion**: Resisting algorithmic advice even when it outperforms humans
- **Appreciation (automation bias)**: Over-relying on AI

Both affect AI adoption and use patterns.

**Calibration**

Match between confidence and accuracy. For AI users: Do they know when to trust AI?

**Noise**

Variability in judgments that should be identical. Human evaluation of AI outputs is noisy.

### Key References

- Kahneman, D. (2011). *Thinking, Fast and Slow*
- Kahneman, D., et al. (2021). *Noise*
- Dietvorst, B.J., et al. (2015). "Algorithm Aversion." *JEPG*

---

## 5.5 Industrial-Organizational Psychology

### Overview

I-O psychology applies psychological principles to workplaces. It informs the "evaluate AI like hiring an employee" metaphor: job analysis, selection, performance appraisal.

### Core Concepts

**Job Analysis**

What tasks comprise the job? What KSAOs are needed? For AI: What should AI do? What capabilities are required?

**Personnel Selection**

Work samples predict performance better than general tests. For AI: evaluate on realistic tasks, not just general benchmarks.

**The Criterion Problem**

What is "good performance"? Ultimate criterion (ideal) vs. actual criterion (measurable). Criterion deficiency (missing aspects) and contamination (irrelevant factors). For AI, defining "good output" is central.

**Structured Evaluation**

Structured assessment consistently outperforms unstructured. Rating scales with behavioral anchors beat global ratings. For AI: structured rubrics reduce noise and bias.

### Key References

- Schmidt, F.L., & Hunter, J.E. (1998). "Validity and Utility of Selection Methods." *Psychological Bulletin*
- Campion, M.A., et al. (1997). "Structure in the Selection Interview." *Personnel Psychology*

---

# Section 6: Evaluation and Assessment Traditions

## 6.1 AI Safety Evaluation (Emerging)

### Overview

AI safety evaluation is developing specifically for AI, drawing on multiple traditions while grappling with AI's distinctive challenges. This section is necessarily brief—the field is developing rapidly.

### Core Concepts

**Capability Evaluation**

What can the model do? Reasoning, coding, knowledge—and dangerous capabilities (cyber offense, biological knowledge, deception). Capabilities may be latent; evaluation must try to surface them.

**Alignment Evaluation**

Does the model behave as intended? Follow instructions, pursue intended goals, avoid deception, behave consistently? Misaligned behavior might appear aligned on evaluation.

**Red Teaming**

Adversarial evaluation: jailbreaking, prompt injection, systematic exploration of harmful capability boundaries.

**Safety Cases**

Structured safety arguments emerging for frontier AI.

**Evaluation Gaming**

AI might behave differently when evaluated: trained on evaluation data, behaving better in evaluation than deployment, deceptive alignment.

### Current Areas

Benchmark design and contamination detection, scalable oversight, dangerous capability evaluation, continuous monitoring, red team methodology development.

### Key References

- Shevlane, T., et al. (2023). "Model Evaluation for Extreme Risks"
- Anthropic, OpenAI, DeepMind safety reports and responsible scaling policies
- METR methodology documentation

---

## 6.2 Program Evaluation

### Overview

Program evaluation assesses programs and interventions—relevant for evaluating AI as an organizational intervention implemented to produce benefit.

### Core Concepts

**Logic Models / Theory of Change**

Inputs → Activities → Outputs → Outcomes → Impact. Makes causal assumptions explicit. For AI: providing tools (input) → AI use (activity) → more documents (output) → time saved (outcome) → improved performance (impact). Each arrow is testable.

**Formative vs. Summative Evaluation**

- **Formative**: Improve during implementation (often more valuable for AI)
- **Summative**: Judge overall effectiveness

**Process vs. Outcome Evaluation**

- **Process**: Was AI actually used? How?
- **Outcome**: Did desired effects occur?

Process evaluation is essential: if AI "doesn't work," is that AI or implementation?

**Implementation Fidelity**

Was intervention delivered as designed? For AI: Did people use it? How often? How well?

**Developmental Evaluation**

For innovative initiatives in complex environments: ongoing, adaptive, emergent. Appropriate when outcomes and paths are uncertain—like AI.

**Realist Evaluation**

"What works, for whom, in what circumstances, and why?" Context-Mechanism-Outcome configurations explain variation.

### Key References

- Patton, M.Q. (2010). *Developmental Evaluation*
- Pawson, R., & Tilley, N. (1997). *Realistic Evaluation*
- Rossi, P.H., et al. (2018). *Evaluation: A Systematic Approach* (8th ed.)

---

## 6.3 Educational Measurement

### Overview

Educational measurement offers insights on high-stakes testing, test security, and effects of testing on behavior—relevant because AI benchmarks are increasingly high-stakes.

### Core Concepts

**High-Stakes Testing**

When results have significant consequences, behavior changes. People optimize for what's measured, sometimes at expense of what matters.

**Test Security**

Preventing item leakage, detecting cheating. For AI, benchmark contamination is the equivalent of test leakage.

**Teaching to the Test**

Instruction shifts toward what's tested. For AI, "training to the benchmark" may not generalize to real tasks.

**Campbell's Law**

"The more any quantitative social indicator is used for social decision-making, the more subject it will be to corruption pressures." Applied to AI: as benchmark stakes increase, benchmarks will be gamed and measure genuine capability less.

### Key References

- Koretz, D. (2008). *Measuring Up: What Educational Testing Really Tells Us*
- Cizek, G.J., & Wollack, J.A. (2016). *Handbook of Quantitative Methods for Detecting Cheating*

---

## 6.4 Clinical Trial Methodology

### Overview

Clinical trials have evolved rigorous approaches for testing interventions. The phased structure, randomization, and post-market surveillance offer models for AI evaluation.

### Core Concepts

**Phased Evaluation**

- Phase I: Safety in small groups
- Phase II: Initial efficacy in larger groups
- Phase III: Definitive efficacy in large randomized trials
- Phase IV: Post-market surveillance

Manage risk: don't proceed to large studies until smaller ones support proceeding. For AI: controlled testing → limited pilot → expanded deployment → continuous monitoring.

**Adaptive Designs**

Modify based on interim results—expand promising treatments, drop ineffective ones. More efficient use of data.

**Post-Market Surveillance**

Approval isn't the end. Detect rare adverse events, long-term effects, effects in underrepresented populations. For AI: post-deployment monitoring detects problems emerging at scale or over time.

**Real-World Evidence**

Evidence from actual practice complements controlled trials. For AI: deployment data complements controlled evaluation.

### Key References

- Friedman, L.M., et al. (2015). *Fundamentals of Clinical Trials* (5th ed.)
- Berry, S.M., et al. (2010). *Bayesian Adaptive Methods for Clinical Trials*

---

# Section 7: Standards and Governance

## 7.1 Metrology (Science of Measurement)

### Overview

Metrology asks fundamental questions about what it means to measure something. Its principles illuminate AI evaluation's immature state and point toward what rigorous AI measurement might require.

### Core Concepts

**Measurement Uncertainty**

All measurements have uncertainty. Metrological practice requires quantifying, reporting, and propagating uncertainty. For AI, measurement uncertainty is substantial but rarely quantified.

**Traceability**

Measurements should be traceable to reference standards, enabling comparison. For AI, different benchmarks define "accuracy" differently; there's no agreed reference standard.

**Calibration**

Instruments must be verified against standards. For AI: Are our evaluation methods themselves accurate?

**Vocabulary of Metrology (VIM)**

- **Accuracy**: Closeness to true value (trueness + precision)
- **Precision**: Repeatability
- **Trueness**: Systematic closeness to true value
- **Bias**: Difference between measured mean and true value

AI evaluation often uses these terms loosely.

### AI Applicability

AI evaluation is metrologically immature. No reference standards, limited institutional infrastructure, substantial unquantified uncertainty.

### Key References

- BIPM. *International Vocabulary of Metrology (VIM)* (3rd ed.)
- JCGM. *Guide to the Expression of Uncertainty in Measurement (GUM)*
- Tal, E. (2017). "Measurement in Science." *Stanford Encyclopedia of Philosophy*

---

## 7.2 Standards Development and Governance

### Overview

Technical standards establish common frameworks. AI evaluation standards are emerging; understanding the landscape helps organizations navigate compliance and contribute to development.

### Core Concepts

**Types of Standards**

- **De jure**: Established through formal SDO processes (ISO, IEEE, NIST)
- **De facto**: Emerge from market adoption
- **Mandatory vs. voluntary**
- **Performance vs. prescriptive**

**Key Organizations**

- **NIST**: AI Risk Management Framework, evaluation research
- **ISO**: ISO/IEC JTC 1/SC 42 developing AI standards
- **IEEE**: AI ethics, transparency standards

**Conformity Assessment**

How to demonstrate compliance: self-declaration, second-party assessment, third-party certification.

**Standards and Innovation**

Timing matters: too early locks in immaturity; too late allows fragmentation.

### Current Landscape

NIST AI RMF, ISO/IEC AI standards in development, EU AI Act, various industry frameworks.

### Key References

- NIST AI Risk Management Framework
- ISO/IEC JTC 1/SC 42
- EU Artificial Intelligence Act

---

# Section 8: Synthesis and Crosswalks

## 8.1 What Transfers Directly

| Discipline | Key Concepts | AI Application |
|------------|--------------|----------------|
| **Software Testing** | Verification vs. validation | Benchmarks ≈ verification; operational testing ≈ validation |
| | Regression mindset | Track performance over time |
| **Systems T&E** | DT/OT paradigm | Lab testing precedes operational pilots |
| | MOPs vs. MOEs | Technical metrics ≠ mission effectiveness |
| | Independent evaluation | Separate evaluator from developer |
| **Autonomous Systems** | Sim-to-real gap | Benchmark-to-real gap |
| | Scenario-based testing | Systematic scenario design |
| | Safety cases | Structured safety argumentation |
| **Cybersecurity** | Adversarial mindset | Actively try to find failures |
| | Red teaming | Structured adversarial evaluation |
| | Defense in depth | Multiple protections |
| **Experimental Design** | Validity framework | Internal, external, construct validity |
| | Control conditions | What's the comparison? |
| | Pre-registration | Commit to analysis plans |
| **Psychometrics** | Reliability concepts | Consistency of measurement |
| | Criterion validity | Does benchmark predict real-world performance? |
| **Econometrics** | Counterfactual thinking | What would have happened without AI? |
| | Selection bias awareness | Who adopts is not random |
| | Heterogeneity analysis | Effects vary |
| **Qualitative Methods** | Understanding "why" | How and why does AI help? |
| | Contextual inquiry | Observe natural settings |
| **Risk Analysis** | Risk-based prioritization | Focus on highest-risk areas |
| | Residual risk | Evaluation reduces but doesn't eliminate risk |
| **Quality Management** | SPC monitoring | Control charts for AI metrics |
| | Continuous improvement | Iterative improvement |
| **Audit** | Independence | Separate evaluator from developer |
| | Evidence standards | Rigor in evidence |
| **Safety Engineering** | Hazard analysis | Systematically identify potential harms |
| | STPA | Systems analysis of human-AI teams |
| **Human Factors** | Trust calibration | Appropriate trust given reliability |
| | Automation surprises | AI surprises frequently |
| **I-O Psychology** | Structured evaluation | Structure reduces noise and bias |
| | Criterion problem | "Good performance" is hard to define |
| **Program Evaluation** | Logic models | How AI creates value |
| | Implementation fidelity | Is AI actually being used? |
| **Clinical Trials** | Phased approach | Start small, expand on results |
| | Post-market surveillance | Monitor after deployment |

---

## 8.2 What Breaks for Generative AI

| Broken Assumption | Affected Disciplines | AI Reality |
|-------------------|---------------------|------------|
| **Determinism** | Software testing, reliability | Stochastic outputs |
| **Enumerable inputs/outputs** | Software testing, traditional ML | Effectively unbounded |
| **Clear ground truth** | Traditional ML, psychometrics | No single "correct" answer |
| **Stable system** | All T&E disciplines | Continuous updates |
| **Stable traits** | Psychometrics, I-O psychology | Capabilities change rapidly |
| **Predictable failures** | Reliability, safety | Jagged capability frontier |
| **Observable processes** | Quality management, safety | Opaque processing |
| **Independent failures** | Reliability, risk | Correlated across applications |
| **Blinding** | Experimental design, clinical trials | Users know they're using AI |
| **Treatment stability** | Experimental design | AI changes during evaluation |
| **Defined treatment** | Econometrics, program evaluation | "Using AI" is variable |
| **Test security** | Psychometrics, educational measurement | Training may include benchmarks |

---

## 8.3 What Requires Adaptation

| Original Concept | Adaptation Needed |
|------------------|-------------------|
| Test coverage | Coverage of capabilities/scenarios, not input space |
| Regression testing | Continuous monitoring, not re-running fixed tests |
| Reliability prediction | Scenario-based rather than component-based |
| FMEA | More emphasis on unknown unknowns |
| Trust calibration | For stochastic, jagged capabilities |
| Implementation fidelity | "Use" is variable and hard to characterize |
| Safety cases | New evidence types and argument structures |

---

## 8.4 What's Genuinely New

Some AI evaluation challenges lack good precedents:

**1. Unbounded Output Evaluation**

No prior field evaluated systems producing outputs from unlimited space. Classification has k classes; AI produces arbitrary text.

**2. Jagged Capability Frontier**

High capability immediately adjacent to surprising failure is unprecedented. Traditional systems have understood boundaries.

**3. Specification Depth Problem**

AI's value lies in tasks that couldn't be specified precisely enough to automate. But unspecifiable tasks are unevaluable by traditional means.

**4. Benchmark Contamination Via Training**

Training may include benchmark items through internet-scale data collection—inflating scores without intentional cheating.

**5. Continuous Evolution**

Most evaluation assumes stable systems. AI may change continuously without clear version boundaries.

**6. Skill Amplification**

Same AI produces dramatically different outcomes for different users. Capability is entangled with user skill.

**7. The "Vibes" Quality Problem**

Experts recognize quality but struggle to articulate criteria. Pervasive across AI's many application domains.

---

## 8.5 Terminology Crosswalk

### Accuracy and Error

| Discipline | Term | Meaning |
|------------|------|---------|
| Traditional ML | Accuracy | Proportion correct |
| Metrology | Accuracy | Closeness to true value (trueness + precision) |
| Software Testing | Defect | Behavior contrary to specification |

### Reliability

| Discipline | Term | Meaning |
|------------|------|---------|
| Psychometrics | Reliability | Measurement consistency |
| Reliability Engineering | Reliability | Probability of successful operation over time |

### Validity and Effectiveness

| Discipline | Term | Meaning |
|------------|------|---------|
| Psychometrics | Validity | Measures intended construct |
| Experimental Design | Validity | Conclusions warranted |
| Systems T&E | Effectiveness/MOE | Mission accomplishment |

### Testing Types

| Discipline | Term | Meaning |
|------------|------|---------|
| Software Testing | Unit/Integration/System | Component → interaction → complete |
| Systems T&E | DT/OT | Development → operational conditions |
| Clinical Trials | Phase I/II/III | Increasing scale and rigor |

### Risk and Hazard

| Discipline | Term | Meaning |
|------------|------|---------|
| Risk Analysis | Risk | Probability × Consequence |
| Safety Engineering | Hazard | Condition that could cause harm |
| Cybersecurity | Threat/Vulnerability | Harm source / exploitable weakness |

### Human-AI Concepts

| Discipline | Term | Meaning |
|------------|------|---------|
| Human Factors | Trust calibration | Trust matched to reliability |
| Human Factors | Automation bias | Uncritical acceptance |
| JDM | Algorithm aversion | Resistance to algorithmic advice |

---

## 8.6 Synthesis: What AI Evaluation Requires

### From Testing Traditions
- Systematic approach over ad hoc probing
- V&V distinction: technical verification ≠ fitness-for-purpose validation
- DT/OT paradigm: lab evaluation differs from operational evaluation
- Adversarial orientation: actively find failures
- Scenario-based coverage for unbounded input spaces

### From Statistical Methods
- Validity framework: internal, external, construct
- Appropriate comparison conditions
- Causal discipline: correlation ≠ causation
- Heterogeneity awareness: average effects mask variation
- Qualitative complement: numbers need context

### From Economics
- Productivity paradox awareness: expect delayed gains
- Complementary investments: AI benefits require organizational change
- Full cost accounting including hidden costs
- Time horizon awareness: short-run ≠ long-run

### From Risk and Quality
- Risk-based prioritization
- Continuous monitoring
- Residual risk acceptance
- Independence for high stakes

### From Human and Organizational Factors
- Human-AI team evaluation
- Trust calibration assessment
- Organizational context matters
- Implementation fidelity checks

### From Evaluation Traditions
- Logic models for value creation
- Developmental approach for learning what works
- Post-deployment surveillance

### Novel for AI
- Benchmark integrity protection
- Dense capability coverage
- Output evaluation methods for unbounded space
- Evolution accommodation
- Skill interaction understanding
- Quality articulation beyond "vibes"

---

## 8.7 Reader Guide

**For T&E Professionals**: Start with Sections 1, 4, 6. Then Section 2 for statistical rigor.

**For Researchers/Methodologists**: Start with Sections 2, 6. Then Section 7.1 for measurement foundations.

**For Acquisition/Management**: Start with Sections 3, 4.4, 7. Then Section 5.3 for implementation factors.

**For Human Factors Specialists**: Start with Section 5. Then Section 1.3 for AI-specific human factors.

**For AI Safety Researchers**: Start with Sections 6.1, 4.5, 1.5. This work bridges fields.

---

*[End of Document]*
