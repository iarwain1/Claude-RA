# Appendix A, Section 5.1: Human-Computer Interaction and User Experience Research

## Overview

Human-Computer Interaction (HCI) studies how people interact with computers and technology. The field provides methods for understanding how users actually work with systems—not how designers intend them to work, but how they actually work in practice.

For AI evaluation, HCI methods reveal how users experience AI, what strategies they develop, and where friction arises. The gap between intended AI use and actual AI use is precisely what HCI methods can illuminate.

---

## Core Concepts

### Usability

Usability has multiple dimensions:

**Effectiveness**: Can users accomplish their goals? Does the system enable users to do what they're trying to do?

**Efficiency**: How much effort does it take? Time, cognitive effort, physical effort.

**Satisfaction**: How do users feel about the experience? Frustration, delight, confidence.

**Learnability**: How easily can new users become proficient? Is the learning curve steep or gentle?

**Error rates**: How often do errors occur? How easily are they recovered?

**Memorability**: Can users return after time away and remember how to use it?

For AI, usability extends to:
- Can users effectively prompt AI? Do they know what to ask?
- Can they recognize and correct AI errors? Do they catch mistakes?
- Is the interaction efficient, or do iteration and error-correction consume time?
- Do users trust AI appropriately? Too much? Too little?

### User-Centered Design

UCD puts users at the center of design:

**Understand users and their contexts**: Who are the users? What are they trying to do? What constraints do they face?

**Involve users throughout design**: Not just at the end for testing, but throughout development.

**Iterate based on user feedback**: Design, test, learn, redesign.

**Evaluate with actual users**: Not just expert review but observation of real users.

For AI, UCD suggests:
- Understanding how actual workers would use AI (not how designers imagine)
- Involving users in developing AI integration
- Iterating based on real-world feedback
- Evaluation with representative users doing realistic tasks

### Usability Evaluation Methods

**Heuristic evaluation**: Experts review against usability principles (visibility of system status, match to real world, user control, consistency, error prevention, recognition over recall, flexibility, aesthetic design, help users recognize/recover from errors, help and documentation).

**Cognitive walkthrough**: Step through tasks from user perspective, asking:
- Will users know what to do?
- Will they recognize that correct actions are available?
- Will they understand feedback?

**Usability testing**: Observe real users attempting realistic tasks. Think-aloud protocols have users verbalize their thoughts while working, revealing reasoning and confusion.

**A/B testing**: Compare different designs with different users, measuring which performs better.

For AI, these methods can be applied:
- Heuristic review of AI interfaces
- Cognitive walkthroughs of AI-assisted workflows
- Observation of users working with AI
- Comparison of different prompting approaches or AI integrations

### Contextual Inquiry

Contextual inquiry studies work in its natural context—observing and interviewing workers in their actual work environment:

**Observe actual practice, not idealized procedures**: What people actually do, not what they say they do or what procedures specify.

**Interview about work in context**: Questions prompted by ongoing work, not abstract retrospection.

**Build understanding of work structure and meaning**: How work is organized, what it means to practitioners.

For AI, contextual inquiry reveals:
- How AI integrates (or doesn't) into complex workflows
- Informal workarounds users develop
- Gaps between intended and actual use
- Social and organizational context of AI use

### Task Analysis

**Hierarchical Task Analysis (HTA)** breaks work into goals, sub-goals, and operations—the structure of what workers do.

**Cognitive Task Analysis (CTA)** examines the cognitive demands of work:
- What decisions are made?
- What knowledge is required?
- What makes tasks difficult?
- What expertise is needed?

For AI integration, task analysis identifies:
- Which tasks might AI support?
- What cognitive demands might AI reduce?
- What human judgment must remain?
- Where in the workflow AI fits

### Mental Models

Users develop mental models of how systems work. These may be incomplete or inaccurate, but they guide interaction.

Mental models affect:
- What users expect from the system
- How users interpret system behavior
- How users troubleshoot problems
- Whether users trust system outputs

For AI, mental model questions include:
- Do users understand what AI can and can't do?
- Do they have accurate models of when AI is reliable?
- Do they understand how prompting affects outputs?
- Mismatched mental models lead to misuse—over-reliance when AI isn't reliable, under-use when AI could help.

### Situated Action

Lucy Suchman's influential work showed that action is always situated in specific contexts. Users don't follow predetermined plans; they improvise with available resources in response to local circumstances.

Implications:
- Can't fully specify how technology will be used in advance
- Users adapt tools to local circumstances
- Context shapes how tools are used
- Designers' intentions don't determine use

For AI, this suggests evaluation in realistic contexts, not isolated tasks. How users work with AI in situated practice may differ from how they respond to standardized evaluation tasks.

---

## What Transfers to AI Evaluation

**Usability methods** can evaluate AI interfaces and interactions. How easy is AI to use? Where does friction arise?

**Contextual inquiry** reveals real AI use patterns, workarounds, and problems. Observation in context catches what surveys miss.

**Task analysis** identifies where AI fits in work structure. What tasks benefit from AI? What human judgment remains essential?

**Mental models** highlight user understanding and misunderstanding of AI. Do users understand AI's capabilities and limitations?

**Situated action** emphasizes evaluation in realistic contexts. Lab tasks may not capture real-world AI use.

---

## What Breaks for Generative AI

**Clear task definition**: HCI often assumes defined tasks; AI use is more open-ended. "Use AI to help with work" isn't a task in the traditional sense.

**Consistent system behavior**: Usability assumes consistent responses; AI varies. The same input may produce different outputs.

**Error definition**: What counts as an "error" when AI output is probabilistic? When is AI "wrong"?

**Designer control**: Traditional HCI assumes designers control system behavior. AI behavior is emergent and unpredictable.

---

## What Can Be Adapted

**Adaptive usability testing** that accounts for AI variability. Multiple trials with same users; focus on patterns rather than single instances.

**Longitudinal studies** that track how AI use evolves over time. Initial use differs from experienced use.

**Mixed-method approaches** combining observation, interview, and log analysis to understand AI use comprehensively.

---

## Implications for AI Evaluation

**Use HCI methods** to understand how users actually work with AI, not just whether AI works technically.

**Conduct contextual inquiry** in real work settings. Observe AI use in context.

**Assess mental models**: Do users understand AI capabilities and limits? Mismatched mental models lead to misuse.

**Recognize situated nature** of AI use. Lab evaluations may not capture real-world use patterns.

**Evaluate usability alongside capability.** AI that's technically capable but unusable doesn't help users.

---

## Key References

- **Nielsen, J. (1993). *Usability Engineering*.** Classic usability text.

- **Beyer, H., & Holtzblatt, K. (1998). *Contextual Design*.** Comprehensive contextual inquiry methodology.

- **Suchman, L. (1987). *Plans and Situated Actions*.** Foundational work on situated action and technology use.

- **Amershi, S., et al. (2019). "Guidelines for Human-AI Interaction." *CHI*.** AI-specific interaction guidelines.

- **Norman, D. (1988). *The Design of Everyday Things*.** Foundational text on user-centered design.

- **Crandall, B., Klein, G., & Hoffman, R.R. (2006). *Working Minds: A Practitioner's Guide to Cognitive Task Analysis*.** CTA methods.

---

## Connections to Other Sections

HCI connects to several other disciplines covered in this appendix:

- **Section 5.2 (Human Factors)** shares concern for human-technology interaction with more emphasis on cognitive factors and automation.

- **Section 5.4 (JDM)** addresses cognitive biases relevant to AI interaction.

- **Section 2.4 (Qualitative Methods)** provides research methods used in HCI.

- **Section 5.5 (I-O Psychology)** addresses work design and performance relevant to AI integration.

- **Section 5.3 (Organizational Behavior)** addresses organizational context of technology adoption.

---

*[End of Section 5.1]*
