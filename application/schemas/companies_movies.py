# from dataclasses import Field
from pydantic import BaseModel
from typing import Optional

class CompaniesMovies(BaseModel):
    id: Optional[str]
    movie_id: int
    company_id: int