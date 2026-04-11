import unittest
from backend.profile_intelligence.engine import ProfileIntelligenceEngine

class TestProfileIntelligenceEngine(unittest.TestCase):
    def setUp(self):
        self.engine = ProfileIntelligenceEngine()

    def test_extract_traits(self):
        profile_data = {
            "name": "John Doe",
            "bio": "I love hiking and reading.",
            "preferences": {
                "hobbies": ["hiking", "reading"],
                "values": ["adventure", "knowledge"]
            }
        }
        traits = self.engine.extract_traits(profile_data)
        self.assertIn("openness", traits)
        self.assertIn("conscientiousness", traits)
        self.assertGreaterEqual(traits["openness"], 0)
        self.assertLessEqual(traits["openness"], 1)

if __name__ == "__main__":
    unittest.main()