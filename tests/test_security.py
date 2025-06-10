import time
from datetime import timedelta

from app.core.token_service import token_service


class TestTokenService:
    def test_create_and_extract_subject(self):
        subject = "user_id_123"
        token = token_service.create_access_token(subject)

        assert isinstance(token, str)

        decoded_subject = token_service.extract_subject(token)
        assert decoded_subject == subject

    def test_decode_invalid_token(self):
        invalid_token = "this.is.not.a.valid.token"

        result = token_service.extract_subject(invalid_token)
        assert result is None

    def test_expired_token(self):
        subject = "user_id_123"
        token = token_service.create_access_token(
            subject, expires_delta=timedelta(seconds=1))

        time.sleep(2)  # Wait for token to expire

        assert token_service.is_token_expired(token) is True
        assert token_service.extract_subject(token) is None

    def test_token_not_expired(self):
        token = token_service.create_access_token(
            "test_user", expires_delta=timedelta(minutes=5))

        assert token_service.is_token_expired(token) is False

    def test_full_decode_token_payload(self):
        subject = "payload_user"
        token = token_service.create_access_token(subject)

        payload = token_service.decode_token(token)

        assert payload["sub"] == subject
        assert "exp" in payload
