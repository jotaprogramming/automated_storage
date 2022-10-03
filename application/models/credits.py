from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import declarative_base, relationship
from application.config.database import meta, engine, Base


class Credits(Base):
    __tablename__ = "credits"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    actor_id = Column(Integer, ForeignKey("actors.id"), nullable=False)
    department_id = Column(Integer, ForeignKey("department.id"), nullable=True)
    actor_character = Column(String(50), nullable=False)

    movies = relationship("Movies", back_populates="credit")
    department = relationship("Department", back_populates="credit")
    actors = relationship("Actors", back_populates="credit")


# credits = Table(
#     "credits",
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
#         "actor_id",
#         Integer,
#         ForeignKey("actors.id"),
#         nullable=False
#     ),
#     Column(
#         "department_id",
#         Integer,
#         ForeignKey("departments.id"),
#         nullable=False
#     ),
#     Column(
#         "character",
#         String(50),
#         nullable=False
#     ),
# )

meta.create_all(engine)
