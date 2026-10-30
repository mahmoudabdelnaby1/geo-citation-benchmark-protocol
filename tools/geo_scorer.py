#!/usr/bin/env python3
"""
Experimental Heuristic GEO Citation Auditor
Analyzes brand entity and domain URL citation occurrences in AI engine text outputs:
- Counts exact brand entity mentions
- Detects explicit domain/URL footnote citations
- Scans for co-occurring recommendation vs cautionary modifier terms
- Computes an experimental heuristic index with explicit methodology disclosure
"""
import re
import json
import argparse
from pathlib import Path
from typing import Dict, Any, List

RECOMMENDATION_WORDS = ["best", "top", "leader", "recommended", "ممتاز", "افضل", "أفضل", "رائد", "موثوق", "معتمد"]
CAUTIONARY_WORDS = ["slow", "expensive", "bad", "poor", "سيء", "مشاكل", "غالي", "غير موثوق", "تحذير"]

def analyze_geo_citation(text: str, brand_name: str, brand_domain: str) -> Dict[str, Any]:
    brand_regex = re.compile(r"\b" + re.escape(brand_name) + r"\b", re.IGNORECASE)
    domain_clean = re.sub(r"^https?://", "", brand_domain.strip().lower()).rstrip("/")
    domain_regex = re.compile(re.escape(domain_clean), re.IGNORECASE)

    brand_mentions = len(brand_regex.findall(text))
    domain_mentions = len(domain_regex.findall(text))

    pos_found = [w for w in RECOMMENDATION_WORDS if re.search(r"\b" + re.escape(w) + r"\b", text, re.IGNORECASE)]
    neg_found = [w for w in CAUTIONARY_WORDS if re.search(r"\b" + re.escape(w) + r"\b", text, re.IGNORECASE)]

    has_url = domain_mentions > 0
    has_brand = brand_mentions > 0

    # Determine objective presence classification
    if has_url and has_brand:
        presence_type = "LINK_AND_ENTITY_CITED"
    elif has_brand:
        presence_type = "ENTITY_MENTIONED_WITHOUT_DIRECT_LINK"
    elif has_url:
        presence_type = "LINK_CITED_WITHOUT_NAMED_ENTITY"
    else:
        presence_type = "NOT_DETECTED"

    # Experimental heuristic calculation (transparently documented)
    # 40% URL presence, 30% entity volume, 30% sentiment terms balance
    url_component = 100.0 if has_url else 0.0
    entity_component = min(100.0, brand_mentions * 35.0)
    sentiment_component = 50.0
    if pos_found and not neg_found:
        sentiment_component = 90.0
    elif neg_found and not pos_found:
        sentiment_component = 20.0

    heuristic_index = round((0.40 * url_component) + (0.30 * entity_component) + (0.30 * sentiment_component), 1)

    return {
        "analysis_type": "EXPERIMENTAL_HEURISTIC_EVALUATION",
        "brand_name": brand_name,
        "brand_domain": domain_clean,
        "observed_metrics": {
            "brand_entity_mentions_count": brand_mentions,
            "domain_citations_count": domain_mentions,
            "has_direct_url_link": has_url,
            "presence_classification": presence_type,
            "co_occurring_positive_keywords": pos_found,
            "co_occurring_cautionary_keywords": neg_found
        },
        "experimental_scoring": {
            "heuristic_index": heuristic_index,
            "components": {
                "url_presence_score": url_component,
                "entity_volume_score": round(entity_component, 1),
                "sentiment_modifier_score": sentiment_component
            }
        },
        "methodology_disclaimer": (
            "This heuristic index is an experimental research tool for sampling LLM response text. "
            "It does not represent an official, verified, or industry-standard search ranking metric."
        )
    }

# Keep calculate_geo_score as backward-compatible wrapper
def calculate_geo_score(text: str, brand_name: str, brand_domain: str) -> Dict[str, Any]:
    res = analyze_geo_citation(text, brand_name, brand_domain)
    # Add backward compatible fields
    res["scores"] = {
        "total_geo_score": res["experimental_scoring"]["heuristic_index"],
        "url_score": res["experimental_scoring"]["components"]["url_presence_score"],
        "entity_score": res["experimental_scoring"]["components"]["entity_volume_score"],
        "sentiment_score": res["experimental_scoring"]["components"]["sentiment_modifier_score"]
    }
    return res

def main():
    parser = argparse.ArgumentParser(description="Experimental GEO Citation Text Auditor")
    parser.add_argument("--file", help="Path to text file containing LLM response")
    parser.add_argument("--text", help="Direct response text string to audit")
    parser.add_argument("--brand", required=True, help="Brand entity name")
    parser.add_argument("--domain", required=True, help="Brand primary domain")
    parser.add_argument("--output", help="Optional output JSON file path")
    args = parser.parse_args()

    content = args.text or ""
    if args.file:
        content = Path(args.file).read_text(encoding="utf-8")

    result = analyze_geo_citation(content, args.brand, args.domain)
    print(json.dumps(result, indent=2, ensure_ascii=False))

    if args.output:
        p = Path(args.output)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

if __name__ == "__main__":
    main()
