import os
from dotenv import load_dotenv
from typing import List, Dict

# Import du port pour définir l'interface à implémenter
from domain.port.text_generator_port import TextGeneratorPort
from domain.port.persistence_port import PersistencePort

# Import du générateur de texte Cohere
from infrastructure.text_generator.cohere_text_generator import CohereTextGenerator

# Import de PineconeVectorDB
from infrastructure.database.pinecone_vector_db import PineconeVectorDB

# Charger les variables d'environnement depuis un fichier .env
load_dotenv()


class TextGeneratorAdapter(TextGeneratorPort):
    def __init__(self, cohere_text_generator: CohereTextGenerator):
        """
        Adaptateur pour connecter le port TextGeneratorPort à l'implémentation CohereTextGenerator.
        :param cohere_text_generator: Instance de CohereTextGenerator.
        """
        self.cohere_text_generator = cohere_text_generator

    def get_generated_text(self, prompt: str) -> str:
        """
        Implémente la méthode du port pour générer du texte.
        :param prompt: Le message utilisateur.
        :return: La réponse générée par Cohere.
        """
        return self.cohere_text_generator.generate_text(prompt=prompt)


class VectorDatabaseAdapter(PersistencePort):
    def __init__(self, vector_db: PineconeVectorDB = None):
        """
        Adaptateur pour connecter l'application à la base de données vectorielle Pinecone.
        :param vector_db: Instance de PineconeVectorDB.
        """
        self.vector_db = vector_db or PineconeVectorDB()  # Utilise une instance par défaut si aucune n'est fournie

    def save_vector(self, vector_id: str, embedding: List[float], metadata: Dict[str, str] = None) -> None:
        """
        Enregistre un vecteur dans Pinecone.
        :param vector_id: Identifiant unique pour le vecteur.
        :param embedding: Liste de flottants représentant l'embedding.
        :param metadata: Métadonnées associées au vecteur (facultatif).
        """
        self.vector_db.upsert_vector(vector_id=vector_id, embedding=embedding, metadata=metadata)

    def delete_vector(self, vector_id: str) -> None:
        """
        Supprime un vecteur de Pinecone.
        :param vector_id: Identifiant unique du vecteur à supprimer.
        """
        self.vector_db.delete_vector(vector_id=vector_id)

    def query_vectors(self, embedding: List[float], top_k: int = 10) -> List[Dict]:
        """
        Recherche les vecteurs les plus proches dans Pinecone.
        :param embedding: Embedding à rechercher.
        :param top_k: Nombre de résultats les plus proches à retourner.
        :return: Liste des résultats de la recherche.
        """
        return self.vector_db.query_vector(embedding=embedding, top_k=top_k)