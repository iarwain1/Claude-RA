# PowerPoint Slides: Evaluating LLM Prompt Effectiveness

## Slide Design Notes
- These slides are designed to fit into a larger presentation
- Each slide includes speaker notes for context
- Visual suggestions included for each slide

---

## Slide 1: The Evaluation Challenge

**Title:** Why Prompt Evaluation Is Hard

**Content:**
- LLMs have an **infinite failure surface area**
- Traditional software testing doesn't apply
- Outputs are non-deterministic
- Quality is often subjective

**Key Stat:**
> "Eval-driven development generally doesn't work"
> — Hamel Husain (30+ company implementations)

**Visual:** Iceberg diagram - visible failures above water, infinite unseen failures below

**Speaker Notes:**
Unlike traditional software where we can enumerate test cases, LLMs can fail in unlimited ways. The key insight from practitioners is that we can't anticipate all failures upfront - we must discover them through observation.

---

## Slide 2: The Three-Level Framework

**Title:** Three Levels of Prompt Evaluation

**Content (as a pyramid or stacked diagram):**

| Level | Method | When | Best For |
|-------|--------|------|----------|
| **Level 3** | A/B Testing | Major changes | Real-world validation |
| **Level 2** | LLM-as-Judge | Weekly cadence | Subjective quality |
| **Level 1** | Code Assertions | Every change | Objective failures |

**Key Principle:**
> ⚠️ Conquer Level 1 before moving to Level 2

**Visual:** Pyramid with Level 1 as foundation, or stacked blocks

**Speaker Notes:**
This framework from Hamel Husain is widely adopted. The key is starting with simple assertions before adding complexity. Many teams prematurely adopt LLM-as-judge when basic assertions would catch most issues.

---

## Slide 3: Error Analysis First

**Title:** Start with Error Analysis, Not Evaluation

**Content (as a process flow):**

```
1. OBSERVE → Review 100+ production traces
     ↓
2. JOURNAL → Open coding (note patterns)
     ↓
3. CATEGORIZE → Build failure taxonomy
     ↓
4. BUILD EVALS → Write evaluators for discovered errors
```

**Anti-Pattern:**
❌ "Let me imagine what could go wrong"

**Best Practice:**
✅ "Let me see what IS going wrong"

**Visual:** Circular flow diagram with observation at the center

**Speaker Notes:**
This methodology comes from qualitative research. The critical insight is that we cannot anticipate LLM failures - we must discover them empirically. Review fresh traces every 2-4 weeks after significant changes.

---

## Slide 4: LLM-as-Judge: Requirements & Limitations

**Title:** Using LLMs to Judge LLMs

**Content (two columns):**

**Requirements:**
- 100+ labeled examples
- 3-4 validation rounds with humans
- Binary Pass/Fail (not 1-5 scales)
- Temperature = 0
- Weekly maintenance

**Limitations:**

| Task Type | LLM Judge? |
|-----------|------------|
| Recall/List | ✅ Suitable |
| Single answer | ✅ Suitable |
| Summarization | ⚠️ Use humans |
| Reasoning | ⚠️ Use humans |

**Key Stat:**
> 64-68% agreement with human SMEs on expert cognitive tasks

**Visual:** Gauge or meter showing agreement rates

**Speaker Notes:**
LLM-as-judge is powerful but requires careful validation. The 64-68% agreement rate comes from DoD research - significantly below what we'd want for expert tasks. Always measure TPR/TNR against human labels.

---

## Slide 5: RAG Evaluation Simplified

**Title:** The 6 RAG Evals Framework

**Content:**

**Three Components:** Question (Q) → Context (C) → Answer (A)

**Three Tiers:**

| Tier | Metrics | When to Use |
|------|---------|-------------|
| **Tier 1** | Precision@K, Recall@K, MRR | First - fast iteration |
| **Tier 2** | Context relevance, Faithfulness, Answer quality | Primary evaluation |
| **Tier 3** | Advanced relationships | Major releases |

**Golden Rule:**
> 🔧 Debug retrieval FIRST, then tackle generation

**Visual:** Flow diagram: Q → Retrieval → C → Generation → A with evaluation points marked

**Speaker Notes:**
Jason Liu's framework simplifies RAG evaluation. The key insight is that retrieval problems should be fixed before evaluating generation - IR metrics are fast and don't require LLM calls. This prevents chasing generation issues caused by bad retrieval.

---

## Slide 6: Agentic System Evaluation

**Title:** Evaluating Multi-Step Agents

**Content (two-level structure):**

**Level 1: End-to-End (Outcome)**
- Did we meet the user's goal?
- Task completion rate

**Level 2: Step-Level (Process)**
- Tool selection accuracy
- Parameter extraction
- Error handling
- Context retention

**Key Insights:**
- Process failures are more deterministic → tackle first
- Early errors cascade → prioritize early stages
- Use **transition failure matrices** for multi-step workflows

**Warning:**
> ⚠️ Avoid "sandbox" environments - use realistic complexity

**Visual:** Flowchart with evaluation checkpoints at each step

**Speaker Notes:**
Agentic systems need evaluation at multiple granularities. The transition failure matrix technique identifies which state transitions cause most failures - this transforms complexity into actionable insights. Test with realistic data and multiple tool calls.

---

## Slide 7: The "Tools Trap"

**Title:** Avoiding the Tools Trap

**Content:**

**The Trap:**
> "If we just find the right evaluation framework/tool, our problems will be solved"

**Reality:**
- Generic metrics create **false confidence**
- Vanity metrics don't correlate with real problems
- Successful teams barely discuss tools

**What Works Instead:**

| ❌ Don't | ✅ Do |
|---------|-------|
| Generic dashboards | Custom data viewers |
| Many metrics | Few meaningful metrics |
| 1-5 scoring | Binary Pass/Fail |
| Outsource to LLM | Human open coding |

**Key Stat:**
> Teams with custom data viewers iterate **10x faster**

**Visual:** Two contrasting paths - one cluttered with tools, one focused on data

**Speaker Notes:**
This is perhaps the most counterintuitive finding. Success comes from obsessing over measurement and iteration, not tool selection. Custom data viewers that let you see actual examples beat complex dashboards every time.

---

## Slide 8: Key Takeaways

**Title:** Prompt Evaluation: What Works

**Content (numbered list with icons):**

1. 🔍 **Error analysis first** — Discover failures, don't imagine them

2. 📊 **Start simple** — Level 1 assertions before LLM judges

3. ✅ **Binary judgments** — Pass/Fail beats Likert scales

4. 🧪 **Validate judges** — Measure TPR/TNR against humans

5. 👥 **Involve domain experts** — They should iterate on prompts directly

6. 🔄 **Iterate continuously** — Review 100+ traces every 2-4 weeks

7. ⚠️ **Avoid the tools trap** — Focus on measurement, not frameworks

**Bottom Line:**
> "Obsess over measurement and iteration, not tools"

**Visual:** Clean checklist or icon grid

**Speaker Notes:**
These principles emerged from reviewing 21 sources including practitioner guides, academic surveys, and vendor documentation. The consistent theme: empirical observation and iteration beat theoretical frameworks and sophisticated tooling.

---

## Appendix: Sources

**Key References:**
- Husain (2024) - "Your AI Product Needs Evals"
- Husain (2024) - "LLM-as-Judge Guide"
- Liu (2025) - "6 RAG Evals"
- O'Brien (2025) - "Test Science of LLM Systems" (ITEA)
- Mei et al. (2025) - "Context Engineering Survey"

**Full bibliography:** 21 papers reviewed
