from pydantic import BaseModel
from typing import Optional

class Categories(BaseModel):
    id: Optional[str]
    name: str