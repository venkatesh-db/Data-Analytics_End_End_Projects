import unittest
from backend.advanced_features.red_flag_detection import RedFlagDetectionSystem

class TestRedFlagDetectionSystem(unittest.TestCase):
    def setUp(self):
        self.detector = RedFlagDetectionSystem()

    def test_detect_red_flags(self):
        messages = [
            "This is a scam message.",
            "No signs of abuse here.",
            "Harassment is not tolerated.",
            "This message is clean."
        ]

        analysis = self.detector.detect_red_flags(messages)
        self.assertEqual(analysis["total_flags"], 3)
        self.assertEqual(analysis["details"]["scam"], 1)
        self.assertEqual(analysis["details"]["abuse"], 1)
        self.assertEqual(analysis["details"]["harassment"], 1)

if __name__ == "__main__":
    unittest.main()