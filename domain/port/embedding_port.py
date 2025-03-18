from abc import ABC, abstractmethod
from typing import List

class EmbeddingPort(ABC):
    @abstractmethod
    def generate_embedding(self, file_content: bytes) -> List[float]:
        """
        Génère un embedding pour le contenu d'un fichier.
        :param file_content: Contenu du fichier en bytes.
        :return: Liste de floats représentant l'embedding.
        """
        pass