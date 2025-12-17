# Appendix A, Section 4.5: Safety Engineering

## Overview

Safety engineering focuses on preventing hazards and ensuring systems don't cause harm. For AI in safety-critical applications, safety engineering methods provide frameworks for hazard analysis and structured safety argumentation.

While safety engineering developed primarily for physical systems (nuclear plants, aircraft, chemical facilities), its methods for systematic hazard analysis and safety argumentation are increasingly being adapted for AI systems.

---

## Core Concepts

### Hazard Analysis

A hazard is a condition that could lead to harm. Safety analysis identifies hazards and their pathways to harm:

**What hazards exist?** Energy sources, dangerous materials, error possibilities, failure modes that could cause harm.

**What triggers them?** Conditions, actions, combinations of factors that activate hazards.

**What are the consequences?** Severity, reversibility, scope of harm.

For AI, hazards include:
- Incorrect outputs leading to bad decisions
- Biased outputs causing discrimination
- AI unavailability at critical moments
- AI being used to cause harm
- AI failures in safety-critical control loops
- Privacy violations from AI processing

### Fault Tree Analysis (FTA)

FTA works top-down from an undesired event to identify causes:

1. Start with the top event (the hazard/accident)
2. Identify immediate causes (connected by AND/OR gates)
3. Continue decomposing until reaching basic events
4. The resulting tree shows all paths to the hazard

**AND gates**: All inputs must occur for output to occur
**OR gates**: Any input occurring causes output

FTA enables:
- Identifying all paths to hazards
- Computing hazard probability from component probabilities
- Identifying single points of failure
- Prioritizing mitigation efforts

For AI, FTA might trace how AI errors could lead to harm, identifying contributing factors at each level.

### Event Tree Analysis (ETA)

ETA works forward from an initiating event through possible outcomes:

1. What initiating events could occur?
2. What barriers/safeguards exist? Do they succeed or fail?
3. What outcomes result from each path?

ETA shows the branching possibilities following an initial event and estimates outcome probabilities based on barrier effectiveness.

For AI, ETA might trace: AI produces incorrect output → Does human review catch it? (Yes/No) → If no, does downstream check catch it? → Final outcomes.

### System-Theoretic Process Analysis (STPA)

STPA, developed by Nancy Leveson, takes a systems perspective:

**Systems fail not just from component failures but from unsafe interactions.** Traditional FTA focuses on component failures; STPA recognizes that accidents can occur when components work as designed but interact unsafely.

**Focus on control structures.** Systems are modeled as hierarchical control structures. Safety analysis examines control actions and their potential for being unsafe.

**Unsafe control actions include:**
- Control action not provided when needed
- Control action provided when shouldn't be
- Control action provided too early/late
- Control action stopped too soon/applied too long

For human-AI systems, STPA is particularly valuable:
- Model the human-AI control structure
- Identify unsafe control actions (human trusts AI when shouldn't, AI provides wrong recommendation, human overrides AI incorrectly)
- Analyze how unsafe actions can occur
- Design constraints to prevent unsafe actions

STPA recognizes that safety isn't just about component reliability—it's about the system structure and interactions.

### Safety Cases

A safety case is a structured argument that a system is acceptably safe:

**Claims**: What safety properties are asserted? What level of safety is claimed?

**Evidence**: What data, test results, analysis, and documentation support each claim?

**Argument**: How does evidence support claims? What logical structure connects them?

**Context**: What assumptions and scope limitations apply? Under what conditions does the argument hold?

**Goal Structuring Notation (GSN)** provides visual representation of safety arguments, showing how top-level goals are supported by sub-goals, ultimately grounded in evidence.

For AI, safety cases are emerging as frameworks for structured safety argumentation. Rather than simply claiming "the AI is safe," safety cases:
- Make claims explicit and precise
- Show what evidence supports each claim
- Make the argument structure visible
- Identify assumptions and limitations
- Enable critical review

### Functional Safety

Functional safety (IEC 61508 and derivatives) addresses safety achieved through control systems:

**Safety Integrity Levels (SIL)** define required reliability:
- SIL 1: Failure probability 10⁻¹ to 10⁻² per hour of dangerous failures
- SIL 4: Failure probability 10⁻⁴ to 10⁻⁵ per hour of dangerous failures

Higher SILs require:
- More rigorous development processes
- More extensive verification
- Hardware architectural requirements
- Proven-in-use or diverse redundancy

**Defense in depth** through multiple independent protections. Don't rely on single barriers.

For AI, functional safety concepts are being adapted, though AI doesn't fit neatly into the framework designed for programmed control systems. AI's non-determinism and opacity challenge traditional functional safety approaches.

### Safety Culture

Safety isn't just technical—it's organizational:

**Reporting culture**: People report safety concerns without fear
**Learning culture**: Organization learns from incidents and near-misses
**Just culture**: Balance accountability with non-punitive reporting
**Informed culture**: Shared understanding of risks

For AI, safety culture means:
- Users empowered to report AI problems
- Organization learning from AI failures
- Non-punitive environment for raising AI concerns
- Shared understanding of AI risks and limitations

---

## What Transfers to AI Evaluation

**Hazard analysis mindset**: Systematically identify how AI could cause harm. What could go wrong? What are the consequences?

**Safety case methodology**: Structured argumentation applicable to AI safety claims. Make arguments explicit and contestable.

**STPA for human-AI systems**: Systems perspective on safety captures interactions. Human-AI teams can fail through interaction failures, not just component failures.

**Defense in depth**: Multiple protections rather than relying on AI alone. Human oversight, automated checks, fallback procedures.

**Safety culture**: Organizational factors affect safety outcomes. Technical controls aren't sufficient without supporting culture.

---

## What Breaks for Generative AI

**Component failure models**: AI doesn't fail like hardware components. Traditional FTA/reliability models assume component failures can be enumerated and their probabilities estimated.

**Quantitative failure rates**: AI failure probabilities are hard to estimate. SIL-style quantitative reliability requirements are difficult to apply.

**Formal verification**: Safety properties generally can't be formally verified for AI. You can't prove AI won't produce harmful outputs.

**Deterministic behavior**: Safety analysis often assumes deterministic systems. AI's stochastic nature complicates analysis.

---

## What Can Be Adapted

**STPA for AI systems**: Apply systems thinking to human-AI interaction, identifying unsafe control actions and how they can occur.

**Qualitative safety cases**: Structure safety arguments even without quantitative probability claims. Make the argument explicit.

**Hazard analysis adapted for AI**: Systematic identification of AI-specific hazards using modified FMEA or HAZOP approaches.

**Layered defenses for AI**: Design multiple layers of protection—AI outputs, human review, automated checks, fallback procedures.

---

## Implications for AI Evaluation

**For safety-critical AI, apply safety engineering methods.** Hazard analysis, safety cases, and STPA provide structured approaches.

**Develop safety cases** for high-stakes deployments. Make safety arguments explicit, evidence-based, and contestable.

**Use STPA** to analyze human-AI control structures. Safety emerges from the system, not just AI capability.

**Design for AI failure**: monitoring, override, fallback. Assume AI will fail and design accordingly.

**Cultivate safety culture** around AI. Technical controls need organizational support.

---

## Key References

- **Leveson, N.G. (2011). *Engineering a Safer World*.** STPA methodology and systems safety thinking.

- **IEC 61508 (Functional Safety).** Foundation for functional safety standards.

- **Bloomfield, R., & Bishop, P. (2010). "Safety and Assurance Cases: Past, Present and Possible Future."** Overview of safety case methodology.

- **Hollnagel, E. (2014). *Safety-I and Safety-II*.** Modern safety thinking emphasizing systems perspective.

- **GSN Community Standard.** Goal Structuring Notation for safety arguments.

- **Koopman, P., & Wagner, M. (2016). "Challenges in Autonomous Vehicle Testing and Validation." *SAE International*.** Safety challenges for AI-adjacent autonomous systems.

---

## Connections to Other Sections

Safety engineering connects to several other disciplines covered in this appendix:

- **Section 4.1 (Risk Analysis)** provides risk frameworks that complement safety analysis.

- **Section 4.2 (Reliability Engineering)** addresses reliability aspects of safety.

- **Section 1.3 (Autonomous Systems)** applies safety concepts to autonomous vehicles and similar systems.

- **Section 5.2 (Human Factors)** addresses human reliability and human-AI interaction in safety contexts.

- **Section 6.1 (AI Safety Evaluation)** addresses emerging AI-specific safety evaluation methods.

- **Section 1.5 (Cybersecurity)** addresses security hazards relevant to AI safety.

---

*[End of Section 4.5]*
