from fastapi import APIRouter, Response, status
from application.config.database import conn
from application.models.users import Users as db
from application.schemas.users import Users as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Users"
router = APIRouter()

@router.get('/users', response_model=list[Schema], tags=[name_tag])
def get_users():
    return conn.execute(db.select()).fetchall()

@router.post('/users', response_model=Schema, tags=[name_tag])
def create_user(body: Schema):
    result = conn.execute(db.insert().values(body.json()))
    return conn.execute(
        body
        .select()
        .where(
            body.c.id == result.lastrowid
        )
    ).first()