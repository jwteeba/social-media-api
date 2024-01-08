from passlib.context import CryptContext
from functools import lru_cache
import requests
import json

from app import config

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@lru_cache
def get_settings():
    return config.Settings()


def hash(password: str):
    return pwd_context.hash(password)


def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def email_validation(email_addr):
    settings = get_settings()
    try:
        response = requests.get(
            f"https://emailvalidation.abstractapi.com/v1/?api_key={settings.api_key}&email={email_addr}"
        )
        return json.loads(response.content)
    except requests.exceptions.RequestException as api_error:
        raise SystemExit(api_error)
