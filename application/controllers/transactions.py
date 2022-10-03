from fastapi import APIRouter, Response, status
from application.config.database import conn
from application.models.transactions import Transactions as db
from application.schemas.transactions import Transactions as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Transactions"
router = APIRouter()

@router.get('/transactions', response_model=list[Schema], tags=[name_tag])
def get_transactions():
    return conn.execute(db.select()).fetchall()

@router.post('/transactions', response_model=Schema, tags=[name_tag])
def create_transaction(body: Schema):
    result = conn.execute(db.insert().values(body.json()))
    return conn.execute(
        body
        .select()
        .where(
            body.c.id == result.lastrowid
        )
    ).first()