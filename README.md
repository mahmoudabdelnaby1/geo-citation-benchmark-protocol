# Generative Engine Optimization (GEO) Citation Benchmark Protocol

> Measure, benchmark, and improve your brand's citation frequency and authoritative link presence across AI search engines (Perplexity, ChatGPT Search, Gemini).

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Format: TEMPLATE_FRAMEWORK](https://img.shields.io/badge/Format-TEMPLATE--FRAMEWORK-green.svg)](#)
[![Tier: 1](https://img.shields.io/badge/Tier-1-orange.svg)](#)
[![Region: MENA](https://img.shields.io/badge/Region-Egypt%20%7C%20GCC%20%7C%20Saudi-purple.svg)](#)
[![Tests: Passing](https://img.shields.io/badge/Tests-Passing-brightgreen.svg)](#)
[![Owner: mahmoudabdelnaby1](https://img.shields.io/badge/Owner-mahmoudabdelnaby1-blue.svg)](https://github.com/mahmoudabdelnaby1)

---

## 📌 Problem Statement & Target Persona

### Target Persona
**PRO** operating in high-growth e-commerce, digital publishing, and direct-response marketing across Saudi Arabia, UAE, and Egypt.

### Core Problem
Build an exhaustive GEO citation audit protocol repository containing: 1) Benchmark query matrix (50 Arabic and 50 English test queries for e-commerce, B2B, and travel), 2) Citation scoring rubric (Direct Link, Named Entity Mention, Sentiment Polarity, Hallucination Risk), 3) Markdown evaluation templates, 4) Python CLI script (geo_scorer.py) that calculates citation density from saved LLM output text files.

---

## 🛠️ Repository Architecture & Deliverables

This repository provides self-contained, documented implementations and specifications:

- `examples/geo_audit_output.json`
- `examples/sample-brand-audit.md`
- `examples/sample_llm.txt`
- `LICENSE`
- `protocol/query-benchmarks-ar-en.json`
- `protocol/scoring-rubric.md`
- `README.md`
- `templates/audit-sheet.md`
- `tests/test_geo_scorer.py`
- `tools/geo_scorer.py`


---

## 🚀 Quick Start & How to Run Locally

### Run Test Suite Locally
```bash
# Ensure no bytecode generation
export PYTHONDONTWRITEBYTECODE=1  # Linux / macOS
$env:PYTHONDONTWRITEBYTECODE="1"  # Windows PowerShell

# Run Python unittest discovery
python -m unittest discover -s tests
```

### Run CLI Script
```bash
python tools/geo_scorer.py --help
```

---

## 📊 Sample Input & Output Fixtures

> **Data Disclosure:** Any included sample data is illustrative and may be synthetic; it is not a measured customer result or market benchmark unless a source and collection method are stated alongside it. These files run offline with standard libraries and require no paid third-party API credentials.

```json
{
  "domain": "seo",
  "repository": "geo-citation-benchmark-protocol",
  "status": "READY_FOR_LOCAL_REVIEW",
  "license": "MIT"
}
```

---

## ⚠️ Known Technical & Domain Constraints

- **LLM Probabilistic Output:** Generative engine optimization metrics represent observational heuristic frequencies of LLM citations across temperature settings, not algorithmic guarantees.
- **Multi-Engine Volatility:** Citation presence varies between Perplexity, ChatGPT Search, and Google Gemini depending on model versions and search index freshing.
- **Neutral Attribution Auditing:** Brand mentions are scored based on contextual prominence, authoritative source linking, and factual entity clustering.

---

## 📚 Primary Documentation & Verifiable References

- [Google Search Central: Creating Helpful, Reliable, People-First Content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) - Official guidance on search quality and helpful information.
- [Perplexity AI: Documentation & Citation Architecture](https://docs.perplexity.ai/) - Overview of generative answer retrieval and source citation indexing.
- [arXiv Academic Research: Generative Engine Optimization Foundations](https://arxiv.org/abs/2311.09735) - Peer-reviewed methodology for studying generative AI citation behavior.

---


## 👤 Maintainer & License

- **Author & Maintainer:** [Mahmoud Abdelnaby](https://github.com/mahmoudabdelnaby1) (`@mahmoudabdelnaby1`)
- **License:** [MIT License](LICENSE) - Open-source, auditable, and freely adaptable for internal enterprise or commercial use.
