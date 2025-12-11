# Appendix A, Section 4: Risk, Quality, and Assurance

## Section 4.1: Risk Analysis and Management

### Overview

Risk analysis and management provide systematic approaches to identifying, assessing, and managing uncertainty and potential harms. For AI evaluation, risk frameworks inform prioritization—where should limited evaluation resources focus?—and help characterize residual uncertainty that remains even after evaluation.

### Core Concepts

**Risk Identification**

The first step in risk management is identifying what could go wrong:

**Hazard analysis** systematically identifies conditions that could lead to harm. For AI, hazards might include: incorrect outputs accepted as correct, biased outputs affecting decisions, system unavailability at critical moments, privacy violations, or adversarial misuse.

**Threat modeling** (from cybersecurity) identifies potential adversaries and attack vectors. For AI: Who might try to make the system behave badly? How might they try?

**Historical analysis** examines past incidents for patterns. AI is too new for deep historical record, but emerging incident databases begin to catalog AI failures.

**Brainstorming and checklists** supplement systematic methods. Checklists of known AI failure modes prompt consideration of specific risks.

**Risk Assessment**

Once identified, risks must be assessed:

**Probability × Impact** is the classic framework. Risk severity = likelihood of occurrence × consequence if it occurs. This produces a single number for comparison.

**Qualitative assessment** (high/medium/low) is simpler but supports less precise prioritization.

**Risk matrices** cross-tabulate probability and impact, creating visual representations of risk landscape.

**Scenario-based assessment** develops specific scenarios and assesses their likelihood and consequences, avoiding the abstraction of probability estimates for never-before-seen events.

For AI, probability estimation is particularly challenging. How likely is a specific failure mode? With limited operating history and unpredictable capability boundaries, probability estimates are highly uncertain.

**Risk Prioritization**

Resources are limited; not all risks can be addressed equally:

**Expected value ranking** prioritizes by probability × impact. But this may underweight low-probability, high-consequence risks.

**Risk appetite** defines what level of risk is acceptable. Different stakeholders may have different appetites.

**Consequence-focused prioritization** may focus on high-consequence risks regardless of probability, especially for catastrophic outcomes.

**Risk Mitigation**

Once prioritized, risks can be addressed:

**Avoid**: Don't deploy AI in high-risk contexts
**Transfer**: Insurance, contractual provisions, shared responsibility
**Mitigate**: Reduce probability or consequence through controls
**Accept**: Acknowledge residual risk after other measures

For AI, mitigations might include: output filtering, human review requirements, usage restrictions, monitoring and alerting, fallback procedures when AI fails.

**Residual Risk**

Risk management reduces but doesn't eliminate risk. Residual risk is what remains after mitigation. It must be:
- Quantified (to the extent possible)
- Documented
- Accepted consciously by appropriate stakeholders
- Monitored over time

For AI, residual risk includes: unknown failure modes, edge cases not tested, adversarial attacks not anticipated, performance degradation over time.

**Enterprise Risk Management**

ERM takes organization-wide view of risk:
- Aggregating risks across units
- Understanding risk interdependencies
- Aligning risk appetite with strategy
- Building risk-aware culture

For AI, ERM perspective considers: How do AI risks relate to other organizational risks? What's the organization's appetite for AI risk? How does AI risk fit strategic objectives?

### What Transfers to AI Evaluation

**Structured risk identification**: Systematic approaches to finding risks, rather than ad hoc consideration.

**Risk-based prioritization**: Focus evaluation resources on highest-risk areas.

**Residual risk concept**: Evaluation reduces but doesn't eliminate risk. Characterize what remains.

**Risk monitoring**: Ongoing risk tracking after deployment, not just pre-deployment assessment.

### What Breaks for Generative AI

**Probability estimation**: AI failure probabilities are hard to estimate with limited history and unpredictable failures.

**Enumerable failures**: Traditional risk analysis assumes you can list what might go wrong. AI failures may be unforeseen.

**Independence assumptions**: Standard risk analysis assumes risks are independent. AI risks may be correlated (same model flaws affect multiple use cases).

### Implications for AI Evaluation

- **Use risk frameworks to prioritize evaluation.** Not all AI uses warrant the same scrutiny.
- **Accept that risk can't be eliminated.** Characterize residual risk honestly.
- **Plan for ongoing risk monitoring.** Pre-deployment evaluation isn't sufficient.
- **Expect unknown unknowns.** Design for detection and response, not just prevention.

### Key References

- **ISO 31000 (Risk Management—Guidelines).** International standard for risk management.

- **NIST AI Risk Management Framework.** AI-specific risk management guidance.

- **Kaplan, S., & Garrick, B.J. (1981). "On the Quantitative Definition of Risk." *Risk Analysis*.** Foundational paper on risk definition.

- **Hubbard, D.W. (2020). *The Failure of Risk Management* (2nd ed.).** Critical examination of risk management practice.

---

## Section 4.2: Reliability Engineering

### Overview

Reliability engineering focuses on ensuring systems perform their required functions over time. While developed primarily for hardware systems, reliability thinking offers frameworks for understanding AI system consistency and monitoring for degradation.

### Core Concepts

**Reliability Definitions**

**Reliability** is the probability that a system performs its required function under specified conditions for a specified time.

**Mean Time Between Failures (MTBF)** measures average time between failures for repairable systems.

**Mean Time To Failure (MTTF)** measures average time to failure for non-repairable systems.

**Availability** is the proportion of time the system is operational: Uptime / (Uptime + Downtime).

For AI, "failure" needs reinterpretation. AI doesn't crash like hardware; it produces outputs that may be wrong, unhelpful, or harmful. "Reliability" might mean: consistency of output quality, availability of service, or probability of meeting some quality threshold.

**Failure Modes and Effects Analysis (FMEA)**

FMEA systematically identifies:
- How can each component fail? (Failure modes)
- What happens when it fails? (Effects)
- How likely is failure? (Occurrence)
- How severe are consequences? (Severity)
- Can failure be detected? (Detection)

Risk Priority Number (RPN) = Occurrence × Severity × Detection guides prioritization.

For AI, FMEA thinking asks: How can AI outputs fail? (Incorrect, biased, harmful, off-topic, etc.) What happens when they do? (User acts on wrong information, decisions are biased, reputation damage, etc.) How detectable are failures? (Some obvious, others subtle.)

**Reliability Growth**

Systems become more reliable as failures are found and fixed. Reliability growth models track improvement over development and deployment:
- **Duane model**: Reliability improves predictably with time/effort
- **AMSAA model**: Reliability growth as power law function

For AI, reliability might improve as: edge cases are identified and addressed, users learn to prompt better, system prompts are refined, fine-tuning addresses weaknesses.

**The Bathtub Curve**

Hardware failure rates often follow a "bathtub" pattern:
- **Early life (infant mortality)**: High initial failures from manufacturing defects
- **Useful life**: Low, constant failure rate
- **Wear-out**: Increasing failures as components age

AI doesn't wear out physically, but analogous patterns might exist: high initial issues during deployment, stabilization, and eventually degradation as the world changes and the model becomes stale.

**Common Cause Failures**

Multiple components failing from the same cause (environmental shock, design flaw, shared supply chain) defeat redundancy designed to handle independent failures.

For AI, common cause concerns include: same model deployed across applications (single point of failure), same training data biases affecting all outputs, same vulnerabilities across deployments.

### What Transfers to AI Evaluation

**Failure mode thinking**: Systematically consider how AI can fail and what happens when it does.

**Reliability monitoring**: Track performance over time looking for degradation.

**Common cause awareness**: AI systems may have correlated failures across applications.

### What Breaks for Generative AI

**Predictable failure distributions**: AI failures don't follow hardware reliability distributions.

**Component-based modeling**: AI isn't modular in ways that enable component reliability analysis.

**Physical failure mechanisms**: AI "fails" differently than hardware.

### Implications for AI Evaluation

- **Apply FMEA thinking** to identify failure modes and their consequences.
- **Monitor for reliability trends** over time.
- **Be aware of common cause risks** when same AI is deployed across multiple uses.
- **Track whether reliability improves** as issues are addressed.

### Key References

- **O'Connor, P.D.T., & Kleyner, A. (2012). *Practical Reliability Engineering* (5th ed.).** Comprehensive reliability engineering text.

- **MIL-HDBK-217.** Military standard for reliability prediction.

---

## Section 4.3: Quality Management

### Overview

Quality management provides systematic approaches to ensuring and improving quality. For AI, quality management concepts inform continuous monitoring and improvement after deployment.

### Core Concepts

**Statistical Process Control (SPC)**

SPC monitors process outputs over time using control charts:
- **Control limits** define the range of expected variation
- **Common cause variation** is inherent to the process; expected
- **Special cause variation** indicates something has changed; requires investigation

When metrics exceed control limits, investigation is triggered. This distinguishes normal variability from meaningful change.

For AI, SPC might monitor output quality metrics, response times, error rates, or user satisfaction over time. Sustained shifts or outliers trigger investigation.

**Process Capability**

Can the process meet specifications? Capability indices (Cp, Cpk) compare process variation to specification tolerance. A capable process consistently produces outputs within acceptable bounds.

For AI, capability asks: Can the AI consistently meet quality requirements? What proportion of outputs meet quality standards?

**Continuous Improvement**

**PDCA (Plan-Do-Check-Act)**: Iterative improvement cycle
- Plan: Identify improvement opportunity
- Do: Implement change on small scale
- Check: Evaluate results
- Act: Standardize if successful; iterate if not

For AI, PDCA might involve: identifying prompt improvement opportunities, testing changes, measuring effects, and standardizing successful improvements.

**Root Cause Analysis**

When quality problems occur, surface symptoms often mask underlying causes. Root cause analysis techniques:
- **5 Whys**: Iteratively ask "why?" to dig deeper
- **Fishbone diagrams**: Categorize potential causes

For AI, root cause analysis is challenging because the "root cause" of an AI error may be obscure (training data? model architecture? prompt design? user interaction?).

### What Transfers to AI Evaluation

**SPC for monitoring**: Control charts can track AI performance metrics over time.

**Continuous improvement mindset**: AI use should improve through deliberate improvement cycles.

**Root cause orientation**: Understand why failures occur, not just that they occur.

### What Breaks for Generative AI

**Clear specifications**: Quality traditionally means meeting specs. AI "specs" are fuzzy.

**Observable processes**: AI processing is opaque; you see inputs and outputs but not the process.

**Stable processes**: AI systems may not be stable enough for traditional SPC.

### Implications for AI Evaluation

- **Apply control chart thinking** to AI monitoring. Define metrics, establish baselines, flag deviations.
- **Use improvement cycles** to systematically enhance AI use.
- **Attempt root cause analysis** even though AI makes it difficult.

### Key References

- **Montgomery, D.C. (2019). *Introduction to Statistical Quality Control* (8th ed.).** Standard quality control text.

- **Wheeler, D.J. (2000). *Understanding Variation*.** Accessible introduction to SPC thinking.

---

## Section 4.4: Audit and Assurance

### Overview

Audit provides independent assurance that something is as claimed. The audit profession has developed rigorous methods for evidence gathering, independence, and professional judgment that can inform AI evaluation governance.

### Core Concepts

**Audit Objectives and Levels of Assurance**

Audits provide opinions on whether claims are accurate:
- **Reasonable assurance**: High but not absolute confidence
- **Limited assurance**: Lower confidence, less extensive procedures

Audit opinions don't guarantee truth but provide independent assessment of claim credibility.

**Independence and Objectivity**

Auditor independence is fundamental:
- Independence from the entity being audited
- No conflicts of interest
- Professional skepticism—not taking claims at face value

For AI, independence means evaluation by parties separate from developers/vendors with no stake in favorable outcomes.

**Materiality**

Not everything warrants equal scrutiny. Materiality focuses attention on what matters:
- What would change decisions if different?
- What are the most consequential claims?

For AI evaluation, materiality suggests focusing on claims that matter most for deployment decisions, not exhaustive evaluation of everything.

**Audit Evidence**

Evidence types include:
- Documentary (records, logs)
- Testimonial (interviews, representations)
- Observational (watching processes)
- Analytical (examining patterns)

Evidence should be sufficient (enough of it) and appropriate (relevant and reliable).

For AI, evidence might include: benchmark results, user studies, incident logs, usage data, expert review of outputs.

**Three Lines of Defense Model**

Organizational assurance is layered:
- **First line**: Operational management and controls
- **Second line**: Risk management and compliance functions
- **Third line**: Internal audit

For AI, this suggests: operational teams monitoring AI use (first line), risk/compliance overseeing AI governance (second line), internal audit independently assessing (third line).

### What Transfers to AI Evaluation

**Independence principle**: Evaluation by parties independent of developers/vendors.

**Materiality**: Focus on what matters for decisions.

**Evidence standards**: Rigor in gathering and evaluating evidence.

**Professional skepticism**: Not accepting claims at face value.

**Layered assurance**: Multiple lines of defense for AI governance.

### What Breaks for Generative AI

**Established standards**: Financial audit has mature standards; AI audit is emerging.

**Clear assertions**: Financial statements have defined assertions; AI claims are fuzzier.

**Audit trail**: Traditional systems have clear trails; AI processing is opaque.

### Implications for AI Evaluation

- **Apply independence** for high-stakes AI decisions.
- **Use materiality** to scope evaluation appropriately.
- **Develop evidence standards** for AI evaluation.
- **Consider governance structures** with appropriate assurance layers.

### Key References

- **AICPA Audit Standards.** Professional standards for financial audit.

- **IIA Standards.** International Standards for Internal Auditing.

- **Raji, I.D., et al. (2020). "Closing the AI Accountability Gap." *FAT*.** Framework for AI auditing.

---

## Section 4.5: Safety Engineering

### Overview

Safety engineering focuses on preventing hazards and ensuring systems don't cause harm. For AI in safety-critical applications, safety engineering methods provide frameworks for hazard analysis and structured safety argumentation.

### Core Concepts

**Hazard Analysis**

A hazard is a condition that could lead to harm. Safety analysis identifies hazards and their pathways to harm:
- **What hazards exist?** (Energy sources, dangerous materials, error possibilities)
- **What triggers them?** (Conditions, actions, combinations)
- **What are the consequences?** (Severity, reversibility)

For AI, hazards include: incorrect outputs leading to bad decisions, biased outputs causing discrimination, AI unavailability at critical moments, AI being used to cause harm.

**Fault Tree Analysis (FTA)**

FTA works top-down from an undesired event to identify causes:
- Start with the top event (the hazard)
- Identify immediate causes (gates connecting events)
- Continue until reaching basic events

The resulting tree shows all paths to the hazard. For AI, FTA might trace how AI errors could lead to harm, identifying contributing factors at each level.

**Event Tree Analysis (ETA)**

ETA works forward from an initiating event through possible outcomes:
- What initiating events could occur?
- What barriers exist? Do they succeed or fail?
- What outcomes result from each path?

ETA shows the branching possibilities following an initial event and estimates outcome probabilities.

**System-Theoretic Process Analysis (STPA)**

STPA, developed by Nancy Leveson, takes a systems perspective:
- Systems fail not just from component failures but from unsafe interactions
- Focus on control structures and unsafe control actions
- Consider emergent properties of the system as a whole

For human-AI systems, STPA is particularly valuable. Rather than just asking how the AI can fail, STPA asks how the control structure (human, AI, organization, environment) can produce unsafe outcomes through interactions and emergent behaviors.

**Safety Cases**

A safety case is a structured argument that a system is acceptably safe:
- **Claims**: What safety properties are asserted?
- **Evidence**: What data supports each claim?
- **Argument**: How does evidence support claims?
- **Context**: What assumptions and scope limitations apply?

Goal Structuring Notation (GSN) provides visual representation of safety arguments.

For AI, safety cases are emerging as frameworks for structured safety argumentation. Rather than simply claiming "the AI is safe," safety cases make the argument explicit and contestable.

**Functional Safety**

Functional safety (IEC 61508 and derivatives) addresses safety achieved through control systems:
- **Safety Integrity Levels (SIL)** define required reliability
- Higher SILs require more rigorous development and verification
- Defense in depth through multiple independent protections

For AI, functional safety concepts are being adapted, though AI doesn't fit neatly into the framework designed for programmed control systems.

### What Transfers to AI Evaluation

**Hazard analysis mindset**: Systematically identify how AI could cause harm.

**Safety case methodology**: Structured argumentation applicable to AI safety claims.

**STPA for human-AI systems**: Systems perspective on safety captures interactions.

**Defense in depth**: Multiple protections rather than relying on AI alone.

### What Breaks for Generative AI

**Component failure models**: AI doesn't fail like hardware components.

**Quantitative failure rates**: AI failure probabilities are hard to estimate.

**Formal verification**: Safety properties generally can't be formally verified for AI.

### Implications for AI Evaluation

- **For safety-critical AI, apply safety engineering methods.**
- **Develop safety cases** for high-stakes deployments.
- **Use STPA** to analyze human-AI control structures.
- **Design for AI failure**: monitoring, override, fallback.

### Key References

- **Leveson, N.G. (2011). *Engineering a Safer World*.** STPA methodology and systems safety thinking.

- **IEC 61508 (Functional Safety).** Foundation for functional safety standards.

- **Bloomfield, R., & Bishop, P. (2010). "Safety and Assurance Cases: Past, Present and Possible Future."** Overview of safety case methodology.

---

*[End of Section 4]*
