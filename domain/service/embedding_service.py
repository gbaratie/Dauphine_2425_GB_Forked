from domain.model.uploaded_file import UploadedFile
from domain.model.file_embedded import FileEmbedded
from domain.port.embedding_port import EmbeddingPort

class EmbeddingService:
    def __init__(self, embedding_port: EmbeddingPort):
        self.embedding_port = embedding_port

    def embed_file(self, uploaded_file: UploadedFile) -> FileEmbedded:
        # Appelle le port pour obtenir l'embedding
        embedding = self.embedding_port.generate_embedding(uploaded_file.content)
        return FileEmbedded(filename=uploaded_file.filename, embedding=embedding)