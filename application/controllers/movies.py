from fastapi import APIRouter, Response, status, Depends
from application.config.database import conn, get_db
from fastapi import HTTPException
from application.models.movies import Movies as Table
from application.models.languages import Languages
from application.models.countries import Countries
from application.models.companies import Companies
from application.models.companies_movies import CompaniesMovies
from application.models.movies_categories import MoviesCategories
from application.schemas.movies import Movies as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from application.services.movies import data
from application.services.movie_detail import getMovieDetail
from application.services.videos import getVideo
from sqlalchemy.orm import Session

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Movies"
router = APIRouter()


def verifyData(data):
    if data:
        return data
    return None


@router.get("/movies", tags=[name_tag])
def get_movies(db: Session = Depends(get_db)):
    result = db.query(Table).all()
    return result


@router.get("/api/movies", tags=[name_tag])
def get_movies_api():
    return data


@router.get("/api/movies/{id}", tags=[name_tag])
def get_movies_detail_api(id):
    return getMovieDetail(id)


@router.get("/movies/create", tags=[name_tag])
def create_movie(db: Session = Depends(get_db)):
    results = []
    for i, page in enumerate(data):
        movie = {}
        for j, item in enumerate(page):
            _id = item["id"]
            movie["id"] = _id
            movie["title"] = verifyData(item["title"])

            for genre in item["genre_ids"]:
                data_movies_categories = {
                    "movie_id": _id, 
                    "category_id": genre
                }
                try:
                    movies_cat = MoviesCategories(**data_movies_categories)
                    # db.add(movies_cat)
                    # db.commit()
                    # db.refresh(movies_cat)
                except HTTPException:
                    print("Duplicated")
                    db.rollback()
                    raise
                
            movie["overview"] = verifyData(item["overview"])
            movie["poster_path"] = verifyData(item["poster_path"])
            movie["release_date"] = verifyData(item["release_date"])
            movie["popularity"] = verifyData(item["popularity"])
            movie["vote_average"] = verifyData(item["vote_average"])
            movie["vote_count"] = verifyData(item["vote_count"])
            movie["adult"] = verifyData(item["adult"])

            detail = getMovieDetail(_id)
            if (
                detail != 0
                and "spoken_languages" in detail
                and len(detail["spoken_languages"]) > 0
            ):
                name = detail["spoken_languages"][0]["name"]
                language_query = db.query(Languages.id).filter(Languages.name == name).all()
                if not language_query:
                    data_language = {"name" : name}
                    language = Languages(**data_language)
                    db.add(language)
                    db.commit()
                    db.refresh(language)
                language_query = db.query(Languages.id).filter(Languages.name == name).all()
                movie["language_id"] = int(language_query[0][0])

            if detail != 0 and "runtime" in detail:
                movie["runtime"] = detail["runtime"]

            video = getVideo(_id)
            if video != 0 and "key" in video:
                movie["video_key"] = video["key"]

            # body = Table(**movie)
            # db.add(body)
            # db.commit()
            # db.refresh(body)
            results.append(movie)
    return results
