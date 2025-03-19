from fastapi import FastAPI

from rest.setup import create_generator_rest_adapter, create_embedding_service, create_file_upload_rest_adapter

from rest.endpoint.root import router as root_router

rest_api = FastAPI()

# Inclusion du routeur racine
rest_api.include_router(root_router)

# Inclusion du routeur pour le générateur
generator_rest_adapter = create_generator_rest_adapter()
rest_api.include_router(generator_rest_adapter.get_router())

# Inclusion du routeur pour l'upload de fichiers
file_upload_rest_adapter = create_file_upload_rest_adapter()
rest_api.include_router(file_upload_rest_adapter.get_router(), prefix="/files", tags=["File Upload"])

# Initialisation du service d'embedding
embedding_service = create_embedding_service()
# Vous pouvez maintenant utiliser embedding_service dans votre application

