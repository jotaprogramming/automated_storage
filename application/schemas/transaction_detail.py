from pydantic import BaseModel
from typing import Optional

class TransactionDetail(BaseModel):
    id: Optional[str]
    movie_id: int
    transaction_id: int
    quantity: int