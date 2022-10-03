from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class Companies(Base):
    __tablename__ = "companies"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=True)

    companies_movies = relationship("CompaniesMovies", back_populates="companies")
    countries = relationship("Countries", back_populates="companies")


# companies = Table(
#     "companies",
#     meta,
#     Column(
#         "id",
#         Integer,
#         primary_key=True
#     ),
#     Column(
#         "name",
#         String(100),
#         nullable=False
#     ),
#     Column(
#         "country_id",
#         Integer,
#         ForeignKey("countries.id"),
#         nullable=False
#     )
# )

meta.create_all(engine)
