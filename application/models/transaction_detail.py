from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class TransactionDetail(Base):
    __tablename__ = "transaction_detail"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"), nullable=False)
    transaction_id = Column(Integer, ForeignKey("transactions.id"), nullable=False)
    quantity = Column(Integer, nullable=False)

    movies = relationship("Movies", back_populates="transaction_detail")
    transactions = relationship("Transactions", back_populates="transaction_detail")


# transaction_detail = Table(
#     "transaction_detail",
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
#         "transaction_id",
#         Integer,
#         ForeignKey("transactions.id"),
#         nullable=False
#     ),
#     Column(
#         "quantity",
#         Integer,
#         nullable=False
#     )
# )

meta.create_all(engine)
