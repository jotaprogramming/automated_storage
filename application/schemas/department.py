from pydantic import BaseModel
from typing import Optional

class Department(BaseModel):
    id: Optional[str]
    name: str