from pydantic import BaseModel

class UploadedFile(BaseModel):
    filename: str
    content_type: str
    size: int
    content: bytes