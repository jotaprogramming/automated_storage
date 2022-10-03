from pydantic import BaseModel
from typing import Optional

class Certification(BaseModel):
    id: Optional[str]
    type_of: str