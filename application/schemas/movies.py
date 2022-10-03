from pydantic import BaseModel
from typing import Optional
from datetime import date

class Movies(BaseModel):
    id: Optional[str]
    title: str
    overview: Optional[str]
    poster_path: Optional[str]
    release_date: date
    popularity: Optional[float]
    vote_average: Optional[float]
    vote_count: Optional[int]
    adult: Optional[bool]
    language_id: Optional[int]
    runtime: Optional[int]
    video_key: Optional[str]