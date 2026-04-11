import numpy as np
from typing import List, Dict
from backend.db.vector_store import VectorStore
from backend.embeddings.pipeline import EmbeddingPipeline

class SemanticMatchingEngine:
    def __init__(self, embedding_dim: int):
        self.vector_store = VectorStore(embedding_dim)
        self.embedding_pipeline = EmbeddingPipeline()

    def add_profiles(self, profiles: List[Dict]):
        """
        Add user profiles to the vector store.

        Args:
            profiles (List[Dict]): List of user profiles.
        """
        embeddings = [self.embedding_pipeline.generate_embedding(profile['bio']) for profile in profiles]
        self.vector_store.add_embeddings(np.array(embeddings, dtype='float32'))

    def find_matches(self, query_profile: Dict, top_k: int = 5) -> List[int]:
        """
        Find the top_k matching profiles for the given query profile.

        Args:
            query_profile (Dict): The profile to match.
            top_k (int): Number of top matches to return.

        Returns:
            List[int]: Indices of the top matching profiles.
        """
        query_embedding = self.embedding_pipeline.generate_embedding(query_profile['bio']).reshape(1, -1)
        _, indices = self.vector_store.search(query_embedding, top_k)
        return indices.tolist()

# Example usage
if __name__ == "__main__":
    engine = SemanticMatchingEngine(embedding_dim=384)

    # Add some sample profiles
    profiles = [
        {"bio": "I enjoy hiking and outdoor adventures."},
        {"bio": "I love reading books and exploring new ideas."},
        {"bio": "Cooking and traveling are my passions."},
        {"bio": "Fitness and healthy living are important to me."},
        {"bio": "I am a tech enthusiast who loves coding."}
    ]
    engine.add_profiles(profiles)

    # Find matches for a query profile
    query = {"bio": "I enjoy outdoor activities and hiking."}
    matches = engine.find_matches(query)
    print("Top matching profiles:", matches)