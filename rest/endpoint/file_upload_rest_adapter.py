from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List

# Import des modèles
from rest.model.uploaded_file import UploadedFile
from rest.model.file_processing_status import FileProcessingStatus

class FileUploadRestAdapter:
    def __init__(self):
        pass

    async def upload_file(self, file: UploadFile = File(...)) -> FileProcessingStatus:
        try:
            # Importer le service d'embedding ici pour éviter l'importation circulaire
            from rest.setup import create_embedding_service
            
            # Créer une instance du service d'embedding
            embedding_service = create_embedding_service()
            
            # Lire le contenu du fichier
            content = await file.read()
            
            # Créer une instance de UploadedFile
            uploaded_file = UploadedFile(
                filename=file.filename,
                content_type=file.content_type,
                size=len(content),
                content=content
            )
            
            # Appeler le service d'embedding
            embedded_file = embedding_service.embed_file(uploaded_file)
            
            # Retourner un statut de succès avec l'embedding
            return FileProcessingStatus(
                status="success",
                message=f"File {uploaded_file.filename} uploaded and embedded successfully.",
                embedding=embedded_file.embedding
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_router(self) -> APIRouter:
        """
        Configure et retourne un routeur FastAPI.
        """
        router = APIRouter()  # Crée un routeur
        router.post("/upload-file")(self.upload_file)  # Associe /upload-file à la méthode upload_file
        return router  # Retourne le routeur