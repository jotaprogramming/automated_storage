from multiprocessing.sharedctypes import Array
from fastapi import APIRouter, Response, status, Depends
from application.config.database import conn, get_db
from application.models.releases import Releases
from application.models.certification import Certification
from application.models.countries import Countries
from application.schemas.releases import Releases as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from application.services.movies import data
from application.services.movie_detail import getMovieDetail
from sqlalchemy.orm import Session

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Releases"
router = APIRouter()


@router.get("/releases", tags=[name_tag])
def get_releases(db: Session = Depends(get_db)):
    result = db.query(Releases).all()
    return result

@router.get("/releases/create", tags=[name_tag])
def create_release(db: Session = Depends(get_db)):
    results = []
    for page in data:
        for item in page:
            _id = item["id"]
            detail = getMovieDetail(_id)
            if detail != 0 and "releases" in detail and len(detail["releases"]) > 0:
                releases = detail["releases"]
                for release in releases["countries"]:
                    if type(release) is dict:
                        certification = release["certification"]
                        iso = release["iso_3166_1"]
                        certification_query = (
                            db.query(Certification.id)
                            .filter(Certification.type_of == certification)
                            .all()
                        )

                        if not certification_query and certification != "":
                            data_iso = {"type_of": certification}
                            res_certification = Certification(**data_iso)
                            db.add(res_certification)
                            db.commit()
                            db.refresh(res_certification)
                        certification_query = (
                            db.query(Certification.id)
                            .filter(Certification.type_of == certification)
                            .all()
                        )

                        if (
                            type(certification_query) is list
                            and len(certification_query) > 0
                        ):
                            if certification_query[0][0]:
                                certification_id = int(certification_query[0][0])
                                release_date = release["release_date"]
                                country_query = (
                                    db.query(Countries.id)
                                    .filter(Countries.iso == iso)
                                    .all()
                                )
                                if (
                                    type(country_query) is list
                                    and len(country_query) > 0
                                    and country_query[0][0]
                                ):
                                    country_id = int(country_query[0][0])
                                    data_release = {
                                        "movie_id": _id,
                                        "country_id": country_id,
                                        "certification_id": certification_id,
                                        "release_date": release_date,
                                    }
                                else:
                                    data_release = {
                                        "movie_id": _id,
                                        "certification_id": certification_id,
                                        "release_date": release_date,
                                    }
                                res_release = Releases(**data_release)
                                db.add(res_release)
                                db.commit()
                                db.refresh(res_release)
                                results.append(data_release)
    return results
