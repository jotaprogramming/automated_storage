from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class Certification(Base):
    __tablename__ = "certification"
    id = Column(Integer, primary_key=True)
    type_of = Column(String(15), nullable=True)

    releases = relationship("Releases", back_populates="certification")


# certification = Table(
#     "certification",
#     meta,
#     Column(
#         "id",
#         Integer,
#         primary_key=True
#     ),
#     Column(
#         "type_of",
#         String(15),
#         nullable=True
#     )
# )

meta.create_all(engine)
