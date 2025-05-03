from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:demo123@localhost:5433/saluniAPI"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """ Access our database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_table():
    """ Create Table """
    Base.metadata.create_all(bind=engine)
