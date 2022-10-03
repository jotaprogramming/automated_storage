from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class Languages(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    movies = relationship("Movies", back_populates="languages")

# languages = Table(
#     "languages",
#     meta,
#     Column(
#         "id",
#         Integer,
#         primary_key=True
#     ),
#     Column(
#         "name",
#         String(50),
#         nullable=False
#     )
# )

meta.create_all(engine)