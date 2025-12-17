# A Field Guide to Rapidly Improving AI Products

**Authors:** Hamel Husain
**Year:** 2025 (March)
**URL:** https://hamel.dev/blog/posts/field-guide/

## Key Contributions

1. **"Tools trap" concept** - the belief that adopting the right tools/frameworks will solve AI problems
2. **Custom data viewers** - teams with thoughtfully designed viewers iterate 10x faster
3. **Domain expert empowerment** - removing technical barriers so domain experts can directly iterate on prompts
4. **Trust maintenance** in evaluation systems - why teams lose faith and revert to gut feeling

## Methodology

Synthesis of lessons from helping 30+ companies build AI products. Practitioner-focused observations rather than controlled study.

## Key Findings

### The "Tools Trap"

**Definition:** The belief that adopting the right tools or frameworks (especially generic metrics) will solve your AI problems.

**Two ways generic metrics actively impede progress:**

1. **Vanity metrics:** Teams think they're data-driven because they have dashboards, but track metrics that don't correlate with real user problems
   > "Teams celebrate improving their 'helpfulness score' by 10% while their actual users were still struggling with basic tasks."

2. **Attention fragmentation:** Too many metrics scatter focus

**Key insight:** Successful teams barely talk about tools. They obsess over **measurement and iteration**.

### Custom Data Viewers

> "Teams with thoughtfully designed data viewers iterate 10x faster than those without them."

**Advantages over dashboards:**
- Custom viewers examining AI outputs yield more insights than complex dashboards with generic metrics
- Can be built in hours using AI-assisted development (Cursor, Loveable)
- Remove friction from data inspection

**The single most impactful investment** AI teams make isn't a fancy evaluation dashboard—it's building a customized interface that lets anyone examine what their AI is actually doing.

### Maintaining Trust in Evaluations

**Problem:** Teams build evaluation systems, then gradually lose faith in them.

**Causes:**
- Metrics don't align with what they observe in production
- Evaluations become too complex to interpret

**Result:** Teams revert to gut feeling and anecdotal feedback, undermining the entire purpose of evaluations.

**Solution:**
- Binary judgments with detailed critiques create clarity while preserving nuance
- Regular alignment checks ensure automated evaluations remain trustworthy

### Empowering Domain Experts

> "The people who understand your domain best are often the ones who can most effectively improve your AI, regardless of their technical background."

**Anti-pattern:** Domain experts communicate principles through PowerPoint → engineers translate to prompts. Creates unnecessary friction.

**Better approach:** Give domain experts tools to write and iterate on prompts directly.

**Jargon barrier example:**
> "Engineers kept saying 'We're going to build an agent' when really the job was writing a prompt, creating artificial barriers for domain experts."

This happens with lawyers, psychologists, doctors at domain-specific startups. **LLMs make AI accessible through natural language**, but teams destroy that advantage by wrapping everything in technical terminology.

### Success Pattern

> "The most successful teams aren't the ones with the most sophisticated tools or the most advanced models – they're the ones that master the fundamentals of measurement, iteration, and learning."

## Relevance to Review

**Highly relevant for operational aspects of prompt evaluation.** Key insights:

1. **Generic prompt quality metrics are dangerous** - can create false confidence
2. **Custom tooling for prompt inspection** is high-ROI
3. **Domain experts should evaluate prompts directly** - technical intermediaries add friction
4. **Evaluation trust must be maintained** - binary judgments + alignment checks

### Implications for Different Prompt Types

| Prompt Type | Implication |
|-------------|-------------|
| System prompts | Domain experts should iterate directly, not through engineers |
| User prompts | Custom viewers to inspect real interactions > generic dashboards |
| Agentic prompts | Avoid jargon barriers ("agent" vs "prompt") with non-technical stakeholders |

## Citations to Follow

- **Vanishing Gradients podcast (Ep. 50)** - Extended discussion of the Field Guide
- Case studies mentioned (education startup, legal tech, healthcare) - specific implementations

## Questions/Notes

- **Strength:** "10x faster iteration" with custom data viewers is a strong claim worth investigating
- **Strength:** "Tools trap" is memorable framing that captures real anti-pattern
- **Practical:** Recommends AI-assisted development (Cursor) for building custom viewers
- **Gap:** Limited specifics on what makes a data viewer "thoughtfully designed"
- **Gap:** No quantitative data on the "10x faster" claim
- **Connects to:** husain2024evals (error analysis), husain2024llmjudge (binary judgments)
- **Currency:** March 2025, very current

## Evidence Quality

**Medium for practical guidance.** Based on extensive consulting experience but no controlled comparisons. Strong for "what successful teams do" patterns; weaker for causal claims about what drives success. The "10x faster" claim should be treated as directional rather than precise.
