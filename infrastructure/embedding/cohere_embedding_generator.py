import os
from dotenv import load_dotenv
import cohere
from typing import List
import logging

# Configurer le logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Charger les variables d'environnement depuis un fichier .env
load_dotenv()
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

class CohereEmbeddingGenerator:
    def __init__(self):
        self.client = cohere.Client(COHERE_API_KEY)

    def generate_embedding(self, file_content: bytes) -> List[float]:
        text = file_content.decode("utf-8")
        logger.info("Embedding endpoint called")
        response = self.client.embed(texts=[text])
        #logger.info(f"Generated embedding: {response.embeddings[0]}")
        return response.embeddings[0]