from abc import ABC, abstractmethod

class TextGeneratorPort(ABC):
    @abstractmethod
    def get_generated_text(self, prompt: str, is_rag: bool = False) -> str:
        pass