# Appendix A, Section 1.3: Autonomous Systems Testing and Evaluation

## Overview

Autonomous systems—vehicles that drive themselves, aircraft that fly without pilots, robots that navigate and manipulate without direct human control—represent the closest existing paradigm to generative AI evaluation. Both involve AI components that make decisions under uncertainty. Both must operate reliably in conditions that cannot be fully anticipated. Both raise profound questions about how to achieve justified confidence in systems whose behavior cannot be exhaustively specified or tested.

The autonomous systems community has grappled with these challenges for decades, developing frameworks for levels of autonomy, methods for testing in simulation and reality, approaches to safety cases, and deep expertise in human-machine teaming. This accumulated wisdom offers valuable resources for generative AI evaluation. At the same time, important differences between autonomous systems and generative AI mean that not everything transfers cleanly.

Autonomous systems operate in physical space, where the laws of physics constrain possible behaviors and consequences are often immediately observable. A self-driving car that makes a wrong decision crashes; a drone that loses control falls. Generative AI operates in information space, where outputs are unbounded, failures may be subtle, and consequences may propagate through human decisions in ways that are difficult to trace. These differences matter for evaluation.

This section surveys the key concepts from autonomous systems T&E, examines what applies to generative AI, identifies where the analogy breaks down, and draws out implications for AI evaluation practice.

---

## Core Concepts

### Levels of Autonomy

One of the most influential contributions from autonomous systems research is the development of frameworks describing degrees of autonomy—the extent to which a system operates independently versus under human control.

The SAE J3016 standard for driving automation defines six levels:

- **Level 0 (No Automation)**: Human performs all driving tasks
- **Level 1 (Driver Assistance)**: System assists with either steering or acceleration/braking
- **Level 2 (Partial Automation)**: System controls both steering and acceleration/braking; human must monitor
- **Level 3 (Conditional Automation)**: System handles all driving in certain conditions; human must be ready to intervene
- **Level 4 (High Automation)**: System handles all driving in certain conditions; no human intervention needed
- **Level 5 (Full Automation)**: System handles all driving in all conditions

Similar frameworks exist for other domains. Sheridan and Verplank's classic 10-level scale for human-computer decision-making ranges from "computer offers no assistance" to "computer decides everything, acts autonomously, ignores human." These frameworks help clarify what kind of system we're evaluating, what human role is expected, and what the evaluation should focus on.

Levels of autonomy matter for evaluation because different levels require different evaluation approaches. A Level 2 system where humans must monitor continuously requires evaluation of human vigilance and intervention capability. A Level 4 system that must handle situations autonomously requires much more comprehensive capability testing. The handoff between automation and human—particularly relevant at Level 3—requires specific evaluation attention.

Generative AI doesn't map neatly onto these frameworks. A coding assistant might be "Level 2" for routine code completion (human reviews all suggestions) but effectively "Level 4" for certain automated workflows (code generated and deployed without human review). The level of autonomy often varies by use case, user, and organizational policy rather than being fixed by system design. Still, the underlying questions are relevant: How much is the human in the loop? What interventions are expected? What happens when the human isn't monitoring effectively?

### Operational Design Domain

The Operational Design Domain (ODD) defines the conditions under which an autonomous system is designed to operate. For a self-driving car, the ODD might specify:

- Geographic areas (mapped urban areas, highway only, specific cities)
- Road types (paved roads, divided highways, excluding unpaved surfaces)
- Weather conditions (clear weather, light rain, excluding snow and ice)
- Time of day (daylight only, or including night with adequate lighting)
- Speed ranges (under 65 mph, under 25 mph in urban areas)
- Traffic conditions (normal traffic, excluding construction zones)

The ODD represents a kind of contract: the system is designed and tested to operate within these conditions, and performance claims apply only within the ODD. Outside the ODD, the system may not function correctly, and evaluation has not established expected performance.

ODD thinking brings discipline to capability claims. Rather than asking "can this self-driving car drive?" we ask "under what conditions can it drive, and how do we know?" This prevents overgeneralization from limited testing. A system tested only on California highways in clear weather hasn't demonstrated capability for Boston winters.

Defining an ODD for generative AI is challenging but valuable. What is the "operating envelope" for a language model assistant? One might specify:

- Task types (drafting text, answering factual questions, code assistance—excluding medical diagnosis, legal advice)
- Languages (English, with limited capability in other languages)
- Context requirements (performs best with clear instructions and relevant context provided)
- User populations (assumes users can evaluate output quality in their domain)
- Use patterns (interactive use with human review, not autonomous execution)

Current AI deployments rarely make ODD-like specifications explicit. Capability claims are often vague ("helpful for a wide range of tasks") rather than bounded. Making the operational envelope explicit—and acknowledging uncertainty about performance outside it—would improve both evaluation and deployment.

### The Simulation-to-Real Gap

Autonomous systems are extensively tested in simulation before real-world deployment. Simulation offers advantages: it's cheaper, safer, faster, and allows testing of dangerous scenarios without actual risk. Simulated miles for self-driving cars can be accumulated far faster than physical miles.

But simulation performance doesn't guarantee real-world performance. The "sim-to-real gap" refers to the differences between simulated and real environments that cause systems to perform differently in each. Simulations inevitably simplify reality—the physics may be approximate, the sensor models imperfect, the variety of situations limited. A system optimized for simulation may exploit artifacts that don't exist in reality, or fail to handle real-world phenomena that weren't simulated.

The autonomous systems community has developed approaches to managing the sim-to-real gap:

- **Domain randomization**: Varying simulation parameters to expose the system to diverse conditions
- **High-fidelity simulation**: Investing in more accurate physics, sensors, and scenarios
- **Transfer learning**: Training techniques that improve generalization from simulation to reality
- **Progressive testing**: Using simulation for initial testing, then validating in controlled real-world conditions, then expanding to broader deployment
- **Scenario validation**: Comparing simulation behavior to real-world behavior on matched scenarios

The sim-to-real gap has a direct analog for generative AI: the benchmark-to-real gap. Benchmarks are simulations of real tasks. They simplify and standardize what are actually diverse, contextual, open-ended activities. Performance on a coding benchmark (simulation) doesn't guarantee performance on actual developer workflows (reality). Performance on a medical question-answering dataset doesn't guarantee useful performance in clinical settings.

The strategies for managing sim-to-real transfer are suggestive for AI evaluation. Domain randomization parallels testing across diverse prompts and conditions rather than narrow benchmark distributions. Progressive testing parallels moving from benchmarks to controlled studies to operational pilots. Scenario validation parallels comparing benchmark performance to operational performance on matched tasks.

### Edge Cases and Scenario-Based Testing

Autonomous systems must handle not just typical conditions but also rare, unusual, or challenging situations—edge cases that may occur infrequently but matter enormously when they do. A self-driving car might handle normal highway driving well but fail catastrophically when encountering an unusual obstacle, a confusing construction zone, or unexpected behavior from other road users.

Testing for edge cases is challenging precisely because they're rare and diverse. You can't wait to encounter them naturally—that would require billions of miles of driving. Instead, autonomous systems testing uses scenario-based approaches:

- **Scenario libraries**: Collections of known challenging scenarios derived from accidents, near-misses, and domain expertise
- **Scenario generation**: Systematic methods for generating scenarios that explore the space of possible situations
- **Adversarial scenarios**: Deliberately designed scenarios that stress system capabilities
- **Importance sampling**: Concentrating testing on high-risk scenarios rather than typical ones
- **Combinatorial testing**: Systematically combining factors (weather, traffic, road type) to cover the space efficiently

The combinatorial explosion of possible scenarios is a fundamental challenge. Even with finite factors, the combinations quickly become astronomical. Risk-based prioritization is essential: focus on scenarios that are both plausible and consequential.

Generative AI faces an even more severe version of this challenge. The "scenario space" for a language model—all possible prompts and contexts—is not just large but effectively infinite and continuous. There's no way to enumerate even the categories of possible inputs, let alone the specific instances. The jagged capability frontier means that small changes in prompts can produce dramatically different performance, making systematic coverage even harder.

Still, scenario-based thinking has value. Testing should deliberately explore:

- Different task types and domains
- Varying difficulty levels within task types
- Tasks near the boundaries of claimed capabilities
- Tasks requiring capabilities the system might lack (current events, precise calculation, etc.)
- Potentially problematic content areas
- Adversarial and stress-test inputs

The goal is not exhaustive coverage—impossible for generative AI—but strategic exploration of the capability space with attention to high-risk regions.

### Safety Cases

A safety case is a structured argument, supported by evidence, that a system is acceptably safe for a given application in a given context. Rather than simply claiming "this system is safe," a safety case makes the reasoning explicit:

- **Claims**: Specific assertions about system safety (e.g., "The system will detect pedestrians with probability > 99% in conditions X, Y, Z")
- **Evidence**: Data, test results, analysis supporting each claim
- **Argument**: Logical structure linking evidence to claims and claims to the overall safety conclusion
- **Context**: Assumptions and scope limitations

Safety cases originated in high-hazard industries (nuclear, aerospace, rail) and have been adopted for autonomous systems. Standards like UL 4600 (Standard for Safety for the Evaluation of Autonomous Products) provide frameworks for autonomous vehicle safety cases.

The value of safety cases lies in making reasoning explicit and contestable. Rather than a black-box assertion of safety, stakeholders can examine the argument structure, evaluate the evidence, identify assumptions, and probe weak points. Regulators can assess whether the argument is sound. Over time, as evidence accumulates or assumptions prove wrong, safety cases can be updated.

Safety case methodology is increasingly being adapted for AI systems, particularly in the AI safety research community. An AI safety case might argue:

- The system has been tested for harmful outputs across categories X, Y, Z with results showing acceptably low rates
- The system includes guardrails that prevent certain types of harmful outputs
- Operational procedures ensure human review of high-stakes outputs
- Monitoring will detect anomalous behavior and trigger review
- Therefore, the system is acceptably safe for deployment in context C

This is an active area of development. Challenges include the difficulty of comprehensive testing (the unbounded output space), uncertainty about what "acceptably safe" means for AI, and the rapid pace of change that may invalidate assumptions. But the discipline of structured safety argumentation is valuable regardless of these challenges.

### Human Supervisory Control

Autonomous systems rarely operate in complete isolation from humans. Even highly automated systems typically involve human supervisory control: humans monitor system operation, intervene when necessary, handle situations beyond system capability, and bear ultimate responsibility for outcomes.

Research on human supervisory control has identified several challenges:

**Vigilance and monitoring**: Humans are poor at sustained monitoring of systems that usually work correctly. Attention wanders. Complacency develops. Rare events that require intervention may not be detected in time.

**Mode confusion**: Complex automated systems have many modes of operation. Users may be uncertain which mode the system is in, leading to unexpected behavior and inappropriate responses.

**Skill degradation**: When automation handles routine tasks, human skills for those tasks may atrophy. If automation fails and humans must take over, they may not be able to perform effectively.

**Automation surprises**: When automated systems behave unexpectedly, humans may be startled, confused, and slow to respond appropriately. The more autonomous the system, the greater the potential for surprises.

**Trust calibration**: Humans must calibrate their trust in automation appropriately—neither trusting too much (failing to catch errors) nor too little (failing to realize benefits). Calibration is difficult when automation reliability varies across conditions.

These challenges are directly relevant to human-AI teaming with generative AI. Users monitoring AI outputs face vigilance challenges—most outputs may be fine, leading to reduced scrutiny that misses errors. AI behavior can be surprising when the jagged capability frontier produces unexpected failures. Trust calibration is difficult when AI reliability varies unpredictably across tasks.

Evaluation of human-AI systems must assess not just AI capability but the entire human-AI team: Can users detect and correct AI errors? Do they trust appropriately? Can they intervene effectively? What happens when the AI fails in unexpected ways?

### Verification and Validation for Autonomy

Traditional verification and validation (V&V) assumes you can specify required behavior and check whether the system exhibits it. For autonomous systems with learned components, this is problematic:

- Behavior emerges from training rather than explicit programming
- Requirements may not fully specify desired behavior
- The space of possible situations is too large to test exhaustively
- System behavior may be difficult to predict or explain

The autonomous systems community has developed adapted V&V approaches:

**Scenario-based V&V**: Rather than verifying all possible behaviors, verify behavior in a defined (if large) set of scenarios. Scenarios are selected to be representative, challenging, and safety-relevant.

**Runtime verification**: Rather than pre-deployment verification alone, monitor system behavior during operation and check that it stays within acceptable bounds. Runtime monitors can detect anomalies and trigger safeguards.

**Formal methods (limited scope)**: Some safety-critical properties can be verified formally, even if overall behavior cannot. For example, verifying that certain actions are never taken regardless of inputs, or that the system always maintains certain invariants.

**Statistical verification**: Rather than proving behavior is always correct, estimate the probability of correct behavior based on testing. This requires careful statistical methodology and acknowledgment of uncertainty.

**Assurance cases**: Using structured arguments (like safety cases) to make the case for adequate verification, even when complete verification is impossible.

These approaches inform AI evaluation. Complete verification of generative AI is impossible—the output space is too large, the "correct" output often undefined. But we can verify behavior in selected scenarios, monitor runtime behavior, formally verify certain properties (e.g., certain outputs are filtered), provide statistical performance estimates, and construct assurance arguments for why our evaluation is adequate for the intended use.

---

## What Transfers to AI Evaluation

Several concepts from autonomous systems evaluation apply directly to generative AI:

**Levels of autonomy thinking** encourages clarity about the human role. Is the AI generating suggestions for human review (lower autonomy) or taking actions with minimal oversight (higher autonomy)? Different levels require different evaluation focus. Higher autonomy demands more comprehensive capability testing; lower autonomy demands more attention to human oversight effectiveness.

**ODD discipline** encourages bounded capability claims. Rather than vague assertions that an AI is "helpful" or "capable," ODD thinking asks: for what tasks, in what conditions, with what user populations, and with what confidence? Making the operational envelope explicit improves both evaluation and deployment.

**Sim-to-real gap awareness** directly parallels benchmark-to-real gap awareness. Autonomous systems researchers know that simulation performance doesn't guarantee real-world performance and have developed strategies for managing this gap. AI evaluation should adopt similar humility about benchmarks and similar strategies for validation.

**Scenario-based testing** provides a framework for exploring capability spaces that are too large for exhaustive testing. Strategic scenario selection—diverse, challenging, risk-weighted—is as relevant for AI as for autonomous systems.

**Safety case methodology** offers structured approaches to arguing for acceptable safety. For high-stakes AI deployments, constructing explicit safety cases—with clear claims, evidence, and arguments—brings discipline and transparency to safety assurance.

**Human supervisory control research** is directly applicable to human-AI teaming. Decades of research on vigilance, trust calibration, automation surprises, and intervention effectiveness inform how we should evaluate and design human-AI systems.

**Runtime verification and monitoring** concepts support continuous AI monitoring. Rather than relying solely on pre-deployment testing, AI systems should be monitored during operation, with mechanisms to detect anomalies and trigger review.

---

## What Breaks for Generative AI

Despite substantial overlap, important differences limit how directly autonomous systems approaches apply to generative AI:

**Physical versus information environments**: Autonomous systems operate in physical space governed by physics, with directly observable outcomes. A car crash is unambiguous. Generative AI operates in information space, where "failure" may be subtle (slightly misleading text, suboptimal code, biased framing) and consequences propagate through human decisions in complex ways. The bounded, physical nature of autonomous systems makes evaluation more tractable in some respects.

**Observable failures**: When an autonomous vehicle makes an error, the error is often immediately apparent—it hits something, goes off the road, or behaves erratically. When a language model produces a flawed output, the flaw may not be apparent to users who lack expertise to evaluate it. The observability of failures differs fundamentally.

**Definable operating envelopes**: While ODD definition is challenging for autonomous systems, it's at least conceptually tractable. Geographic bounds, weather conditions, and road types can be specified. For generative AI, the "conditions of operation" are far harder to define. What's the boundary between prompts the system should handle and prompts it shouldn't? The continuous, high-dimensional nature of text makes boundary definition much harder.

**Failure mode predictability**: Autonomous system failures, while not fully predictable, follow patterns related to sensor limitations, environmental conditions, and scenario difficulty. With experience, practitioners develop intuition for likely failure modes. Generative AI failures are less predictable—the jagged capability frontier means that similar-seeming inputs can produce dramatically different performance, without clear patterns explaining why.

**Formal verification scope**: Some autonomous system properties can be formally verified—collision avoidance guarantees, geofencing constraints, speed limits. Generative AI properties are much harder to formalize. What would it mean to formally verify that outputs are "helpful" or "not harmful"? The output space is too large and the relevant properties too ill-defined.

**Development and deployment stability**: Autonomous vehicle development involves long cycles of testing before deployment, with relatively stable software versions. Generative AI systems are often updated continuously, sometimes without user notification. The rapid pace of change challenges evaluation approaches that assume stable systems.

**Regulatory and institutional context**: Autonomous vehicles are subject to emerging regulatory frameworks that shape evaluation requirements. Generative AI largely lacks such frameworks. This cuts both ways—less regulatory overhead, but also less institutional structure supporting rigorous evaluation.

---

## What Can Be Adapted

Many autonomous systems concepts can be adapted for generative AI with appropriate modifications:

**ODD specification for AI** may never achieve the crispness of geographic bounds and weather conditions, but approximate capability boundaries can still be articulated. This AI system is designed for: drafting professional communications (not legal documents), answering factual questions (with limitations on recent events), code assistance (with human review required), English language (limited other language capability). Even imprecise boundaries are better than unbounded capability claims.

**Scenario libraries for AI** can be developed, even though the space can't be enumerated. Collections of challenging prompts, known failure modes, and adversarial inputs can inform systematic testing. These libraries will never be complete, but they can grow with experience and be shared across organizations.

**Sim-to-real validation strategies** can inform benchmark validation. Just as autonomous systems validate simulation with real-world comparison, AI benchmarks can be validated by comparing benchmark performance to operational performance on matched tasks. Finding substantial gaps should reduce confidence in benchmark results.

**Progressive deployment** models from autonomous systems—limited testing, then controlled pilots, then bounded deployment, then broader deployment—can structure AI rollout. Each phase generates evidence and builds confidence, with expansion contingent on positive results.

**Safety case frameworks** can be adapted for AI, as the AI safety community is actively doing. The specific claims and evidence will differ, but the discipline of structured argumentation transfers. What claims about AI safety are we making? What evidence supports each claim? What assumptions are we making? How strong is the overall argument?

**Runtime monitoring concepts** can inform AI monitoring. Define metrics that should stay within acceptable bounds. Implement continuous monitoring. Establish alerting and response procedures for anomalies. This doesn't require solving all AI monitoring challenges—just applying systematic monitoring discipline.

**Human factors evaluation methods** from autonomous systems can be applied to human-AI teams. Evaluate vigilance and oversight quality. Assess trust calibration. Test intervention capabilities. Measure situation awareness. These methods need adaptation for the different human-AI interface (conversation versus vehicle controls), but the underlying concerns are similar.

---

## Implications for AI Evaluation

Drawing on autonomous systems experience, several principles should guide generative AI evaluation:

**Define the operating envelope.** Even if precise boundaries aren't achievable, articulate what the AI is designed and tested for—and what it isn't. Capability claims should be bounded, not open-ended. Evaluation should verify performance within the claimed envelope and probe boundaries and limitations.

**Take the benchmark-to-real gap seriously.** Benchmark performance is necessary but not sufficient, just as simulation performance is necessary but not sufficient for autonomous systems. Plan for validation of benchmark results against operational performance. Investigate discrepancies. Don't assume benchmark success predicts deployment success.

**Use scenario-based testing strategically.** Develop and maintain collections of test scenarios—diverse, challenging, risk-weighted. Include known failure modes, edge cases, and adversarial inputs. Update scenario libraries as new failure modes are discovered. Share scenario resources across organizations where possible.

**Build safety cases for high-stakes deployments.** For AI applications with significant consequences, construct explicit safety cases. Make claims, evidence, and arguments clear and documented. Subject safety cases to review and challenge. Update them as evidence accumulates or assumptions change.

**Evaluate the human-AI system.** Capability evaluation of AI alone is insufficient. Evaluate the full human-AI system: Can users detect errors? Do they trust appropriately? Can they intervene effectively? Human factors evaluation methods from autonomous systems provide a starting point.

**Plan for runtime monitoring.** Pre-deployment evaluation cannot guarantee ongoing performance. Plan monitoring from the start: What will you measure? What are acceptable bounds? How will anomalies be detected and handled? Monitoring is not an afterthought but a core component of evaluation strategy.

**Adopt progressive deployment.** Rather than binary deploy/don't-deploy decisions, consider staged deployment: limited initial deployment with intensive monitoring, expansion based on operational evidence, ongoing monitoring at scale. This generates operational evidence while managing risk.

**Recognize the limits of the analogy.** Autonomous systems experience offers valuable resources, but generative AI is not just another autonomous system. The information-space environment, unbounded outputs, subtle failures, and less predictable behavior all create evaluation challenges beyond what autonomous systems research has addressed. Humility about these limits is appropriate.

---

## Key References

**Levels of Autonomy and Frameworks**

- **SAE International. (2021). SAE J3016: Taxonomy and Definitions for Terms Related to Driving Automation Systems for On-Road Motor Vehicles.** The standard reference for driving automation levels, with broader influence on autonomy discussions.

- **Sheridan, T.B., & Verplank, W.L. (1978). Human and Computer Control of Undersea Teleoperators.** Classic framework for levels of automation in human-computer systems.

- **Parasuraman, R., Sheridan, T.B., & Wickens, C.D. (2000). "A Model for Types and Levels of Human Interaction with Automation." *IEEE Transactions on Systems, Man, and Cybernetics*.** Influential framework analyzing automation across stages of information processing.

**Operational Design Domain**

- **NHTSA. (2017). Automated Driving Systems: A Vision for Safety 2.0.** Introduces ODD concept for regulatory discussion of automated vehicles.

- **BSI PAS 1883:2020. Operational Design Domain (ODD) Taxonomy for an Automated Driving System.** Structured taxonomy for specifying ODDs.

**Simulation and Testing**

- **Kalra, N., & Paddock, S.M. (2016). "Driving to Safety: How Many Miles of Driving Would It Take to Demonstrate Autonomous Vehicle Reliability?" *Transportation Research Part A*.** RAND analysis showing the challenge of demonstrating safety through testing alone—billions of miles required.

- **Koopman, P., & Wagner, M. (2016). "Challenges in Autonomous Vehicle Testing and Validation." *SAE International Journal of Transportation Safety*.** Overview of testing challenges for autonomous vehicles.

- **Corso, A., Moss, R., Koren, M., Lee, R., & Kochenderfer, M.J. (2021). "A Survey of Algorithms for Black-Box Safety Validation of Cyber-Physical Systems." *Journal of Artificial Intelligence Research*.** Survey of approaches to finding failure modes in autonomous systems.

**Safety Cases**

- **UL 4600. (2020). Standard for Safety for the Evaluation of Autonomous Products.** Industry standard providing framework for autonomous vehicle safety cases.

- **ISO 21448. (2022). Road Vehicles—Safety of the Intended Functionality (SOTIF).** Standard addressing safety of intended functionality, beyond traditional functional safety.

- **Bloomfield, R., & Bishop, P. (2010). "Safety and Assurance Cases: Past, Present and Possible Future." In *Making Systems Safer*.** Overview of safety case methodology and its evolution.

- **Haddon-Cave, C. (2009). The Nimrod Review.** Influential analysis of safety case weaknesses in a major accident, with lessons for safety case practice.

**Human Factors in Autonomy**

- **Endsley, M.R. (2017). "Autonomous Driving Systems: A Preliminary Naturalistic Study of the Tesla Model S." *Journal of Cognitive Engineering and Decision Making*.** Study of human interaction with vehicle automation.

- **Lee, J.D. (2018). "Perspectives on Automotive Automation and Autonomy." *Journal of Cognitive Engineering and Decision Making*.** Overview of human factors challenges in vehicle automation.

- **Seppelt, B.D., & Lee, J.D. (2019). "Keeping the Driver in the Loop: Dynamic Feedback to Support Appropriate Use of Imperfect Vehicle Control Automation." *International Journal of Human-Computer Studies*.** Research on maintaining appropriate human engagement with automation.

**V&V for Autonomous Systems**

- **Koopman, P., & Wagner, M. (2017). "Autonomous Vehicle Safety: An Interdisciplinary Challenge." *IEEE Intelligent Transportation Systems Magazine*.** Discussion of safety validation challenges.

- **Thorn, E., Kimmel, S., & Chaka, M. (2018). A Framework for Automated Driving System Testable Cases and Scenarios. (DOT HS 812 623).** NHTSA framework for AV testing scenarios.

- **Webb, N., Smith, D., Ludwick, C., Victor, T., Hommes, Q., Favarò, F., Ivanov, G., & Daniel, T. (2020). "Waymo's Safety Methodologies and Safety Readiness Determinations." *arXiv preprint*.** Waymo's public description of their safety methodology.

**AI Safety Cases (Emerging)**

- **Clymer, J., et al. (2024). "Safety Cases: How to Justify the Safety of Advanced AI Systems." *arXiv preprint*.** Emerging framework for AI safety cases.

- **CLTC. (2025). "Assessing Confidence in Frontier AI Safety Cases." [2502.05791].** Analysis of challenges in AI safety case assessment.

---

## Connections to Other Sections

Autonomous systems T&E connects to several other disciplines covered in this appendix:

- **Section 1.1 (Software Testing)** provides foundational testing concepts that autonomous systems extend to AI-enabled software.

- **Section 1.2 (Systems T&E)** provides the defense acquisition context within which many autonomous systems are evaluated.

- **Section 1.4 (Traditional ML Evaluation)** covers evaluation of the machine learning components within autonomous systems.

- **Section 4.1 (Risk Analysis)** provides risk assessment frameworks applicable to autonomous system safety.

- **Section 4.5 (Safety Engineering)** develops safety analysis methods (FMEA, FTA, STPA) applicable to autonomous systems.

- **Section 5.2 (Human Factors)** expands on human-machine teaming concepts introduced here.

- **Section 6.1 (AI Safety Evaluation)** covers the emerging AI-specific adaptation of safety evaluation concepts, building on autonomous systems foundations.

---

*[End of Section 1.3]*
