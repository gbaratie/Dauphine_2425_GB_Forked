from domain.adapter.generator_controller_adapter import GeneratorControllerAdapter
from domain.service.text_generation_service import TextGenerationService
from domain.service.system_prompt_service import SystemPromptService 
from domain.service.chat_history_service import ChatHistoryService  
from domain.service.embedding_service import EmbeddingService # Nouveau service

from infrastructure.adapter.text_generator_adapter import TextGeneratorAdapter
from infrastructure.text_generator.cohere_text_generator import CohereTextGenerator  # Import du générateur Cohere
from infrastructure.adapter.embedding_adapter import EmbeddingAdapter
from infrastructure.embedding.cohere_embedding_generator import CohereEmbeddingGenerator

from rest.endpoint.generator_rest_adapter import GeneratorRestAdapter

def create_generator_rest_adapter():
    # Initialiser les services
    system_prompt_service = SystemPromptService()
    chat_history_service = ChatHistoryService()

    # Initialiser le générateur Cohere avec le service de prompt
    cohere_text_generator = CohereTextGenerator(system_prompt_service, chat_history_service)

    # Injecter CohereTextGenerator dans TextGeneratorAdapter
    text_generator_adapter = TextGeneratorAdapter(cohere_text_generator=cohere_text_generator)

    # Configurer les services et adaptateurs
    text_generation_service = TextGenerationService(text_generator_adapter)
    generator_controller_adapter = GeneratorControllerAdapter(text_generation_service)
    return GeneratorRestAdapter(generator_controller_adapter)


def create_embedding_service():
    cohere_embedding_generator = CohereEmbeddingGenerator()
    embedding_adapter = EmbeddingAdapter(cohere_embedding_generator)
    return EmbeddingService(embedding_adapter)
