# Claude 4 Best Practices

**Authors:** Anthropic
**Year:** 2025
**URL:** https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/claude-4-best-practices

## Key Contributions

1. **Claude 4.x-specific guidance:** Techniques for Opus 4.1, Opus 4, Sonnet 4, Sonnet 4.5, Haiku 4.5
2. **Explicit instruction emphasis:** More precise instruction following than previous generations
3. **Thinking capabilities guidance:** How to leverage extended thinking for complex tasks
4. **Long-horizon task support:** Best practices for extended sessions

## Key Findings

### Explicit Instructions

> "Claude 4.x models respond well to clear, explicit instructions. Being specific about your desired output can help enhance results."

**Key change from previous models:**
> "Customers who desire the 'above and beyond' behavior from previous Claude models might need to more explicitly request these behaviors with newer models."

| Principle | Application |
|-----------|-------------|
| Don't assume inference | State requirements directly |
| Use simple language | Avoid ambiguity |
| Be specific about output | Define format, length, style |

### Examples and Details

> "Claude 4.x models pay close attention to details and examples as part of their precise instruction following capabilities."

**Best practices:**
- Ensure examples align with desired behaviors
- Minimize examples of behaviors to avoid
- Use detailed, representative examples

### Thinking Capabilities

> "Claude 4.x models offer thinking capabilities that can be especially helpful for tasks involving reflection after tool use or complex multi-step reasoning."

**Applications:**
- Post-tool-use reflection
- Complex multi-step reasoning
- Guided initial or interleaved thinking

### Long-Horizon Tasks

> "Claude 4.5 models excel at long-horizon reasoning tasks with exceptional state tracking capabilities."

**Strategy:**
> "Maintains orientation across extended sessions by focusing on incremental progress—making steady advances on a few things at a time rather than attempting everything at once."

### System Prompt Design (from Context Engineering guidance)

> "System prompts should be extremely clear and use simple, direct language that presents ideas at the right altitude for the agent."

**Goldilocks zone between:**
- **Too specific:** Hardcoding complex, brittle logic (fragility)
- **Too vague:** High-level guidance without concrete signals

**Few-shot best practice:**
> "Rather than stuffing a laundry list of edge cases into a prompt, curate a set of diverse, canonical examples that effectively portray expected behavior."

## Relevance to Review

**Directly relevant for Claude-specific prompt evaluation.** Key insights:

### For Prompt Evaluation

1. **Explicit instruction testing:** Evaluate if prompts are sufficiently explicit for Claude 4.x
2. **Example quality assessment:** Test example alignment with desired behaviors
3. **Thinking guidance evaluation:** Test effectiveness of reasoning guidance
4. **Long-horizon metrics:** Evaluate state tracking across extended sessions

### Evaluation Implications

| Claude 4.x Feature | Evaluation Approach |
|-------------------|---------------------|
| Precise instruction following | Test explicit vs. implicit instruction variants |
| Example sensitivity | A/B test with/without examples |
| Thinking capabilities | Evaluate reasoning quality with different guidance |
| Long-horizon | Test state consistency over extended interactions |

### Model-Specific Considerations

| Aspect | Previous Claude | Claude 4.x |
|--------|-----------------|------------|
| "Above and beyond" behavior | Automatic | Needs explicit request |
| Detail attention | Moderate | High |
| Example influence | Significant | Very significant |
| State tracking | Limited | Exceptional (4.5) |

## Citations to Follow

- Claude 4.x model cards
- Anthropic extended thinking documentation
- Effective context engineering for AI agents (Anthropic blog)

## Questions/Notes

- **Strength:** Official vendor guidance for latest models
- **Strength:** Clear behavioral changes from previous versions
- **Strength:** Practical instruction quality guidance
- **Practical insight:** "Above and beyond" now needs explicit prompting
- **Limitation:** Claude-specific, may not generalize to other models
- **Gap:** Limited specific metrics for measuring instruction clarity
- **Gap:** No comparative data on performance differences
- **Connects to:** anthropic2025promptengineering (overview), practical-guidance subtopic
- **Currency:** 2025, actively maintained

## Evidence Quality

**Medium for vendor documentation.** Authoritative for Claude models but limited empirical validation provided. Strong for "what to do"; weaker for "measured impact."
