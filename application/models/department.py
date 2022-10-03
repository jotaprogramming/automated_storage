from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from sqlalchemy.orm import declarative_base, relationship
from application.config.database import meta, engine, Base


class Department(Base):
    __tablename__ = "department"
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False)

    credit = relationship("Credits", back_populates="department")


# department = Table(
#     "department",
#     meta,
#     Column(
#         "id",
#         Integer,
#         primary_key=True
#     ),
#     Column(
#         "name",
#         String(25),
#         nullable=False
#     )
# )

meta.create_all(engine)
