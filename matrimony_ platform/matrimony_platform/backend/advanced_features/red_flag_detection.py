from typing import List, Dict

class RedFlagDetectionSystem:
    def __init__(self):
        self.red_flag_keywords = ["abuse", "violence", "harassment", "scam", "fraud"]

    def detect_red_flags(self, messages: List[str]) -> Dict:
        """
        Detect red flags in a list of messages.

        Args:
            messages (List[str]): List of messages to analyze.

        Returns:
            Dict: Detected red flags and their counts.
        """
        red_flag_counts = {keyword: 0 for keyword in self.red_flag_keywords}

        for message in messages:
            for keyword in self.red_flag_keywords:
                if keyword in message.lower():
                    red_flag_counts[keyword] += 1

        total_flags = sum(red_flag_counts.values())
        return {
            "total_flags": total_flags,
            "details": red_flag_counts
        }

# Example usage
if __name__ == "__main__":
    detector = RedFlagDetectionSystem()

    messages = [
        "This is a scam message.",
        "No signs of abuse here.",
        "Harassment is not tolerated.",
        "This message is clean."
    ]

    analysis = detector.detect_red_flags(messages)
    print("Red Flag Analysis:", analysis)