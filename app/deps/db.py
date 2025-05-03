from typing import Generator
from app.db.session import SessionLocal


def get_db() -> Generator:
    """ Access our database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
