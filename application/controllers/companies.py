from fastapi import APIRouter, Response, status, Depends
from application.config.database import conn, get_db
from application.models.companies import Companies
from application.schemas.companies import Companies as Schema
from cryptography.fernet import Fernet
from starlette.status import HTTP_204_NO_CONTENT
from application.models.countries import Countries
from application.models.releases import Releases
from application.models.companies_movies import CompaniesMovies
from application.services.movies import data
from application.services.movie_detail import getMovieDetail
from sqlalchemy.orm import Session

key = Fernet.generate_key()
f = Fernet(key)

name_tag = "Companies"
router = APIRouter()

@router.get('/companies', response_model=list[Schema], tags=[name_tag])
def get_companiesies():
    return conn.execute(db.select()).fetchall()

@router.get('/api/companies', response_model=list[Schema], tags=[name_tag])
def get_companiesies_api():
    return conn.execute(db.select()).fetchall()

@router.get('/companies/create', tags=[name_tag])
def create_companies(db: Session = Depends(get_db)):
    for i, page in enumerate(data):
        companies = []
        countries = []
        for j, item in enumerate(page):
            _id = item["id"]
            detail = getMovieDetail(_id)
            if (
                detail != 0
                and "production_countries" in detail
                and len(detail["production_countries"]) > 0
            ):
                for country in detail["production_countries"]:
                    name_country = country["name"]
                    iso_country = country["iso_3166_1"]
                    print(name_country, iso_country)
                    countries_query = db.query(Countries.id).filter(Countries.name == name_country).all()
                    if not countries_query:
                        data_countries = {"name" : country["name"], "iso": iso_country}
                        country = Countries(**data_countries)
                        db.add(country)
                        db.commit()
                        db.refresh(country)
                    countries_query = db.query(Countries.id).filter(Countries.name == name_country).all()
                    country_id = int(countries_query[0][0])
                    # countries["country_id"] = country_id
            if (
                detail != 0
                and "production_companies" in detail
                and len(detail["production_companies"]) > 0
            ):
                for company in detail["production_companies"]:
                    name_country = company["name"]
                    origin_country = company["origin_country"]
                    print(name_country, origin_country)
                    companies_query = db.query(Companies.id).filter(Companies.name == name_country).all()
                    countries_query = db.query(Countries.id).filter(Countries.iso == origin_country).all()
                    print(countries_query)
                    if not companies_query:
                        if countries_query and len(countries_query) > 0:
                            country_id = int(countries_query[0][0])
                            data_company = {"name" : company["name"], "country_id": country_id}
                        else:
                            data_company = {"name" : company["name"]}
                        company = Companies(**data_company)
                        db.add(company)
                        db.commit()
                        db.refresh(company)
                    companies_query = db.query(Companies.id).filter(Companies.name == name_country).all()
                    company_id = int(companies_query[0][0])
                    data_companies_movies = {"movie_id": _id, "company_id" : company_id}
                    print(data_companies_movies)
                    # companies_movies = CompaniesMovies(**data_companies_movies)
                    # db.add(companies_movies)
                    # db.commit()
                    # db.refresh(companies_movies)
                    companies.append(data_companies_movies)
    return companies