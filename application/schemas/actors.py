from pydantic import BaseModel
from typing import Optional

class Actors(BaseModel):
    id: Optional[str]
    name: str
    profile_path: Optional[str]

    class Config:
        orm_mode = True