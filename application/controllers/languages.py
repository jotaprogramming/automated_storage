from fastapi import APIRouter, Response, status
from application.config.database import conn
from application.models.languages import Languages as db
from application.schemas.languages import Languages as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Languages"
router = APIRouter()

@router.get('/languages', response_model=list[Schema], tags=[name_tag])
def get_languages():
    return conn.execute(db.select()).fetchall()

@router.post('/languages', response_model=Schema, tags=[name_tag])
def create_language(body: Schema):
    result = conn.execute(db.insert().values(body.json()))
    return conn.execute(
        body
        .select()
        .where(
            body.c.id == result.lastrowid
        )
    ).first()