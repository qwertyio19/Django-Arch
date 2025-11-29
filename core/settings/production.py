import os
from .base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]

from dotenv import load_dotenv

load_dotenv()

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
