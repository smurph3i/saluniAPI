from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


# echo=True for SQL logging
engine = create_engine(settings.database_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
