# Measuring Agents in Production

**arXiv:** https://arxiv.org/abs/2512.04123
**Authors:** Melissa Z. Pan, Negar Arabzadeh, Riccardo Cogo, Yuxuan Zhu, Alexander Xiong, Lakshya A Agrawal, Huanzhi Mao, Emma Shen, Sid Pallerla, Liana Patel, Shu Liu, Tianneng Shi, Xiaoyuan Liu, Jared Quincy Davis, Emmanuele Lacavalla, Alessandro Basile, Shuyi Yang, Paul Castro, Daniel Kang, Joseph E. Gonzalez, Koushik Sen, Dawn Song, Ion Stoica, Matei Zaharia, Marquita Ellis
**Date:** 2025-12-02

## Abstract

AI agents are actively running in production across diverse industries, yet little is publicly known about which technical approaches enable successful real-world deployments. This paper presents the first large-scale systematic study of AI agents in production, surveying 306 practitioners and conducting 20 in-depth case studies via interviews across 26 domains. The study investigates why organizations build agents, how they build them, how they evaluate them, and what the top development challenges are.

Key findings include that production agents typically use simple, controllable approaches: 68% execute at most 10 steps before requiring human intervention, 70% rely on prompting off-the-shelf models instead of weight tuning, and 74% depend primarily on human evaluation.

## Claude Summary

This is a significant empirical study on the actual state of AI agent deployment in production environments. The findings challenge common assumptions about agent complexity - real-world agents tend to be much simpler than research prototypes, with short action chains and heavy reliance on human oversight.

The reliance on human evaluation (74%) rather than automated metrics suggests that agent evaluation remains an unsolved problem in practice. The preference for prompting over fine-tuning (70%) indicates practitioners value flexibility and controllability over performance optimization.

This paper is highly relevant for understanding the gap between AI agent research and practical deployment, and for informing evaluation methodology development.
