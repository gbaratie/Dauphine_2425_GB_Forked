from domain.model.uploaded_file import UploadedFile
from domain.model.file_embedded import FileEmbedded
from domain.port.embedding_port import EmbeddingPort
from domain.port.persistence_port import PersistencePort

import logging

# Configurer le logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EmbeddingService:
    def __init__(self, embedding_port: EmbeddingPort, persistence_port: PersistencePort):
        """
        Service pour gérer les embeddings.
        :param embedding_port: Port pour générer des embeddings.
        :param persistence_port: Port pour sauvegarder les embeddings.
        """
        self.embedding_port = embedding_port
        self.persistence_port = persistence_port

    def embed_file(self, uploaded_file: UploadedFile) -> FileEmbedded:
        # Appelle le port pour obtenir l'embedding
        embedding = self.embedding_port.generate_embedding(uploaded_file.content)
        logger.info(f"Generated embedding : {embedding}")

        # Sauvegarde l'embedding dans Pinecone via le port de persistance
        file_embedded = FileEmbedded(filename=uploaded_file.filename, embedding=embedding)
        self.persistence_port.save_vector(file_embedded.filename, file_embedded.embedding)

        return file_embedded
    
    def embed_string(self, string: str) -> FileEmbedded:
        # Appelle le port pour obtenir l'embedding
        embedding = self.embedding_port.generate_embedding(string.encode("utf-8"))
        logger.info(f"Generated embedding for string: {embedding}")

        # Sauvegarde l'embedding dans Pinecone via le port de persistance
        # Utilise un nom fictif pour identifier cet embedding
        string_embedded = FileEmbedded(filename="string_embedding", embedding=embedding)

        return string_embedded