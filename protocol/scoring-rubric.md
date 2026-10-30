# Generative Engine Optimization (GEO) Scoring Rubric & Evaluation Framework

## 1. Overview
This protocol provides an objective scoring methodology to benchmark brand visibility, source attribution, and citation frequency across major Generative AI search engines (Perplexity, ChatGPT Search, Google AI Overviews, Gemini).

## 2. Quantitative Scoring Weights
The overall GEO Citation Score (0 - 100) is calculated using four distinct dimensions:

| Dimension | Weight | Description | Evaluation Criteria |
| :--- | :--- | :--- | :--- |
| **Direct URL Attribution** | 35% | Presence of clickable markdown or citation footnote linking directly to brand domain. | 0 = None, 50 = Secondary source mentioning brand, 100 = Direct domain link in citation chips. |
| **Named Entity Prominence** | 25% | Occurrence of verified brand name in prime response body (first 2 paragraphs). | 0 = Absent, 50 = Buried in bullet points, 100 = Primary recommendation or top entity. |
| **Sentiment & Context Polarity**| 20% | Semantic tone of LLM regarding brand reliability and product capability. | 0 = Negative/Cautionary, 50 = Neutral/Listed, 100 = Strong endorsement or category benchmark. |
| **Hallucination & Accuracy Risk**| 20% | Factual correctness of pricing, features, and specs stated by the LLM. | 0 = Severe factual error/hallucination, 50 = Outdated info, 100 = 100% Factually accurate. |

## 3. Mathematical Formula
$$GEO\_Score = 0.35(URL) + 0.25(Entity) + 0.20(Sentiment) + 0.20(Accuracy)$$

## 4. Benchmark Thresholds
- **Tier 1 (Authoritative Sovereign):** GEO Score >= 85 (Primary source cited in >= 70% of category prompts).
- **Tier 2 (Visible Contender):** GEO Score 65 - 84 (Mentioned in comparison tables, secondary citations).
- **Tier 3 (Underrepresented):** GEO Score 40 - 64 (Occasional generic mention without direct URL).
- **Tier 4 (Invisible):** GEO Score < 40 (Competitors dominate generative synthesis).
