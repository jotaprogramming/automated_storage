from fastapi import APIRouter, Response, status
from application.config.database import conn
from application.models.transaction_detail import TransactionDetail as db
from application.schemas.transaction_detail import TransactionDetail as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Transaction Detail"
router = APIRouter()

@router.get('/transaction_detail', response_model=list[Schema], tags=[name_tag])
def get_transaction_detail():
    return conn.execute(db.select()).fetchall()

@router.post('/transaction_detail', response_model=Schema, tags=[name_tag])
def create_transaction_detail(body: Schema):
    result = conn.execute(db.insert().values(body.json()))
    return conn.execute(
        body
        .select()
        .where(
            body.c.id == result.lastrowid
        )
    ).first()