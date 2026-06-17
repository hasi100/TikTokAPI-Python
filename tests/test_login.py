import importlib.util
import pathlib
import sys

import pytest

_spec = importlib.util.spec_from_file_location(
    "tiktokapi_login",
    pathlib.Path(__file__).resolve().parent.parent / "TikTokAPI" / "login.py",
)
_login = importlib.util.module_from_spec(_spec)
sys.modules["tiktokapi_login"] = _login
_spec.loader.exec_module(_login)

LoginError = _login.LoginError
validate_credentials = _login.validate_credentials
validate_email = _login.validate_email
validate_password = _login.validate_password


def test_valid_credentials_normalizes_email():
    result = validate_credentials("  User@Example.com ", "password123")
    assert result == {"email": "user@example.com", "password": "password123"}


def test_invalid_email_format():
    with pytest.raises(LoginError, match="invalid email"):
        validate_email("not-an-email")


def test_email_length_cap():
    long_email = ("a" * 250) + "@b.co"
    with pytest.raises(LoginError, match="invalid email"):
        validate_email(long_email)


def test_short_password():
    with pytest.raises(LoginError, match="8-1024"):
        validate_password("short")


def test_long_password():
    with pytest.raises(LoginError, match="8-1024"):
        validate_password("a" * 1025)


def test_non_string_email():
    with pytest.raises(LoginError, match="email must be a string"):
        validate_email(None)
    with pytest.raises(LoginError, match="email must be a string"):
        validate_email(b"user@example.com")


def test_non_string_password():
    with pytest.raises(LoginError, match="password must be a string"):
        validate_password(None)
