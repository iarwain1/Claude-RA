# Jailbreak-Tuning: Models Efficiently Learn Jailbreak Susceptibility

**arXiv:** [2507.11630](https://arxiv.org/abs/2507.11630)
**Authors:** Brendan Murphy, Dillon Bowen, Shahrad Mohammadzadeh, Tom Tseng, Julius Broomfield, et al. (7 total)
**Date:** 2025-07-15
**Categories:** cs.CR, cs.AI, cs.CL

## Abstract

AI systems are rapidly advancing in capability, and frontier model developers broadly acknowledge the need for safeguards against serious misuse. However, this paper demonstrates that fine-tuning, whether via open weights or closed fine-tuning APIs, can produce helpful-only models with safeguards destroyed. In contrast to prior work which is blocked by modern moderation systems or achieved only partial removal of safeguards or degraded output quality, our jailbreak-tuning method teaches models to generate detailed, high-quality responses to arbitrary harmful requests. For example, OpenAI, Google, and Anthropic models will fully comply with requests for CBRN assistance, executing cyberattacks, and other criminal activity. We further show that backdoors can increase not only the stealth but also the severity of attacks. Stronger jailbreak prompts become even more effective in fine-tuning attacks, linking attacks and potentially defenses in the input and weight spaces. Not only are current models vulnerable, more recent ones also appear to be becoming even more vulnerable to these attacks, underscoring the urgent need for tamper-resistant safeguards. Until such safeguards are discovered, companies and policymakers should view the release of any fine-tunable model as simultaneously releasing its evil twin: equally capable as the original model, and usable for any malicious purpose within its capabilities.

---
*Metadata fetched via arxiv API on 2025-12-31*
