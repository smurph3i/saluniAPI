from sqlalchemy import Column, Integer, String
from app.db.base import Base


class User(Base):
    __tablename__ = 'users'  # The name of the table in the database

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    full_name = Column(String, index=True)
