from abc import ABC, abstractmethod
from typing import List, Dict

class PersistencePort(ABC):
    @abstractmethod
    def save_vector(self, vector_id: str, embedding: List[float], metadata: Dict[str, str] = None) -> None:
        """
        Sauvegarde un embedding dans une base de données ou un service externe.
        :param vector_id: L'identifiant du vecteur.
        :param embedding: La liste des valeurs du vecteur.
        :param metadata: Les métadonnées associées au vecteur.
        """
        pass

    @abstractmethod
    def query_vector(self, embedding: List[float], top_k: int = 10) -> List[Dict]:
        """
        Interroge la base de données vectorielle pour trouver les vecteurs les plus proches.
        :param embedding: La liste des valeurs du vecteur à interroger.
        :param top_k: Le nombre de résultats à retourner.
        :return: Une liste de dictionnaires contenant les vecteurs correspondants.
        """
        pass

    @abstractmethod
    def delete_vector(self, vector_id: str) -> None:
        """
        Supprime un vecteur de la base de données vectorielle.
        :param vector_id: L'identifiant du vecteur à supprimer.
        """
        pass