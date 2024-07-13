from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4


class ImageRecord(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), alias='_id')
    filename: str
    path: str
