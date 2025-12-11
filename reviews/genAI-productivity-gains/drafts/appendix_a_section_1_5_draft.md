# Appendix A, Section 1.5: Cybersecurity Testing and Red Teaming

## Overview

Cybersecurity testing represents one of the most adversarially mature evaluation disciplines. For decades, security professionals have grappled with a fundamental challenge that resonates deeply with AI evaluation: how do you assess a system against attackers whose methods are unknown, constantly evolving, and deliberately designed to find weaknesses you haven't anticipated?

The security field's answer has been to develop an adversarial evaluation culture—one where the goal is not merely to confirm that systems work under expected conditions, but to actively discover how they can be made to fail. Red teaming, penetration testing, bug bounties, and threat modeling all embody this adversarial mindset. They assume that the most important failures are the ones you haven't thought of yet, and they create structured approaches for thinking the unthinkable.

For AI evaluation, cybersecurity provides both methods and mindset. The methods—structured red teaming, threat modeling, fuzzing, responsible disclosure—can be adapted for AI safety evaluation. The mindset—assume adversaries exist, assume you've missed something, design for resilience not just prevention—may be even more valuable. AI systems face not just malicious adversaries but also the ordinary creativity of users who will inevitably push systems in unanticipated directions.

This section surveys key concepts from cybersecurity testing, examines how they apply to AI evaluation, identifies where the security paradigm breaks down, and draws implications for AI evaluation practice.

---

## Core Concepts

### Red Team / Blue Team / Purple Team

The red team/blue team model divides security evaluation into distinct adversarial roles:

**Red teams** are authorized attackers who attempt to find and exploit vulnerabilities. Their job is to think like adversaries—identify weaknesses, develop exploits, and demonstrate what a real attacker could achieve. Red teams operate under rules of engagement that scope their activities but within those bounds try to be as creative and persistent as real attackers.

**Blue teams** are defenders responsible for protecting systems, detecting attacks, and responding to incidents. They represent the organization's actual security posture and capabilities.

**Purple teams** facilitate collaboration between red and blue, ensuring that red team findings translate into improved defenses. Rather than simply revealing vulnerabilities and moving on, purple team activities focus on learning and improvement.

This tripartite model creates productive tension. Red teams provide independent, adversarial assessment unconstrained by defensive assumptions. Blue teams provide real-world defensive context. Purple teams ensure the adversarial findings actually improve security rather than just documenting it.

For AI, the red team concept has been directly adopted. AI red teaming involves adversarial probing for harmful outputs, jailbreaking attempts, and systematic exploration of failure modes. The red team framing emphasizes that evaluation should actively try to make the AI fail—not just confirm it works in expected cases—and that this adversarial probing provides information that cooperative testing cannot.

### Penetration Testing

Penetration testing ("pentesting") is a structured methodology for authorized attack simulation:

1. **Scoping**: Define what systems are in scope, what techniques are permitted, and what success looks like
2. **Reconnaissance**: Gather information about the target system
3. **Vulnerability identification**: Find potential weaknesses
4. **Exploitation**: Attempt to exploit identified vulnerabilities
5. **Post-exploitation**: Assess what an attacker could do after initial compromise
6. **Reporting**: Document findings, severity, and recommendations

Penetration testing is bounded and authorized—testers have explicit permission to attack within defined scope. This distinguishes it from actual attacks and enables organizations to learn from simulated attacks without actual harm.

The structured pentesting methodology offers a template for AI evaluation. Scoping parallels defining what AI capabilities and behaviors are being evaluated. Reconnaissance parallels understanding how the AI system works—its interfaces, capabilities, and potential attack surfaces. Vulnerability identification parallels finding prompts, contexts, or inputs that might produce undesired outputs. Exploitation parallels demonstrating that these vulnerabilities can actually produce harmful results. Reporting parallels documenting AI failure modes, their severity, and recommendations for mitigation.

### Threat Modeling

Before testing for specific vulnerabilities, security practitioners engage in threat modeling—systematic identification of potential threats:

**Who might attack?** Different adversaries have different motivations, capabilities, and resources. A nation-state actor poses different threats than a curious teenager or a disgruntled employee.

**What are their goals?** Data theft, system disruption, financial fraud, reputation damage, or something else? Understanding adversary goals helps prioritize defenses.

**What methods might they use?** Known attack patterns, novel techniques, social engineering, supply chain compromise, insider threats? The attack surface encompasses all paths an adversary might exploit.

**What assets need protection?** Not everything is equally valuable or vulnerable. Prioritize based on asset value and exposure.

Threat models inform both defensive architecture and testing priorities. Testing should focus on likely and consequential threats, not just easy-to-test scenarios.

For AI, threat modeling asks: Who might try to make the AI behave badly? Malicious users seeking harmful content, competitors seeking embarrassment, researchers probing for weaknesses, or ordinary users who stumble into problematic areas? What might they try to achieve? Generating harmful content, extracting training data, manipulating the AI's behavior, or bypassing safety measures? Threat modeling for AI helps prioritize red team activities and evaluation resources.

### Bug Bounties and Responsible Disclosure

Bug bounty programs enlist external researchers to find vulnerabilities in exchange for rewards. They leverage a global community of security researchers who may find vulnerabilities that internal teams miss:

**Advantages**: Diverse perspectives, scalable effort, real-world adversarial skill, cost-effective (pay only for results)

**Challenges**: Managing submissions, avoiding exploitation of found vulnerabilities, defining scope and severity, potential for noise

**Responsible disclosure** refers to coordinated practices for reporting vulnerabilities: researchers notify vendors before public disclosure, vendors have time to develop fixes, and disclosure occurs in ways that minimize harm.

Bug bounty models are emerging for AI. Programs like the DEFCON AI Village and various company-sponsored initiatives invite researchers to find AI vulnerabilities. The challenge is defining what counts as an AI "vulnerability"—security vulnerabilities have relatively clear definitions, while AI failure modes are often fuzzier. Still, crowdsourcing failure discovery can find problems internal testing misses.

### Zero-Day Vulnerabilities and Unknown Unknowns

A "zero-day" vulnerability is one unknown to defenders at the time of exploitation—the defenders have "zero days" of warning. Zero-days represent the scariest class of security threats: you can't defend against what you don't know exists.

The security field has developed several responses to unknown unknowns:

**Defense in depth**: Don't rely on any single protection. Layer multiple defenses so that if one fails, others remain. Assume breaches will occur and limit their impact.

**Anomaly detection**: Rather than only detecting known bad patterns, look for deviations from normal behavior. Unknown attacks may still produce detectable anomalies.

**Assume breach**: Design systems and processes assuming that compromise is inevitable. Limit lateral movement, segment networks, encrypt data at rest, and plan incident response.

**Resilience over prevention**: Since perfect prevention is impossible, prioritize resilience—the ability to continue functioning and recover quickly even when attacks succeed.

For AI, zero-day thinking is essential. The "jagged capability frontier" means AI systems fail in unexpected ways that weren't anticipated during development or testing. No testing can enumerate all possible failure modes. Assume that deployed AI will fail in ways you haven't predicted. Design for detection, containment, and recovery, not just prevention.

### Security Testing Automation

Security testing uses various automated techniques to explore large input spaces:

**Fuzzing**: Automatically generating semi-random inputs to find inputs that cause crashes, hangs, or unexpected behavior. Fuzzing doesn't require understanding of specific vulnerabilities—it explores the input space looking for anything that breaks.

**Static analysis**: Examining code without executing it to find potential vulnerabilities—buffer overflows, injection vulnerabilities, insecure patterns. Scales well but may miss runtime-dependent issues.

**Dynamic analysis**: Examining system behavior during execution—memory access patterns, API calls, network traffic. Catches runtime issues but requires actually running the code.

**Symbolic execution**: Systematically exploring program paths to find inputs that reach specific states. More thorough than fuzzing but computationally expensive.

For AI, fuzzing concepts translate to automated prompt exploration—systematically trying many prompt variations to find inputs that produce undesired outputs. The challenge is defining what "crash" or "unexpected behavior" means for AI; the output is always some text, so identifying problematic outputs requires either human judgment or automated classifiers.

---

## What Transfers to AI Evaluation

Several elements of cybersecurity testing apply directly to AI evaluation:

**The adversarial mindset** is perhaps the most valuable transfer. Security testing assumes you need to actively try to break the system because the most important failures are the ones you haven't anticipated. This orientation—adversarial rather than cooperative—provides different information than testing whether AI performs well on expected inputs. AI evaluation should include adversarial components as standard practice.

**Red teaming methodology** provides structured approaches for adversarial evaluation. The practices of scoping red team engagements, defining rules of engagement, documenting findings, and tracking remediation can be adapted for AI red teaming. The key insight is that red teaming should be structured and systematic, not just ad hoc probing.

**Threat modeling** helps prioritize evaluation effort. Rather than treating all possible AI failures as equally likely or important, threat modeling asks: What failures are most likely? What failures would be most consequential? What adversary capabilities should we assume? This risk-based prioritization makes evaluation tractable.

**Bug bounty models** offer approaches for crowdsourcing failure discovery. Internal teams may miss failure modes that external researchers find. Creating mechanisms for responsible disclosure of AI failures—with appropriate incentives—can augment internal evaluation.

**Defense in depth** applies to AI deployment. Don't rely on the model itself to prevent all harms. Layer additional protections: output filters, use policies, monitoring, human review for high-stakes outputs. Assume some failures will occur and design systems that limit their impact.

**Unknown unknowns awareness** is essential for AI. Security professionals have long experience with unforeseen vulnerabilities and have developed strategies for managing this uncertainty. AI evaluation should expect unexpected failure modes and prioritize detection and recovery alongside prevention.

---

## What Breaks for Generative AI

Despite substantial applicability, some aspects of security testing translate poorly to AI:

**Clear vulnerability definitions** exist in security: unauthorized access, data exposure, code execution, denial of service. These have relatively crisp definitions—either the attacker achieved the goal or didn't. AI "failures" are often fuzzy: Is this response harmful? Is this output good enough? Is this behavior acceptable? The fuzziness makes it harder to determine whether a "vulnerability" exists.

**Exploit reproducibility** is typically high in security—the same vulnerability reliably produces the same exploit. AI jailbreaks may be stochastic: a prompt that produces harmful output once might not do so consistently. This variability complicates both discovery and remediation. A "fix" might reduce harmful output probability without eliminating it.

**Patching vulnerabilities** is possible for traditional software—fix the bug, deploy the patch. AI weaknesses may be more fundamental, emerging from training data or model architecture in ways that can't be simply patched. Mitigations (output filters, system prompts) may address symptoms without fixing underlying issues, and may introduce new failure modes.

**Formal security properties** can sometimes be verified—cryptographic correctness, access control logic, protocol compliance. AI safety properties generally cannot be formally verified. There's no way to prove that a language model will never produce harmful content, only to test extensively and monitor continuously.

**Clear attack surface** can be defined for traditional systems—network interfaces, APIs, user inputs. AI "attack surface" is less clear. Any input can potentially produce undesired output. The boundary between normal use and adversarial use is blurry.

---

## What Can Be Adapted

Several security concepts can be adapted for AI evaluation with appropriate modifications:

**Structured red teaming frameworks** can be developed for AI. Define scope (what capabilities/behaviors are being tested), rules of engagement (what methods are permitted), deliverables (how findings are documented), and follow-up (how issues are addressed). The DEFCON AI Village CTFs and various industry frameworks are early examples.

**Fuzzing for AI** can involve systematic exploration of the prompt space. Rather than completely random inputs, informed fuzzing can focus on prompt patterns likely to produce problematic outputs—drawing on known jailbreaks, adversarial prompt patterns, and edge cases. Automated generation and screening can scale this exploration.

**Coordinated disclosure for AI** can be developed—practices for responsibly reporting AI failures, allowing developers time to address issues before public disclosure. This requires defining what constitutes an AI "vulnerability" worth reporting, establishing channels for reports, and creating norms around disclosure timing.

**Capture the flag for AI** adapts the security CTF competition format. Competitions where teams try to find AI failures, generate specific outputs, or bypass safety measures can motivate creative adversarial evaluation and develop the community of AI red teamers.

**Assume breach for AI** translates to assuming AI will produce some problematic outputs. Design deployment contexts accordingly: monitoring for problematic outputs, limiting where AI outputs go without human review, and having response plans for when issues arise.

---

## Implications for AI Evaluation

Drawing on cybersecurity testing experience, several principles should guide AI evaluation:

**Adopt the adversarial orientation.** Don't just test whether AI performs well on expected uses; actively try to make it fail. Adversarial testing reveals different information than cooperative testing. For high-stakes deployments, adversarial evaluation is not optional.

**Structure adversarial evaluation.** Ad hoc probing misses things. Use structured red teaming with defined scope, methodology, documentation, and follow-up. Adapt penetration testing frameworks for AI context.

**Apply threat modeling.** Before testing everything, think about what failures are most likely and most consequential. Prioritize evaluation based on risk. Consider who might try to misuse the AI and how.

**Consider crowdsourcing.** Internal teams may miss failures that external researchers find. Bug bounty programs, research collaborations, and community engagement can augment internal evaluation—if managed carefully.

**Design for resilience.** Since perfect prevention is impossible, design AI deployments that can detect, contain, and recover from failures. Defense in depth, monitoring, and response plans are as important as pre-deployment testing.

**Expect the unexpected.** Zero-day thinking applies to AI: assume that deployed systems will fail in ways not anticipated during testing. Build monitoring and response capabilities, not just testing.

**Develop the community.** Security has a mature community of researchers, practitioners, and institutions. AI evaluation needs similar infrastructure: shared methodologies, training programs, career paths, and ethical norms.

---

## Key References

**Security Testing Foundations**

- **NIST SP 800-115 (Technical Guide to Information Security Testing and Assessment).** Government guidance on security testing methodology.

- **PTES (Penetration Testing Execution Standard).** Industry standard for penetration testing methodology and reporting.

- **MITRE ATT&CK Framework.** Knowledge base of adversary tactics, techniques, and procedures organized as a taxonomy.

- **OWASP Testing Guide.** Comprehensive guide to web application security testing.

**Threat Modeling**

- **Shostack, A. (2014). *Threat Modeling: Designing for Security*.** Comprehensive treatment of threat modeling methods.

- **STRIDE Threat Model.** Microsoft's framework for categorizing security threats.

**AI Red Teaming**

- **Ganguli, D., et al. (2022). "Red Teaming Language Models to Reduce Harms." *arXiv preprint*.** Anthropic's description of red teaming methodology.

- **Perez, E., et al. (2022). "Red Teaming Language Models with Language Models." *arXiv preprint*.** Using AI to automate red teaming.

- **Brundage, M., et al. (2020). "Toward Trustworthy AI Development: Mechanisms for Supporting Verifiable Claims."** Broader framework for AI assurance including adversarial testing.

- **Anthropic, OpenAI, DeepMind responsible scaling policies and safety documentation.** Industry practices for AI red teaming.

**Bug Bounties and Disclosure**

- **HackerOne and Bugcrowd.** Major bug bounty platforms with methodology documentation.

- **ISO/IEC 29147 and 30111.** Standards for vulnerability disclosure and handling.

---

## Connections to Other Sections

Cybersecurity testing connects to several other disciplines covered in this appendix:

- **Section 1.1 (Software Testing)** provides foundational testing concepts; cybersecurity extends these with an adversarial orientation that's particularly relevant to AI.

- **Section 4.1 (Risk Analysis)** provides frameworks for the risk-based prioritization that informs threat modeling and test prioritization.

- **Section 4.5 (Safety Engineering)** develops hazard analysis methods that complement adversarial security analysis for safety-critical AI.

- **Section 6.1 (AI Safety Evaluation)** covers the emerging field of AI-specific safety evaluation, which draws heavily on security red teaming concepts.

- **Section 1.3 (Autonomous Systems)** addresses adversarial testing in the context of physically embodied AI systems.

---

*[End of Section 1.5]*
