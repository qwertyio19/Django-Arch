from .base import *
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("DEBUG")   

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

CSRF_TRUSTED_ORIGINS = [
    f"https://{host}" for host in ALLOWED_HOSTS
] + [
    f"http://{host}" for host in ALLOWED_HOSTS
]

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

STATS_LOG_VERBOSE = os.getenv("STATS_LOG_VERBOSE", "0") == "1"
STATS_LOG_LEVEL = os.getenv("STATS_LOG_LEVEL", "INFO")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "simple": {
            "format": "[{levelname}] {asctime} {name}: {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
    },
    "loggers": {
        "stats": {
            "handlers": ["console"],
            "level": STATS_LOG_LEVEL,
            "propagate": False,
        },
    },
}

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
USE_X_FORWARDED_HOST = True
