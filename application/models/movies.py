from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, String, Float, Date, Boolean
from sqlalchemy.orm import declarative_base, relationship
from application.config.database import meta, engine, Base

class Movies(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    overview = Column(String(250), nullable=True)
    poster_path = Column(String(100), nullable=True)
    release_date = Column(Date, nullable=True)
    popularity = Column(Float, nullable=True)
    vote_average = Column(Float, nullable=True)
    vote_count = Column(Integer, nullable=True)
    adult = Column(Boolean, nullable=True)
    language_id = Column(Integer, ForeignKey("languages.id"), nullable=True)
    runtime = Column(Integer, nullable=True)
    video_key = Column(String(50), nullable=True)

    credit = relationship("Credits", back_populates="movies")
    movies_categories = relationship("MoviesCategories", back_populates="movies")
    companies_movies = relationship("CompaniesMovies", back_populates="movies")
    releases = relationship("Releases", back_populates="movies")
    transaction_detail = relationship("TransactionDetail", back_populates="movies")
    languages = relationship("Languages", back_populates="movies")


# movies = Table(
#     "movies",
#     meta,
#     Column(
#         "id",
#         Integer,
#         primary_key=True
#     ),
#     Column(
#         "title",
#         String(100),
#         nullable=False
#     ),
#     Column(
#         "overview",
#         String(250),
#         nullable=True
#     ),
#     Column(
#         "poster_path",
#         String(100),
#         nullable=True
#     ),
#     Column(
#         "release_date",
#         Date,
#         nullable=True
#     ),
#     Column(
#         "popularity",
#         Float,
#         nullable=True
#     ),
#     Column(
#         "vote_average",
#         Float,
#         nullable=True
#     ),
#     Column(
#         "vote_count",
#         Integer,
#         nullable=True
#     ),
#     Column(
#         "adult",
#         Boolean,
#         nullable=True
#     ),
#     Column(
#         "language_id",
#         Integer,
#         ForeignKey("languages.id"),
#         nullable=True
#     ),
#     Column(
#         "runtime",
#         Integer,
#         nullable=True
#     ),
#     Column(
#         "video_key",
#         String(50),
#         nullable=True
#     )
# )

meta.create_all(engine)
