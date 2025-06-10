from datetime import timedelta
from fastapi import status
from fastapi.testclient import TestClient
from jose import jwt
from app.main import app
from app.db.session import SessionLocal
from app.models import User
from app.core.security import create_access_token, get_password_hash
from app.core.config import settings

client = TestClient(app)


def register_user(email: str, password: str, full_name: str):
    # Optional: cleanup previous user with same email if needed
    db = SessionLocal()
    db.query(User).filter(User.email == email).delete()
    db.commit()
    db.close()

    return client.post("/api/v1/users/register", json={
        "email": email,
        "password": password,
        "full_name": full_name
    })


class TestLogin:
    def test_login_success(self):
        register_user("loginuser@example.com",
                      "securepassword123", "Login User")

        response = client.post("/api/v1/login", data={
            "username": "loginuser@example.com",
            "password": "securepassword123"
        })

        assert response.status_code == 200
        data = response.json()
        assert "access_token" in data
        assert data["token_type"] == "bearer"

    def test_login_invalid_password(self):
        register_user("wrongpass@example.com",
                      "correctpassword", "Wrong Pass User")

        response = client.post("/api/v1/login", data={
            "username": "wrongpass@example.com",
            "password": "wrongpassword"
        })

        assert response.status_code == 401

    def test_login_non_existent_user(self):
        response = client.post("/api/v1/login", data={
            "username": "notreal@example.com",
            "password": "somepassword"
        })

        assert response.status_code == 401

    def test_login_missing_fields(self):
        response = client.post("/api/v1/login", data={})
        assert response.status_code == 422

    def test_login_inactive_user(self, db_session):
        user = User(
            email="inactive@example.com",
            hashed_password=get_password_hash("password123"),
            full_name="Inactive User",
            is_active=False
        )
        db_session.add(user)
        db_session.commit()

        try:
            response = client.post("/api/v1/login", data={
                "username": "inactive@example.com",
                "password": "password123"
            })

            assert response.status_code in [401, 403]

        finally:
            db_session.delete(user)
            db_session.commit()

    def test_token_payload(self):
        response = client.post("/api/v1/login", data={
            "username": "loginuser@example.com",
            "password": "securepassword123"
        })
        # Ensure login is successful and we get a token
        assert response.status_code == 200
        token = response.json()["access_token"]

        payload = jwt.decode(token, settings.secret_key,
                             algorithms=[settings.algorithm])
        assert "sub" in payload

        # Fetch the user ID from the DB
        db = SessionLocal()
        user = db.query(User).filter_by(email="loginuser@example.com").first()
        db.close()

        assert payload["sub"] == str(user.id)


class TestTokenValidation:
    def test_expired_token(self):
        expired_token = create_access_token(
            "1", expires_delta=timedelta(seconds=-1))
        response = client.get(
            "/api/v1/users/profile",
            headers={"Authorization": f"Bearer {expired_token}"}
        )
        assert response.status_code == 401
        assert response.json()["detail"] == "Token has expired"

    def test_invalid_token(self):
        response = client.get(
            "/api/v1/users/profile",
            headers={"Authorization": "Bearer not.a.real.token"}
        )
        assert response.status_code == 401
        assert response.json()["detail"] == "Could not validate credentials"
