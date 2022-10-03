from pydantic import BaseModel
from typing import Optional

class MoviesCategories(BaseModel):
    id: Optional[str]
    movie_id: int
    category_id: int