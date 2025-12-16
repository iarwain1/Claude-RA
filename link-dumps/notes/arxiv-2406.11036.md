# garak: A Framework for Security Probing Large Language Models

**arXiv:** https://arxiv.org/abs/2406.11036
**Authors:** Leon Derczynski, Erick Galinkin, Jeffrey Martin, Subho Majumdar, Nanna Inie
**Date:** 2024-06
**GitHub:** https://github.com/leondz/garak

## Abstract

garak is an open-source framework designed for security probing and vulnerability scanning of Large Language Models. Named after the Star Trek: Deep Space Nine character, it provides systematic tools for assessing LLM safety.

## Key Features

**Probe Types:**
- Prompt injection vulnerabilities
- Jailbreaking susceptibility
- Data leakage detection
- Harmful content generation
- Encoding-based attacks
- Many other security concerns

**Architecture:**
- Modular probe system
- Multiple detector types
- Configurable attack strategies
- Automated evaluation pipelines

## Functionality

1. **Probing**: Runs series of probes against target models
2. **Detection**: Evaluates responses for problematic outputs
3. **Reporting**: Generates vulnerability reports
4. **Extensibility**: Allows custom probes and detectors

## Claude Summary

garak fills an important gap in the LLM security ecosystem:

**Why it matters**:
- Provides standardized security testing for LLMs
- Enables reproducible vulnerability assessments
- Open-source allows community contribution and validation

**Use cases**:
- Red-teaming before deployment
- Comparing model safety across versions
- Validating safety interventions
- Research on LLM vulnerabilities

**Comparison to other tools**:
- More comprehensive than ad-hoc testing
- Systematic coverage of known vulnerability classes
- Continuously updated with new probes

## Relevance

Important tool for anyone deploying or evaluating LLMs. Enables systematic security assessment rather than relying on manual testing. Useful for both researchers studying LLM vulnerabilities and practitioners ensuring deployment safety.
