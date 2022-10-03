from fastapi import APIRouter, Response, status, Depends
from application.config.database import conn, get_db
from application.models.categories import Categories as Table
from application.schemas.categories import Categories as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from application.services.categories import data
from sqlalchemy.orm import Session

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Categories"
router = APIRouter()

@router.get('/categories', tags=[name_tag])
def get_categories(db: Session = Depends(get_db)):
    result = db.query(Table).all()
    return result

@router.get('/categories/api', tags=[name_tag])
def get_categories_api():
    return data

@router.get('/categories/create', tags=[name_tag])
def create_category(db: Session = Depends(get_db)):
    for item in data:
        body = Table(**item)
        db.add(body)
        db.commit()
        db.refresh(body)
    return data