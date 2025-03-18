from pydantic import BaseModel
from typing import Optional

class FileProcessingStatus(BaseModel):
    status: str
    message: Optional[str] = None