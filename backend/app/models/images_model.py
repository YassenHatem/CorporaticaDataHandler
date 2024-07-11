from pydantic import BaseModel, Field
from typing import Optional

class ImageRecord(BaseModel):
    id: Optional[str] = Field(None, alias='_id')
    filename: str
    path: str
