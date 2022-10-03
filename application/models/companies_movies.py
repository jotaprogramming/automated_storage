from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class CompaniesMovies(Base):
    __tablename__ = "companies_movies"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    company_id = Column(Integer, ForeignKey("companies.id"), nullable=False)

    movies = relationship("Movies", back_populates="companies_movies")
    companies = relationship("Companies", back_populates="companies_movies")

# companies_movies = Table(
#     "companies_movies",
#     meta,
#     Column(
#         "id",
#         Integer,
#         primary_key=True
#     ),
#     Column(
#         "movies_id",
#         Integer,
#         ForeignKey("movies.id"),
#         nullable=False
#     ),
#     Column(
#         "company_id",
#         Integer,
#         ForeignKey("companies.id"),
#         nullable=False
#     )
# )

meta.create_all(engine)