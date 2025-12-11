# Appendix A, Section 5.2: Human Factors and Human-Machine Systems

## Overview

Human factors engineering studies how humans interact with systems, emphasizing human capabilities and limitations. For human-AI teaming, this field provides deep expertise on trust, automation, workload, and situation awareness—directly applicable to understanding how people work with AI.

Human factors emerged from studying complex systems like aviation, nuclear power, and military operations. Its insights about automation are directly relevant to AI, which is a new form of automation.

---

## Core Concepts

### Human Information Processing

Human cognition has well-documented characteristics and limitations:

**Attention** is limited and selective. Humans can't attend to everything; attention is a scarce resource that must be allocated.

**Working memory** can hold only a few items (roughly 4-7 chunks). Complex information must be chunked or externalized.

**Long-term memory** is vast but retrieval is imperfect. We forget, misremember, and confuse memories.

**Decision making** uses heuristics and is subject to biases. We satisfice rather than optimize; we're influenced by framing and context.

AI assistance interacts with these characteristics:
- AI might reduce cognitive load (good) or add new monitoring demands (bad)
- AI might support decision making or induce new biases
- AI outputs must fit within human cognitive limits to be usable

### Workload

Workload refers to mental and physical demands on operators:

**Underload** can lead to:
- Boredom and disengagement
- Vigilance failure (missing important events)
- Skill degradation from lack of practice
- Loss of situation awareness

**Overload** can lead to:
- Errors from rushing or cutting corners
- Stress and poor judgment
- Breakdown and inability to cope
- Tunnel vision and missed information

**NASA-TLX** measures perceived workload across dimensions: mental demand, physical demand, temporal demand, performance, effort, frustration.

AI's effect on workload is not straightforward:
- AI might reduce some task demands
- AI might add monitoring demands (checking AI outputs)
- Managing AI output quality is itself work
- Net effect depends on task, AI quality, and user skill

### Situation Awareness

Endsley's model of situation awareness has three levels:

**Level 1: Perception** of elements in the environment. What's happening?

**Level 2: Comprehension** of their meaning. What does it mean?

**Level 3: Projection** of future status. What will happen next?

Loss of situation awareness is implicated in many accidents. People lose track of what's happening and are surprised by events.

For human-AI teams:
- Does AI support or undermine situation awareness?
- If AI handles tasks automatically, does the human lose awareness of what's happening?
- Out-of-the-loop performance problems: humans can't intervene effectively if they've lost situation awareness
- AI might improve SA (providing information) or degrade it (hiding what's happening)

### Trust in Automation

Trust determines whether and how humans use automation:

**Overtrust (complacency)**: Accepting automation outputs uncritically. Failing to catch errors because you assume automation is reliable.

**Undertrust (disuse)**: Not using automation when it would help. Ignoring good recommendations because you don't trust the system.

**Calibrated trust**: Matching trust to actual reliability. Trusting when automation is reliable; questioning when it's not.

Trust calibration is difficult when reliability varies across conditions. The jagged capability frontier—where AI performs well on some tasks but fails unpredictably on similar tasks—makes trust calibration particularly challenging.

Trust develops through experience, feedback, and understanding. Appropriate trust requires:
- Accurate understanding of system capabilities
- Feedback about system performance
- Experience across varied conditions

### Automation Surprises

When automation behaves unexpectedly, humans experience "automation surprises":
- "What's it doing?"
- "Why did it do that?"
- "What will it do next?"

**Mode confusion**—not knowing what mode the automation is in—contributes to surprises. If users don't know the system state, they can't predict its behavior.

AI's unpredictable behavior generates frequent surprises. Users may not understand why AI produced particular outputs or how to get different results.

### Levels of Automation

Sheridan and Verplank's 10-level scale ranges from fully manual to fully autonomous:

1. Human does everything
2. Computer offers suggestions
3. Computer suggests one alternative
4. Computer narrows alternatives
5. Computer executes if human approves
6. Computer executes; human can veto
7. Computer executes; informs human
8. Computer executes; informs if asked
9. Computer executes; informs if it decides to
10. Computer does everything, ignores human

Different levels have different evaluation needs:
- Lower levels (human-in-the-loop): Evaluate human use of AI suggestions
- Higher levels (AI autonomous): Evaluate AI capability comprehensively
- Middle levels: Evaluate human-AI coordination

Most AI assistants operate at levels 2-4: offering suggestions that humans can accept, modify, or reject. Evaluation must address both AI suggestion quality and human use of suggestions.

### Skill Degradation

When automation handles tasks, human skills for those tasks may atrophy. If automation fails and humans must take over, they may not be able to perform effectively.

This creates a paradox:
- Automation handles routine tasks
- Humans only intervene for unusual situations
- But unusual situations require skills that have degraded from disuse
- Performance in exactly the situations where humans are needed may be worst

For AI, skill degradation concerns ask:
- If workers rely on AI for tasks, do their underlying skills decline?
- Can they perform without AI if needed?
- Does AI deskill the workforce over time?

---

## What Transfers to AI Evaluation

**Trust calibration research** directly applies. Are users trusting AI appropriately? Not too much, not too little?

**Automation surprises** occur frequently with AI. Understanding and mitigating them is essential.

**Situation awareness** concepts apply to human-AI teams. Do humans maintain awareness of AI-assisted work?

**Workload effects** should be measured, not assumed positive. AI may increase monitoring workload while reducing task workload.

**Skill degradation** is a legitimate concern for AI-assisted work. Track skill effects over time.

---

## What Breaks for Generative AI

**Predictable automation**: Traditional automation is more predictable than AI. Trust calibration research assumes you can characterize reliability conditions.

**Defined interfaces**: AI interaction is often conversational, not button-based. Traditional automation has clearer interfaces.

**Stable reliability**: AI reliability varies unpredictably across tasks. Traditional automation has more stable reliability profiles.

**Clear modes**: AI doesn't have "modes" in the traditional sense. Mode confusion takes different forms with AI.

---

## What Can Be Adapted

**Trust calibration interventions**: Training and feedback to help users calibrate trust appropriately. Show users where AI is reliable and where it isn't.

**Transparency mechanisms**: Make AI reasoning more visible to support situation awareness. Help users understand what AI is doing.

**Workload management**: Design AI use to manage total workload, not just task completion.

---

## Implications for AI Evaluation

**Evaluate the human-AI team**, not just AI capability. How do humans use AI? Is the team effective?

**Assess trust calibration**: Are users appropriately skeptical or trusting? Neither complacency nor disuse is desirable.

**Monitor for automation surprises** and their effects. Where are users surprised? What goes wrong?

**Consider workload** effects holistically. AI may shift workload rather than reduce it.

**Track potential skill effects** over time. Monitor whether AI use affects underlying human capabilities.

**Design for human-AI coordination**, not just AI capability.

---

## Key References

- **Parasuraman, R., & Riley, V. (1997). "Humans and Automation: Use, Misuse, Disuse, Abuse." *Human Factors*.** Classic typology of automation use problems.

- **Lee, J.D., & See, K.A. (2004). "Trust in Automation: Designing for Appropriate Reliance." *Human Factors*.** Comprehensive review of automation trust.

- **Endsley, M.R. (2016). *Designing for Situation Awareness* (2nd ed.).** Situation awareness framework and measurement.

- **Wickens, C.D., et al. (2015). *Engineering Psychology and Human Performance* (4th ed.).** Comprehensive human factors textbook.

- **Bainbridge, L. (1983). "Ironies of Automation." *Automatica*.** Classic paper on automation paradoxes.

---

## Connections to Other Sections

Human factors connects to several other disciplines covered in this appendix:

- **Section 5.1 (HCI)** shares concern for human-technology interaction with more emphasis on design.

- **Section 5.4 (JDM)** addresses cognitive biases relevant to trust and decision making.

- **Section 1.3 (Autonomous Systems)** applies human factors to autonomous vehicles and similar systems.

- **Section 4.5 (Safety Engineering)** addresses human factors in safety-critical systems.

- **Section 5.5 (I-O Psychology)** addresses training and performance relevant to skill degradation concerns.

---

*[End of Section 5.2]*
