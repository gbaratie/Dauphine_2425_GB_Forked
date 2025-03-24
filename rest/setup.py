from domain.adapter.generator_controller_adapter import GeneratorControllerAdapter
from domain.service.text_generation_service import TextGenerationService
from domain.service.system_prompt_service import SystemPromptService 
from domain.service.chat_history_service import ChatHistoryService  
from domain.service.embedding_service import EmbeddingService

from infrastructure.adapter.text_generator_adapter import TextGeneratorAdapter, VectorDatabaseAdapter
from infrastructure.text_generator.cohere_text_generator import CohereTextGenerator
from infrastructure.adapter.embedding_adapter import EmbeddingAdapter
from infrastructure.embedding.cohere_embedding_generator import CohereEmbeddingGenerator
from infrastructure.database.pinecone_vector_db import PineconeVectorDB

from rest.endpoint.generator_rest_adapter import GeneratorRestAdapter
from rest.endpoint.file_upload_rest_adapter import FileUploadRestAdapter

def create_generator_rest_adapter():
    # Initialiser les services
    system_prompt_service = SystemPromptService()
    chat_history_service = ChatHistoryService()

    # Initialiser le générateur Cohere avec le service de prompt
    cohere_text_generator = CohereTextGenerator(system_prompt_service, chat_history_service)
    cohere_embedding_generator = CohereEmbeddingGenerator()
    pinecone_vector_db = PineconeVectorDB()

    # Injecter CohereTextGenerator dans TextGeneratorAdapter
    text_generator_adapter = TextGeneratorAdapter(cohere_text_generator=cohere_text_generator)
    embedding_adapter = EmbeddingAdapter(cohere_embedding_generator=cohere_embedding_generator)
  # Créer une instance de PineconeVectorDB
    persistence_adapter = VectorDatabaseAdapter(pinecone_vector_db)

    # Configurer les services et adaptateurs
    text_generation_service = TextGenerationService(text_generator_adapter, embedding_adapter, persistence_adapter)
    generator_controller_adapter = GeneratorControllerAdapter(text_generation_service)
    return GeneratorRestAdapter(generator_controller_adapter)

def create_embedding_service():
    cohere_embedding_generator = CohereEmbeddingGenerator()
    embedding_adapter = EmbeddingAdapter(cohere_embedding_generator)
    pinecone_vector_db = PineconeVectorDB()  # Créer une instance de PineconeVectorDB
    persistence_adapter = VectorDatabaseAdapter(pinecone_vector_db)  # Créer une instance de VectorDatabaseAdapter
    return EmbeddingService(embedding_adapter, persistence_adapter)  # Passer les deux adaptateurs au constructeur

def create_file_upload_rest_adapter():
    # Créez et configurez l'adaptateur pour l'upload de fichiers ici
    return FileUploadRestAdapter()
