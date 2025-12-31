# Flow: Modularized Agentic Workflow Automation

**arXiv:** [2501.07834](https://arxiv.org/abs/2501.07834)
**Authors:** Boye Niu, Yiliao Song, Kai Lian, Yifan Shen, Yu Yao, et al. (7 total)
**Date:** 2025-01-14
**Categories:** cs.AI, cs.LG, cs.MA

## Abstract

Multi-agent frameworks powered by large language models (LLMs) have demonstrated great success in automated planning and task execution. However, the effective adjustment of agentic workflows during execution has not been well studied. An effective workflow adjustment is crucial in real-world scenarios, as the initial plan must adjust to unforeseen challenges and changing conditions in real time to ensure the efficient execution of complex tasks. In this paper, we define workflows as an activity-on-vertex (AOV) graph, which allows continuous workflow refinement by LLM agents through dynamic subtask allocation adjustment based on historical performance and previous AOVs. To further enhance framework performance, we emphasize modularity in workflow design based on evaluating parallelism and dependency complexity. With this design, our proposed multi-agent framework achieves efficient concurrent execution of subtasks, effective goal achievement, and enhanced error tolerance. Empirical results across various practical tasks demonstrate significant improvements in the efficiency of multi-agent frameworks through dynamic workflow refinement and modularization. The code is available at: https://github.com/tmllab/2025_ICLR_FLOW.

---
*Metadata fetched via arxiv API on 2025-12-31*
