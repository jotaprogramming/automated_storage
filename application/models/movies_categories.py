from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class MoviesCategories(Base):
    __tablename__ = "movies_categories"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)

    movies = relationship("Movies", back_populates="movies_categories")
    categories = relationship("Categories", back_populates="movies_categories")


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
#         "category_id",
#         Integer,
#         ForeignKey("categories.id"),
#         nullable=False
#     )
# )

meta.create_all(engine)
