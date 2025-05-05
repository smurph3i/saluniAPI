from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from app.main import app
from app.db.session import SessionLocal
from app.models.user import User

client = TestClient(app)


def test_user_registration():
    test_email = "testuser@example.com"
    payload = {
        "email": test_email,
        "password": "strongpassword123",
        "full_name": "Test User"
    }

    # Create test user
    response = client.post("/users/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == test_email

    # Cleanup: delete test user from DB
    db: Session = SessionLocal()
    try:
        user = db.query(User).filter(User.email == test_email).first()
        if user:
            db.delete(user)
            db.commit()
    finally:
        db.close()
