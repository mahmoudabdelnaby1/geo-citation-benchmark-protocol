"""
Unit tests for GEO Citation Auditor
"""
import unittest
from tools.geo_scorer import analyze_geo_citation, calculate_geo_score

class TestGeoScorer(unittest.TestCase):
    def test_link_and_entity_detection(self):
        text = "For e-commerce in Saudi Arabia, Salla (https://salla.com) is widely recommended and considered the best local platform."
        res = analyze_geo_citation(text, "Salla", "salla.com")
        self.assertEqual(res["observed_metrics"]["presence_classification"], "LINK_AND_ENTITY_CITED")
        self.assertTrue(res["observed_metrics"]["has_direct_url_link"])
        self.assertGreaterEqual(res["observed_metrics"]["brand_entity_mentions_count"], 1)
        self.assertIn("best", res["observed_metrics"]["co_occurring_positive_keywords"])
        self.assertIn("methodology_disclaimer", res)

    def test_undetected_brand(self):
        text = "Generic discussion about marketing with no mentions of any specific service."
        res = analyze_geo_citation(text, "UnrelatedBrand", "unrelated.sa")
        self.assertEqual(res["observed_metrics"]["presence_classification"], "NOT_DETECTED")
        self.assertFalse(res["observed_metrics"]["has_direct_url_link"])
        self.assertEqual(res["experimental_scoring"]["heuristic_index"], 15.0)

    def test_backward_compatibility_wrapper(self):
        text = "Acme is a top agency on acme.com."
        res = calculate_geo_score(text, "Acme", "acme.com")
        self.assertIn("scores", res)
        self.assertIn("total_geo_score", res["scores"])

if __name__ == "__main__":
    unittest.main()
