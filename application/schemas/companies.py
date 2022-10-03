from pydantic import BaseModel
from typing import Optional

class Companies(BaseModel):
    id: Optional[str]
    name: str
    country_id: Optional[int]