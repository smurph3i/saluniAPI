from datetime import datetime, timedelta, timezone
from typing import Union, Any

from jose import jwt, JWTError, ExpiredSignatureError

from app.core.config import settings


class TokenService:
    def __init__(self):
        self.secret_key = settings.secret_key
        self.algorithm = settings.algorithm
        self.default_expire_minutes = settings.access_token_expire_minutes

    def create_access_token(self, subject: Union[str, Any], expires_delta: timedelta | None = None) -> str:
        expire = datetime.now(tz=timezone.utc) + (
            expires_delta if expires_delta else timedelta(
                minutes=self.default_expire_minutes)
        )
        to_encode = {
            "exp": expire,
            "sub": str(subject),
        }
        return jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)

    def decode_token(self, token: str) -> Union[dict, None]:
        try:
            payload = jwt.decode(token, self.secret_key,
                                 algorithms=[self.algorithm])
            return payload
        except ExpiredSignatureError:
            raise ExpiredSignatureError("Token has expired")
        except JWTError as e:
            raise JWTError("Invalid token") from e

    def extract_subject(self, token: str) -> Union[str, None]:
        payload = self.decode_token(token)
        return payload.get("sub") if payload else None


token_service = TokenService()
