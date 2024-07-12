from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4


class TabularRecord(BaseModel):
    """
    TabularRecord model representing the structure of a record in the tabular data.
    """
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), alias='_id')
    name: str
    value: float
