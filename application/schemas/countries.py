from pydantic import BaseModel
from typing import Optional

class Countries(BaseModel):
    id: Optional[str]
    name: str
    iso: Optional[str]