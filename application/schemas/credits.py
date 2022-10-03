from pydantic import BaseModel
from typing import Optional

class Credits(BaseModel):
    id: Optional[str]
    movie_id: int
    actor_id: int
    department_id: Optional[int]
    actor_character: str