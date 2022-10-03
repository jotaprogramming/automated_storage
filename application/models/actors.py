from sqlalchemy import Table, Column
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql.sqltypes import Integer, String


class Actors(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    profile_path = Column(String(100), nullable=True)

    credit = relationship("Credits", back_populates="actors")


# actors = Table(
#     "actors",
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
#         "profile_path",
#         String(100),
#         nullable=False
#     )
# )
