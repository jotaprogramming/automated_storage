from pydantic import BaseModel
from typing import Optional
from datetime import date

class Releases(BaseModel):
    id: Optional[str]
    movie_id: int
    country_id: Optional[int]
    certification_id: Optional[int]
    release_date: Optional[date]