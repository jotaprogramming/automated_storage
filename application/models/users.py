from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    password = Column(String(100), nullable=False)

    transactions = relationship("Transactions", back_populates="users")


# users = Table(
#     "users",
#     meta,
#     Column(
#         "id",
#         Integer,
#         primary_key=True
#     ),
#     Column(
#         "email",
#         String(50),
#         nullable=False
#     ),
#     Column(
#         "name",
#         String(50),
#         nullable=False
#     ),
#     Column(
#         "password",
#         String(100),
#         nullable=False
#     )
# )

meta.create_all(engine)
