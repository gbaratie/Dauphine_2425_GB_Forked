import logging
from domain.port.text_generator_port import TextGeneratorPort
from domain.port.embedding_port import EmbeddingPort
from domain.port.persistence_port import PersistencePort

logger = logging.getLogger(__name__)

class TextGenerationService:
    def __init__(self, text_generator: TextGeneratorPort, embedding_service: EmbeddingPort, persistence_service: PersistencePort):
        """
        Service pour gérer la génération de texte.
        :param text_generator: Port pour générer du texte.
        :param embedding_service: Service pour gérer les embeddings.
        """
        self.text_generator = text_generator
        self.embedding_service = embedding_service  # Injection du service d'embedding
        self.persistence_service = persistence_service

    def get_generated_text(self, prompt: str, is_rag: bool = False) -> str:
        if is_rag:
            logger.info("RAG mode activated: Retrieval-Augmented Generation will be used.")

            # Étape 1 : Générer un embedding pour le prompt
            embedding = self.embedding_service.embed_string(prompt)
            #logger.info(f"Generated embedding for prompt: {embedding}")

            # Étape 2 : Récupérer les passages pertinents avec cet embedding
            # Vérifier que l'embedding est une liste de flottants
            if not isinstance(embedding, list) or not all(isinstance(x, float) for x in embedding):
                logger.error(f"Invalid embedding format: {embedding}")
                raise ValueError("Embedding must be a list of floats.")
            
        
            relevant_passages = self.persistence_service.query_vector(embedding, top_k=5)
            relevant_texts = [match["metadata"]["content"] for match in relevant_passages]
            logger.info(f"Retrieved {len(relevant_texts)} relevant passages.")
            


            # Étape 3 : Construire le contexte enrichi et appeler le générateur de texte
            # ...

        else:
            logger.info("Standard mode activated: Direct call to Cohere.")
        
        # Appel standard au générateur de texte
        return self.text_generator.get_generated_text(prompt, is_rag=is_rag)