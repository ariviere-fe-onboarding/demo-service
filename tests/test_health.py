import unittest

from health import health_status


class HealthStatusTests(unittest.TestCase):
    def test_health_contract(self):
        self.assertEqual(
            health_status(),
            {"service": "demo-service", "status": "ok"},
        )

    def test_responses_are_independent(self):
        response = health_status()
        response["status"] = "changed"
        self.assertEqual(health_status()["status"], "ok")


if __name__ == "__main__":
    unittest.main()
