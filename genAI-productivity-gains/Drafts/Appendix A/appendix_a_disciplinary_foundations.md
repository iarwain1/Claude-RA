# Appendix A: Disciplinary Foundations for AI Evaluation

## Purpose and How to Use This Appendix

This appendix surveys the disciplines and fields that inform AI evaluation, organized to help readers:

1. **Connect to existing expertise**: Readers with backgrounds in specific fields can see how their knowledge applies (and where it breaks down)
2. **Find entry points**: Readers unfamiliar with a field can understand its core contributions and access key literature
3. **Understand what's new**: By systematically examining what transfers and what doesn't, we can identify what's genuinely novel about AI evaluation

**Structure for each discipline**:
- Overview: What the field is and what it studies
- Core concepts: Key ideas and methods relevant to AI evaluation
- What transfers: Approaches that apply directly
- What breaks: Where the field's assumptions don't hold for GenAI
- What can be adapted: Approaches that work with modification
- Implications for AI evaluation: Practical takeaways
- Key references: Entry points to the literature
- Connections: Links to other disciplines in this appendix

**Reading suggestions**:
- T&E professionals: Start with Sections 1, 4, 5
- Researchers/methodologists: Start with Sections 2, 6
- Acquisition/management professionals: Start with Sections 3, 4, 7
- Human factors specialists: Start with Sections 3, 5

---

## Section 1: Testing and Evaluation Traditions

### 1.1 Software Testing and Quality Assurance

#### Overview
The discipline of systematically evaluating software to identify defects, verify requirements are met, and validate that the software serves its intended purpose. Encompasses unit testing, integration testing, system testing, acceptance testing, and related practices.

#### Core Concepts

**Verification vs. Validation (V&V)**
- Verification: "Are we building it right?" (Does implementation match specification?)
- Validation: "Are we building the right thing?" (Does it meet user needs?)
- This distinction maps directly to AI evaluation challenges

**Test Coverage**
- Statement coverage, branch coverage, path coverage
- The goal of ensuring all code paths are exercised
- Coverage metrics as proxy for test adequacy

**Test Oracles**
- How do you know if output is correct?
- Specification-based oracles, reference implementations, metamorphic testing
- The oracle problem: sometimes no clear "right answer"

**Regression Testing**
- Re-running tests after changes to detect new defects
- Assumes deterministic behavior and stable test suite
- Foundation for continuous integration

**Boundary Testing and Edge Cases**
- Testing at the boundaries of input domains
- Systematic identification of edge cases
- Equivalence partitioning to manage test space

**Fault Injection and Mutation Testing**
- Deliberately introducing faults to test detection capability
- Assessing test suite quality, not just software quality

#### What Transfers

- **V&V framing**: Distinguishing technical correctness from fitness for purpose is directly applicable; benchmarks are closer to verification, operational evaluation to validation
- **Test planning discipline**: Systematic approach to identifying what to test, why, and how
- **Coverage thinking**: Even if we can't achieve full coverage, thinking about coverage gaps is valuable
- **Regression mindset**: Tracking performance over time to detect degradation
- **Edge case identification**: Systematic thinking about where failures might occur

#### What Breaks

- **Determinism assumption**: Software testing assumes same input → same output; AI violates this fundamentally
- **Enumerable test space**: Software has finite (if large) input space; GenAI input space is unbounded
- **Clear oracles**: Software often has specifications defining correct behavior; GenAI outputs often lack clear "correct" answers
- **Fault isolation**: When software fails a test, you can usually trace to the bug; AI failures are opaque
- **Stable system under test**: Software version is fixed during testing; AI models may change

#### What Can Be Adapted

- **Coverage concepts**: Can't achieve full coverage, but can reason about coverage gaps and prioritize high-risk areas
- **Metamorphic testing**: Testing relationships between inputs/outputs rather than specific outputs; applicable to AI (e.g., paraphrase should give similar answer)
- **Differential testing**: Comparing outputs across models or versions; useful for regression detection
- **Property-based testing**: Testing invariants rather than specific outputs; applicable to some AI properties

#### Implications for AI Evaluation

- Borrow the discipline and systematic thinking from software testing
- Adapt coverage and oracle concepts for probabilistic, unbounded systems
- Accept that testing cannot be exhaustive; focus on risk-based prioritization
- Build monitoring rather than relying solely on pre-deployment testing

#### Key References

- Beizer, B. (1990). *Software Testing Techniques*
- Myers, G. et al. (2011). *The Art of Software Testing*
- Ammann, P. & Offutt, J. (2016). *Introduction to Software Testing*
- IEEE 829 Standard for Software Test Documentation
- Segura, S. et al. (2016). "A Survey on Metamorphic Testing" (for adaptation to AI)

#### Connections
- See 1.4 (Traditional ML Evaluation) for statistical testing approaches
- See 2.1 (Experimental Design) for controlled comparison methods
- See 4.2 (Reliability Engineering) for system-level reliability concepts

---

### 1.2 Systems Engineering and Hardware T&E

#### Overview
The discipline of testing complex hardware and integrated systems, particularly in defense and aerospace contexts. Encompasses developmental testing (DT), operational testing (OT), and the frameworks governing major acquisition programs.

#### Core Concepts

**Developmental Testing (DT) vs. Operational Testing (OT)**
- DT: Testing during development to support design refinement; controlled conditions
- OT: Testing under realistic operational conditions to assess effectiveness and suitability
- The DT→OT transition as key evaluation milestone

**Measures of Performance (MOPs) vs. Measures of Effectiveness (MOEs)**
- MOPs: Technical performance parameters (speed, range, accuracy)
- MOEs: How well the system accomplishes its mission
- Critical insight: good MOPs don't guarantee good MOEs

**Suitability**
- Beyond effectiveness: Is the system usable, maintainable, supportable?
- Human factors and logistics considerations
- Often harder to measure than effectiveness

**Test and Evaluation Master Plan (TEMP)**
- Comprehensive planning document for system evaluation
- Links evaluation to requirements and program milestones
- Integrates DT and OT planning

**Modeling and Simulation (M&S) Accreditation**
- Formal process for determining when M&S is adequate for decision support
- Addresses question: "Is this simulation good enough to inform this decision?"
- Directly analogous to benchmark validity questions

**Operational Test Agencies**
- Independent organizations conducting OT
- Separation from developer to reduce bias
- Importance of independent evaluation

#### What Transfers

- **DT/OT paradigm**: Distinguishing early capability exploration from realistic operational assessment applies directly
- **MOP/MOE distinction**: Technical AI metrics (benchmark scores) vs. mission effectiveness is the same distinction
- **M&S accreditation thinking**: "When is a benchmark good enough?" mirrors "When is a simulation good enough?"
- **Independent evaluation**: Value of separation between developer/vendor and evaluator
- **Suitability focus**: Human factors and integration matter, not just raw capability
- **TEMP discipline**: Comprehensive evaluation planning applicable to major AI acquisitions

#### What Breaks

- **Stable system configuration**: Hardware doesn't change during OT; AI systems may be updated
- **Physical test environments**: Hardware testing has defined environments; AI "environment" is information space
- **Failure mode predictability**: Hardware failures follow physical laws; AI failures are less predictable
- **Requirements stability**: Hardware requirements are usually fixed; AI capabilities and expectations co-evolve
- **Test infrastructure**: Hardware test ranges exist; AI evaluation infrastructure is immature

#### What Can Be Adapted

- **Scenario-based testing**: OT scenario development can inform AI evaluation scenario design
- **Operational realism requirements**: Emphasis on testing in realistic conditions directly applicable
- **Integrated testing**: Combining DT and OT thinking for more efficient evaluation
- **Critical Operational Issues (COIs)**: Framework for identifying key evaluation questions

#### Implications for AI Evaluation

- Apply DT/OT paradigm: benchmarks and lab studies are DT; operational pilots are OT
- Distinguish AI performance metrics (MOPs) from mission outcome metrics (MOEs)
- Consider suitability (usability, supportability) not just effectiveness
- Build in independent evaluation for high-stakes decisions
- Develop comprehensive evaluation planning for major AI acquisitions

#### Key References

- DoD 5000 series acquisition guidance
- DoDI 5000.89 (Test and Evaluation)
- GAO Cost Estimating and Assessment Guide
- Developmental Test and Evaluation (DT&E) policy documents
- Director, Operational Test and Evaluation (DOT&E) annual reports

#### Connections
- See 1.3 (Autonomous Systems) for AI-adjacent systems T&E
- See 4.1 (Risk Analysis) for risk-based test planning
- See 5.2 (Human-Machine Systems) for suitability evaluation

---

### 1.3 Autonomous Systems Testing and Evaluation

#### Overview
The evaluation of systems that sense, decide, and act with varying degrees of independence from human operators. Includes robotics, unmanned vehicles, self-driving cars, and AI-enabled autonomous capabilities. The closest existing paradigm to GenAI evaluation.

#### Core Concepts

**Levels of Autonomy**
- Frameworks describing degrees of human vs. machine control (e.g., SAE J3016 for vehicles)
- From fully manual to fully autonomous
- Implications for testing: higher autonomy = more complex evaluation

**Operational Design Domain (ODD)**
- The conditions under which an autonomous system is designed to operate
- Geographic, temporal, environmental, traffic, and other constraints
- Defines the "envelope" within which the system should function

**Simulation-to-Real (Sim2Real) Gap**
- The challenge of simulation performance not transferring to real world
- Well-studied problem with known mitigation approaches
- Directly analogous to benchmark-to-real gap

**Edge Case and Scenario Testing**
- Systematic identification of challenging scenarios
- Combinatorial explosion of possible conditions
- Risk-based prioritization of test scenarios

**Safety Cases**
- Structured arguments that a system is acceptably safe
- Claims, evidence, and argument linking them
- Increasingly adopted for AI safety

**Human Supervisory Control**
- How humans monitor and intervene with autonomous systems
- Trust calibration and situation awareness
- Handoff and takeover scenarios

**Verification and Validation for Autonomy**
- Specialized V&V approaches for learning-enabled components
- Run-time verification and monitoring
- Formal methods for safety-critical properties

#### What Transfers

- **Levels of autonomy thinking**: Useful framework even though GenAI doesn't fit neatly
- **ODD concept**: Defining conditions under which AI is expected to work (though harder to specify for GenAI)
- **Sim2Real gap awareness**: The gap between controlled evaluation and deployment is a known problem with studied mitigations
- **Scenario-based testing**: Systematic scenario identification and prioritization
- **Safety case methodology**: Structured argumentation applicable to AI
- **Human supervisory control research**: Directly relevant to human-AI teaming
- **Run-time monitoring**: Applicable to continuous AI evaluation

#### What Breaks

- **Bounded physical environment**: Autonomous vehicles operate in physical space with constraints; GenAI operates in unbounded information space
- **Observable failures**: Autonomous system failures are usually evident (crash, wrong turn); GenAI failures may be subtle (plausible but wrong)
- **Defined ODD**: Hard to specify ODD for general-purpose GenAI (what's the "operating envelope" for a chatbot?)
- **Formal verification**: Some autonomous system properties can be formally verified; GenAI properties generally cannot
- **Replay and reproducibility**: Can often replay autonomous system scenarios exactly; GenAI is stochastic

#### What Can Be Adapted

- **Edge case discovery methods**: Techniques for finding challenging scenarios can be adapted
- **Coverage metrics for scenarios**: Measuring scenario coverage rather than input coverage
- **Degraded mode testing**: Testing how system behaves at capability boundaries
- **Human factors integration**: Methods for evaluating human-automation interaction

#### Implications for AI Evaluation

- Draw on scenario-based testing approaches from autonomous systems
- Adapt ODD thinking: even if we can't fully specify the operating envelope, thinking about boundaries is useful
- Learn from Sim2Real gap research to understand benchmark-to-real gap
- Apply safety case methodology for high-stakes AI deployments
- Leverage human supervisory control research for human-AI teaming evaluation

#### Key References

- SAE J3016 (Levels of Driving Automation)
- Koopman, P. & Wagner, M. (2016). "Challenges in Autonomous Vehicle Testing and Validation"
- NHTSA AV Test Initiative documentation
- Kalra, N. & Paddock, S. (2016). "Driving to Safety" (RAND)
- ISO 21448 (Safety of the Intended Functionality - SOTIF)
- UL 4600 Standard for Autonomous Products

#### Connections
- See 1.4 (Traditional ML) for ML-specific evaluation
- See 4.5 (Safety Engineering) for safety analysis methods
- See 5.2 (Human-Machine Systems) for human factors in autonomy

---

### 1.4 Traditional Machine Learning Evaluation

#### Overview
The established practices for evaluating predictive ML models (classification, regression, etc.) that preceded the generative AI era. Foundational for AI evaluation but requires significant adaptation for GenAI.

#### Core Concepts

**Train/Test Split and Cross-Validation**
- Holding out data not seen during training
- K-fold cross-validation for robust estimates
- Preventing overfitting to test data

**Performance Metrics**
- Classification: accuracy, precision, recall, F1, AUC-ROC
- Regression: MSE, MAE, R²
- Metric selection based on task and costs

**Confusion Matrices and Error Analysis**
- Understanding types of errors (false positives, false negatives)
- Cost-sensitive evaluation
- Class imbalance considerations

**Generalization and Overfitting**
- Training performance vs. test performance
- Learning curves and validation curves
- Regularization and model selection

**Fairness and Bias Evaluation**
- Group fairness metrics (demographic parity, equalized odds)
- Individual fairness
- Disparate impact analysis

**Distribution Shift**
- Train/test distribution mismatch
- Covariate shift, label shift, concept drift
- Domain adaptation evaluation

**Baseline Comparisons**
- Comparing to simple baselines (random, majority class)
- Ablation studies
- Statistical significance testing

#### What Transfers

- **Hold-out principle**: Not evaluating on training data remains fundamental
- **Metric pluralism**: Using multiple metrics for different aspects of performance
- **Error analysis discipline**: Understanding not just how much error but what kind
- **Fairness evaluation**: Checking for disparate performance across groups
- **Distribution shift awareness**: Concern about evaluation data matching deployment
- **Baseline discipline**: Comparing to reasonable baselines

#### What Breaks

- **Bounded output space**: Classification/regression have bounded outputs; GenAI outputs are unbounded text
- **Clear ground truth**: Traditional ML has labeled ground truth; GenAI often has no single "correct" answer
- **Automated metrics**: Traditional ML metrics are fully automated; GenAI often requires human judgment
- **Task specificity**: Traditional ML is trained for specific tasks; GenAI is general-purpose
- **Static model assumption**: Traditional ML evaluates a fixed model; GenAI models may be updated continuously
- **IID assumptions**: Traditional ML assumes test data is IID sample; GenAI use cases may be highly variable

#### What Can Be Adapted

- **Stratified evaluation**: Evaluating performance across different subgroups/conditions
- **Calibration**: Assessing whether model confidence matches actual accuracy
- **Robustness testing**: Perturbation analysis, adversarial testing
- **Learning curve analysis**: Understanding performance as function of context/examples

#### Implications for AI Evaluation

- Hold-out principle remains essential: avoid contamination of benchmarks
- Multiple metrics needed because GenAI performance is multidimensional
- Ground truth is often unavailable; need human judgment and proxy metrics
- Evaluation must account for general-purpose nature and diverse use cases
- Continuous evaluation needed because models change

#### Key References

- Hastie, T. et al. (2009). *The Elements of Statistical Learning*
- James, G. et al. (2013). *An Introduction to Statistical Learning*
- Barocas, S. et al. (2019). *Fairness and Machine Learning*
- Koh, P.W. et al. (2021). "WILDS: A Benchmark for In-the-Wild Distribution Shift"
- Ribeiro, M.T. et al. (2020). "Beyond Accuracy: Behavioral Testing of NLP Models with CheckList"

#### Connections
- See 2.2 (Psychometrics) for human judgment in evaluation
- See 2.3 (Econometrics) for causal inference methods
- See 6.1 (AI Safety Evaluation) for safety-specific metrics

---

### 1.5 Cybersecurity Testing and Red Teaming

#### Overview
The discipline of adversarial security evaluation—systematically attempting to find vulnerabilities and bypass protections. Provides mindset and methods for adversarial AI evaluation.

#### Core Concepts

**Red Team / Blue Team / Purple Team**
- Red team: Attackers trying to find vulnerabilities
- Blue team: Defenders protecting the system
- Purple team: Collaborative improvement

**Penetration Testing**
- Systematic attempt to exploit vulnerabilities
- Scoped and authorized attack simulation
- Reporting and remediation

**Threat Modeling**
- Identifying potential attackers, motivations, capabilities
- Attack surface analysis
- Risk prioritization

**Bug Bounties and Responsible Disclosure**
- Crowdsourcing vulnerability discovery
- Coordinated disclosure practices
- Incentive structures for security research

**Zero-Day Vulnerabilities**
- Previously unknown vulnerabilities
- The challenge of unknown unknowns
- Defense in depth

**Security Testing Automation**
- Fuzzing: automated random input generation
- Static analysis: code review without execution
- Dynamic analysis: runtime testing

#### What Transfers

- **Adversarial mindset**: Actively trying to make the system fail is essential for AI
- **Red teaming methodology**: Structured adversarial evaluation with clear scope and reporting
- **Threat modeling**: Thinking about who might attack AI systems and how
- **Bug bounty model**: Crowdsourcing failure discovery; emerging in AI (e.g., DEFCON AI Village)
- **Defense in depth**: Not relying on single protection; multiple evaluation layers
- **Unknown unknowns awareness**: Security field is experienced with unforeseen vulnerabilities

#### What Breaks

- **Clear vulnerability definition**: Security has clear notion of vulnerability (unauthorized access, data exposure); AI "failures" are often fuzzy
- **Exploit reproducibility**: Security exploits are usually reproducible; AI jailbreaks may be stochastic
- **Patching**: Security vulnerabilities can be patched; AI weaknesses may be fundamental
- **Formal security properties**: Some security properties can be formally verified; AI safety properties generally cannot

#### What Can Be Adapted

- **Structured red teaming**: Scoped adversarial evaluation with clear goals and deliverables
- **Fuzzing concepts**: Automated exploration of input space; applicable to prompt testing
- **Coordinated disclosure**: Responsible reporting of AI vulnerabilities
- **Capture the flag**: Competitive security exercises; adaptable to AI safety evaluation

#### Implications for AI Evaluation

- Adopt adversarial mindset: don't just test expected uses, try to break it
- Structured red teaming should be part of high-stakes AI evaluation
- Threat modeling helps prioritize evaluation resources
- Bug bounty models may help discover failures not found by internal testing
- Expect unknown unknowns; design for resilience, not just prevention

#### Key References

- NIST SP 800-115 (Technical Guide to Information Security Testing and Assessment)
- PTES (Penetration Testing Execution Standard)
- MITRE ATT&CK Framework
- Brundage, M. et al. (2020). "Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims"
- Ganguli, D. et al. (2022). "Red Teaming Language Models to Reduce Harms"

#### Connections
- See 4.1 (Risk Analysis) for risk-based prioritization
- See 4.5 (Safety Engineering) for hazard analysis
- See 6.1 (AI Safety Evaluation) for AI-specific red teaming

---

## Section 2: Experimental and Statistical Methods

### 2.1 Experimental Design and Analysis

#### Overview
The science of designing studies to support valid causal inferences. Foundational for understanding what we can conclude from AI evaluation studies.

#### Core Concepts

**Randomized Controlled Trials (RCTs)**
- Random assignment to treatment and control
- The gold standard for causal inference
- Internal validity through randomization

**Validity Types**
- Internal validity: Can we attribute effects to the treatment?
- External validity: Do findings generalize beyond the study?
- Construct validity: Are we measuring what we intend to measure?
- Statistical conclusion validity: Are statistical inferences appropriate?

**Control and Comparison Conditions**
- Within-subject vs. between-subject designs
- Active control vs. passive control
- Placebo effects and blinding

**Confounding and Bias**
- Selection bias
- Attrition bias
- Experimenter effects
- Demand characteristics (participants guess hypothesis)

**Statistical Power and Sample Size**
- Power analysis: How many observations needed?
- Effect size estimation
- Multiple comparisons and correction

**Replication and Reproducibility**
- Direct replication vs. conceptual replication
- Reproducibility crisis lessons
- Pre-registration and registered reports

#### What Transfers

- **Validity framework**: Internal, external, construct validity distinctions directly applicable
- **Control condition thinking**: Need comparison to interpret AI effects
- **Bias awareness**: Selection, attrition, and other biases affect AI studies
- **Power analysis**: Sample size planning essential for AI evaluation
- **Pre-registration**: Committing to analysis plan in advance reduces p-hacking

#### What Breaks

- **Treatment stability**: Experiments assume stable treatment; AI systems change
- **Blinding**: Often can't blind participants to whether they're using AI
- **Replicability**: AI stochasticity and model updates make exact replication hard
- **Effect size benchmarks**: No established benchmarks for AI productivity effects
- **Lab conditions**: Lab experiments may not capture real-world AI use

#### What Can Be Adapted

- **Quasi-experimental designs**: When RCTs aren't possible (difference-in-differences, regression discontinuity)
- **Mixed methods**: Combining quantitative and qualitative approaches
- **Adaptive designs**: Modifying study based on interim results
- **N-of-1 trials**: Individual-level experimentation; relevant for personalized AI use

#### Implications for AI Evaluation

- Apply validity framework to assess AI evaluation quality
- Design comparison conditions carefully (baseline matters)
- Plan for adequate sample sizes given AI and human variability
- Consider quasi-experimental designs when RCTs aren't feasible
- Pre-register evaluation plans for high-stakes decisions

#### Key References

- Shadish, W.R. et al. (2002). *Experimental and Quasi-Experimental Designs for Generalized Causal Inference*
- Gerber, A.S. & Green, D.P. (2012). *Field Experiments: Design, Analysis, and Interpretation*
- Campbell, D.T. & Stanley, J.C. (1963). *Experimental and Quasi-Experimental Designs for Research*
- Simmons, J.P. et al. (2011). "False-Positive Psychology"

#### Connections
- See 2.2 (Psychometrics) for measurement theory
- See 2.3 (Econometrics) for causal inference methods
- See 6.2 (Program Evaluation) for field application

---

### 2.2 Psychometrics and Measurement Theory

#### Overview
The science of psychological measurement. Provides deep frameworks for understanding what it means to measure something, especially when that something is an unobservable construct like "capability" or "intelligence."

#### Core Concepts

**Reliability**
- Test-retest reliability: Consistency over time
- Inter-rater reliability: Agreement across judges
- Internal consistency: Do items measure the same thing?
- Standard error of measurement

**Validity (Expanded)**
- Content validity: Does the test cover the domain adequately?
- Criterion validity: Does the test predict relevant outcomes?
  - Concurrent: Correlation with current criterion
  - Predictive: Correlation with future criterion
- Construct validity: Does the test measure the theoretical construct?
  - Convergent: Correlates with related measures
  - Discriminant: Doesn't correlate with unrelated measures

**Classical Test Theory (CTT)**
- Observed score = True score + Error
- Reliability as ratio of true score variance to observed variance
- Standard error of measurement

**Item Response Theory (IRT)**
- Models the relationship between latent ability and item responses
- Item difficulty and discrimination
- Allows items to be on same scale
- Computer adaptive testing

**Generalizability Theory (G-Theory)**
- Multiple sources of error (raters, occasions, items)
- Partitioning variance components
- Designing efficient measurement

**Standard Setting**
- How to determine cut scores (pass/fail thresholds)
- Bookmark method, Angoff method, etc.
- Involves judgment, not just statistics

#### What Transfers

- **Reliability concepts**: Understanding sources of inconsistency in measurement
- **Validity framework**: Especially construct and predictive validity for benchmarks
- **Multiple sources of error**: Human judges vary; AI outputs vary; both contribute to measurement error
- **Content validity**: Does the benchmark adequately sample the task domain?
- **Criterion validity**: Do benchmark scores predict real-world performance?

#### What Breaks

- **Stable trait assumption**: Psychometrics assumes relatively stable traits; AI capabilities aren't stable
- **Population/norming**: Psychometric norms developed on populations; can't "norm" across AI models the same way
- **Test security assumptions**: Psychometrics assumes examinees haven't seen items; AI may have trained on benchmarks
- **Individual differences framing**: Psychometrics focuses on differences between people; AI variation is within a single "entity"

#### What Can Be Adapted

- **IRT for benchmark design**: Some items more informative than others; could optimize benchmark composition
- **G-theory for evaluation design**: Understanding variance components helps design efficient evaluation
- **Standard setting methods**: Could be adapted for determining AI capability thresholds
- **Reliability estimation**: Quantifying measurement error in AI evaluation

#### Implications for AI Evaluation

- Apply validity framework rigorously: What does the benchmark actually measure?
- Quantify and report reliability (multiple samples, multiple raters)
- Recognize that criterion validity (prediction of real-world performance) is the key question
- Use IRT thinking to design informative benchmarks
- Be aware that many psychometric assumptions don't hold

#### Key References

- Cronbach, L.J. & Meehl, P.E. (1955). "Construct Validity in Psychological Tests"
- Messick, S. (1989). "Validity" in *Educational Measurement*
- Kane, M.T. (2013). "Validating the Interpretations and Uses of Test Scores"
- Brennan, R.L. (2001). *Generalizability Theory*
- Embretson, S.E. & Reise, S.P. (2000). *Item Response Theory for Psychologists*

#### Connections
- See 2.1 (Experimental Design) for validity in experiments
- See 6.3 (Educational Measurement) for applied psychometrics
- See 2.4 (Qualitative Methods) for non-quantitative validity

---

### 2.3 Econometrics and Causal Inference

#### Overview
Statistical methods for estimating causal effects from observational data and natural experiments. Essential for understanding AI productivity effects when RCTs aren't feasible.

#### Core Concepts

**The Fundamental Problem of Causal Inference**
- Can't observe counterfactual (what would have happened without intervention)
- All causal inference methods are strategies for approximating counterfactual

**Difference-in-Differences (DiD)**
- Compare changes in treatment group to changes in control group
- Accounts for baseline differences and time trends
- Parallel trends assumption

**Regression Discontinuity (RD)**
- Exploit sharp cutoffs in treatment assignment
- Compare units just above vs. just below threshold
- Local average treatment effect

**Instrumental Variables (IV)**
- Use exogenous variation to isolate causal effect
- Addresses endogeneity and selection bias
- Requires valid instrument (strong, excludable)

**Propensity Score Methods**
- Match treatment and control on likelihood of treatment
- Reduces selection bias
- Assumes selection on observables

**Synthetic Control**
- Construct weighted combination of control units to match treatment
- Useful for case study with few treated units
- Allows for time-varying effects

**Heterogeneous Treatment Effects**
- Effects may vary across subgroups
- Conditional average treatment effects
- Machine learning for heterogeneity (causal forests, etc.)

#### What Transfers

- **Counterfactual thinking**: Essential for interpreting AI impact
- **Selection bias awareness**: Who adopts AI is not random
- **DiD design**: Useful for evaluating AI rollout effects
- **Heterogeneity analysis**: Effects of AI vary across users/contexts
- **Natural experiment mindset**: Looking for exogenous variation

#### What Breaks

- **Stable unit treatment value assumption (SUTVA)**: AI use by one person may affect others
- **Long panel data**: AI is too new for long pre/post periods
- **Clear treatment definition**: What is "using AI"? Highly variable
- **Exclusion restrictions**: Hard to find valid instruments for AI use

#### What Can Be Adapted

- **Staggered adoption designs**: Different units adopt AI at different times
- **Event study designs**: Examining effects relative to adoption date
- **Synthetic control for organizations**: Constructing comparison for AI-adopting org
- **Causal forests for heterogeneity**: ML-based heterogeneous effects estimation

#### Implications for AI Evaluation

- When RCTs aren't possible, quasi-experimental methods can provide evidence
- Selection into AI use is a major concern; must be addressed
- Look for natural experiments in AI adoption
- Analyze heterogeneity—average effects may mask important variation
- Be explicit about assumptions required for causal interpretation

#### Key References

- Angrist, J.D. & Pischke, J.S. (2009). *Mostly Harmless Econometrics*
- Cunningham, S. (2021). *Causal Inference: The Mixtape*
- Huntington-Klein, N. (2021). *The Effect: An Introduction to Research Design and Causality*
- Athey, S. & Imbens, G.W. (2017). "The State of Applied Econometrics: Causality and Policy Evaluation"

#### Connections
- See 2.1 (Experimental Design) for RCT methods
- See 3.3 (Productivity Measurement) for productivity-specific methods
- See 6.2 (Program Evaluation) for applied causal inference

---

### 2.4 Qualitative Research Methods

#### Overview
Methods for understanding phenomena through non-numerical data—interviews, observations, documents, artifacts. Essential complement to quantitative methods, especially when we don't know what questions to ask or how to measure what matters.

#### Core Concepts

**Ethnography and Participant Observation**
- Extended immersion in a setting
- Understanding practice from participants' perspective
- Rich description of context and meaning

**Interviews**
- Structured: Fixed questions, standardized
- Semi-structured: Key topics with flexibility
- Unstructured: Open-ended exploration
- Focus groups: Group discussion dynamics

**Grounded Theory**
- Building theory from data rather than testing hypotheses
- Iterative coding and constant comparison
- Theoretical sampling and saturation

**Case Study Methodology**
- In-depth study of bounded cases
- Multiple data sources
- Analytical generalization (to theory, not population)

**Thematic Analysis**
- Identifying patterns across qualitative data
- Coding and theme development
- Can be more or less theory-driven

**Process Tracing**
- Tracing causal mechanisms, not just associations
- Evidence about how X leads to Y
- Within-case analysis

**Validity in Qualitative Research**
- Credibility, transferability, dependability, confirmability
- Member checking, triangulation, thick description
- Reflexivity about researcher role

#### What Transfers

- **Understanding "why"**: Qualitative methods explain mechanisms, not just measure effects
- **Exploratory power**: Useful when we don't know what to measure
- **Context sensitivity**: Captures how AI use is situated in work practices
- **User perspective**: Understands AI use from user point of view

#### What Breaks

- **Generalization concerns**: Qualitative findings may not generalize widely
- **Resource intensity**: Deep qualitative work is time-consuming
- **Credibility for some audiences**: Some stakeholders discount qualitative evidence

#### What Can Be Adapted

- **Rapid qualitative methods**: Shortened timelines for practical application
- **Mixed methods**: Combining qualitative and quantitative
- **Evaluation-focused interviews**: Structured around evaluation questions

#### Implications for AI Evaluation

- Use qualitative methods to understand the "vibes" problem—what does quality look like?
- Observation of AI use in practice reveals things surveys and experiments miss
- Essential for understanding failed adoptions and unexpected uses
- Combine with quantitative methods for comprehensive evaluation
- Particularly valuable in early/exploratory evaluation stages

#### Key References

- Creswell, J.W. & Poth, C.N. (2018). *Qualitative Inquiry and Research Design*
- Yin, R.K. (2018). *Case Study Research and Applications*
- Miles, M.B. et al. (2014). *Qualitative Data Analysis*
- Charmaz, K. (2014). *Constructing Grounded Theory*
- Suchman, L. (1987). *Plans and Situated Actions* (for technology in context)

#### Connections
- See 5.1 (HCI/UX Research) for technology-focused qualitative methods
- See 6.2 (Program Evaluation) for evaluation-focused qualitative work
- See 2.1 (Experimental Design) for mixed methods integration

---

### 2.5 Survey Methodology

#### Overview
The science of collecting self-report data through questionnaires. Relevant to AI evaluation for measuring user experience, perceived productivity, and attitudes.

#### Core Concepts

**Questionnaire Design**
- Item wording and response options
- Question order effects
- Reducing social desirability bias
- Validated scales vs. custom items

**Sampling**
- Probability vs. non-probability sampling
- Response rates and non-response bias
- Weighting and post-stratification

**Measurement Error**
- Reliability of self-report
- Validity of survey measures
- Reference periods and recall bias

**Mixed-Mode Surveys**
- Web, phone, in-person modes
- Mode effects on responses
- Coverage error across modes

#### What Transfers

- **Questionnaire design principles**: Careful item wording reduces error
- **Validated scales**: Using established measures where available (e.g., technology acceptance scales)
- **Non-response awareness**: Who responds to AI surveys may be biased sample
- **Measurement error**: Self-reported productivity may not match actual productivity

#### What Breaks

- **Self-report accuracy for AI use**: People may not accurately report AI use patterns or effects
- **Rapidly changing context**: Standard surveys assume stable phenomena

#### What Can Be Adapted

- **Experience sampling**: Repeated brief surveys during AI use
- **Diary methods**: Users record AI use in real-time
- **Combined with behavioral data**: Survey + logs for validation

#### Implications for AI Evaluation

- User surveys are valuable but have known limitations
- Self-reported productivity gains should be validated against behavioral measures
- Consider who responds and who doesn't
- Use validated scales where available; develop new ones carefully

#### Key References

- Groves, R.M. et al. (2009). *Survey Methodology*
- Dillman, D.A. et al. (2014). *Internet, Phone, Mail, and Mixed-Mode Surveys*
- Tourangeau, R. et al. (2000). *The Psychology of Survey Response*

#### Connections
- See 2.2 (Psychometrics) for measurement theory
- See 5.1 (HCI/UX) for user experience measurement
- See 3.3 (Productivity) for productivity self-report issues

---

## Section 3: Economics and Productivity

### 3.1 Information Systems Economics

#### Overview
The study of how information technology affects organizations and economies. Provides frameworks for understanding AI's organizational impacts.

#### Core Concepts

**IT Productivity Paradox**
- "You can see the computer age everywhere but in the productivity statistics" (Solow)
- IT investments didn't show productivity gains for decades
- Resolution: complementary investments (reorg, skills, processes) needed

**Complementary Investments**
- IT gains require organizational restructuring
- Skills, processes, culture must co-evolve
- Explains lag between adoption and benefits

**Task-Technology Fit**
- Performance depends on match between task and technology
- Not all tasks benefit equally from IT
- User characteristics also matter

**IT Business Value**
- Process-level vs. firm-level impacts
- Intermediate measures vs. ultimate outcomes
- Measurement challenges

**Digital Transformation**
- IT as enabler of fundamental change, not just efficiency
- New capabilities, not just faster old ones
- Organizational redesign implications

#### What Transfers

- **Productivity paradox awareness**: Don't expect immediate measured productivity gains from AI
- **Complementary investments**: AI gains will require other investments
- **Task-technology fit**: AI will help some tasks more than others
- **Measurement challenges**: IT productivity measurement is hard; AI is harder
- **Transformation vs. efficiency**: AI may enable new things, not just speed up old

#### What Breaks

- **Slower IT change**: Historical IT changed slowly compared to AI
- **Clearer IT capabilities**: IT capabilities were more predictable
- **IT-specific methods**: Some IS research methods assume IT-specific contexts

#### Implications for AI Evaluation

- Don't expect AI to show productivity gains immediately
- Budget for complementary investments (training, reorg, process change)
- Measure at multiple levels (task, process, firm)
- Consider new capabilities, not just efficiency gains
- Learn from IT productivity research about patience and prerequisites

#### Key References

- Brynjolfsson, E. (1993). "The Productivity Paradox of Information Technology"
- Brynjolfsson, E. & Hitt, L. (2000). "Beyond Computation: IT, Organizational Transformation and Business Performance"
- Melville, N. et al. (2004). "Review: IT and Organizational Performance"
- Aral, S. et al. (2012). "Three-Way Complementarities: Performance Pay, Human Resource Analytics, and Information Technology"

#### Connections
- See 3.2 (Productivity Measurement) for measurement methods
- See 3.4 (Organizational Behavior) for organizational change
- See 5.3 (IS Implementation) for implementation factors

---

### 3.2 Productivity Measurement and Economics

#### Overview
The economics of measuring output per input. Foundational for understanding claims about AI productivity gains.

#### Core Concepts

**Productivity Definitions**
- Labor productivity: Output per worker or per hour
- Total Factor Productivity (TFP): Output beyond explained by inputs
- Multifactor productivity: Accounts for multiple inputs

**Output Measurement Challenges**
- Manufacturing: Relatively clear (units produced)
- Services: Harder (what's the "output" of a consultant?)
- Knowledge work: Very hard (what's the "output" of research?)
- Quality adjustment: More output isn't better if quality drops

**Input Measurement**
- Hours worked vs. effort
- Capital services vs. capital stock
- Intangible inputs (data, software, organizational capital)

**Aggregation Issues**
- Firm-level vs. industry-level vs. economy-level
- Composition effects (shifts between high/low productivity units)
- Baumol's cost disease

**Long-run vs. Short-run**
- Short-run: Utilization effects, learning curves
- Long-run: Structural productivity growth
- Adjustment periods between

**Macro vs. Micro Evidence**
- Macro: Economy-wide productivity trends
- Micro: Firm or worker-level productivity studies
- Reconciliation challenges

#### What Transfers

- **Output measurement awareness**: Productivity claims require credible output measures
- **Quality adjustment**: Must account for quality changes
- **Aggregation concerns**: Task-level ≠ firm-level ≠ economy-level
- **Long-run perspective**: Effects take time to materialize
- **TFP concept**: Understanding productivity beyond simple output/input

#### What Breaks

- **Clear output for AI-assisted work**: Even harder to define than typical knowledge work
- **Existing measurement systems**: Built for manufacturing and traditional services
- **Time series**: AI is too new for long-term productivity data

#### Implications for AI Evaluation

- Be very careful about productivity claims; measurement is hard
- Define output measures clearly and acknowledge limitations
- Don't assume task-level gains aggregate to firm-level gains
- Quality matters; adjust for it or acknowledge you're not
- Allow for long-run effects; short-term may underestimate or overestimate

#### Key References

- Syverson, C. (2011). "What Determines Productivity?"
- Diewert, W.E. (1976). "Exact and Superlative Index Numbers"
- Nordhaus, W.D. (2007). "Two Centuries of Productivity Growth in Computing"
- Byrne, D.M. et al. (2016). "Does the United States Have a Productivity Slowdown or a Measurement Problem?"
- Brynjolfsson, E. et al. (2021). "The Economics of AI" (NBER)

#### Connections
- See 3.1 (IS Economics) for IT productivity paradox
- See 2.3 (Econometrics) for causal inference
- See Report Part 2 for AI-specific productivity studies

---

### 3.3 Cost Analysis and Investment Evaluation

#### Overview
Methods for analyzing costs and evaluating investments, particularly for technology. Relevant to understanding AI acquisition economics.

#### Core Concepts

**Total Cost of Ownership (TCO)**
- All costs over system lifetime
- Direct and indirect costs
- Hidden costs and cost drivers

**Cost-Benefit Analysis (CBA)**
- Comparing costs to benefits in common units
- Net present value
- Dealing with uncertainty and intangibles

**Return on Investment (ROI)**
- Ratio of benefits to costs
- Payback period
- Risk-adjusted returns

**Real Options Analysis**
- Value of flexibility under uncertainty
- Option to expand, abandon, wait
- Stage-gate investments

**Learning Curves**
- Costs decrease with experience
- Implications for timing
- Firm-specific vs. industry learning

**Sunk Costs and Lock-in**
- Sunk costs are sunk; shouldn't affect future decisions
- Switching costs and lock-in effects
- Vendor lock-in concerns

#### What Transfers

- **TCO thinking**: Full cost accounting including hidden costs
- **CBA framework**: Structured comparison of costs and benefits
- **Real options**: Value of flexibility when AI is uncertain
- **Learning curve awareness**: Costs of using AI decrease with experience
- **Lock-in concerns**: Vendor and technology lock-in relevant

#### What Breaks

- **Quantifiable benefits**: AI benefits often hard to quantify
- **Stable cost structures**: AI costs (especially usage-based) may be unpredictable
- **Comparable alternatives**: May lack good comparison cases

#### Implications for AI Evaluation

- Account for full costs including training, QA, adaptation
- Acknowledge difficulty quantifying benefits; use ranges and scenarios
- Value flexibility; avoid premature lock-in
- Consider learning curve; early costs may not reflect steady-state
- Evaluation costs are part of TCO; budget for them

#### Key References

- Ellram, L. (1995). "Total Cost of Ownership: An Analysis Approach for Purchasing"
- Boardman, A. et al. (2017). *Cost-Benefit Analysis: Concepts and Practice*
- Dixit, A.K. & Pindyck, R.S. (1994). *Investment Under Uncertainty*

#### Connections
- See 3.1 (IS Economics) for IT investment research
- See 4.1 (Risk Analysis) for risk assessment
- See Report Part 4 for acquisition guidance

---

## Section 4: Risk, Quality, and Assurance

### 4.1 Risk Analysis and Management

#### Overview
Systematic approaches to identifying, assessing, and managing risks. Foundational for risk-based AI evaluation planning.

#### Core Concepts

**Risk Identification**
- Hazard analysis, threat modeling
- Brainstorming and checklists
- Historical incident analysis

**Risk Assessment**
- Probability × Impact frameworks
- Qualitative (high/medium/low) vs. quantitative
- Risk matrices and heat maps

**Risk Prioritization**
- Expected value ranking
- Risk tolerance and appetite
- Focus on high-consequence risks

**Risk Mitigation**
- Accept, avoid, transfer, mitigate
- Controls and countermeasures
- Defense in depth

**Residual Risk**
- Risk remaining after mitigation
- Must be accepted, not ignored
- Monitored and managed

**Risk Monitoring**
- Key risk indicators
- Trigger points and escalation
- Regular risk reviews

**Enterprise Risk Management (ERM)**
- Organization-wide risk perspective
- Risk culture and governance
- Integration with strategy

**Probabilistic Risk Assessment (PRA)**
- Quantitative risk analysis
- Fault trees, event trees
- Common in nuclear, aerospace

#### What Transfers

- **Structured risk identification**: Systematic approach to finding risks
- **Risk assessment frameworks**: Probability × Impact and similar
- **Risk-based prioritization**: Focus evaluation on highest-risk areas
- **Residual risk concept**: Evaluation reduces but doesn't eliminate risk
- **Risk monitoring**: Ongoing risk tracking post-deployment

#### What Breaks

- **Probability estimation**: AI failure probabilities hard to estimate
- **Enumerable failures**: AI failures may be unforeseen
- **Independence assumptions**: AI risks may be correlated
- **Historical data**: Limited history for AI risk estimation

#### What Can Be Adapted

- **PRA for AI**: Active research area on adapting PRA methods
- **Scenario-based risk assessment**: Using scenarios rather than probabilities
- **Red team risk discovery**: Adversarial methods to find risks

#### Implications for AI Evaluation

- Use risk frameworks to prioritize evaluation effort
- Higher stakes → more rigorous evaluation
- Accept that risk can't be eliminated; characterize residual risk
- Plan for ongoing risk monitoring
- Adapt traditional frameworks for AI's novel risk properties

#### Key References

- ISO 31000 (Risk Management)
- NIST AI Risk Management Framework
- Kaplan, S. & Garrick, B.J. (1981). "On the Quantitative Definition of Risk"
- Hubbard, D.W. (2020). *The Failure of Risk Management*
- [2504.18536] "Adapting Probabilistic Risk Assessment for AI"

#### Connections
- See 1.5 (Cybersecurity) for adversarial risk
- See 4.5 (Safety Engineering) for safety-specific risk
- See Report Part 4 for risk-based evaluation planning

---

### 4.2 Reliability Engineering

#### Overview
Engineering discipline focused on ensuring systems perform their required functions over time. Relevant to understanding AI system reliability and monitoring.

#### Core Concepts

**Reliability Definitions**
- Probability of successful operation over time
- Mean Time Between Failures (MTBF)
- Mean Time To Repair (MTTR)

**Failure Modes and Effects Analysis (FMEA)**
- Systematic identification of failure modes
- Effects of each failure
- Prioritization for mitigation

**Reliability Prediction**
- Estimating failure rates before deployment
- Component-based prediction
- Environmental and stress factors

**Reliability Growth**
- Systems become more reliable as failures are found and fixed
- Duane model, AMSAA model
- Test-fix-test cycles

**Bathtub Curve**
- Failure rate over lifetime
- Early life (infant mortality), useful life, wear-out
- Different failure mechanisms in each phase

**Accelerated Life Testing**
- Stressing systems to reveal failures faster
- Temperature, vibration, etc.
- Inference from accelerated to normal conditions

**Common Cause Failures**
- Multiple components failing from same cause
- Design dependencies, shared environments
- Particularly important for redundant systems

**Availability and Maintainability**
- Availability = Uptime / (Uptime + Downtime)
- Maintainability: Ease of repair
- Design for serviceability

#### What Transfers

- **Failure mode thinking**: Systematically considering how AI can fail
- **Reliability monitoring**: Tracking performance over time
- **Common cause awareness**: AI systems may have correlated failures
- **Availability concepts**: Uptime and accessibility considerations

#### What Breaks

- **Predictable failure distributions**: AI failures don't follow typical reliability distributions
- **Component-based modeling**: AI isn't modular in the same way
- **Physical failure mechanisms**: AI "fails" differently than hardware
- **Wear-out**: AI doesn't wear out in traditional sense (but may degrade differently)

#### What Can Be Adapted

- **FMEA for AI**: Identifying failure modes and their effects
- **Reliability growth tracking**: Monitoring improvement over time
- **Stress testing**: Adversarial and edge-case testing as accelerated testing
- **Availability monitoring**: Tracking AI system uptime and responsiveness

#### Implications for AI Evaluation

- Think systematically about failure modes
- Monitor for performance degradation over time
- Be aware of common cause failure risks (shared training, shared infrastructure)
- Adapt reliability concepts rather than apply directly

#### Key References

- O'Connor, P.D.T. & Kleyner, A. (2011). *Practical Reliability Engineering*
- MIL-HDBK-217 (Reliability Prediction)
- Blischke, W.R. & Murthy, D.N.P. (2000). *Reliability: Modeling, Prediction, and Optimization*

#### Connections
- See 4.1 (Risk Analysis) for risk-based prioritization
- See 4.3 (Quality Management) for ongoing monitoring
- See 4.5 (Safety Engineering) for safety-critical reliability

---

### 4.3 Quality Management

#### Overview
Systematic approaches to ensuring and improving quality. Relevant to continuous monitoring and improvement of AI systems.

#### Core Concepts

**Statistical Process Control (SPC)**
- Monitoring process outputs over time
- Control charts and control limits
- Distinguishing common cause from special cause variation

**Process Capability**
- Whether process can meet specifications
- Capability indices (Cp, Cpk)
- Relationship to defect rates

**Total Quality Management (TQM)**
- Organization-wide quality focus
- Customer focus, continuous improvement
- Employee involvement

**Six Sigma**
- Statistical approach to reducing defects
- DMAIC (Define, Measure, Analyze, Improve, Control)
- Data-driven problem solving

**Continuous Improvement**
- Kaizen and incremental improvement
- PDCA (Plan, Do, Check, Act) cycle
- Learning from defects and variation

**Root Cause Analysis**
- Going beyond symptoms to underlying causes
- 5 Whys, fishbone diagrams
- Corrective and preventive action

**Quality Audits**
- Independent assessment of quality systems
- Internal and external audits
- Compliance and improvement focus

#### What Transfers

- **SPC for monitoring**: Control charts applicable to AI performance metrics
- **Continuous improvement mindset**: AI systems should improve over time
- **Root cause thinking**: Understanding why AI fails, not just that it fails
- **Audit discipline**: Regular independent assessment

#### What Breaks

- **Clear specifications**: Quality traditionally means meeting specs; AI "specs" are fuzzy
- **Observable processes**: AI processing is opaque
- **Root cause tractability**: Hard to identify root causes of AI failures
- **Stable processes**: AI systems may not be stable

#### What Can Be Adapted

- **Control charts for AI metrics**: Monitoring output quality, response time, etc.
- **DMAIC for AI improvement**: Structured improvement methodology
- **AI-adapted audits**: Regular assessment of AI performance and use

#### Implications for AI Evaluation

- Apply SPC concepts to continuous AI monitoring
- Establish control limits for key metrics
- Use improvement cycles to enhance AI use over time
- Adapt root cause analysis for AI context
- Build quality mindset into AI deployment

#### Key References

- Montgomery, D.C. (2019). *Introduction to Statistical Quality Control*
- Juran, J.M. & De Feo, J.A. (2010). *Juran's Quality Handbook*
- ISO 9001 (Quality Management Systems)
- Wheeler, D.J. (2000). *Understanding Variation*

#### Connections
- See 4.2 (Reliability) for reliability monitoring
- See 4.4 (Audit) for assessment methods
- See Report Part 4 for continuous monitoring recommendations

---

### 4.4 Audit and Assurance

#### Overview
Systematic methods for providing independent assurance that something is as claimed. Relevant to AI evaluation governance and third-party assessment.

#### Core Concepts

**Audit Objectives**
- Providing reasonable assurance
- Opinion on compliance, accuracy, or effectiveness
- Varying levels of assurance

**Audit Methodology**
- Planning and risk assessment
- Evidence gathering
- Testing and sampling
- Reporting and opinion

**Independence and Objectivity**
- Auditor independence from auditee
- Avoiding conflicts of interest
- Professional skepticism

**Materiality**
- Focusing on what matters
- Not everything needs equal scrutiny
- Risk-based scoping

**Audit Evidence**
- Types of evidence (documentary, observational, testimonial)
- Sufficiency and appropriateness
- Corroboration and triangulation

**Audit Sampling**
- Statistical and non-statistical sampling
- Sample size and selection
- Inference from sample to population

**Attestation Standards**
- What it means to "certify" or "attest"
- Levels of assurance
- Reporting standards

**Three Lines of Defense Model**
- First line: Management controls
- Second line: Risk management and compliance
- Third line: Internal audit
- External audit beyond

#### What Transfers

- **Independence principle**: Separation between vendor/developer and evaluator
- **Materiality concept**: Focus evaluation on what matters
- **Evidence standards**: Rigor in gathering and assessing evidence
- **Three lines model**: Layered assurance structure
- **Professional skepticism**: Not taking claims at face value

#### What Breaks

- **Established standards**: Financial audit has mature standards; AI audit is emerging
- **Clear assertions**: Financial statements have defined assertions; AI claims are fuzzier
- **Audit trail**: Traditional systems have clear trails; AI processing is opaque
- **Sampling applicability**: Traditional sampling may not work for AI's unbounded output space

#### What Can Be Adapted

- **Algorithmic auditing**: Emerging field adapting audit concepts for AI
- **Risk-based audit planning**: Focusing on high-risk AI applications
- **Evidence triangulation**: Multiple sources of evidence about AI performance

#### Implications for AI Evaluation

- Apply independence principle: vendor self-evaluation is insufficient for high stakes
- Use materiality thinking to scope evaluation
- Develop evidence standards for AI evaluation
- Consider three lines model for organizational AI governance
- Draw on emerging algorithmic auditing methods

#### Key References

- AICPA Audit Standards
- IIA (Institute of Internal Auditors) Standards
- ISO 19011 (Auditing Management Systems)
- Raji, I.D. et al. (2020). "Closing the AI Accountability Gap"
- Mökander, J. et al. (2022). "Auditing Large Language Models"

#### Connections
- See 4.1 (Risk) for risk-based scoping
- See 6.1 (AI Safety) for AI-specific audit approaches
- See Report Part 4 for governance recommendations

---

### 4.5 Safety Engineering

#### Overview
Engineering discipline focused on preventing hazards and ensuring safety. Relevant to AI evaluation for safety-critical applications.

#### Core Concepts

**Hazard Analysis**
- Systematic identification of hazards
- Hazard: condition that could lead to harm
- Distinction from risk (hazard + exposure + consequence)

**Fault Tree Analysis (FTA)**
- Top-down analysis of failure causes
- Boolean logic structure
- Quantitative or qualitative

**Event Tree Analysis (ETA)**
- Forward-looking analysis of event sequences
- Branching probabilities
- Consequence estimation

**HAZOP (Hazard and Operability Study)**
- Structured brainstorming with guide words
- Designed for process industries
- Systematic deviation analysis

**System-Theoretic Process Analysis (STPA)**
- Based on systems theory, not component failure
- Focus on unsafe control actions
- Considers system interactions and emergent properties

**Safety Cases**
- Structured arguments that system is safe
- Claims, evidence, and argument structure
- Goal structuring notation (GSN)
- Increasingly adopted for AI

**Functional Safety**
- Safety through proper function of safety-related systems
- IEC 61508 and derivatives
- Safety Integrity Levels (SIL)

**Fail-Safe and Fail-Secure**
- How system behaves when it fails
- Designing for graceful degradation
- Human oversight requirements

#### What Transfers

- **Hazard analysis mindset**: Systematically identifying how AI could cause harm
- **Safety case methodology**: Structured safety argumentation applicable to AI
- **STPA approach**: System-theoretic perspective fits human-AI systems
- **Fail-safe thinking**: Designing for AI failure scenarios
- **Human oversight**: Role of humans in safety-critical AI use

#### What Breaks

- **Component failure models**: AI doesn't fail like hardware components
- **Quantitative failure rates**: AI failure probabilities hard to estimate
- **Clear safety functions**: AI's role in safety may be diffuse
- **Certification paradigm**: Traditional certification approaches may not apply

#### What Can Be Adapted

- **STPA for AI**: Analyzing AI as part of control structure
- **Safety cases for AI**: Active development in AI safety community
- **Functional safety concepts**: Adapting for learning-enabled systems

#### Implications for AI Evaluation

- For safety-critical applications, apply safety engineering methods
- Develop safety cases for high-stakes AI deployments
- Use STPA to understand human-AI control structure
- Design for AI failure: monitoring, override, fallback
- Draw on emerging AI safety case literature

#### Key References

- Leveson, N.G. (2011). *Engineering a Safer World*
- IEC 61508 (Functional Safety)
- ISO 26262 (Automotive Functional Safety)
- Bloomfield, R. & Bishop, P. (2010). "Safety and Assurance Cases"
- CLTC "Assessing confidence in frontier AI safety cases" [2502.05791]

#### Connections
- See 1.3 (Autonomous Systems) for autonomous safety evaluation
- See 4.1 (Risk) for risk assessment
- See 6.1 (AI Safety) for AI-specific safety evaluation

---

## Section 5: Human and Organizational Factors

### 5.1 Human-Computer Interaction and User Experience Research

#### Overview
Study of how people interact with computers and technology. Provides methods for understanding how people actually use AI systems.

#### Core Concepts

**Usability**
- Effectiveness, efficiency, satisfaction
- Learnability and memorability
- Error rates and recovery

**User-Centered Design**
- Understanding users and their needs
- Iterative design with user feedback
- Evaluation throughout development

**Usability Evaluation Methods**
- Heuristic evaluation: Expert review against principles
- Cognitive walkthrough: Stepping through tasks as user would
- Usability testing: Observing real users with tasks

**Contextual Inquiry**
- Studying work in its natural context
- Observation + interview hybrid
- Understanding practice, not just opinions

**Task Analysis**
- Hierarchical Task Analysis (HTA): Breaking tasks into subtasks
- Cognitive Task Analysis (CTA): Understanding cognitive demands
- Understanding work structure

**Mental Models**
- Users' understanding of how systems work
- Mismatches between mental model and actual system
- Design to support accurate mental models

**Affordances and Signifiers**
- What actions a system allows/suggests
- How design communicates possibilities
- Discoverability and feedback

**Situated Action**
- Action is always situated in context
- Can't fully specify procedures in advance
- Users improvise with resources at hand

#### What Transfers

- **Usability evaluation methods**: Applicable to AI interfaces
- **Contextual inquiry**: Essential for understanding real AI use
- **Task analysis**: Understanding work AI is meant to support
- **Mental model concept**: Users' understanding of AI matters
- **Situated action perspective**: AI use is improvised in context

#### What Breaks

- **Clear task definition**: HCI often assumes defined tasks; AI use is more open-ended
- **Consistent system behavior**: Usability assumes consistent responses; AI is variable
- **Error definition**: What's an "error" when AI output is probabilistic?

#### What Can Be Adapted

- **Think-aloud with AI**: Users narrate as they work with AI
- **Diary studies**: Users record AI use over time
- **Contextual inquiry for AI**: Observing real AI use in context

#### Implications for AI Evaluation

- Use HCI methods to understand how people actually use AI
- Don't just measure outcomes; understand the process
- Pay attention to mental models—do users understand AI capabilities and limits?
- Recognize that AI use is situated and variable

#### Key References

- Nielsen, J. (1994). *Usability Engineering*
- Beyer, H. & Holtzblatt, K. (1998). *Contextual Design*
- Suchman, L. (1987). *Plans and Situated Actions*
- Norman, D. (2013). *The Design of Everyday Things*
- Amershi, S. et al. (2019). "Guidelines for Human-AI Interaction"

#### Connections
- See 2.4 (Qualitative Methods) for research methods
- See 5.2 (Human Factors) for cognitive aspects
- See 5.4 (JDM) for decision aspects

---

### 5.2 Human Factors and Human-Machine Systems

#### Overview
The study of how humans interact with systems, emphasizing capabilities and limitations of human performance. Foundational for human-AI teaming evaluation.

#### Core Concepts

**Human Information Processing**
- Perception, cognition, response
- Attention and working memory limits
- Decision making under uncertainty

**Workload**
- Mental and physical demands
- Overload and underload effects
- Workload assessment methods (NASA-TLX, etc.)

**Situation Awareness**
- Perception of elements in environment
- Comprehension of their meaning
- Projection of future status
- SA measurement methods

**Trust in Automation**
- Factors affecting trust (reliability, predictability, etc.)
- Overtrust (complacency) and undertrust (disuse)
- Trust calibration: matching trust to actual reliability

**Automation Surprises**
- Unexpected automation behavior
- "What's it doing?" "Why did it do that?" "What will it do next?"
- Mode confusion and mode errors

**Levels of Automation**
- Sheridan & Verplank's 10 levels
- Parasuraman's 4-stage model (acquisition, analysis, decision, action)
- Human-in-the-loop, on-the-loop, out-of-the-loop

**Human-Automation Function Allocation**
- Deciding what human does vs. what automation does
- Fitts' List and its limitations
- Dynamic allocation

**Skill Degradation**
- Skills may atrophy when automation takes over
- Implications for human backup capability
- "Out of the loop" performance decrement

#### What Transfers

- **Trust calibration research**: Directly applicable to AI
- **Automation surprises**: AI creates many surprises (jagged frontier)
- **Situation awareness**: Relevant to human-AI teaming
- **Workload concepts**: AI may reduce or increase workload
- **Levels of automation**: Useful framework though imperfect fit

#### What Breaks

- **Predictable automation**: Traditional automation is more predictable than AI
- **Defined interfaces**: AI interaction is often conversational, not button-based
- **Stable allocation**: Function allocation with AI may be dynamic and unclear
- **Skill categories**: Traditional skill taxonomies may not capture "AI skill"

#### What Can Be Adapted

- **Trust measurement for AI**: Adapting trust scales and methods
- **Automation surprise analysis**: Documenting and analyzing AI surprises
- **SA for AI teaming**: Assessing situation awareness in human-AI teams

#### Implications for AI Evaluation

- Evaluate human-AI team, not just AI capability
- Assess trust calibration: are users appropriately trusting/skeptical?
- Monitor for automation surprises and their effects
- Consider workload effects (may not be simple reduction)
- Apply levels of automation thinking to AI integration

#### Key References

- Parasuraman, R. & Riley, V. (1997). "Humans and Automation: Use, Misuse, Disuse, Abuse"
- Lee, J.D. & See, K.A. (2004). "Trust in Automation"
- Endsley, M.R. (2016). *Designing for Situation Awareness*
- Billings, C.E. (1997). *Aviation Automation*
- Sheridan, T.B. (2002). *Humans and Automation: System Design and Research Issues*

#### Connections
- See 1.3 (Autonomous Systems) for autonomous systems evaluation
- See 5.4 (JDM) for decision making
- See Report Part 3 for human-AI teaming framework

---

### 5.3 Organizational Behavior and Change Management

#### Overview
Study of how organizations function and how to manage organizational change. Essential for understanding AI adoption and implementation.

#### Core Concepts

**Technology Adoption Models**
- Technology Acceptance Model (TAM): Perceived usefulness + ease of use
- Diffusion of Innovations: Adoption curves, adopter categories
- TOE Framework: Technology, Organization, Environment factors

**Absorptive Capacity**
- Organization's ability to recognize, assimilate, apply new knowledge
- Depends on prior knowledge and learning capabilities
- Affects ability to benefit from AI

**Organizational Change Models**
- Lewin: Unfreeze, Change, Refreeze
- Kotter's 8 Steps
- ADKAR (Awareness, Desire, Knowledge, Ability, Reinforcement)

**Resistance to Change**
- Sources: uncertainty, loss of control, competence concerns
- Strategies: communication, participation, support
- Legitimate concerns vs. resistance per se

**Organizational Culture**
- Shared values, beliefs, practices
- Culture-technology fit
- Innovation culture

**Organizational Learning**
- Single-loop vs. double-loop learning
- Learning from failure
- Knowledge management

**Implementation Research**
- Why implementations succeed or fail
- Implementation fidelity
- Critical success factors

#### What Transfers

- **Adoption models**: Understanding what drives AI adoption
- **Change management**: AI adoption is organizational change
- **Absorptive capacity**: Organizations differ in ability to use AI
- **Implementation research**: Insights on why tech implementations fail

#### What Breaks

- **Slower change context**: Traditional change models assumed slower change
- **Clearer technology**: AI is more ambiguous than typical IT
- **Stable technology**: AI changes during adoption

#### What Can Be Adapted

- **Adoption models for AI**: Extending TAM and DOI for AI
- **Agile change management**: Iterative approach fitting AI pace
- **Learning organization for AI**: Building ongoing AI learning capability

#### Implications for AI Evaluation

- Evaluation results depend on organizational context
- Failed pilots may reflect change management, not AI failure
- Consider organizational readiness before expecting benefits
- Support ongoing organizational learning about AI
- Draw on implementation research for deployment planning

#### Key References

- Rogers, E.M. (2003). *Diffusion of Innovations*
- Venkatesh, V. et al. (2003). "User Acceptance of Information Technology"
- Kotter, J.P. (2012). *Leading Change*
- Tornatzky, L.G. & Fleischer, M. (1990). *The Processes of Technological Innovation*
- Edmondson, A.C. (2018). *The Fearless Organization*

#### Connections
- See 3.1 (IS Economics) for IT adoption research
- See 6.2 (Program Evaluation) for implementation evaluation
- See Report Part 4 for deployment recommendations

---

### 5.4 Judgment and Decision Making (JDM)

#### Overview
The study of how people make judgments and decisions, including systematic biases. Relevant to understanding how humans use (and misuse) AI advice.

#### Core Concepts

**Heuristics and Biases**
- Cognitive shortcuts that usually work but can lead to errors
- Availability, representativeness, anchoring, etc.
- Bounded rationality

**Algorithm Aversion**
- Resistance to using algorithms even when they outperform humans
- Seeing algorithm err reduces trust more than seeing human err
- Desire for control and understanding

**Algorithm Appreciation**
- The flip side: over-reliance on algorithmic advice
- Automation bias: accepting recommendations uncritically
- Varies by context and individual

**Advice Taking and Discounting**
- Judge-Advisor Systems (JAS) paradigm
- People typically discount advice (weight < 50%)
- Factors: perceived expertise, confidence, match to prior beliefs

**Calibration**
- Match between confidence and accuracy
- Overconfidence is common
- Calibration training can help

**Noise**
- Variability in judgments that should be identical
- Distinct from bias (systematic error)
- Noise in expert judgment is substantial

**Dual Process Theory**
- System 1: Fast, intuitive, automatic
- System 2: Slow, deliberate, effortful
- When each system is engaged

**Decision Hygiene**
- Practices to reduce noise and bias
- Structured decisions, independent judgments, aggregation
- Checklists and guidelines

#### What Transfers

- **Bias awareness**: Evaluators and users subject to biases
- **Algorithm aversion/appreciation**: Affects AI adoption and use
- **Advice taking**: AI as advisor; users discount or accept
- **Calibration**: Both AI and human calibration matter
- **Noise**: Human judgment in evaluation is noisy
- **Decision hygiene**: Structured evaluation reduces error

#### What Breaks

- **Static advice context**: JDM studied one-shot advice; AI interaction is iterative
- **Human advisor models**: AI is different kind of "advisor"

#### What Can Be Adapted

- **Calibration training for AI use**: Teaching appropriate trust
- **Decision hygiene for AI evaluation**: Structuring evaluation judgments
- **Bias awareness training**: For both users and evaluators

#### Implications for AI Evaluation

- Human evaluators of AI are subject to biases; design to minimize
- Users may over- or under-rely on AI; evaluate for appropriate reliance
- Noise in human judgment affects evaluation reliability
- Structure evaluation processes to reduce noise and bias
- Consider training for calibrated AI use

#### Key References

- Kahneman, D. (2011). *Thinking, Fast and Slow*
- Kahneman, D., Sibony, O., & Sunstein, C.R. (2021). *Noise*
- Dietvorst, B.J. et al. (2015). "Algorithm Aversion"
- Logg, J.M. et al. (2019). "Algorithm Appreciation"
- Bonaccio, S. & Dalal, R.S. (2006). "Advice Taking and Decision-Making"

#### Connections
- See 5.2 (Human Factors) for automation trust
- See 2.2 (Psychometrics) for measurement
- See 2.1 (Experimental Design) for bias reduction

---

### 5.5 Industrial-Organizational (I-O) Psychology

#### Overview
Psychology applied to workplace settings. Provides frameworks for personnel selection, performance appraisal, and training that inform the "alien intern" framing.

#### Core Concepts

**Job Analysis**
- Systematic study of job requirements
- Tasks, KSAOs (Knowledge, Skills, Abilities, Other characteristics)
- Foundation for selection and training

**Personnel Selection**
- Predictors of job performance
- Selection methods (tests, interviews, work samples, etc.)
- Validity and fairness of selection

**Validity Generalization**
- Do selection tests predict performance across contexts?
- Meta-analytic findings: some generalization, some context-dependence
- Situational specificity vs. generalizability

**Criterion Problem**
- What is "good performance"? Harder than it seems
- Ultimate vs. immediate criteria
- Criterion deficiency and contamination

**Structured vs. Unstructured Assessment**
- Structured interviews outperform unstructured
- Rating scales with behavioral anchors
- Reduces evaluator variability

**Performance Appraisal**
- Methods for evaluating job performance
- Rating biases (halo, leniency, recency)
- Multi-source feedback (360-degree)

**Training and Development**
- Kirkpatrick's four levels (Reaction, Learning, Behavior, Results)
- Training transfer
- Needs assessment

**Assessment Centers**
- Multi-method, multi-rater evaluation
- Simulations and exercises
- For complex jobs where tests aren't enough

#### What Transfers

- **Selection research insights**: What predicts performance? Implications for AI assessment
- **Criterion problem**: Relevant to AI evaluation—what is "good"?
- **Structured evaluation**: Reduces noise and bias in AI assessment
- **Training framework**: Kirkpatrick applicable to AI training evaluation
- **Assessment center model**: Multi-method AI evaluation

#### What Breaks

- **Human-centric**: I-O psychology is about humans; AI is different
- **Stable traits**: I-O psychology assumes relatively stable individual differences
- **Selection context**: "Hiring" AI is different from hiring people

#### What Can Be Adapted

- **Job analysis for AI**: What tasks should AI do? What capabilities needed?
- **Assessment center for AI**: Multiple methods to evaluate AI "candidate"
- **Training evaluation for AI users**: Kirkpatrick for AI training programs
- **Structured rating scales**: For human evaluation of AI outputs

#### Implications for AI Evaluation

- The "hiring" metaphor is useful: interview the AI before deploying
- Structured evaluation methods outperform unstructured "vibes"
- The criterion problem is central: what is good AI performance?
- Multi-method evaluation (like assessment centers) increases validity
- Apply training evaluation frameworks to AI user training

#### Key References

- Schmidt, F.L. & Hunter, J.E. (1998). "The Validity and Utility of Selection Methods in Personnel Psychology"
- Cascio, W.F. & Aguinis, H. (2019). *Applied Psychology in Talent Management*
- Campion, M.A. et al. (1997). "A Review of Structure in the Selection Interview"
- Kirkpatrick, J.D. & Kirkpatrick, W.K. (2016). *Kirkpatrick's Four Levels of Training Evaluation*

#### Connections
- See 2.2 (Psychometrics) for measurement
- See 3.2 (Productivity) for output measurement
- See Report Part 3 for human analogy framework

---

## Section 6: Evaluation and Assessment Traditions

### 6.1 AI Safety Evaluation (Emerging Field)

#### Overview
The emerging discipline focused on evaluating AI systems for safety properties. Directly relevant though still developing.

#### Core Concepts

**Capability Evaluation**
- What can the model do?
- Dangerous capabilities (cyber, bio, etc.)
- Capability elicitation methods

**Alignment Evaluation**
- Does the model behave as intended?
- Value alignment, goal alignment
- Reward hacking detection

**Red Teaming for AI**
- Adversarial probing for harmful outputs
- Jailbreaking and prompt injection
- Structured red team methodology

**Safety Cases for AI**
- Structured arguments for safety
- Claims, evidence, argument
- Emerging methodologies

**Deceptive Alignment and Scheming**
- Could AI appear aligned while not being so?
- Evaluation for deceptive behaviors
- Emerging research area

**Robustness Evaluation**
- Performance under distribution shift
- Adversarial robustness
- Out-of-distribution detection

**Evaluation Gaming**
- AI behaving differently when being evaluated
- Training on evaluation data
- Implications for benchmark validity

#### What Transfers

Everything here is directly relevant—this is the emerging field.

#### Key Active Areas

- Benchmark design and contamination detection
- Scalable oversight and interpretability
- Dangerous capability evaluation
- Safety case methodology
- Continuous monitoring approaches
- Red teaming methodology development

#### Key References

- Anthropic, OpenAI, DeepMind safety reports and research
- METR evaluation methodology
- Shevlane, T. et al. (2023). "Model Evaluation for Extreme Risks"
- [2502.05791] "Assessing confidence in frontier AI safety cases"
- [2510.20487] "Steering Evaluation-Aware Language Models"

#### Connections
- See 4.5 (Safety Engineering) for general safety
- See 1.5 (Cybersecurity) for red teaming
- See Report Part 2 for literature review

---

### 6.2 Program Evaluation

#### Overview
The systematic assessment of programs and interventions. Provides frameworks for evaluating AI as an organizational intervention.

#### Core Concepts

**Theory of Change / Logic Models**
- Making causal assumptions explicit
- Inputs → Activities → Outputs → Outcomes → Impact
- Identifying assumptions and testing them

**Formative vs. Summative Evaluation**
- Formative: Improve the program during implementation
- Summative: Judge overall worth/effectiveness
- Different purposes, different methods

**Process vs. Outcome Evaluation**
- Process: Was the program implemented as intended?
- Outcome: Did it achieve desired effects?
- Both needed for complete picture

**Implementation Fidelity**
- Was the intervention delivered as designed?
- Dosage, adherence, quality
- Essential for interpreting outcomes

**Utilization-Focused Evaluation**
- Design evaluation to be useful to decision-makers
- Involve stakeholders in evaluation design
- Evaluation use is the goal, not just doing evaluation

**Developmental Evaluation**
- For innovative initiatives in complex environments
- Evaluator as part of development team
- Adaptive, emergent approach
- Highly relevant for AI where we're still learning

**Realist Evaluation**
- "What works for whom in what circumstances?"
- Context-Mechanism-Outcome configurations
- Not just "average effect" but understanding variation

**Participatory Evaluation**
- Involving stakeholders in evaluation
- Those affected help design and conduct evaluation
- Builds ownership and use

#### What Transfers

- **Logic model discipline**: Making AI's theory of change explicit
- **Implementation fidelity**: Was AI actually used? How?
- **Utilization focus**: Design AI evaluation to inform decisions
- **Developmental evaluation**: Appropriate for novel AI deployment
- **Realist perspective**: Understanding what works when and for whom

#### What Breaks

- **Program stability**: Programs are usually stable; AI changes
- **Defined intervention**: AI intervention is less defined
- **Longer timelines**: Program evaluation often has more time

#### Implications for AI Evaluation

- Develop logic models for AI: How is it supposed to create value?
- Check implementation fidelity: Are people actually using AI? How?
- Take utilization-focused approach: What decisions will evaluation inform?
- Apply developmental evaluation for new AI deployments
- Seek realist understanding: What works for whom, when?

#### Key References

- Patton, M.Q. (2010). *Developmental Evaluation*
- Patton, M.Q. (2008). *Utilization-Focused Evaluation*
- Pawson, R. & Tilley, N. (1997). *Realistic Evaluation*
- Rossi, P.H. et al. (2018). *Evaluation: A Systematic Approach*
- Chen, H.T. (2014). *Practical Program Evaluation*

#### Connections
- See 2.1 (Experimental Design) for methods
- See 2.3 (Econometrics) for causal inference
- See 5.3 (Org Behavior) for implementation

---

### 6.3 Educational Measurement

#### Overview
The assessment of learning and educational outcomes. Provides insights on test design, test security, and stakes in assessment.

#### Core Concepts

**High-Stakes Testing**
- Tests with significant consequences
- Effects on behavior (teaching to the test)
- Validity and fairness concerns

**Test Security**
- Preventing item leakage
- Detecting cheating
- Maintaining score validity

**Fairness in Testing**
- Differential item functioning
- Bias and opportunity to learn
- Accommodation and accessibility

**Standard Setting**
- Determining cut scores
- Criterion-referenced interpretation
- Judgment-based processes

**Teaching to the Test**
- Alignment of instruction with assessment
- Beneficial (curriculum alignment) vs. detrimental (narrow teaching)
- Campbell's Law: measurement affects what's measured

**Test Preparation Effects**
- Coaching and its effects on validity
- Distinguishing real skill from test-taking skill

#### What Transfers

- **Test security concerns**: Benchmark contamination parallels item leakage
- **Teaching to the test**: AI may be optimized for benchmarks specifically
- **Campbell's Law**: Metrics become targets and lose validity
- **Fairness concepts**: AI should perform fairly across contexts

#### What Breaks

- **Student motivation**: Students try to pass; AI doesn't "try"
- **Learning context**: Educational testing is about learning; AI isn't learning from the test

#### Implications for AI Evaluation

- Treat benchmark security seriously—contamination is a real threat
- Expect optimization for evaluation (Campbell's Law for AI)
- Consider fairness: Does AI perform consistently across contexts and users?
- Learn from educational measurement about high-stakes testing pitfalls

#### Key References

- Lane, S. et al. (2015). *Handbook of Test Development*
- Haladyna, T.M. (2004). *Developing and Validating Multiple-Choice Test Items*
- Koretz, D. (2008). *Measuring Up: What Educational Testing Really Tells Us*
- Cizek, G.J. & Wollack, J.A. (2016). *Handbook of Quantitative Methods for Detecting Cheating*

#### Connections
- See 2.2 (Psychometrics) for measurement theory
- See 1.4 (Traditional ML) for contamination detection
- See 6.1 (AI Safety) for evaluation gaming

---

### 6.4 Clinical Trial Methodology

#### Overview
The methodology of testing medical interventions. Provides models for rigorous, staged evaluation.

#### Core Concepts

**Phase Structure**
- Phase I: Safety in small group
- Phase II: Efficacy signals in larger group
- Phase III: Definitive efficacy in large RCT
- Phase IV: Post-market surveillance

**Randomization and Blinding**
- Random assignment to treatment/control
- Single-blind, double-blind, triple-blind
- Reducing bias

**Adaptive Trials**
- Modifying trial based on interim results
- Bayesian adaptive designs
- More efficient use of data

**Interim Analysis and Stopping Rules**
- Planned looks at accumulating data
- Stop for efficacy, futility, or safety
- Statistical adjustment for multiple looks

**Post-Market Surveillance**
- Continuing to monitor after approval
- Detecting rare adverse events
- Long-term safety

**Real-World Evidence**
- Evidence from real-world use (vs. trials)
- Complements trial evidence
- Pharmacoepidemiology

#### What Transfers

- **Phase structure**: Staged AI evaluation (screening → pilot → deployment → monitoring)
- **Adaptive designs**: Modifying AI evaluation based on interim findings
- **Post-market surveillance**: Continuous monitoring after AI deployment
- **Real-world evidence**: Importance of evidence from actual use

#### What Breaks

- **Blinding**: Often can't blind users to AI
- **Longer timelines**: Clinical trials run years; AI context changes faster
- **Clear outcomes**: Clinical outcomes often clearer than productivity outcomes
- **Regulatory structure**: Clinical trials have mature regulatory framework

#### Implications for AI Evaluation

- Consider phased approach: Start with limited testing, expand based on results
- Plan for post-deployment surveillance from the start
- Use adaptive designs to be efficient with evaluation resources
- Real-world evidence is essential, not just controlled trials

#### Key References

- Friedman, L.M. et al. (2015). *Fundamentals of Clinical Trials*
- Berry, S.M. et al. (2010). *Bayesian Adaptive Methods for Clinical Trials*
- Sherman, R.E. et al. (2016). "Real-World Evidence—What Is It and What Can It Tell Us?"

#### Connections
- See 2.1 (Experimental Design) for trial methods
- See 4.3 (Quality Management) for monitoring
- See Report Part 4 for phased approach

---

## Section 7: Standards and Governance

### 7.1 Metrology (Science of Measurement)

#### Overview
The science of measurement itself. Provides rigorous frameworks for understanding what measurement means.

#### Core Concepts

**Measurement Uncertainty**
- All measurements have uncertainty
- Quantifying and reporting uncertainty
- Uncertainty propagation

**Traceability**
- Measurements traceable to reference standards
- Chains of comparison
- International standardization

**Reference Standards**
- Agreed-upon standards for comparison
- Primary and secondary standards
- Interlaboratory comparisons

**Calibration**
- Ensuring measurement instruments are accurate
- Regular recalibration
- Calibration certificates

**Vocabulary of Metrology (VIM)**
- Internationally agreed definitions
- Precision, accuracy, trueness, etc.
- Common language for measurement

**Proficiency Testing**
- Testing measurement capability
- Comparison across labs
- Ensuring measurement quality

#### What Transfers

- **Uncertainty awareness**: AI evaluation has uncertainty; should quantify
- **Traceability concept**: What are AI evaluation results traceable to?
- **Calibration mindset**: Is our evaluation methodology itself valid?

#### What Breaks

- **Physical measurement focus**: Metrology focused on physical quantities
- **Reference standards**: No agreed reference standards for AI evaluation
- **Mature infrastructure**: AI evaluation lacks metrological infrastructure

#### Implications for AI Evaluation

- AI evaluation is metrologically immature; recognize this
- Report uncertainty in evaluation results
- Work toward shared reference benchmarks
- Consider evaluation methodology validation ("calibrating" our evaluation methods)

#### Key References

- BIPM. *International Vocabulary of Metrology (VIM)*
- JCGM. *Guide to the Expression of Uncertainty in Measurement (GUM)*
- Tal, E. (2017). "Measurement in Science" in *Stanford Encyclopedia of Philosophy*

#### Connections
- See 2.2 (Psychometrics) for measurement in social science
- See 7.2 (Standards) for standardization
- See Report Part 6 for research gaps

---

### 7.2 Standards Development and Governance

#### Overview
How technical standards are developed and used. Relevant to understanding emerging AI evaluation standards.

#### Core Concepts

**Types of Standards**
- De jure (formal) vs. de facto (market-driven)
- Mandatory vs. voluntary
- Performance vs. prescriptive

**Standards Development Organizations (SDOs)**
- ISO, IEEE, NIST, etc.
- Consensus-based processes
- Stakeholder participation

**Conformity Assessment**
- Determining whether product/service meets standard
- Self-declaration, second-party, third-party
- Certification and accreditation

**Standards and Innovation**
- Early standardization can lock in bad approaches
- Late standardization misses coordination benefits
- Dynamic standards and versioning

**International Standards Coordination**
- Mutual recognition
- Trade implications
- Harmonization efforts

#### What Transfers

- **Standards awareness**: Know what standards exist and are emerging
- **Conformity assessment**: How to show compliance with AI standards
- **Timing concerns**: AI evaluation standards are still developing

#### Current State for AI

- NIST AI RMF (risk management framework)
- ISO standards in development
- Industry frameworks (various)
- Still early; standards are emerging

#### Implications for AI Evaluation

- Engage with emerging standards (NIST AI RMF, etc.)
- Recognize standards are developing; don't wait for them
- Consider contributing to standards development
- Be aware of what conformity assessment might require

#### Key References

- NIST AI Risk Management Framework
- ISO/IEC JTC 1/SC 42 (AI standards)
- OECD AI Principles
- EU AI Act requirements

#### Connections
- See 6.1 (AI Safety) for safety standards
- See 4.4 (Audit) for conformity assessment
- See Report Part 4 for governance recommendations

---

## Section 8: Synthesis and Summary

### 8.1 What Transfers Directly

| Discipline | Key Transferable Concepts |
|------------|--------------------------|
| Software T&E | V&V distinction, coverage thinking, regression mindset |
| Systems T&E | DT/OT paradigm, MOPs/MOEs, independent evaluation |
| Autonomous Systems | Scenario-based testing, safety cases, sim-to-real gap |
| Experimental Design | Validity framework, control conditions, bias awareness |
| Psychometrics | Reliability concepts, construct validity, criterion validity |
| Econometrics | Counterfactual thinking, selection bias awareness |
| Qualitative Methods | Understanding "why," context sensitivity |
| Risk Analysis | Structured risk identification, risk-based prioritization |
| Quality Management | SPC for monitoring, continuous improvement |
| Human Factors | Trust calibration, automation surprises |
| Program Evaluation | Logic models, implementation fidelity, utilization focus |
| I-O Psychology | Structured evaluation, criterion problem, multi-method assessment |

### 8.2 What Breaks for GenAI

| Assumption That Breaks | Disciplines Affected | AI Reality |
|-----------------------|---------------------|------------|
| Determinism | Software T&E, Reliability | Inherently stochastic |
| Enumerable inputs/outputs | Software T&E, ML Eval | Unbounded spaces |
| Clear ground truth | ML Eval, Psychometrics | Often no "right answer" |
| Stable system under test | All T&E disciplines | Continuous updates |
| Stable traits/capabilities | Psychometrics, I-O Psych | Rapid capability change |
| Predictable failures | Reliability, Safety | Jagged capability frontier |
| Observable processes | Quality Mgmt, Safety | Opaque processing |
| Clear system boundaries | Systems Engineering | Fuzzy (model + prompt + user) |

### 8.3 What Requires Adaptation

| Concept | Adaptation Needed |
|---------|------------------|
| Test coverage | Coverage of scenarios/capabilities, not inputs |
| Regression testing | Monitoring over time, not re-running fixed tests |
| IRT/psychometric methods | For benchmark design, not stable trait measurement |
| Safety cases | For AI, with different evidence types |
| FMEA | For AI failure modes, recognizing unpredictability |
| Trust calibration | For AI with stochastic, jagged capabilities |
| Implementation fidelity | For AI where "use" is highly variable |

### 8.4 What's Genuinely New

Some AI evaluation challenges don't have good precedents:

1. **Unbounded output evaluation**: No prior field has evaluated systems with essentially unlimited output space
2. **Jagged capability frontier**: Unprecedented pattern of high capability adjacent to surprising failure
3. **Specification depth problem**: The value is in handling tasks you can't specify
4. **Benchmark contamination via training**: Prior testing contexts don't have this exact problem
5. **Continuous improvement during deployment**: Systems that get better (or worse) without explicit intervention
6. **Skill amplification**: Extreme variance in user outcomes from same system
7. **The "vibes" quality problem**: Genuine difficulty articulating what good looks like

---

## Appendix A References (Complete Bibliography)

*[To be compiled: All references cited in this appendix, organized alphabetically or by section]*

---

## Notes on Using This Appendix

**For quick reference**: Use Section 8 tables to identify relevant disciplines for your question.

**For depth**: Each discipline section provides core concepts, what transfers, what breaks, and key references.

**For the literature review** (Report Part 2): This appendix provides the disciplinary context; Part 2 provides the recent AI-specific work.

**For practitioners**: Focus on "What Transfers" and "Implications for AI Evaluation" in each section.

**For researchers**: "What Breaks" and Section 8.4 ("What's Genuinely New") identify research opportunities.
