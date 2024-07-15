from pydantic import BaseModel, Field
from typing import Optional
from uuid import uuid4


class TextRecord(BaseModel):
    """
    Represents a text record in the database.

    Attributes:
        id (Optional[str]): The unique identifier of the text record.
        text (str): The text content.
        summary (Optional[str]): The summary of the text.
        keywords (Optional[list]): The list of keywords extracted from the text.
        sentiment (Optional[str]): The sentiment analysis result of the text.
    """
    id: Optional[str] = Field(default_factory=lambda: str(uuid4()), alias='_id')
    text: str
    summary: Optional[str] = None
    keywords: Optional[list] = None
    sentiment: Optional[float] = None
