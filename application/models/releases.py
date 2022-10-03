from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, Date
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class Releases(Base):
    __tablename__ = "releases"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    country_id = Column(Integer, ForeignKey("countries.id"), nullable=True)
    certification_id = Column(Integer, ForeignKey("certification.id"), nullable=True)
    release_date = Column(Date, nullable=True)

    movies = relationship("Movies", back_populates="releases")
    countries = relationship("Countries", back_populates="releases")
    certification = relationship("Certification", back_populates="releases")

# releases = Table(
#     "releases",
#     meta,
#     Column(
#         "id",
#         Integer,
#         primary_key=True
#     ),
#     Column(
#         "movie_id",
#         Integer,
#         ForeignKey("movies.id"),
#         nullable=False
#     ),
#     Column(
#         "country_id",
#         Integer,
#         ForeignKey("countries.id"),
#         nullable=False
#     ),
#     Column(
#         "certification_id",
#         Integer,
#         ForeignKey("certifications.id"),
#         nullable=True
#     ),
#     Column(
#         "releases_date",
#         Date,
#         nullable=True
#     )
# )

meta.create_all(engine)