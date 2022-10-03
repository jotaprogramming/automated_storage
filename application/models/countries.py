from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class Countries(Base):
    __tablename__ = "countries"
    id = Column(Integer, primary_key=True)
    name = Column(String(40), nullable=False)
    iso = Column(String(5), nullable=True)

    companies = relationship("Companies", back_populates="countries")
    releases = relationship("Releases", back_populates="countries")


# countries = Table(
#     "countries",
#     meta,
#     Column(
#         "id",
#         Integer,
#         primary_key=True
#     ),
#     Column(
#         "name",
#         String(40),
#         nullable=False
#     )
# )

meta.create_all(engine)
