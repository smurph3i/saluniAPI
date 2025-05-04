from app.core import security


def test_password_hash_and_verify():
    password = "super-secret-password"
    hashed = security.get_password_hash(password)

    assert hashed != password  # Hashed output should be different
    assert security.verify_password(password, hashed) is True
    assert security.verify_password("wrong-password", hashed) is False


def test_create_and_decode_jwt():
    subject = "user_id_123"
    token = security.create_access_token(subject)

    assert isinstance(token, str)

    decoded_subject = security.decode_access_token(token)
    assert decoded_subject == subject


def test_decode_invalid_jwt():
    invalid_token = "this.is.not.a.valid.token"
    result = security.decode_access_token(invalid_token)

    assert result is None
