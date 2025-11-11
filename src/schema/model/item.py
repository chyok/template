from pydantic import BaseModel, ConfigDict
from typing import Optional


class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    model_config = ConfigDict(from_attributes=True)
