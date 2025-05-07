import os
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient

from app.db.base_class import Base
from app.db.session import engine
from app.main import app
from app.db.deps import get_db
from app.core.config import settings

from app import models  # 👈 This registers all models with Base


# Set the TESTING environment variable
os.environ["TESTING"] = "1"

# Create engine and session using the test database URL
engine = create_engine(settings.actual_database_url, connect_args={
                       "check_same_thread": False} if "sqlite" in settings.actual_database_url else {})
TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# Override the get_db dependency


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# Pytest fixture for test client


@pytest.fixture(scope="module")
def client():
    # Recreate the test DB schema
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with TestClient(app) as c:
        yield c

    # Optionally clean up again after tests
    Base.metadata.drop_all(bind=engine)
