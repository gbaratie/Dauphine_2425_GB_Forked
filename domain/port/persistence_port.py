from abc import ABC, abstractmethod
from domain.model.file_embedded import FileEmbedded

class PersistencePort(ABC):
    @abstractmethod
    def save_vector(self, file_embedded: FileEmbedded) -> None:
        """
        Sauvegarde un embedding dans une base de données ou un service externe.
        :param file_embedded: L'objet contenant le fichier et son embedding.
        """
        pass