import unittest
from backend.advanced_features.chat_compatibility import ChatCompatibilityAnalyzer

class TestChatCompatibilityAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = ChatCompatibilityAnalyzer()

    def test_analyze_compatibility(self):
        user1_chat = ["traveling", "cooking", "movies"]
        user2_chat = ["cooking", "sports", "movies"]

        analysis = self.analyzer.analyze_compatibility(user1_chat, user2_chat)
        self.assertEqual(analysis["common_topics"], 2)
        self.assertEqual(analysis["total_topics"], 4)
        self.assertAlmostEqual(analysis["compatibility_score"], 0.5)

if __name__ == "__main__":
    unittest.main()