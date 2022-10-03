from sqlalchemy import Table, Column, ForeignKey
from sqlalchemy.sql.sqltypes import Integer, DateTime, Boolean
from application.config.database import meta, engine, Base
from sqlalchemy.orm import declarative_base, relationship


class Transactions(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    create_date = Column(DateTime, nullable=False)
    expiration_date = Column(DateTime, nullable=False)
    status = Column(Boolean, nullable=True)

    transaction_detail = relationship(
        "TransactionDetail", back_populates="transactions"
    )
    users = relationship("Users", back_populates="transactions")


meta.create_all(engine)
