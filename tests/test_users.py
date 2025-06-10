from fastapi.testclient import TestClient
from app.main import app
from app.db.session import SessionLocal
from app.models import User
from app.core.security import get_password_hash, create_access_token


# Test client for FastAPI app
client = TestClient(app)

# Helper function to register a user


def register_user(email: str, password: str, full_name: str):
    db = SessionLocal()
    db.query(User).filter(User.email == email).delete()
    db.commit()
    db.close()

    return client.post("/api/v1/users/register", json={
        "email": email,
        "password": password,
        "full_name": full_name
    })


class TestUser:
    def test_register_user(self):
        # Test user registration
        response = register_user(
            "testuser@example.com", "securepassword123", "Test User")

        assert response.status_code == 201
        data = response.json()
        assert "id" in data
        assert data["email"] == "testuser@example.com"
        assert data["full_name"] == "Test User"

    def test_get_profile(self, client, db_session):
        user = User(
            email="profileuser@example.com",
            full_name="Profile User",
            hashed_password=get_password_hash("password123"),
            is_active=True,
        )
        db_session.add(user)
        db_session.commit()
        db_session.refresh(user)

        token = create_access_token(subject=user.id)

        response = client.get(
            "/api/v1/users/profile",
            headers={"Authorization": f"Bearer {token}"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["email"] == "profileuser@example.com"
        assert data["full_name"] == "Profile User"

        db_session.delete(user)
        db_session.commit()
