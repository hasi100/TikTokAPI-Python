import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


class LoginError(ValueError):
    pass


def validate_email(email):
    if not isinstance(email, str) or not EMAIL_RE.match(email):
        raise LoginError("invalid email")
    return email


def validate_password(password):
    if not isinstance(password, str) or len(password) < 8:
        raise LoginError("password must be at least 8 characters")
    return password


def login(email, password):
    validate_email(email)
    validate_password(password)
    return {"email": email, "authenticated": True}
