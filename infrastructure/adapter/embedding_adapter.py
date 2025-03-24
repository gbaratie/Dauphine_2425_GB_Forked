from domain.port.embedding_port import EmbeddingPort
from typing import List
from infrastructure.embedding.cohere_embedding_generator import CohereEmbeddingGenerator

class EmbeddingAdapter(EmbeddingPort):
    def __init__(self, cohere_embedding_generator: CohereEmbeddingGenerator):
        self.cohere_embedding_generator = cohere_embedding_generator

    def generate_embedding(self, file_content: bytes) -> List[float]:
        return self.cohere_embedding_generator.generate_embedding(file_content)

    def embed_string(self, string: str) -> List[float]:
        return self.cohere_embedding_generator.generate_embedding(string.encode("utf-8"))