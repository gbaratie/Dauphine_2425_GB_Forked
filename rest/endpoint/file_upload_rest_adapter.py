from fastapi import APIRouter, HTTPException, UploadFile, File
from typing import List

# Import des modèles
from rest.model.uploaded_file import UploadedFile
from rest.model.file_processing_status import FileProcessingStatus

# Import du service d'embedding
from rest.setup import create_embedding_service

router = APIRouter()

# Créer une instance du service d'embedding
embedding_service = create_embedding_service()

@router.post("/upload-file", response_model=FileProcessingStatus)
async def upload_file(file: UploadFile = File(...)):
    try:
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