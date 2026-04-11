from typing import List, Dict

class ChatCompatibilityAnalyzer:
    def __init__(self):
        pass

    def analyze_compatibility(self, chat_history_user1: List[str], chat_history_user2: List[str]) -> Dict:
        """
        Analyze the compatibility between two users based on their chat history.

        Args:
            chat_history_user1 (List[str]): Chat history of user 1.
            chat_history_user2 (List[str]): Chat history of user 2.

        Returns:
            Dict: Compatibility score and analysis.
        """
        # Placeholder logic for compatibility analysis
        common_topics = len(set(chat_history_user1) & set(chat_history_user2))
        total_topics = len(set(chat_history_user1) | set(chat_history_user2))
        compatibility_score = common_topics / total_topics if total_topics > 0 else 0

        return {
            "compatibility_score": round(compatibility_score, 2),
            "common_topics": common_topics,
            "total_topics": total_topics
        }

# Example usage
if __name__ == "__main__":
    analyzer = ChatCompatibilityAnalyzer()

    user1_chat = ["traveling", "cooking", "movies"]
    user2_chat = ["cooking", "sports", "movies"]

    analysis = analyzer.analyze_compatibility(user1_chat, user2_chat)
    print("Chat Compatibility Analysis:", analysis)