from pydantic import BaseModel, Field
from typing import Optional

class TabularRecord(BaseModel):
    id: Optional[str] = Field(None, alias='_id')
    name: str
    value: float
