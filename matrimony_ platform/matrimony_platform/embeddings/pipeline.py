import numpy as np
from sentence_transformers import SentenceTransformer

class EmbeddingPipeline:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

    def generate_embedding(self, text: str) -> np.ndarray:
        """
        Generate an embedding for the given text.

        Args:
            text (str): The input text to embed.

        Returns:
            np.ndarray: The generated embedding as a numpy array.
        """
        return self.model.encode(text)

# Example usage
if __name__ == "__main__":
    pipeline = EmbeddingPipeline()
    sample_text = "Looking for a kind and adventurous partner."
    embedding = pipeline.generate_embedding(sample_text)
    print("Generated embedding:", embedding)