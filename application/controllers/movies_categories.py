from fastapi import APIRouter, Response, status
from application.config.database import conn
from application.models.movies_categories import MoviesCategories as db
from application.schemas.movies_categories import MoviesCategories as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Movies Categories"
router = APIRouter()

@router.get('/movies_categories', response_model=list[Schema], tags=[name_tag])
def get_movies_categories():
    return conn.execute(db.select()).fetchall()

@router.post('/movies_categories', response_model=Schema, tags=[name_tag])
def create_movies_categories(body: Schema):
    result = conn.execute(db.insert().values(body.json()))
    return conn.execute(
        body
        .select()
        .where(
            body.c.id == result.lastrowid
        )
    ).first()