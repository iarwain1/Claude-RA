# MathReader : Text-to-Speech for Mathematical Documents

**arXiv:** [2501.07088](https://arxiv.org/abs/2501.07088)
**Authors:** Sieun Hyeon, Kyudan Jung, Nam-Joon Kim, Hyun Gon Ryu, Jaeyoung Do
**Date:** 2025-01-13
**Categories:** cs.AI, cs.SD, eess.AS

## Abstract

TTS (Text-to-Speech) document reader from Microsoft, Adobe, Apple, and OpenAI have been serviced worldwide. They provide relatively good TTS results for general plain text, but sometimes skip contents or provide unsatisfactory results for mathematical expressions. This is because most modern academic papers are written in LaTeX, and when LaTeX formulas are compiled, they are rendered as distinctive text forms within the document. However, traditional TTS document readers output only the text as it is recognized, without considering the mathematical meaning of the formulas. To address this issue, we propose MathReader, which effectively integrates OCR, a fine-tuned T5 model, and TTS. MathReader demonstrated a lower Word Error Rate (WER) than existing TTS document readers, such as Microsoft Edge and Adobe Acrobat, when processing documents containing mathematical formulas. MathReader reduced the WER from 0.510 to 0.281 compared to Microsoft Edge, and from 0.617 to 0.281 compared to Adobe Acrobat. This will significantly contribute to alleviating the inconvenience faced by users who want to listen to documents, especially those who are visually impaired. The code is available at https://github.com/hyeonsieun/MathReader.

---
*Metadata fetched via arxiv API on 2025-12-31*
