from fastapi import APIRouter, Response, status
from application.config.database import conn
from application.models.companies_movies import CompaniesMovies as db
from application.schemas.companies_movies import CompaniesMovies as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Companies Movies"
router = APIRouter()

@router.get('/companies_movies', response_model=list[Schema], tags=[name_tag])
def get_companies():
    return conn.execute(db.select()).fetchall()

@router.post('/companies_movies', response_model=Schema, tags=[name_tag])
def create_company(body: Schema):
    result = conn.execute(db.insert().values(body.json()))
    return conn.execute(
        body
        .select()
        .where(
            body.c.id == result.lastrowid
        )
    ).first()