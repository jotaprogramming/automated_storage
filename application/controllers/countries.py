from fastapi import APIRouter, Response, status
from application.config.database import conn
from application.models.countries import Countries as db
from application.schemas.countries import Countries as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Countries"
router = APIRouter()

@router.get('/countries', response_model=list[Schema], tags=[name_tag])
def get_countries():
    return conn.execute(db.select()).fetchall()

@router.post('/countries', response_model=Schema, tags=[name_tag])
def create_country(body: Schema):
    result = conn.execute(db.insert().values(body.json()))
    return conn.execute(
        body
        .select()
        .where(
            body.c.id == result.lastrowid
        )
    ).first()