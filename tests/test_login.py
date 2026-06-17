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
login = _login.login
validate_email = _login.validate_email
validate_password = _login.validate_password


def test_valid_login():
    result = login("user@example.com", "password123")
    assert result == {"email": "user@example.com", "authenticated": True}


def test_invalid_email():
    with pytest.raises(LoginError):
        validate_email("not-an-email")


def test_short_password():
    with pytest.raises(LoginError):
        validate_password("short")


def test_non_string_inputs():
    with pytest.raises(LoginError):
        login(None, "password123")
    with pytest.raises(LoginError):
        login("user@example.com", None)
