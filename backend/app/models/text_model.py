from pydantic import BaseModel, Field
from typing import Optional

class TextRecord(BaseModel):
    id: Optional[str] = Field(None, alias='_id')
    text: str
    summary: Optional[str]
    keywords: Optional[list]
    sentiment: Optional[dict]
