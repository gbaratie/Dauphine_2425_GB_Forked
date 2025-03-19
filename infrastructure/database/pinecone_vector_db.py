import os
from dotenv import load_dotenv
import pinecone
from typing import List, Dict
import logging

# Configurer le logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
PINECONE_ENVIRONMENT = os.environ.get('PINECONE_ENVIRONMENT')
PINECONE_INDEX_NAME = os.environ.get('PINECONE_INDEX_NAME', 'default-index')  # Nom par défaut de l'index

class PineconeVectorDB:
    def __init__(self):
        # Initialiser Pinecone
        self.pinecone_client = pinecone.Pinecone(api_key=PINECONE_API_KEY)
        #self.index_name = PINECONE_INDEX_NAME
        logger.info("Pinecone client initialized")

        # Vérifier si l'index existe, sinon le créer
        if PINECONE_INDEX_NAME not in self.pinecone_client.list_indexes().names():
            self.pinecone_client.create_index(PINECONE_INDEX_NAME, dimension=768)  # Ajustez la dimension selon vos embeddings
            logger.info(f"Created Pinecone index: {PINECONE_INDEX_NAME}")

        # Connecter à l'index
        self.index = self.pinecone_client.Index(PINECONE_INDEX_NAME)
        logger.info(f"Connected to Pinecone index: {PINECONE_INDEX_NAME}")

    def upsert_vector(self, vector_id: str, embedding: List[float], metadata: Dict[str, str] = None) -> None:
      
        logger.info(f"Upserting vector with ID: {vector_id}")
        self.index.upsert(vectors=[(vector_id, embedding, metadata)])

    def query_vector(self, embedding: List[float], top_k: int = 10) -> List[Dict]:
        logger.info(f"Querying Pinecone index with embedding: {embedding[:5]}... (truncated)")
        results = self.index.query(queries=[embedding], top_k=top_k)
        return results['matches']

    def delete_vector(self, vector_id: str) -> None:
        logger.info(f"Deleting vector with ID: {vector_id}")
        self.index.delete(ids=[vector_id])


