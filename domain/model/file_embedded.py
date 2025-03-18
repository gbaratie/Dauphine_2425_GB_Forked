from typing import List

class FileEmbedded:
    def __init__(self, filename: str, embedding: List[float]):
        self.filename = filename
        self.embedding = embedding