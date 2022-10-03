from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Users(BaseModel):
    id: Optional[str]
    email: str
    name: str
    password: str