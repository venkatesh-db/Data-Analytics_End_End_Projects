from typing import Dict

class ExplainableAI:
    def __init__(self):
        # This constructor is intentionally left empty for future initialization logic.
        pass

    def generate_explanation(self, user_profile: Dict, matched_profile: Dict, similarity_score: float) -> str:
        """
        Generate an explanation for why two profiles were matched.

        Args:
            user_profile (Dict): The user's profile data.
            matched_profile (Dict): The matched profile data.
            similarity_score (float): The similarity score between the two profiles.

        Returns:
            str: A human-readable explanation.
        """
        explanation = (
            f"User '{user_profile['name']}' was matched with '{matched_profile['name']}' with a similarity score of {similarity_score:.2f}. "
            f"Both share interests in {', '.join(set(user_profile['preferences']['hobbies']) & set(matched_profile['preferences']['hobbies']))}. "
            f"Additionally, their values align on {', '.join(set(user_profile['preferences']['values']) & set(matched_profile['preferences']['values']))}."
        )
        return explanation

# Example usage
if __name__ == "__main__":
    explainer = ExplainableAI()

    user_profile = {
        "name": "Alice",
        "preferences": {
            "hobbies": ["reading", "traveling", "cooking"],
            "values": ["adventure", "creativity"]
        }
    }

    matched_profile = {
        "name": "Bob",
        "preferences": {
            "hobbies": ["traveling", "hiking", "cooking"],
            "values": ["creativity", "health"]
        }
    }

    similarity_score = 0.87
    explanation = explainer.generate_explanation(user_profile, matched_profile, similarity_score)
    print("Match Explanation:", explanation)