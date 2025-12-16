# Approaching Human-Level Forecasting with Language Models

**arXiv:** https://arxiv.org/abs/2402.18563
**Authors:** Danny Halawi, Fred Zhang, Chen Yueh-Han, Jacob Steinhardt (UC Berkeley)
**Date:** 2024-02-28

## Abstract

Forecasting future events is important for policy and decision making. This work studies whether language models (LMs) can forecast at the level of competitive human forecasters.

The authors developed a retrieval-augmented LM system designed to:
1. Automatically search for relevant information
2. Generate forecasts
3. Aggregate predictions

They collected a large dataset of questions from competitive forecasting platforms and evaluated the system against aggregates of human forecasts.

## Key Results

- On average, the system nears the crowd aggregate of competitive forecasters
- In some settings, it surpasses human forecasters
- Demonstrates that LMs could provide accurate predictions at scale

## System Architecture

1. **Retrieval**: LM generates search queries, retrieves articles from historical news APIs
2. **Ranking**: LM ranks articles on relevancy, summarizes top-k articles
3. **Reasoning**: LM takes question + summaries and generates forecasts
4. **Aggregation**: Forecasts aggregated using trimmed mean

## Claude Summary

This paper demonstrates that LLMs can approach competitive human forecasting performance:

**Significance**:
- Forecasting is a key test of model reasoning and real-world knowledge
- Competitive forecasters are specifically skilled at this task
- Matching them suggests genuine capability, not just pattern matching

**Methodology**:
- Retrieval-augmented approach is crucial - pure LLM forecasting would be limited by knowledge cutoffs
- Aggregation of multiple forecasts improves reliability

**Implications**:
- Could scale forecasting for institutional decision-making
- Useful for policy analysis, risk assessment
- Raises questions about AI's role in prediction markets

## Relevance

Important for understanding LLM capabilities in reasoning about uncertain future events. Relevant to AI safety research on model forecasting abilities and for practical applications in decision support.
