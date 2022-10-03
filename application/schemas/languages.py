from pydantic import BaseModel
from typing import Optional

class Languages(BaseModel):
    id: Optional[str]
    name: str