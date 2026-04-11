import faiss
import numpy as np

class VectorStore:
    def __init__(self, embedding_dim: int):
        """
        Initialize the FAISS vector store.

        Args:
            embedding_dim (int): The dimension of the embeddings.
        """
        self.index = faiss.IndexFlatL2(embedding_dim)

    def add_embeddings(self, embeddings: np.ndarray):
        """
        Add embeddings to the vector store.

        Args:
            embeddings (np.ndarray): A 2D numpy array of embeddings.
        """
        self.index.add(embeddings)

    def search(self, query_embedding: np.ndarray, top_k: int = 5):
        """
        Search for the top_k nearest neighbors of the query embedding.

        Args:
            query_embedding (np.ndarray): The query embedding.
            top_k (int): The number of nearest neighbors to return.

        Returns:
            tuple: Distances and indices of the nearest neighbors.
        """
        distances, indices = self.index.search(query_embedding, top_k)
        return distances, indices

# Example usage
if __name__ == "__main__":
    vector_store = VectorStore(embedding_dim=384)  # Example embedding dimension

    # Add some dummy embeddings
    rng = np.random.default_rng()
    dummy_embeddings = rng.random((10, 384), dtype='float32')
    vector_store.add_embeddings(dummy_embeddings)

    # Perform a search
    query = rng.random((1, 384), dtype='float32')
    distances, indices = vector_store.search(query)
    print("Nearest neighbors:", indices)