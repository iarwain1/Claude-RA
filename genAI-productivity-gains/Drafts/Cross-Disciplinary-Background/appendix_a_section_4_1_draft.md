# Appendix A, Section 4.1: Risk Analysis and Management

## Overview

Risk analysis and management provide systematic approaches to identifying, assessing, and managing uncertainty and potential harms. For AI evaluation, risk frameworks inform prioritization—where should limited evaluation resources focus?—and help characterize residual uncertainty that remains even after evaluation.

Risk thinking is essential for AI evaluation because no evaluation can be exhaustive. Given unlimited AI capabilities and limited evaluation resources, risk-based approaches help focus effort where it matters most.

---

## Core Concepts

### Risk Identification

The first step in risk management is identifying what could go wrong:

**Hazard analysis** systematically identifies conditions that could lead to harm. For AI, hazards might include: incorrect outputs accepted as correct, biased outputs affecting decisions, system unavailability at critical moments, privacy violations, or adversarial misuse.

**Threat modeling** (from cybersecurity) identifies potential adversaries and attack vectors. For AI: Who might try to make the system behave badly? How might they try? What vulnerabilities exist?

**Historical analysis** examines past incidents for patterns. AI is too new for deep historical record, but emerging incident databases begin to catalog AI failures. Learning from others' failures is efficient.

**Brainstorming and checklists** supplement systematic methods. Checklists of known AI failure modes prompt consideration of specific risks. Expert brainstorming can identify risks that systematic methods miss.

**SWIFT (Structured What-If Technique)** asks structured "what if" questions about system operation to identify hazards.

### Risk Assessment

Once identified, risks must be assessed:

**Probability × Impact** is the classic framework. Risk severity = likelihood of occurrence × consequence if it occurs. This produces a single number for comparison and prioritization.

**Qualitative assessment** (high/medium/low) is simpler but supports less precise prioritization. Often used when quantitative probability estimates aren't feasible.

**Risk matrices** cross-tabulate probability and impact, creating visual representations of risk landscape. Common in many industries for communicating risk profiles.

**Scenario-based assessment** develops specific scenarios and assesses their likelihood and consequences, avoiding the abstraction of probability estimates for never-before-seen events.

**Bow-tie analysis** maps causes (left side) through the hazard (center) to consequences (right side), identifying prevention barriers and mitigation barriers.

For AI, probability estimation is particularly challenging:
- How likely is a specific failure mode?
- With limited operating history, probability estimates are highly uncertain
- Unpredictable capability boundaries make failure prediction difficult
- Novel failures may not resemble historical patterns

### Risk Prioritization

Resources are limited; not all risks can be addressed equally:

**Expected value ranking** prioritizes by probability × impact. Simple and intuitive, but may underweight low-probability, high-consequence risks.

**Risk appetite** defines what level of risk is acceptable. Different stakeholders may have different appetites—organizations must decide whose risk appetite governs.

**Consequence-focused prioritization** may focus on high-consequence risks regardless of probability, especially for catastrophic outcomes. Some consequences are unacceptable even at low probability.

**ALARP (As Low As Reasonably Practicable)** framework balances risk reduction against cost of reduction. Reduce risk until further reduction is disproportionate to benefit.

### Risk Mitigation

Once prioritized, risks can be addressed through several strategies:

**Avoid**: Don't deploy AI in high-risk contexts. Eliminate the risk by eliminating the activity. Sometimes the right answer is not to use AI.

**Transfer**: Insurance, contractual provisions, shared responsibility. Shift risk to parties better able to bear it.

**Mitigate**: Reduce probability or consequence through controls. For AI, this might include output filtering, human review requirements, usage restrictions, monitoring and alerting, fallback procedures.

**Accept**: Acknowledge residual risk after other measures. Some risk remains; accept it consciously.

**Controls** can be:
- **Preventive**: Reduce probability (access controls, input validation)
- **Detective**: Identify when problems occur (monitoring, anomaly detection)
- **Corrective**: Reduce consequences (rollback, human override)

### Residual Risk

Risk management reduces but doesn't eliminate risk. Residual risk is what remains after mitigation. It must be:
- Quantified (to the extent possible)
- Documented clearly
- Accepted consciously by appropriate stakeholders
- Monitored over time

For AI, residual risk includes:
- Unknown failure modes
- Edge cases not tested
- Adversarial attacks not anticipated
- Performance degradation over time
- Model changes by providers

Acknowledging residual risk is essential. Evaluation doesn't guarantee safety—it reduces risk and characterizes what remains.

### Enterprise Risk Management (ERM)

ERM takes organization-wide view of risk:
- Aggregating risks across units
- Understanding risk interdependencies
- Aligning risk appetite with strategy
- Building risk-aware culture

For AI, ERM perspective considers:
- How do AI risks relate to other organizational risks?
- What's the organization's appetite for AI risk?
- How does AI risk fit strategic objectives?
- Are AI risks correlated across different applications?

---

## What Transfers to AI Evaluation

**Structured risk identification**: Systematic approaches to finding risks, rather than ad hoc consideration. Use checklists, structured methods, and diverse perspectives.

**Risk-based prioritization**: Focus evaluation resources on highest-risk areas. Not all AI uses warrant the same scrutiny.

**Residual risk concept**: Evaluation reduces but doesn't eliminate risk. Characterize what remains honestly.

**Risk monitoring**: Ongoing risk tracking after deployment, not just pre-deployment assessment. Risks evolve; monitoring must be continuous.

**Risk communication**: Clear communication of risk levels to decision-makers. Don't hide uncertainty behind false precision.

---

## What Breaks for Generative AI

**Probability estimation**: AI failure probabilities are hard to estimate with limited history and unpredictable failures. Traditional probability estimates may not be meaningful.

**Enumerable failures**: Traditional risk analysis assumes you can list what might go wrong. AI failures may be unforeseen—the space of possible failures is unbounded.

**Independence assumptions**: Standard risk analysis assumes risks are independent. AI risks may be correlated (same model flaws affect multiple use cases).

**Clear boundaries**: Risk analysis assumes clear system boundaries. AI systems have fuzzy boundaries—where does the AI system end and the user/context begin?

---

## What Can Be Adapted

**Scenario planning** that develops specific scenarios rather than abstract probability estimates. Focus on plausible scenarios and their consequences.

**Red team-informed risk assessment** that uses adversarial testing to inform risk identification. What attacks actually succeed informs probability estimates.

**Dynamic risk assessment** that updates as new information emerges. Initial assessments are tentative; update based on experience.

---

## Implications for AI Evaluation

**Use risk frameworks to prioritize evaluation.** Not all AI uses warrant the same scrutiny. Focus on highest-consequence applications.

**Accept that risk can't be eliminated.** Characterize residual risk honestly. Don't promise certainty that evaluation can't provide.

**Plan for ongoing risk monitoring.** Pre-deployment evaluation isn't sufficient. Continuous monitoring is essential.

**Expect unknown unknowns.** Design for detection and response, not just prevention. Some failures can't be anticipated.

**Communicate risk clearly.** Decision-makers need honest risk assessments, not false precision or hidden uncertainty.

---

## Key References

- **ISO 31000 (Risk Management—Guidelines).** International standard for risk management.

- **NIST AI Risk Management Framework.** AI-specific risk management guidance.

- **Kaplan, S., & Garrick, B.J. (1981). "On the Quantitative Definition of Risk." *Risk Analysis*.** Foundational paper on risk definition.

- **Hubbard, D.W. (2020). *The Failure of Risk Management* (2nd ed.).** Critical examination of risk management practice.

- **Aven, T. (2012). *Foundations of Risk Analysis* (2nd ed.).** Comprehensive treatment of risk analysis foundations.

---

## Connections to Other Sections

Risk analysis connects to several other disciplines covered in this appendix:

- **Section 4.5 (Safety Engineering)** provides hazard analysis methods and safety case approaches.

- **Section 1.5 (Cybersecurity)** offers threat modeling and red teaming for adversarial risk assessment.

- **Section 4.2 (Reliability Engineering)** addresses failure modes and reliability assessment.

- **Section 3.3 (Cost Analysis)** incorporates risk into investment evaluation through risk-adjusted returns.

- **Section 7.2 (Standards)** includes emerging AI risk management standards.

---

*[End of Section 4.1]*
