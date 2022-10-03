from fastapi import APIRouter, Response, status, Depends
from application.config.database import conn, get_db
from application.models.credits import Credits
from application.models.department import Department
from application.models.actors import Actors
from application.schemas.credits import Credits as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from application.services.movies import data
from application.services.credits import getCast
from application.services.movie_detail import getMovieDetail
from application.services.videos import getVideo
from sqlalchemy.orm import Session

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Credits"
router = APIRouter()


@router.get("/credits", tags=[name_tag])
def get_credists(db: Session = Depends(get_db)):
    result = db.query(Credits).all()
    return result


@router.get("/api/credits/{id}", tags=[name_tag])
def get_credit_api(id):
    return getCast(id)


@router.get("/credits/create", tags=[name_tag])
def create_credit(db: Session = Depends(get_db)):
    results = []
    for page in data:
        movie = {}
        for item in page:
            _id = item["id"]
            print(_id)
            casting = getCast(_id)
            for cast in casting:
                name_department = cast["known_for_department"]
                department_query = (
                    db.query(Department.id)
                    .filter(Department.name == name_department)
                    .all()
                )
                if not department_query:
                    data_department = {"name": name_department}
                    department = Department(**data_department)
                    db.add(department)
                    db.commit()
                    db.refresh(department)
                department_query = (
                    db.query(Department.id)
                    .filter(Department.name == name_department)
                    .all()
                )
                department_id = int(department_query[0][0])
                # print(department_id)

                name_actor = cast["name"]
                actor_query = (
                    db.query(Actors.id).filter(Actors.name == name_actor).all()
                )
                if not actor_query:
                    profile_path = cast["profile_path"]
                    data_actor = {"name": name_actor, "profile_path": profile_path}
                    actors = Actors(**data_actor)
                    db.add(actors)
                    db.commit()
                    db.refresh(actors)
                actor_query = (
                    db.query(Actors.id).filter(Actors.name == name_actor).all()
                )
                actor_id = int(actor_query[0][0])
                # print(actor_id)

                character = cast["character"]
                data_credits = {
                    "movie_id": _id,
                    "actor_id": actor_id,
                    "department_id": department_id,
                    "actor_character": character,
                }
                credit = Credits(**data_credits)
                db.add(credit)
                db.commit()
                db.refresh(credit)
                results.append(data_credits)
                # print(actor_id)
    return results
