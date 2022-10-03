from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Transactions(BaseModel):
    id: Optional[str]
    user_id: int
    create_date: datetime
    expiration_date: datetime
    status: bool