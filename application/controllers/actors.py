from fastapi import APIRouter, Response, status, Depends
from application.config.database import conn, get_db
from application.models.actors import Actors as Table
from application.schemas.actors import Actors as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session
from sqlalchemy import select

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Actors"
router = APIRouter()

@router.get('/actors', tags=[name_tag])
def get_actors(db: Session = Depends(get_db)):
    
    statement = select(Table)
    result = db.execute(statement).all()
    return result

@router.post('/actors', response_model=Schema, tags=[name_tag])
def create_actor(body: Schema, db: Session = Depends(get_db)):
    # db_table = Table(**body.dict())
    # db.add(db_table)
    # db.commit()
    # db.refresh(db_table)
    # return ParentSchema.from_orm(db_table)
    result = conn.execute(db.insert().values(body.json()))
    return conn.execute(
        body
        .select()
        .where(
            body.c.id == result.lastrowid
        )
    ).first()