import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

IS_PRODUCTION = os.getenv("PRODUCTION", "False").lower() == "true"

if IS_PRODUCTION:
    from core.settings.production import *
else:
    from core.settings.development import *

THEME_APPS = [
    'jazzmin',
]

MY_APPS = [
]

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LIBRARY_APPS = [
    'rest_framework',
    'drf_yasg',
    'ckeditor',
    'modeltranslation',
    "corsheaders",
]

INSTALLED_APPS = [
    *THEME_APPS,
    *DJANGO_APPS,
    *LIBRARY_APPS,
    *MY_APPS,
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'



AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Asia/Bishkek'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LANGUAGES = [
    ('ru', _('Russian')),
    ('ky', _('Kyrgyz')),
    ('en', _('English')),
]


MEDIA_URL = 'back_media/'
MEDIA_ROOT = BASE_DIR / 'back_media/'


STATIC_URL = '/back_static/'
STATIC_ROOT = BASE_DIR / 'back_static/'
