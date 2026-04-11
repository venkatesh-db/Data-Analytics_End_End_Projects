from typing import Dict
from backend.profile_intelligence.engine import ProfileIntelligenceEngine

class UserProfile:
    def __init__(self, name: str, bio: str, preferences: Dict):
        self.name = name
        self.bio = bio
        self.preferences = preferences
        self.traits = {}

    def analyze_traits(self):
        """
        Analyze and extract personality traits using the Profile Intelligence Engine.
        """
        engine = ProfileIntelligenceEngine()
        self.traits = engine.extract_traits({
            "name": self.name,
            "bio": self.bio,
            "preferences": self.preferences
        })

# Example usage
if __name__ == "__main__":
    profile = UserProfile(
        name="Jane Doe",
        bio="I love painting, traveling, and exploring new cultures.",
        preferences={
            "hobbies": ["painting", "traveling"],
            "values": ["creativity", "adventure"]
        }
    )
    profile.analyze_traits()
    print("User Traits:", profile.traits)