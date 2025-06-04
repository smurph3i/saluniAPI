import os
import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fastapi.testclient import TestClient

from app.db.base_class import Base
from app.db.deps import get_db
from app.main import app
from app.core.config import settings
from app import models  # this is needed to register the models

# Ensure TESTING=1 is set
os.environ["TESTING"] = "1"

# Create test engine using actual test DB URL
engine = create_engine(settings.actual_database_url)

TestingSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)

# Override the dependency


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

# ✅ Pytest fixture to set up schema and client


@pytest.fixture(scope="session")
def client():
    # Make sure all models are registered
    print("Creating tables in test DB...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    with TestClient(app) as c:
        yield c

    # Optionally clean up
    Base.metadata.drop_all(bind=engine)
