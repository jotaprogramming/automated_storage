from fastapi import APIRouter, Response, status
from application.config.database import conn
from application.models.department import Department as db
from application.schemas.department import Department as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Deparment"
router = APIRouter()

@router.get('/deparment', response_model=list[Schema], tags=[name_tag])
def get_deparments():
    return conn.execute(db.select()).fetchall()

@router.post('/deparment', response_model=Schema, tags=[name_tag])
def create_deparment(body: Schema):
    result = conn.execute(db.insert().values(body.json()))
    return conn.execute(
        body
        .select()
        .where(
            body.c.id == result.lastrowid
        )
    ).first()