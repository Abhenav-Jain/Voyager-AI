"""
Automated Integration and Scenario Verification Test Suite.
Tests the FastAPI backend, AI synthesis, and the 3 user scenarios.
"""

import sys
import os
import unittest

# Add project root to sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi.testclient import TestClient
from app.main import app

class TestTravelPlanner(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = TestClient(app)

    def test_01_health_check(self):
        """Verifies system diagnostics and Transformer models status."""
        resp = self.client.get("/api/auth/health")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertIn("transformer_engine", data)
        self.assertEqual(data["transformer_engine"]["transformer_models_loaded"], 3)
        self.assertIn("database", data)

    def test_02_scenario_1_solo_weekend(self):
        """Verifies Scenario 1: Solo Traveler Weekend Getaway in Tokyo."""
        resp = self.client.get("/api/scenarios/scenario-1")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["traveler_type"], "solo")
        self.assertEqual(data["group_size"], 1)
        self.assertEqual(data["total_days"], 2)
        self.assertGreater(len(data["days"]), 0)
        self.assertTrue(any("Tokyo" in d["theme"] or "Welcome" in d["theme"] for d in data["days"]))

    def test_03_scenario_2_couple_vacation(self):
        """Verifies Scenario 2: Couple Personalized Vacation in Florence."""
        resp = self.client.get("/api/scenarios/scenario-2")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["traveler_type"], "couple")
        self.assertEqual(data["group_size"], 2)
        self.assertEqual(data["budget_level"], "luxury")
        self.assertEqual(data["total_days"], 4)

        # Test Day Regeneration on Day 2
        trip_id = data["id"]
        regen_resp = self.client.post(
            f"/api/trips/{trip_id}/regenerate-day",
            json={"day_number": 2, "feedback": "Add secluded vineyard and sunset terrace"}
        )
        self.assertEqual(regen_resp.status_code, 200)
        regen_data = regen_resp.json()
        day2 = next(d for d in regen_data["days"] if d["day_number"] == 2)
        self.assertIn("Refined Day 2", day2["theme"])

    def test_04_scenario_3_group_trip(self):
        """Verifies Scenario 3: Small Group Coordinating Multi-Day Trip in Barcelona."""
        resp = self.client.get("/api/scenarios/scenario-3")
        self.assertEqual(resp.status_code, 200)
        data = resp.json()
        self.assertEqual(data["traveler_type"], "group")
        self.assertEqual(data["group_size"], 4)
        self.assertGreater(data["cost_per_person"], 0)
        self.assertAlmostEqual(data["estimated_total_cost"], data["cost_per_person"] * 4, delta=1.0)

    def test_05_custom_trip_generation(self):
        """Verifies custom user generation through the Smart Trip Builder."""
        payload = {
            "destination": "Paris, France",
            "start_date": "2026-12-01",
            "end_date": "2026-12-03",
            "traveler_type": "couple",
            "group_size": 2,
            "budget_level": "moderate",
            "target_budget_usd": 600,
            "interests": ["culture", "food"],
            "pacing": "balanced"
        }
        resp = self.client.post("/api/trips/generate", json=payload)
        self.assertEqual(resp.status_code, 200)
        trip = resp.json()
        self.assertEqual(trip["destination"], "Paris")
        self.assertEqual(trip["total_days"], 3)

        # Test Exports
        trip_id = trip["id"]
        md_resp = self.client.get(f"/api/trips/{trip_id}/export?format=markdown")
        self.assertEqual(md_resp.status_code, 200)
        self.assertIn("# 3-Day Couple Trip to Paris", md_resp.text)

        ics_resp = self.client.get(f"/api/trips/{trip_id}/export?format=ics")
        self.assertEqual(ics_resp.status_code, 200)
        self.assertIn("BEGIN:VCALENDAR", ics_resp.text)

if __name__ == "__main__":
    unittest.main()
