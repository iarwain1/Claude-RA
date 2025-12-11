# Beyond Benchmarks: Evaluating AI Productivity for Defense Acquisition

## Working Title Options
- "Evaluating AI for Acquisition: From Benchmarks to Operational Effectiveness"
- "Testing AI for Real-World Impact: Methods for Acquisition and Deployment"
- "Beyond Benchmarks: Evaluating AI Productivity for Defense Acquisition"
- "The Benchmark-Utility Gap: A Framework for AI Evaluation in Acquisition"

---

## Paper Outline (Comprehensive Revision v3)

---

### 1. Introduction: The Benchmark-Utility Gap

**Core problem**: AI systems demonstrate impressive benchmark performance, yet organizations struggle to translate this into predictable productivity gains. This gap between measured capability and realized value is the central challenge for anyone acquiring, deploying, or evaluating AI systems.

**Primary audience hook**: "You're being asked to acquire AI systems based on benchmark scores and vendor demonstrations. What should you actually trust? How do you evaluate claims about productivity gains? And how do you know if the AI is actually delivering value after deployment?"

**Secondary audience hook**: "The challenge of predicting operational effectiveness from developmental testing is familiar—but generative AI introduces complications that existing T&E frameworks weren't designed to handle. Some traditional approaches transfer well; others break in important ways."

**Section goals**:
- Establish the practical stakes for acquisition decisions
- Preview the paper's contribution: a framework for AI evaluation that builds on existing disciplines while acknowledging what's genuinely new
- Introduce the "alien intern" metaphor: AI as a highly capable but unpredictable collaborator that requires new approaches to hiring, supervision, and performance evaluation
- Acknowledge what we know, what we don't, and what we're learning

**Key empirical anchors**:
- Remote Labor Index finding: ~2.5% of tasks actually automated on real freelance projects despite high benchmark scores
- Anthropic productivity study methodology and limitations
- METR developer productivity studies showing mixed results
- The persistent gap between benchmark improvements and demonstrated real-world gains

---

### 2. Learning from Adjacent Disciplines

*Before diving into AI-specific challenges, survey what existing fields offer—and where their approaches fall short. This serves readers who come from these backgrounds (they'll see connections to their expertise) and readers who don't (they'll get pointers to relevant literature).*

#### 2A. Software and Systems Testing & Evaluation

**What transfers:**
- Verification vs. Validation distinction ("Did we build it right?" vs. "Did we build the right thing?")
- MOPs vs. MOEs (technical performance doesn't guarantee mission effectiveness)
- DT → OT progression (lab performance doesn't guarantee field performance)
- M&S accreditation frameworks (when is a simulation "good enough" to inform decisions?)
- Test adequacy criteria and coverage metrics
- Red teaming and adversarial evaluation mindset
- Configuration management and version control

**What breaks:**
- Determinism assumption (same input → same output)
- Fault isolation and debugging (AI failures are often opaque)
- Regression testing (model may change between test runs)
- Requirements traceability (emergent capabilities weren't "required")
- Enumerable test cases (can't list all possible inputs)

#### 2B. Experimental Design and Statistical Analysis

**What transfers:**
- Internal vs. external validity trade-off
- Construct validity (are we measuring what we think we're measuring?)
- Ecological validity (do experimental conditions match real-world conditions?)
- Selection effects and sampling bias
- Power analysis and effect size estimation
- Randomization and control conditions

**What breaks:**
- Replicability assumptions (the "same" model may behave differently over time)
- Treatment stability (AI systems evolve during studies)
- Effect size interpretation baselines
- Independence assumptions (AI outputs may be correlated in subtle ways)

#### 2C. Psychometrics and Human Assessment

**What transfers:**
- Reliability concepts (consistency of measurement)
- Validity framework (content, criterion, construct validity)
- Item Response Theory (some test items are more informative than others)
- Assessment center methodology (multi-method evaluation)
- Predictive validity studies (do tests predict real-world performance?)
- Structured vs. unstructured evaluation (structured outperforms "vibes")

**What breaks:**
- Stable trait assumption (AI capabilities aren't stable over time)
- Population generalization (norms don't transfer across models)
- Within-individual variation (AI varies on same task; humans vary between individuals)

#### 2D. Econometrics and Productivity Measurement

**What transfers:**
- Total Factor Productivity frameworks
- IT Productivity Paradox insights (complementary investments required)
- Task-based automation models (Autor, Acemoglu)
- Counterfactual estimation approaches
- Difference-in-differences and other causal inference methods

**What breaks:**
- Output measurement for knowledge work
- Quality adjustment challenges
- Time horizons (effects may take years to materialize)
- Attribution in multi-factor environments

#### 2E. Information Systems Research

**What transfers:**
- Task-Technology Fit models
- Technology Acceptance frameworks
- Sociotechnical systems perspective
- Implementation success/failure research
- Decision support systems literature (automation bias, appropriate trust)

**What breaks:**
- System stability assumptions
- Narrower skill distribution assumptions
- Clearer system boundaries

#### 2F. Program Evaluation

**What transfers:**
- Logic models and theory of change
- Formative vs. summative evaluation distinction
- Implementation fidelity assessment
- Developmental evaluation for innovative initiatives
- Utilization-focused evaluation design
- Realist evaluation ("what works for whom in what circumstances?")
- Participatory evaluation methods

**What breaks:**
- Program stability assumptions
- Clearer intervention definitions

#### 2G. Human Factors and Ergonomics

**What transfers:**
- Trust calibration research
- Workload and situation awareness
- Automation surprises literature
- Levels of automation frameworks
- Human-machine interface design principles

**What breaks:**
- More predictable automation behavior in traditional systems
- Clearer failure mode identification
- More stable system capabilities

#### 2H. Judgment and Decision Making

**What transfers:**
- Algorithm aversion and appreciation research
- Advice taking and discounting
- Calibration research and training
- Cognitive bias frameworks
- Noise vs. bias distinction

**Implications for AI evaluation:**
- Users may reject good AI advice or over-rely on bad advice
- Evaluators subject to same biases as other judges
- Need for debiasing in evaluation design

#### 2I. Organizational Behavior and Change Management

**What transfers:**
- Technology adoption models (Diffusion of Innovations, TOE framework)
- Change management frameworks
- Absorptive capacity concept
- Organizational learning theories
- Resistance to change literature

**Implications for AI evaluation:**
- Evaluation results depend on organizational context
- Failed pilots may reflect poor change management, not poor AI
- Adoption readiness affects outcomes

#### 2J. Audit and Assurance

**What transfers:**
- Systematic assurance methodology
- Three lines of defense framework
- Materiality and risk-based scoping
- Sampling methodology
- Independence and objectivity requirements
- Documentation and audit trail standards

**Emerging relevance:**
- Algorithmic auditing as developing field
- Third-party AI assessment frameworks

#### 2K. Risk Analysis and Management

**What transfers:**
- Risk = Probability × Impact frameworks
- FMEA and hazard analysis methods
- Probabilistic Risk Assessment
- Risk matrices and registers
- Residual risk concept
- NIST Risk Management Framework (adapted for AI)

**What breaks:**
- Unknown unknowns (can't enumerate all failure modes)
- Correlated failures across AI systems
- Adversarial risk dimension

#### 2L. Reliability Engineering

**What transfers:**
- Reliability prediction methods
- Accelerated testing concepts
- Availability and maintainability frameworks
- Common cause failure analysis

**What breaks:**
- Different "aging" patterns for AI
- Less predictable failure distributions

#### 2M. Quality Management

**What transfers:**
- Statistical Process Control for monitoring
- Process capability concepts
- Continuous improvement frameworks
- Root cause analysis methods

**What breaks:**
- AI processes are less observable
- Root causes harder to identify

#### 2N. Cost Analysis

**What transfers:**
- Total Cost of Ownership frameworks
- Cost-Benefit Analysis under uncertainty
- Real Options Analysis (value of flexibility)
- IT investment evaluation methods

**AI-specific considerations:**
- Hidden costs (prompt engineering, QA, error correction, retraining)
- Unusual depreciation patterns
- Uncertain switching costs
- Evaluation costs as substantial line item

#### 2O. Forecasting and Prediction

**What transfers:**
- Calibration and overconfidence research
- Base rate anchoring
- Reference class forecasting
- Scenario planning methods
- Expert elicitation techniques

**Implications:**
- Evaluation is retrospective; acquisition decisions require prediction
- How to translate evaluation results into forward-looking judgments

#### 2P. Qualitative Research Methods

**What this adds:**
- Ethnography and observation (how AI is actually used vs. claimed)
- Interview methods for understanding user experience
- Case study methodology
- Process tracing for causal mechanisms
- Grounded theory for building understanding

**Why this matters:**
- Quantitative evaluation tells you *what*; qualitative tells you *why*
- The "vibes" problem may require qualitative unpacking
- Essential complement to quantitative approaches

**Synthesis table**: What each field offers vs. where it falls short for AI evaluation

| Field | Key Contribution | Key Limitation for AI |
|-------|------------------|----------------------|
| Software T&E | V&V frameworks, coverage concepts | Assumes determinism |
| Experimental design | Validity frameworks | Assumes stable treatments |
| Psychometrics | Reliability/validity theory | Assumes stable traits |
| Econometrics | Causal inference methods | Output measurement hard |
| IS Research | Sociotechnical perspective | Assumes stable systems |
| Program evaluation | Logic models, utilization focus | Assumes defined interventions |
| Human factors | Trust calibration, automation bias | Assumes predictable automation |
| JDM | Bias awareness | Mainly descriptive |
| Org behavior | Change management | Slower change contexts |
| Audit | Assurance methodology | Still developing for AI |
| Risk analysis | Structured risk frameworks | Harder to enumerate risks |
| Qualitative methods | Understanding mechanisms | Generalization challenges |

---

### 3. Evaluation Challenges: A Unified Framework

*Organize around validity concepts, translated into accessible language, with explicit T&E analogies throughout. Each challenge is general but has AI-specific complications.*

#### 3A. Coverage and Representativeness

**The challenge**: Can we test enough of the task space to predict real-world performance?

**T&E analogy**: Scenario selection in OT—how do you ensure test scenarios represent operational conditions?

**Psychometric connection**: Content validity—does the test adequately sample the domain?

**AI-specific complications**:
- General-purpose tools have unbounded task spaces
- "Jagged capability frontier"—capability doesn't degrade gracefully
- Can't enumerate edge cases as you can for traditional software
- Task distribution in benchmarks may not match deployment distribution

**Implications**: No finite test set can guarantee coverage; must reason about generalization

#### 3B. Specification and Success Criteria

**The challenge**: Can we define "good enough" well enough to measure it?

**T&E analogy**: Developing MOEs for novel capabilities—sometimes the hardest part is knowing what to measure

**Psychometric connection**: Construct validity—are we measuring what we think we're measuring?

**Program evaluation connection**: The "criterion problem"—defining what good performance means

**AI-specific complications**:
- Part of AI's value is handling tasks you can't fully specify in advance
- "Vibes" problem: practitioners recognize quality but struggle to articulate criteria
- Quality is often context-dependent (the "right" answer depends on downstream use)
- Multi-dimensional quality (accuracy, helpfulness, safety, style may trade off)

**Implications**: May need to involve domain experts in evaluation; criteria may need to be developed iteratively

#### 3C. Generalization and Transfer

**The challenge**: Will performance in test conditions hold in deployment?

**T&E analogy**: DT→OT transition; lab vs. field performance

**Experimental design connection**: External validity and ecological validity

**IS connection**: Task-technology fit—performance depends on match between task and tool

**AI-specific complications**:
- Same model performs differently with different prompts, system configurations, surrounding workflows
- Performance depends heavily on user skill and adaptation
- Benchmark performance may not transfer to realistic task variants
- Context that's implicit in benchmarks may not be present in deployment

**Implications**: Evaluation in realistic conditions essential for high-stakes decisions

#### 3D. Attribution and Confounding

**The challenge**: Can we isolate AI's contribution from user skill, workflow changes, other factors?

**T&E analogy**: Human-machine teaming evaluation—you're measuring the system, not just the technology

**Econometric connection**: The fundamental problem of causal inference

**AI-specific complications**:
- Users adapt to and around the AI over time
- Hard to separate "AI made the task easier" from "AI changed how we do the task"
- Defining the appropriate baseline is contested
- Multiple confounders in organizational settings

**Implications**: Controlled studies sacrifice realism; realistic studies sacrifice attribution

#### 3E. Temporal Stability and System Drift

**The challenge**: Will today's evaluation remain valid as models, users, and contexts change?

**T&E analogy**: This is *less familiar* from traditional T&E—systems under test don't usually improve themselves

**Quality management connection**: Process drift and statistical process control

**AI-specific complications**:
- Model providers update systems continuously (often without notice)
- User skill with the system evolves over weeks/months
- Evaluation findings have a "shelf life"
- The system evaluated may not be the system deployed

**Implications**: Evaluation must be ongoing, not one-time; need monitoring capabilities

#### 3F. Reliability and Consistency

**The challenge**: Does the AI give consistent results, and do our evaluations give consistent judgments?

**Psychometric connection**: Test-retest reliability, inter-rater reliability

**JDM connection**: Noise in human judgment affects evaluation quality

**AI-specific complications**:
- AI stochasticity means literally different outputs on same input
- Human evaluators vary in their judgments of AI output quality
- Aggregating across variable outputs and variable judges compounds uncertainty

**Implications**: Need multiple samples; need evaluator calibration; need uncertainty quantification

#### 3G. Gaming and Contamination

**The challenge**: Can evaluation results be manipulated or invalidated?

**Educational measurement connection**: Teaching to the test; test security

**Cybersecurity connection**: Adversarial evaluation; red teaming

**AI-specific complications**:
- Models may have trained on benchmark data (contamination)
- Models may be optimized to perform well on benchmarks specifically
- Evaluation-aware behavior (models behave differently when they detect evaluation)
- Vendors have incentives to optimize for evaluations used in procurement

**Implications**: Need evaluation approaches resistant to gaming; adversarial mindset valuable

---

### 4. What Makes Generative AI Distinctive

*Synthesis: How does GenAI evaluation differ from traditional software, traditional ML, autonomous systems, and human evaluation? This helps readers calibrate which prior experience transfers.*

#### 4A. Comparison with Traditional Software

| Aspect | Traditional Software | Generative AI |
|--------|---------------------|---------------|
| Determinism | High (same input → same output) | Inherently stochastic |
| Failure modes | Bounded, enumerable | Unbounded, unpredictable |
| Specification | Requirements capture intent | Deep specification problem |
| Testing coverage | Achievable in principle | Fundamentally incomplete |
| Debugging | Trace to source | Largely opaque |
| Versioning | Explicit, controlled | Often implicit, continuous |
| User skill variance | Moderate | Extreme |

#### 4B. Comparison with Traditional ML (Predictive Models)

| Aspect | Traditional ML | Generative AI |
|--------|---------------|---------------|
| Task definition | Well-defined (classification, regression) | Open-ended, generative |
| Evaluation metrics | Clear (accuracy, F1, AUC) | Contested, often requires human judgment |
| Output space | Bounded (classes, numbers) | Unbounded (any text, code, etc.) |
| Failure modes | Wrong class, off by X | Hallucination, harmful content, subtle errors |
| Train/test separation | Clean | Blurry (in-context learning, RLHF) |
| Interpretability | Feature importance available | Much harder |

**Key insight**: Traditional ML evaluation (train/test split, cross-validation, held-out test sets) breaks down for GenAI because task space is unbounded and outputs aren't easily scored.

#### 4C. Comparison with Autonomous Systems (Robotics, Self-Driving, UAVs)

| Aspect | Autonomous Systems | Generative AI |
|--------|-------------------|---------------|
| Environment | Physical, constrained | Information, unconstrained |
| Failure consequences | Physical harm, bounded | Information effects, diffuse |
| Sim-to-real gap | Well-studied | Different character (benchmark-to-real) |
| Verification | Some formal methods possible | Formal verification much harder |
| Human-machine interface | Physical controls, defined roles | Conversational, role ambiguity |
| Levels of autonomy | Well-defined frameworks (SAE) | Emerging frameworks |
| Operating envelope | Definable | Hard to define |

**What transfers from autonomous systems**:
- Operational testing philosophy
- Human-machine teaming research
- Trust calibration literature
- Edge case and scenario-based testing
- Safety case methodology

**What breaks**: GenAI operates in information space where failures are less observable and constraints are less definable.

#### 4D. Comparison with Human Evaluation (The "Alien Intern" Analogy)

| Aspect | Humans | AI |
|--------|--------|-----|
| Consistency | Variable between individuals | Variable within single "individual" |
| Learning | Slow, cumulative | Fast within session, resets between |
| Motivation | Complex (money, status, meaning) | None (but trained behaviors) |
| Values | Stable, internalized | Malleable, from training |
| Fatigue | Yes | No (but context window limits) |
| Scaling | Expensive, slow | Cheap, instant |
| Expertise | Developed over years | Emerges from training data |
| Self-knowledge | Moderate | Poor (doesn't know what it doesn't know) |
| Social awareness | High | Improving but limited |

**What transfers from personnel selection**:
- Structured evaluation outperforms unstructured
- Multiple assessment methods increase validity
- Predictive validity studies inform expectations
- Training and onboarding timelines matter

**What transfers from performance appraisal**:
- Criterion problem (what is "good performance"?)
- Rater biases affect evaluation
- Multiple perspectives valuable

**The "alien intern" framing**:
- Extremely capable in some ways, bafflingly incompetent in others
- Requires supervision; can't be trusted with unsupervised consequential tasks
- Eager to please, sometimes to a fault (sycophancy)
- Doesn't know what it doesn't know
- Needs clear instructions but can handle ambiguity better than traditional software

**Where the analogy breaks**:
- Can't "fire" and hire different individual of same type
- Scales trivially
- No continuous learning across sessions (mostly)
- No genuine motivation or values

#### 4E. Synthesis: The Unique Character of GenAI Evaluation

**Properties that make GenAI evaluation distinctively challenging**:

1. **Stochasticity**: Same input → different outputs, requiring multiple samples
2. **Jagged capability frontier**: Unpredictable failure modes on similar-seeming tasks
3. **Pace of change**: Models improve/change faster than evaluation cycles
4. **Specification depth**: Value comes from handling tasks that can't be fully specified
5. **Human-AI co-adaptation**: Performance depends on how users learn to work with the system
6. **Unbounded output space**: Can't enumerate possible outputs or failure modes
7. **Context sensitivity**: Performance depends heavily on prompt, system setup, workflow
8. **Skill amplification**: Magnifies differences between skilled and unskilled users
9. **Evaluation opacity**: Hard to understand why AI produced a given output

**Implication**: AI evaluation requires *new* approaches, not just borrowing from existing fields—but existing fields provide essential foundations.

---

### 5. Evaluation Methods: A Tiered Approach

*A hierarchy of increasing ecological validity (and cost), with explicit guidance on when each tier is appropriate. Draw on methodological traditions for each tier.*

#### 5A. Tier 1: Benchmarks and Automated Evaluation

**What it measures**: Model capabilities on standardized tasks with automated scoring

**Methods** (drawing on psychometrics and software testing):
- Standardized test suites (coding, math, reasoning, knowledge)
- Automated metrics (BLEU, ROUGE, pass@k, etc.)
- Model-graded evaluation (using another AI to score outputs)

**Appropriate for**:
- Initial screening of candidate models
- Tracking capability over time
- Comparing models on specific dimensions
- Detecting major capability gaps

**Limitations**:
- Limited predictive validity for real-world use
- Gaming and contamination risks
- Narrow task coverage
- Metrics may not align with user values
- Doesn't capture user interaction effects

**Acquisition relevance**: Useful for filtering, not for final decisions

**Best practices**:
- Use multiple benchmarks, not single scores
- Understand what each benchmark actually measures
- Look for benchmark contamination evidence
- Treat as necessary but not sufficient

#### 5B. Tier 2: Expert-Evaluated Task Studies

**What it measures**: Performance on realistic tasks judged by domain experts

**Methods** (drawing on psychometrics and qualitative research):
- Expert blind evaluation of outputs
- Comparative judgment (which output is better?)
- Structured rating scales with clear criteria
- Think-aloud protocols while experts evaluate

**Appropriate for**:
- Validating claims about specific capabilities
- Understanding task-level strengths and weaknesses
- Developing evaluation criteria
- Generating hypotheses about failure modes

**Limitations**:
- Still narrow scope
- Expert judgment introduces variance (inter-rater reliability)
- May not generalize to non-expert users or different task variants
- Expensive and slow

**Acquisition relevance**: Good for validating vendor claims about specific use cases

**Best practices**:
- Use multiple experts
- Develop clear rubrics
- Measure inter-rater reliability
- Include realistic task variants, not just canonical examples

#### 5C. Tier 3: Controlled Workflow Studies (Lab-based RCTs)

**What it measures**: Task completion in realistic workflows under controlled conditions

**Methods** (drawing on experimental design and IS research):
- Randomized controlled trials with representative users
- Within-subject or between-subject designs
- Realistic task sequences, not isolated tasks
- Multiple outcome measures (time, quality, user experience)

**Appropriate for**:
- Pre-deployment validation
- Understanding integration challenges
- Generating evidence for go/no-go decisions
- Understanding user heterogeneity

**Limitations**:
- Lab conditions may not reflect deployment reality
- User selection effects (who participates?)
- Hawthorne effects (behavior change from observation)
- Short time horizons (can't capture adaptation)
- Expensive and time-consuming

**Examples**: GDPval-style studies, METR developer productivity studies

**Acquisition relevance**: Appropriate for significant investments; generates evidence for go/no-go decisions

**Best practices** (drawing on experimental design):
- Power analysis to determine sample size
- Representative user recruitment
- Realistic task selection
- Multiple outcome measures
- Pre-registration of hypotheses and analysis plan

#### 5D. Tier 4: Operational Pilots (Field Studies)

**What it measures**: Performance in actual deployment context with real users doing real work

**Methods** (drawing on program evaluation and field experiments):
- Phased rollout with comparison groups
- Matched comparison designs
- Interrupted time series
- Mixed methods (quantitative outcomes + qualitative process)

**Appropriate for**:
- Final validation before scale-up
- Understanding organizational fit
- Identifying implementation challenges
- Building organizational experience

**Challenges**:
- Attribution harder (many confounders)
- User adaptation begins (changing what you're measuring)
- Expensive and organizationally disruptive
- Ethical issues with withholding potentially valuable tool

**Acquisition relevance**: Required for high-stakes decisions; should inform contract terms

**Best practices** (drawing on program evaluation):
- Clear logic model linking AI to expected outcomes
- Implementation fidelity monitoring (is AI actually being used?)
- Mixed methods to understand mechanisms
- Realistic timeline for adaptation
- Plan for iteration based on findings

#### 5E. Tier 5: Continuous Operational Monitoring

**What it measures**: Ongoing performance as systems, users, and contexts evolve

**Methods** (drawing on quality management and reliability engineering):
- Statistical process control for key metrics
- Automated anomaly detection
- Regular sampling and expert review
- User feedback collection and analysis
- Incident tracking and analysis

**Appropriate for**:
- Post-deployment governance
- Detecting degradation or drift
- Informing iteration and improvement
- Building organizational learning

**Key insight**: The system you deployed may not be the system you're running in 6 months (model updates, user adaptation, context changes)

**Acquisition relevance**: Should be required in contracts; need to plan for this from the start

**Best practices** (drawing on SPC and post-market surveillance):
- Define key metrics and acceptable ranges
- Establish monitoring cadence
- Create escalation procedures for anomalies
- Regular review cycles with stakeholders
- Connect to organizational learning processes

#### 5F. Cross-Cutting Considerations

**Qualitative methods across tiers**:
- Tier 2: Think-aloud protocols, expert interviews
- Tier 3: Post-task interviews, observation
- Tier 4: Ethnographic observation, user interviews, case studies
- Tier 5: Incident analysis, user feedback analysis

**Cost-validity trade-off**:

| Tier | Cost | Internal Validity | External Validity | Time to Results |
|------|------|-------------------|-------------------|-----------------|
| 1 | Low | High (controlled) | Low | Fast |
| 2 | Medium | Medium-High | Low-Medium | Medium |
| 3 | High | Medium-High | Medium | Slow |
| 4 | Very High | Low-Medium | High | Very Slow |
| 5 | Ongoing | Low | High | Continuous |

---

### 6. Levels of Analysis: Task → Job → Organization → Society

*Why productivity gains at one level don't automatically translate to the next. Draws on econometrics, IS research, and organizational behavior.*

#### 6A. Task-Level Measurement

**What it captures**: Performance on discrete, defined tasks

**Typical metrics**: Time to completion, output quality, error rates

**Strengths**: Most tractable to measure; clearest attribution

**Key limitation**: Task speedup ≠ job productivity

**Why the gap exists**:
- Bottlenecks may be elsewhere
- Task may be small fraction of job
- Quality assurance may consume savings
- New tasks may emerge

#### 6B. Job-Level Measurement

**What it captures**: Productivity across the bundle of tasks that constitute a job

**Must account for**:
- Workflow integration (does AI fit into how work actually happens?)
- Bottleneck shifting (did speeding up one task move the bottleneck?)
- New capabilities enabled (can workers now do things they couldn't before?)
- Quality assurance costs (time spent checking AI outputs)
- Task composition changes (AI may change which tasks are done)

**Key insight**: AI often doesn't just make existing tasks faster—it changes which tasks are done

**Measurement approaches**:
- Time diaries and activity tracking
- Output quantity and quality measures
- Self-reported productivity
- Supervisor assessments

**Limitations**: Attribution still challenging; many confounders

#### 6C. Organizational-Level Measurement

**What it captures**: Aggregate productivity effects across the organization

**Must account for**:
- Coordination costs (does AI create new coordination needs?)
- Restructuring effects (are jobs and teams reorganized?)
- Training investments (what's the learning curve cost?)
- Complementary investments (what else is needed to realize gains?)
- Opportunity costs (what else could resources have been spent on?)
- Risk and error costs (what are the costs of AI mistakes?)

**The IT Productivity Paradox parallel**: IT took decades to show productivity gains because complementary investments (reorganization, skills, processes) were needed. AI may follow similar pattern.

**Measurement approaches** (drawing on econometrics):
- Total Factor Productivity analysis
- Financial performance metrics
- Operational metrics (throughput, cycle time)
- Quasi-experimental methods with comparison organizations

**Key limitation**: Attribution extremely difficult; many confounders; long time horizons

#### 6D. The Aggregation Problem

**Why you can't simply sum task-level gains to estimate organizational impact**:

1. **Composition effects**: Saving 20% on a task that's 5% of a job saves 1% on the job
2. **Bottleneck effects**: Speeding up non-bottleneck tasks may not speed up the process
3. **Substitution effects**: Workers may spend saved time on other activities (valuable or not)
4. **Jevons paradox**: Efficiency may increase total activity rather than save time
5. **Quality-quantity trade-offs**: More output may come with quality changes
6. **Complementary investment requirements**: Gains may require other investments to realize
7. **Coordination effects**: Individual productivity gains may not aggregate to team gains

**Empirical anchor**: The Remote Labor Index finding (2.5% actual task automation vs. high benchmark scores) illustrates this gap

#### 6E. Temporal Dynamics

**Short-term vs. long-term effects**:
- Short-term: Learning curve costs, disruption
- Medium-term: Productivity gains as users adapt
- Long-term: Organizational restructuring effects, new capabilities

**User adaptation trajectory**:
- Initial learning and experimentation
- Development of effective workflows
- Skill plateau and routinization
- Possible capability expansion into new uses

**Implications for evaluation timing**: When you measure affects what you find

#### 6F. Societal and Market-Level Considerations

*May be out of scope for main paper, but worth acknowledging*

- Labor market effects (displacement, augmentation, new jobs)
- Competitive dynamics (AI as competitive advantage)
- Cumulative effects of widespread adoption
- Second-order effects on education, training, career paths

---

### 7. Human-AI Teaming: A Critical Lens

*Given the importance of human-machine systems to the T&E audience, and the central role of human factors in AI productivity, this topic deserves dedicated treatment.*

#### 7A. Why Human-AI Teaming Complicates Evaluation

**Core insight**: Performance is a property of the *team*, not the AI alone

**Factors that affect team performance**:
- User skill and expertise (domain expertise ≠ AI expertise)
- Trust calibration (appropriate trust leads to best outcomes)
- Mental models (accurate understanding of AI capabilities and limitations)
- Workflow integration (how AI fits into work patterns)
- Feedback and adaptation (how user and AI adjust to each other)

**The "being good at AI" phenomenon** (Mollick's observation):
- AI proficiency is independent of domain expertise
- Some experts gain little from AI; some novices gain much
- This skill varies enormously and affects all evaluation results
- Skill can be developed but requires deliberate effort

#### 7B. Lessons from Human-Machine Teaming Research

**Trust calibration** (from human factors literature):
- Under-trust: Not using AI when it would help (algorithm aversion)
- Over-trust: Relying on AI when it's wrong (automation bias, complacency)
- Appropriate trust: Calibrated to actual AI reliability in context

**Factors affecting trust**:
- Past experience (direct and vicarious)
- System transparency and explainability
- Perceived competence and reliability
- Individual differences (propensity to trust automation)

**Automation surprises**: When automated systems behave unexpectedly
- More common with AI due to jagged capability frontier
- Can rapidly erode trust
- Require recovery strategies

**Levels of autonomy frameworks** (from autonomous systems):
- Useful for thinking about AI integration
- But GenAI doesn't fit neatly into existing frameworks (conversation vs. control)

#### 7C. User Heterogeneity and Its Implications

**Sources of variation**:
- Domain expertise
- AI proficiency ("prompt engineering" skill)
- Learning orientation (willingness to experiment)
- Trust propensity
- Task type match with AI strengths

**Implications for evaluation**:
- Average effects may hide important heterogeneity
- Need to understand who benefits and who doesn't
- User selection in studies may not match deployment population
- Training and support can shift the distribution

#### 7D. Adaptation and Learning Over Time

**User adaptation**:
- Initial exploration and experimentation
- Discovery of effective patterns
- Development of personal workflows
- Eventual routinization or continued innovation

**Time to proficiency**: Not well understood, but likely weeks to months, not hours

**Implications**:
- Short-term studies may underestimate long-term effects (or overestimate if novelty effects dominate)
- Need to account for learning curve in evaluation design
- Early adopter results may not generalize

#### 7E. Implications for Acquisition

**Training and adaptation timelines matter**:
- Budget for learning curve
- Don't expect immediate productivity gains
- Plan for ongoing skill development

**Expertise requirements for effective use**:
- What skills do users need?
- Who will develop and maintain these skills?
- How will expertise be distributed across the organization?

**Evaluation should capture human-AI system performance**:
- Not AI capability in isolation
- Include realistic users, not just best-case
- Measure across skill distribution
- Track adaptation over time

---

### 8. Risk-Based Evaluation Planning

*Drawing on risk analysis frameworks familiar to the acquisition audience, develop an approach to scoping evaluation efforts based on risk.*

#### 8A. Risk Taxonomy for AI Deployment

**Performance risks**:
- AI doesn't deliver expected productivity gains
- Performance varies unacceptably across users/contexts
- Quality issues offset productivity gains

**Operational risks**:
- Errors with consequential downstream effects
- Reliability and availability issues
- Integration failures with existing systems

**Security risks**:
- Data exposure through AI systems
- Prompt injection and adversarial attacks
- Unauthorized use or access

**Organizational risks**:
- Adoption failure (users don't use it)
- Skill dependency (over-reliance on specific individuals)
- Change management failure

**Strategic risks**:
- Vendor lock-in
- Capability gaps vs. competitors
- Regulatory compliance issues

**Reputational risks**:
- High-visibility AI failures
- Bias or fairness concerns
- Public perception issues

#### 8B. How Evaluation Reduces (But Doesn't Eliminate) Risk

**What evaluation can do**:
- Identify capability gaps before deployment
- Estimate performance in realistic conditions
- Reveal failure modes and edge cases
- Inform risk mitigation strategies
- Build organizational understanding

**What evaluation can't do**:
- Guarantee future performance
- Identify all possible failure modes
- Eliminate uncertainty
- Substitute for ongoing monitoring

**Residual risk**: Risk that remains after evaluation and mitigation
- Must be accepted, not ignored
- Should be explicitly characterized
- Informs monitoring and contingency planning

#### 8C. Risk-Based Scoping of Evaluation Effort

**Higher evaluation investment warranted when**:
- Consequences of failure are severe
- AI is in critical decision pathways
- Deployment scale is large
- Reversibility is low
- Organizational experience is limited

**Lower evaluation investment may be acceptable when**:
- Consequences of failure are limited
- AI is advisory, not autonomous
- Deployment is small-scale or pilotable
- Easy to reverse or adjust
- Organization has relevant experience

**Connection to NIST AI RMF**: For organizations required to comply

#### 8D. Adversarial Evaluation and Red Teaming

**The adversarial mindset**: Actively trying to make the system fail

**Red teaming approaches**:
- Capability elicitation (finding what AI can do)
- Failure mode discovery (finding how AI fails)
- Security testing (finding vulnerabilities)
- Bias and fairness probing

**When essential**: Safety-critical applications, security-sensitive contexts, high-visibility deployments

**Resources**: Emerging methodologies from AI safety community

---

### 9. Cost and Value Analysis

*Drawing on cost analysis frameworks to help acquisition professionals think about evaluation economics and AI ROI.*

#### 9A. Total Cost of Ownership for AI Systems

**Visible costs**:
- Licensing/subscription fees
- Infrastructure (compute, storage)
- Initial integration and deployment

**Often-overlooked costs**:
- Prompt engineering and optimization
- Quality assurance and error correction
- User training and ongoing support
- Evaluation and monitoring
- Retraining when models change
- Internal expertise development

**Distinctive AI cost patterns**:
- Usage-based pricing creates variable costs
- Hidden costs often substantial
- Costs may scale non-linearly with use

#### 9B. Benefit Estimation Challenges

**Why AI benefits are hard to quantify**:
- Output of knowledge work is hard to measure
- Quality improvements may be more important than time savings
- New capabilities don't fit old metrics
- Benefits may be diffuse and hard to attribute

**Approaches to benefit estimation**:
- Time savings (most common, but limited)
- Output quantity (if measurable)
- Quality improvements (often subjective)
- Capability expansion (enabling new activities)
- Error reduction (cost of errors avoided)

**The complementary investment problem**: Benefits may require other investments to realize, complicating ROI calculation

#### 9C. Evaluation Costs as Investment

**Evaluation has costs**:
- Direct costs (staff time, tools, infrastructure)
- Opportunity costs (could be deploying faster)
- Organizational attention

**Evaluation has value**:
- Reduces risk of bad deployment decisions
- Builds organizational understanding
- Informs effective implementation
- Enables course correction

**The underinvestment problem**: Organizations often underinvest in evaluation because costs are visible and immediate while benefits are diffuse and future

#### 9D. Value of Flexibility and Options

**Real options perspective**: There's value in approaches that preserve flexibility

**Examples**:
- Avoiding vendor lock-in
- Building evaluation capability (enables future decisions)
- Staged deployment (learn before committing)
- Multiple small experiments vs. one big bet

**Implications for acquisition**: Contracts and decisions should preserve optionality where possible

#### 9E. Building the Business Case

**Elements of a credible business case**:
- Clear logic model linking AI to outcomes
- Realistic benefit estimates with uncertainty ranges
- Full cost accounting including hidden costs
- Risk assessment and mitigation costs
- Timeline for expected value realization
- Monitoring plan for tracking actual vs. expected

---

### 10. Fit-for-Purpose Evaluation: Matching Rigor to Stakes and Maturity

*Practical guidance: What level of evaluation is appropriate for what kind of decision? Drawing on materiality concepts from audit and risk-based approaches.*

#### 10A. The Decision Matrix

| Decision Type | Stakes | Appropriate Tiers | Key Considerations |
|---------------|--------|-------------------|-------------------|
| Exploratory/learning | Low | 1-2 | Fast iteration; accept uncertainty; goal is learning |
| Pilot program design | Medium | 2-3 | Need enough validity to interpret pilot results |
| Acquisition go/no-go | High | 3-4 | Realistic conditions; may need independent evaluation |
| Scaling decision | High | 4 | Operational data essential; understand heterogeneity |
| Ongoing governance | Ongoing | 5 | Continuous monitoring; planned from start |

**Key insight**: Not every decision needs operational-level evidence, but organizations should be explicit about what level of uncertainty they're accepting

#### 10B. Organizational Evaluation Maturity

*Drawing on maturity model concepts to help organizations assess and develop their evaluation capability*

**Level 1 - Ad hoc**:
- No systematic evaluation
- Trust vendor claims or informal "vibes"
- React to problems after deployment

**Level 2 - Reactive**:
- Evaluate when problems arise
- Post-hoc assessment when things go wrong
- Limited proactive evaluation

**Level 3 - Defined**:
- Have evaluation processes
- Apply inconsistently or only for major decisions
- Some internal expertise

**Level 4 - Managed**:
- Systematic evaluation across decisions
- Metrics and standards in place
- Regular review and improvement

**Level 5 - Optimizing**:
- Continuous improvement of evaluation itself
- Learning across evaluations
- Contributing to broader community knowledge

**Implications**: 
- Evaluation rigor should match both decision stakes AND organizational maturity
- Organizations at lower maturity may need to build capability before sophisticated evaluation is possible
- Maturity can be developed through deliberate investment

#### 10C. Constraints and Trade-offs

**When ideal evaluation isn't possible**:
- Time pressure (decision needed before thorough evaluation possible)
- Resource constraints (can't afford comprehensive evaluation)
- Access constraints (can't get necessary data or users)

**Strategies for constrained evaluation**:
- Focus on highest-risk areas
- Use proxy measures and indicators
- Leverage existing evidence (with caution about generalization)
- Plan for rapid iteration and monitoring
- Be explicit about uncertainty

---

### 11. Common Pitfalls in AI Evaluation

*Explicit guidance on what NOT to do—acquisition audiences find this valuable. Drawing on lessons from multiple fields.*

#### 11A. Pitfalls in Interpreting Evidence

1. **Trusting vendor benchmarks without context**
   - Benchmarks can be gamed or contaminated
   - Task distributions may not match your use case
   - Scores without uncertainty estimates are misleading
   - *What to do instead*: Understand what benchmarks measure; seek independent evaluation; conduct your own testing

2. **Extrapolating from task studies to organizational productivity**
   - Task-level gains don't sum to job-level gains
   - Job-level gains don't sum to organizational gains
   - Controlled studies don't capture implementation challenges
   - *What to do instead*: Be explicit about level of evidence; pilot before scaling; measure at multiple levels

3. **Over-weighting single studies**
   - One study ≠ reliable evidence
   - Effect sizes vary across contexts
   - Publication bias favors positive results
   - *What to do instead*: Look for replication; consider context match; treat single studies as indicative, not definitive

4. **Ignoring user heterogeneity**
   - Average effects hide important variation
   - Early adopters differ from average users
   - Expert users differ from novices
   - *What to do instead*: Examine heterogeneity in evidence; test with representative users; plan for skill development

#### 11B. Pitfalls in Evaluation Design

5. **Ignoring the "system" in AI systems**
   - Same model performs differently with different prompts, workflows, users
   - What you're evaluating is the full system, not just the model
   - Lab setup may not match deployment setup
   - *What to do instead*: Evaluate in realistic configurations; include realistic users and workflows

6. **Evaluating once and assuming stability**
   - Models change (often without notice)
   - Users adapt and learn
   - Contexts evolve
   - *What to do instead*: Plan for ongoing monitoring; re-evaluate periodically; track changes

7. **Using inappropriate baselines**
   - "AI vs. no tool" ≠ "AI vs. existing tools"
   - "AI vs. novice" ≠ "AI vs. expert"
   - Current state may not be the right baseline
   - *What to do instead*: Choose baselines carefully; be explicit about what comparison you're making

8. **Inadequate sample sizes**
   - AI outputs vary; human judgments vary
   - Small samples give unreliable estimates
   - Power analysis often skipped
   - *What to do instead*: Calculate needed sample size; report uncertainty; aggregate appropriately

#### 11C. Pitfalls in Deployment Decisions

9. **Assuming expert-level performance from average users**
   - "Being good at AI" is a skill
   - Demo results may reflect expert prompting
   - Average users may not achieve advertised results
   - *What to do instead*: Test with representative users; budget for training; set realistic expectations

10. **Neglecting quality assurance costs**
    - AI outputs require verification
    - Verification takes time
    - Errors that slip through have costs
    - *What to do instead*: Include QA in productivity estimates; design verification workflows; measure error costs

11. **Underestimating implementation challenges**
    - Integration is often harder than expected
    - Change management is essential
    - Training and support are ongoing needs
    - *What to do instead*: Learn from implementation research; plan for change management; budget for support

12. **Planning for static deployment**
    - Models will change
    - User needs will evolve
    - Context will shift
    - *What to do instead*: Plan for iteration; build monitoring capability; maintain flexibility

---

### 12. Recommendations by Acquisition Phase

*Practical guidance organized by decision stage, drawing on evaluation best practices and acquisition context.*

#### 12A. Pre-Acquisition: Evaluating Vendor Claims and Options

**Understanding vendor evidence**:
- What benchmarks are cited? What do they actually measure?
- What user studies support claims? What were the conditions?
- What limitations are acknowledged? What's not addressed?
- How generalizable is the evidence to your context?

**Questions to ask vendors**:
- What are the failure modes and limitations?
- How does performance vary across users and contexts?
- What training and support is needed for effective use?
- How will the system change over time? How will you be notified?
- What evaluation data can you provide or support?

**Red flags in vendor demonstrations**:
- Cherry-picked examples without systematic data
- Reluctance to discuss limitations or failure modes
- Claims that seem too good or too general
- Lack of evidence from realistic deployment contexts
- Inability to explain how results were achieved

**Value of independent evaluation**:
- When stakes are high, independent assessment is valuable
- Vendors have incentives that may not align with yours
- Third-party evaluation services are emerging

#### 12B. Pilot Design and Execution

**Selecting use cases for pilots**:
- Start with use cases where value is likely and failure costs are manageable
- Include diverse contexts to test generalizability
- Don't cherry-pick—include representative challenges
- Consider edge cases and stress scenarios

**Designing pilots that generate actionable evidence** (drawing on program evaluation):
- Clear logic model: What's the theory of how AI creates value?
- Measurable outcomes at multiple levels (task, job, organizational)
- Comparison condition (even if not full RCT)
- Realistic timeline for user adaptation
- Mixed methods (quantitative outcomes + qualitative understanding)

**Implementation fidelity**: Was the AI actually used as intended?
- Track actual usage patterns
- Understand workarounds and adaptations
- Distinguish pilot failure from AI failure

**Common pilot failure modes**:
- Too short to allow adaptation
- Unrepresentative users or contexts
- Poor change management
- Inadequate training and support
- Mismeasurement of outcomes

**Setting appropriate success criteria**:
- Define before pilot, not after
- Realistic given timeline and context
- Multiple criteria, not single metric
- Allow for learning, not just pass/fail

#### 12C. Contract Structuring

**Evaluation requirements to build into contracts**:
- Access to performance data
- Rights to conduct independent evaluation
- Notification of model changes
- Performance metrics and monitoring provisions
- Audit rights

**Handling model updates and version changes**:
- Notification requirements
- Right to decline updates
- Rollback provisions
- Re-evaluation triggers

**Performance guarantees and their limitations**:
- What can realistically be guaranteed?
- How will disputes be resolved?
- What are the remedies for underperformance?

**Flexibility provisions**:
- Exit and switching terms
- Volume adjustment
- Scope changes as needs evolve

#### 12D. Deployment and Integration

**Phased rollout strategies**:
- Start small and expand based on evidence
- Geographic or organizational phasing
- Task-based phasing (easier tasks first)
- User-based phasing (more skilled users first, then expand)

**Training and support**:
- Initial training for all users
- Ongoing support for questions and problems
- Skill development for power users
- Communities of practice for learning sharing

**Quality assurance integration**:
- What outputs require review?
- Who reviews and how?
- How are errors caught and addressed?
- How is quality tracked over time?

**Change management**:
- Communication about expectations
- Addressing resistance
- Celebrating successes
- Learning from failures

#### 12E. Ongoing Governance

**Continuous monitoring requirements**:
- Key metrics to track
- Monitoring cadence
- Anomaly detection and alerting
- Regular reporting

**Trigger points for re-evaluation**:
- Model version changes
- Significant performance changes
- Expansion to new use cases
- User population changes
- Incident occurrence

**Managing model updates**:
- Notification and communication
- Testing before deployment
- Rollback capability
- Documentation

**Incident management**:
- Incident identification and reporting
- Root cause analysis
- Corrective action
- Learning and sharing

**Exit and switching considerations**:
- Data portability
- Workflow dependencies
- User retraining needs
- Transition planning

#### 12F. Internal Capability Building

**Expertise needed**:
- Technical understanding of AI systems
- Evaluation methodology expertise
- Domain expertise for quality judgment
- Change management and implementation skills
- Vendor management capabilities

**Building vs. buying evaluation capability**:
- What must be internal? (context-specific knowledge, ongoing monitoring)
- What can be external? (specialized technical assessment, benchmarking)
- What partnerships or relationships are valuable?

**Developing organizational learning**:
- Documenting evaluation findings
- Sharing across teams and projects
- Building institutional knowledge
- Contributing to broader community

---

### 13. Research Gaps and Uncertainties

*Honest accounting of what we don't know how to do well. Frames future research needs and calibrates reader expectations.*

#### 13A. Methodological Gaps

- **Generalization methods**: Better approaches for predicting operational performance from controlled studies
- **Continuous monitoring**: Validated approaches for detecting drift and degradation
- **Attribution in human-AI teams**: Methods for isolating AI contribution in realistic contexts
- **Quality metrics**: Better measures for knowledge work output quality
- **Uncertainty quantification**: Standards for reporting evaluation uncertainty
- **Cross-context comparability**: Methods for comparing results across organizations and contexts

#### 13B. Empirical Gaps

- **Long-term effects**: Most evidence is short-term; need longitudinal studies
- **Domain breadth**: Most evidence is from software development and writing; other domains understudied
- **Organizational-level effects**: Task and job effects better studied than organizational effects
- **Negative cases**: Publication bias toward positive results; need systematic evidence on failures
- **User heterogeneity**: Who benefits and who doesn't? What predicts success?
- **Skill development**: How does AI proficiency develop? What training works?

#### 13C. Conceptual Gaps

- **What are we measuring?**: Better frameworks for "AI capability" and "AI productivity"
- **Transfer theory**: When should we expect benchmark performance to transfer?
- **Appropriate trust**: What does well-calibrated trust in AI look like?
- **System boundaries**: How to define and evaluate the full human-AI system?

#### 13D. Standards and Infrastructure Gaps

- **Benchmark standards**: No agreed standards for benchmark quality and contamination
- **Reporting standards**: No agreed standards for evaluation reporting
- **Reference benchmarks**: No "gold standard" benchmarks for real-world productivity
- **Comparison infrastructure**: No easy way to compare results across studies

#### 13E. Organizational Gaps

- **Best practices**: Emerging but not yet codified
- **Competency frameworks**: What skills do organizations need?
- **Governance models**: How should AI evaluation be governed?

---

### 14. Conclusion

**Summary of key takeaways**:
- The benchmark-utility gap is real and substantial; benchmark performance doesn't reliably predict operational value
- AI evaluation faces genuinely novel challenges, but existing disciplines provide essential foundations
- Evaluation should be tiered (matching rigor to stakes), continuous (not one-time), and systemic (human-AI team, not AI alone)
- Multiple levels of analysis matter: task, job, organization
- Human factors are central, not peripheral
- Risk-based thinking should guide evaluation scope and investment
- Organizations need to build evaluation capability as a core competency

**The path forward**:
- Treat evaluation as investment, not cost
- Build internal expertise while leveraging external resources
- Plan for continuous evaluation and adaptation
- Contribute to the broader community's learning

**Living with uncertainty**:
- Perfect evaluation is impossible; decisions must be made under uncertainty
- Be explicit about what you know and don't know
- Plan for iteration and course correction
- Monitor and adapt

---

## Appendices

### Appendix A: Glossary

*Key terms with definitions, bridging T&E terminology and AI terminology*

- **Benchmark**: Standardized test or task set used to evaluate AI capabilities
- **Construct validity**: Whether a measure actually measures the underlying concept it claims to
- **DT (Developmental Testing)**: Testing during development to support design refinement
- **Ecological validity**: Whether experimental conditions match real-world conditions
- **External validity**: Whether findings generalize to other contexts
- **Internal validity**: Whether observed effects can be attributed to the intervention
- **Jagged capability frontier**: Pattern where AI capabilities are uneven across similar-seeming tasks
- **MOE (Measure of Effectiveness)**: Metric capturing operational outcome achievement
- **MOP (Measure of Performance)**: Metric capturing technical performance characteristics
- **OT (Operational Testing)**: Testing under realistic operational conditions
- **Predictive validity**: Whether test performance predicts real-world performance
- **Reliability**: Consistency of measurement
- **V&V (Verification and Validation)**: "Build it right" (V) and "Build the right thing" (V)

### Appendix B: Summary of Key Empirical Studies

*Quick reference table of major studies cited, with methodology and key findings*

| Study | Organization | Method | Key Finding | Limitations |
|-------|--------------|--------|-------------|-------------|
| Remote Labor Index | Scale/CAIS | Real freelance projects | ~2.5% task automation rate | Specific to remote freelance work |
| GDPval | OpenAI | Multi-task comparative study | Varies by task category | Lab conditions |
| Anthropic productivity | Anthropic | Self-estimated from conversations | 80% estimated time savings | Self-report, selection bias |
| METR developer study | METR | RCT with experienced developers | Mixed results; heterogeneous effects | Specific tasks and population |
| UpBench | Upwork | Real freelance tasks | [To be added] | [To be added] |

### Appendix C: Evaluation Checklist by Acquisition Phase

*One-page practical reference*

**Pre-Acquisition**
- [ ] Understand what benchmarks measure and their limitations
- [ ] Request evidence from realistic deployment contexts
- [ ] Ask about failure modes and limitations
- [ ] Consider independent evaluation for high-stakes decisions
- [ ] Assess vendor claims against your specific context

**Pilot Design**
- [ ] Define clear logic model linking AI to expected outcomes
- [ ] Select representative use cases (not just easiest wins)
- [ ] Plan realistic timeline including adaptation period
- [ ] Design for multiple outcome measures
- [ ] Include comparison condition where feasible
- [ ] Plan mixed methods (quantitative + qualitative)

**Pilot Execution**
- [ ] Track actual usage (implementation fidelity)
- [ ] Collect quantitative outcome data
- [ ] Gather qualitative user feedback
- [ ] Monitor for problems and adaptations
- [ ] Document lessons learned

**Contract**
- [ ] Include evaluation data access rights
- [ ] Specify model change notification requirements
- [ ] Define performance metrics and monitoring
- [ ] Include audit rights
- [ ] Plan for flexibility and exit

**Deployment**
- [ ] Plan phased rollout
- [ ] Provide adequate training and support
- [ ] Integrate quality assurance
- [ ] Manage change deliberately

**Ongoing**
- [ ] Monitor key metrics continuously
- [ ] Establish re-evaluation triggers
- [ ] Manage model updates systematically
- [ ] Track and respond to incidents
- [ ] Document and share learnings

### Appendix D: Disciplinary Resources for Further Reading

*Pointers to key resources in each relevant field*

**Software T&E**
- [Key references]

**Experimental Design**
- [Key references]

**Psychometrics**
- Cronbach & Meehl on construct validity
- Kane's argument-based approach to validity
- [Additional key references]

**Econometrics and Productivity**
- Brynjolfsson et al. on IT productivity paradox
- Autor on task-based automation
- [Additional key references]

**Program Evaluation**
- Patton on utilization-focused evaluation
- Pawson & Tilley on realist evaluation
- [Additional key references]

**Human Factors**
- Parasuraman & Riley on automation trust
- Lee & See on trust in automation
- [Additional key references]

**Risk Analysis**
- NIST AI Risk Management Framework
- [Additional key references]

**Emerging AI Evaluation**
- METR methodology documentation
- Anthropic evaluation approaches
- OpenAI GDPval methodology
- [Additional key references]

### Appendix E: Emerging AI Evaluation Ecosystem

*Survey of current initiatives, frameworks, and resources*

**Standards and Frameworks**
- NIST AI RMF
- ISO standards (developing)
- Industry frameworks (Microsoft, Google, etc.)

**Evaluation Platforms and Benchmarks**
- Major benchmark suites
- Leaderboards and their limitations
- Emerging real-world evaluation efforts

**Third-Party Assessment**
- Emerging audit and assessment services
- Academic research groups
- Non-profit initiatives

**Incident and Learning**
- AI Incident Database
- Other incident tracking
- Lessons learned resources

---

## Change Log from Previous Versions

### Changes from v2:
1. Added comprehensive Section 2 (Learning from Adjacent Disciplines) surveying 16+ relevant fields
2. Expanded Section 4 (What Makes AI Distinctive) with detailed comparison tables
3. Added Section 8 (Risk-Based Evaluation Planning) drawing on risk analysis frameworks
4. Added Section 9 (Cost and Value Analysis) drawing on cost analysis frameworks
5. Expanded Section 10 to include organizational evaluation maturity model
6. Significantly expanded Section 11 (Common Pitfalls) with 12 specific pitfalls
7. Added qualitative methods throughout as essential complement to quantitative
8. Added new appendices (D: Disciplinary Resources, E: Emerging Ecosystem)
9. Strengthened human analogy framing throughout
10. Added JDM/behavioral economics perspective to human-AI teaming discussion
11. Added organizational change management perspective to recommendations
12. Added forecasting/prediction perspective to evidence interpretation
13. Added audit/assurance perspective to governance discussion
14. Incorporated program evaluation frameworks (logic models, formative/summative, utilization-focused)
15. Added metrology perspective on measurement maturity
