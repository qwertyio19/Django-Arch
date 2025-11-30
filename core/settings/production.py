from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = False  # для прода/стейджа — всегда False

SECRET_KEY = os.getenv("SECRET_KEY")

ALLOWED_HOSTS = [
    h.strip()
    for h in os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",")
    if h.strip()
]

CORS_ALLOW_ALL_ORIGINS = os.getenv("DJANGO_CORS_ALLOW_ALL_ORIGINS", "False").lower() == "true"

CORS_ALLOWED_ORIGINS = [
    o.strip()
    for o in os.getenv("DJANGO_CORS_ALLOWED_ORIGINS", "").split(",")
    if o.strip()
]

CORS_ALLOW_CREDENTIALS = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get("POSTGRES_DB", "my_db"),
        'USER': os.environ.get("POSTGRES_USER", "my_user"),
        'PASSWORD': os.environ.get("POSTGRES_PASSWORD", "my_password"),
        'HOST': os.environ.get("POSTGRES_HOST", "localhost"),
        'PORT': os.environ.get("POSTGRES_PORT", "5432"),
    }
}
