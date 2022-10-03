from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

engine = create_engine("mysql+pymysql://root:@localhost:3306/coexbuster_py")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

meta = MetaData(engine)

conn = engine.connect()

Base = declarative_base()