from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.db.session import SessionLocal
from app.models.user import User

client = TestClient(app)


def test_user_registration():
    test_email = "testuser@example.com"

    # Clean up any pre-existing test user
    db = SessionLocal()
    user = db.query(User).filter(User.email == test_email).first()
    if user:
        db.delete(user)
        db.commit()
    db.close()

    payload = {
        "email": test_email,
        "password": "strongpassword123",
        "full_name": "Test User"
    }

    response = client.post("/api/v1/users/register", json=payload)
    assert response.status_code == 201
