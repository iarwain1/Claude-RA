# Recommended Reference Additions - Dec 31, 2025

Based on systematic review of link-dumps database for recent sources (Oct 2025+) relevant to GenAI productivity gains literature review.

## High Priority Additions (8 papers)

### 1. Construct Validity & Benchmark Methodology

**arxiv-2511.04703** - "Measuring what Matters: Construct Validity in Large Language Model Benchmarks"
- **Authors:** Andrew M. Bean, Ryan Othniel Kearns, Angelika Romanou, et al. (40+ authors)
- **Date:** Nov 3, 2025
- **Priority:** 10 (Essential)
- **Subtopics:** benchmarks, evaluation-methodology
- **Why add:** Landmark systematic review of 445 LLM benchmarks by 29 expert reviewers. Identifies pervasive construct validity issues - benchmarks often don't measure what they claim. Provides 8 key recommendations for developing valid benchmarks. Essential for understanding benchmark-utility gap.
- **Note file exists:** `link-dumps/notes/arxiv-2511.04703.md`
- **Key findings:**
  - Systematic patterns undermining validity across 445 benchmarks
  - Disconnect between claimed phenomena and actual tasks
  - 8 actionable recommendations for valid benchmark design

---

**epoch-ai-benchmark** - "Why Benchmarking is Hard"
- **Authors:** Florian Brand, Jean-Stanislas Denain (Epoch AI)
- **Date:** Dec 23, 2025
- **URL:** https://epoch.ai/gradient-updates/why-benchmarking-is-hard
- **Priority:** 9 (Very important)
- **Subtopics:** benchmarks, evaluation-methodology
- **Why add:** Epoch AI analysis of practical benchmarking challenges. Documents how setup variables (prompts, scaffolds, sampling) and API access issues cause 11-15% variance in scores. Explains why independent evaluations are difficult and why results don't replicate. Critical for understanding benchmark reliability.
- **Note file exists:** `link-dumps/notes/epoch-ai-why-benchmarking-is-hard.md`
- **Key findings:**
  - Scaffolds cause 11-15% variance on SWE-bench Verified
  - API provider selection yields divergent results for identical models
  - Resource barriers particularly impact smaller organizations

---

**arxiv-2512.00193** - "A Rosetta Stone for AI Benchmarks"
- **Authors:** Anson Ho, Jean-Stanislas Denain, David Atanasov, Samuel Albanie, Rohin Shah
- **Date:** Nov 28, 2025
- **Priority:** 8 (Important)
- **Subtopics:** benchmarks, evaluation-methodology
- **Why add:** Novel statistical framework addressing benchmark saturation problem. Stitches benchmarks together on unified scale, enabling long-term capability tracking and cross-benchmark model comparison. Important for Part 1 (Benchmark-Utility Gap) discussion of benchmark lifecycle and saturation.
- **Note file exists:** `link-dumps/notes/arxiv-2512.00193.md`
- **Related to:** epoch2025rosetta already in references.yaml but this is the full paper

---

### 2. Agent Evaluation & Real-World Deployment

**arxiv-2512.04123** - "Measuring Agents in Production"
- **Authors:** Melissa Z. Pan, Negar Arabzadeh, et al. (UC Berkeley, Databricks)
- **Date:** Dec 2, 2025
- **Priority:** 10 (Essential)
- **Subtopics:** agent-evaluation, productivity-studies, deployment
- **Why add:** First large-scale systematic study of AI agents in production (306 practitioners, 20 case studies, 26 domains). KEY FINDINGS: 68% execute ≤10 steps before human intervention, 70% use prompting vs fine-tuning, 74% rely on human evaluation. Reveals massive gap between research prototypes and production reality. Essential for Part 4 (Practical Guidance).
- **Note file exists:** `link-dumps/notes/arxiv-2512.04123.md`
- **Key findings:**
  - Production agents much simpler than research prototypes
  - Human evaluation dominates (74%) - automated metrics insufficient
  - Short action chains (68% ≤10 steps) before human oversight needed

---

**arxiv-2512.08296** - "Towards a Science of Scaling Agent Systems"
- **Authors:** Yubin Kim, Ken Gu, et al. (19 authors from MIT, Google, Meta)
- **Date:** Dec 9, 2025
- **Priority:** 9 (Very important)
- **Subtopics:** agent-evaluation, scaling-laws, multi-agent
- **Why add:** Proposes scientific framework for understanding agent system scaling. Addresses gap in understanding how multi-agent systems scale compared to single models. Relevant for Part 6 (Research Agenda) and future acquisition considerations as DoD explores multi-agent systems.
- **Note file exists:** `link-dumps/notes/arxiv-2512.08296.md`

---

### 3. Productivity & Economic Impact

**anthropic-ai-transforming-work** - "How AI is Transforming Work at Anthropic"
- **Authors:** Saffron Huang, Bryan Seethor, et al. (Anthropic)
- **Date:** Dec 2, 2025
- **URL:** https://www.anthropic.com/research/how-ai-is-transforming-work-at-anthropic
- **Priority:** 9 (Very important)
- **Subtopics:** productivity-studies, human-ai-teaming
- **Why add:** **UPDATED** internal study from earlier Aug 2025 version already in references (anthropic2025internal). Dec 2 version may have updated data. Should verify if this is substantively different or just republished. If updated, should replace or supplement existing entry.
- **Note file exists:** `link-dumps/notes/anthropic-ai-transforming-work.md`
- **Already in references.yaml as:** anthropic2025internal (listed as Aug 2025)
- **Action needed:** Compare note files to determine if Dec version has new data

---

### 4. Consumer-Facing & Application Evaluation

**arxiv-2512.04921** - "The AI Consumer Index (ACE)"
- **Authors:** Julien Benchek, Rohit Shetty, et al. (Google DeepMind)
- **Date:** Dec 4, 2025
- **Priority:** 7 (Useful)
- **Subtopics:** benchmarks, evaluation-methodology, applications
- **Why add:** Novel benchmark for evaluating AI on consumer-facing tasks (shopping, travel, entertainment). Complements productivity-focused evaluations. Relevant for understanding breadth of AI economic impact and potential dual-use applications in DoD context.
- **Note file exists:** `link-dumps/notes/arxiv-2512.04921.md`

---

**lmarena-expert-comparison** - "Arena Expert Model Comparison"
- **Authors:** LMArena team
- **Date:** Dec 2025
- **URL:** https://news.lmarena.ai/arena-expert-model-comparison/
- **Priority:** 8 (Important)
- **Subtopics:** benchmarks, evaluation-methodology, human-ai-teaming
- **Why add:** Analysis showing expert users rate models differently than general users. Critical for understanding how user skill/expertise affects perceived AI utility. Directly relevant to heterogeneity findings (experts vs novices) discussed in Brynjolfsson, Noy studies. Important for acquisition guidance on who should evaluate systems.
- **Note file exists:** `link-dumps/notes/lmarena-expert-comparison.md`

---

## Medium Priority Additions (3 papers)

### Safety & Alignment (relevant for Part 5: T&E Considerations)

**arxiv-2512.16856** - "Distributional AGI Safety"
- **Date:** Dec 2025
- **Priority:** 7 (Useful)
- **Subtopics:** risk-management, ai-safety
- **Why add:** Addresses safety considerations for advanced AI systems. Relevant for Part 5 (T&E Considerations for GenAI-Based Systems) risk assessment frameworks.
- **Note file exists:** `link-dumps/notes/arxiv-2512.16856.md`

---

**arxiv-2512.15584** - "A Decision-Theoretic Approach for Managing Misalignment"
- **Date:** Dec 2025
- **Priority:** 7 (Useful)
- **Subtopics:** risk-management, ai-safety, decision-theory
- **Why add:** Decision-theoretic framework for managing AI misalignment. Relevant for Part 5 risk management and Part 3 evaluation framework development.
- **Note file exists:** `link-dumps/notes/arxiv-2512.15584.md`

---

**anthropic-project-vend-2** - "Project Vend: Phase Two"
- **Date:** Dec 18, 2025
- **Priority:** 8 (Important)
- **Subtopics:** agent-evaluation, ai-safety, deployment
- **Why add:** Anthropic's autonomous AI agent running vending machine business. Real-world test of agent autonomy, decision-making, and alignment. Important case study for understanding agent capabilities and limitations in extended autonomous operation.
- **Note file exists:** `link-dumps/notes/anthropic-project-vend-2.md`

---

## Lower Priority / Specialized (3 sources)

**arxiv-2512.10047** - "Detailed balance in large language model-driven agents"
- **Date:** Dec 2025
- **Priority:** 6 (Background)
- **Subtopics:** agent-evaluation, theory
- **Why add:** Theoretical analysis of agent systems using physics concepts. More specialized but may inform agent evaluation methodology.
- **Note file exists:** `link-dumps/notes/arxiv-2512.10047.md`

---

**coding-agents-for-research** - GitHub BRAIN_DUMP_ORGANIZED
- **Date:** Dec 2025
- **Priority:** 6 (Background)
- **Subtopics:** agent-evaluation, research-tools
- **Why add:** Community knowledge on coding agents. Less formal but may contain practitioner insights on agent evaluation challenges.
- **Note file exists:** `link-dumps/notes/coding-agents-for-research.md`

---

**continuous-claude** - "Continuous Claude: Context Management"
- **Date:** Dec 2025
- **Priority:** 5 (Reference)
- **Subtopics:** tools, deployment
- **Why add:** Practical tool for managing long contexts. Relevant for understanding operational considerations in AI deployment but not core to literature review.
- **Note file exists:** `link-dumps/notes/continuous-claude.md`

---

## Summary Statistics

**Total recommended additions:** 14 papers
- **High priority (9-10):** 8 papers
- **Medium priority (7-8):** 3 papers
- **Lower priority (5-6):** 3 papers

**By subtopic:**
- Benchmarks & Evaluation Methodology: 7 papers
- Agent Evaluation & Deployment: 4 papers
- Productivity Studies: 1 paper (+ 1 potential update)
- Risk Management & Safety: 3 papers
- Tools & Applications: 2 papers

**Coverage of report sections:**
- Part 1 (Benchmark-Utility Gap): 7 papers directly relevant
- Part 2 (Literature Review): All papers relevant
- Part 3 (Framework): 5 papers relevant
- Part 4 (Practical Guidance): 4 papers relevant
- Part 5 (T&E Considerations): 4 papers relevant
- Part 6 (Research Agenda): 3 papers relevant

---

## Next Steps

1. **Immediate:** Add high-priority papers (8) to references.yaml with detailed metadata
2. **Verify:** Check if Dec 2 Anthropic paper is substantively different from Aug version
3. **Read:** Prioritize reading queue for high-priority papers
4. **Medium-term:** Add medium-priority papers (3) to references.yaml
5. **Consider:** Lower-priority papers (3) for appendices or background reading

---

*Generated: 2025-12-31*
*Source: Systematic review of link-dumps database (664 entries)*
*Focus: Oct 2025+ publications relevant to GenAI productivity gains*
