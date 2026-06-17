import re

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
MAX_EMAIL_LEN = 254
MIN_PASSWORD_LEN = 8
MAX_PASSWORD_LEN = 1024


class LoginError(ValueError):
    pass


def validate_email(email):
    if not isinstance(email, str):
        raise LoginError("email must be a string")
    email = email.strip().lower()
    if len(email) > MAX_EMAIL_LEN or not EMAIL_RE.match(email):
        raise LoginError("invalid email")
    return email


def validate_password(password):
    if not isinstance(password, str):
        raise LoginError("password must be a string")
    if not (MIN_PASSWORD_LEN <= len(password) <= MAX_PASSWORD_LEN):
        raise LoginError(
            f"password must be {MIN_PASSWORD_LEN}-{MAX_PASSWORD_LEN} characters"
        )
    return password


def validate_credentials(email, password):
    return {
        "email": validate_email(email),
        "password": validate_password(password),
    }
