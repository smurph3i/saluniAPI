from datetime import datetime, timedelta, timezone
from typing import Union, Any

from jose import jwt, JWTError, ExpiredSignatureError

from app.core.config import settings


class TokenService:
    def __init__(self):
        self.secret_key = settings.secret_key
        self.algorithm = settings.algorithm
        self.default_expiry_minutes = settings.access_token_expire_minutes

    def create_access_token(
        self, subject: Union[str, Any], expires_delta: timedelta | None = None
    ) -> str:
        expire = datetime.now(tz=timezone.utc) + (
            expires_delta or timedelta(minutes=self.default_expiry_minutes)
        )
        to_encode = {
            "exp": expire,
            "sub": str(subject),
        }
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> dict:
        """Return full decoded payload or raise JWTError."""
        return jwt.decode(token, self.secret_key, algorithms=[self.algorithm])

    def extract_subject(self, token: str) -> Union[str, None]:
        """Return 'sub' from token or None if invalid."""
        try:
            payload = self.decode_token(token)
            return payload.get("sub")
        except (JWTError, ExpiredSignatureError):
            return None

    def is_token_expired(self, token: str) -> bool:
        """Return True if token is expired, otherwise False."""
        try:
            payload = self.decode_token(token)
            exp = payload.get("exp")
            if exp:
                return datetime.fromtimestamp(exp, tz=timezone.utc) < datetime.now(timezone.utc)
        except ExpiredSignatureError:
            return True
        except JWTError:
            return False
        return False


token_service = TokenService()
