# Appendix A, Section 4.4: Audit and Assurance

## Overview

Audit provides independent assurance that something is as claimed. The audit profession has developed rigorous methods for evidence gathering, independence, and professional judgment that can inform AI evaluation governance.

For AI evaluation, audit concepts are relevant in two ways: audit methods can inform how AI evaluation is conducted, and AI systems themselves may become subjects of audit as AI governance matures.

---

## Core Concepts

### Audit Objectives and Levels of Assurance

Audits provide opinions on whether claims are accurate:

**Reasonable assurance**: High but not absolute confidence. The auditor has gathered sufficient evidence to support an opinion. This is the standard for financial statement audits.

**Limited assurance**: Lower confidence, less extensive procedures. The auditor hasn't found anything wrong, but procedures were limited. Common for review engagements.

Audit opinions don't guarantee truth but provide independent assessment of claim credibility. An unqualified audit opinion means the auditor found claims to be fairly stated based on evidence examined.

**Audit scope** defines what's covered. Scope limitations affect what conclusions can be drawn.

### Independence and Objectivity

Auditor independence is fundamental:

**Independence in fact**: Actually having objective judgment

**Independence in appearance**: Being seen as objective by reasonable observers

Key independence principles:
- Independence from the entity being audited
- No conflicts of interest
- No financial ties that could bias judgment
- Professional skepticism—not taking claims at face value

For AI, independence means evaluation by parties separate from developers/vendors with no stake in favorable outcomes. Self-evaluation lacks the credibility of independent evaluation.

### Materiality

Not everything warrants equal scrutiny. Materiality focuses attention on what matters:

**Quantitative materiality**: How large is the potential misstatement? Small errors may not be material.

**Qualitative materiality**: What would change decisions if different? Some small errors matter if they're qualitatively significant.

Materiality thresholds determine audit scope—auditors focus on items likely to be material, not exhaustive checking of everything.

For AI evaluation, materiality suggests focusing on claims that matter most for deployment decisions, not exhaustive evaluation of everything. What errors would change the decision?

### Audit Evidence

Evidence types include:

**Documentary**: Records, logs, documents. Often considered more reliable than testimony.

**Testimonial**: Interviews, representations. Subject to bias but provides context.

**Observational**: Watching processes in action. Reveals what actually happens vs. what's claimed.

**Analytical**: Examining patterns, comparing to expectations. Flags anomalies for investigation.

Evidence should be:
- **Sufficient**: Enough of it to support conclusions
- **Appropriate**: Relevant and reliable for the purpose

Evidence from independent sources is generally more reliable than evidence from the entity being audited.

For AI, evidence might include:
- Benchmark results (documentary)
- User studies (testimonial and observational)
- Incident logs (documentary)
- Usage data (documentary)
- Expert review of outputs (observational/analytical)

### The Three Lines of Defense Model

Organizational assurance is layered:

**First line**: Operational management and controls. The people doing the work and their immediate oversight.

**Second line**: Risk management and compliance functions. Independent functions monitoring the first line.

**Third line**: Internal audit. Independent assurance on the effectiveness of both first and second lines.

**External audit** provides independent assurance to external stakeholders.

For AI, this suggests:
- First line: Operational teams monitoring AI use, catching obvious problems
- Second line: Risk/compliance overseeing AI governance, ensuring policies are followed
- Third line: Internal audit independently assessing AI controls and governance
- External: Independent evaluation for high-stakes decisions

### Audit Procedures

Common audit procedures include:

**Inspection**: Examining records and documents
**Observation**: Watching processes in action
**Inquiry**: Asking questions of knowledgeable parties
**Confirmation**: Obtaining third-party verification
**Recalculation**: Independently verifying calculations
**Reperformance**: Independently performing procedures
**Analytical procedures**: Evaluating through analysis of relationships

For AI evaluation, analogous procedures might include:
- Inspection: Reviewing evaluation records, benchmark results
- Observation: Watching AI use in practice
- Inquiry: Interviewing users about experiences
- Reperformance: Independently running evaluations
- Analytical: Analyzing patterns in AI outputs and errors

---

## What Transfers to AI Evaluation

**Independence principle**: Evaluation by parties independent of developers/vendors. For high-stakes decisions, independent evaluation is essential.

**Materiality**: Focus on what matters for decisions. Not all AI capabilities warrant equal scrutiny.

**Evidence standards**: Rigor in gathering and evaluating evidence. Multiple sources; appropriate methods.

**Professional skepticism**: Not accepting claims at face value. Probe, verify, triangulate.

**Layered assurance**: Multiple lines of defense for AI governance. Don't rely on single evaluation point.

---

## What Breaks for Generative AI

**Established standards**: Financial audit has mature standards; AI audit is emerging. No consensus yet on what "AI audit" means.

**Clear assertions**: Financial statements have defined assertions; AI claims are fuzzier. What exactly is being asserted about AI capability?

**Audit trail**: Traditional systems have clear trails; AI processing is opaque. You can't trace how AI reached a conclusion.

**Stable criteria**: Audit compares against stable criteria (GAAP, regulations). AI evaluation criteria are contested and evolving.

---

## What Can Be Adapted

**Adapted audit frameworks** for AI evaluation, specifying what claims are being assessed, what evidence is appropriate, and what assurance level can be achieved.

**Tiered assurance levels** recognizing that not all AI deployments need the same assurance level. High stakes warrant more rigorous evaluation.

**Independence requirements** scaled to decision stakes. Routine AI may be self-evaluated; high-stakes AI needs independent assessment.

---

## Implications for AI Evaluation

**Apply independence** for high-stakes AI decisions. Don't rely solely on vendor evaluations.

**Use materiality** to scope evaluation appropriately. Focus on what matters for the decision at hand.

**Develop evidence standards** for AI evaluation. What evidence supports what conclusions? How much evidence is sufficient?

**Consider governance structures** with appropriate assurance layers. First, second, and third line functions for AI governance.

**Maintain professional skepticism.** Don't accept AI capability claims at face value. Probe, verify, test.

---

## Key References

- **AICPA Audit Standards.** Professional standards for financial audit.

- **IIA Standards.** International Standards for Internal Auditing.

- **Raji, I.D., et al. (2020). "Closing the AI Accountability Gap." *FAccT*.** Framework for AI auditing.

- **PCAOB Standards.** Public company audit standards.

- **COSO Internal Control Framework.** Framework for organizational controls relevant to assurance.

---

## Connections to Other Sections

Audit connects to several other disciplines covered in this appendix:

- **Section 4.1 (Risk Analysis)** informs risk-based audit planning and prioritization.

- **Section 4.3 (Quality Management)** provides quality systems that auditors assess.

- **Section 7.2 (Standards)** addresses emerging AI governance standards relevant to audit.

- **Section 1.2 (Systems T&E)** shares independence principles for evaluation.

- **Section 6.1 (AI Safety Evaluation)** addresses emerging AI-specific evaluation frameworks.

---

*[End of Section 4.4]*
