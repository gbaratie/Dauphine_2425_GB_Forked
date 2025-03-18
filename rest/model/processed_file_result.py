from pydantic import BaseModel
from typing import Dict


#Il faudra peut-être le supprimer car ce document n'est pas utilisé dans le front

class ProcessedFileResult(BaseModel):
    result: Dict[str, str]  # Par exemple, un dictionnaire contenant des détails sur le traitement