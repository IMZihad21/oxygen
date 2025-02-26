"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from datetime import timedelta
from pathlib import Path

import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_DIR = BASE_DIR.joinpath("static")
MEDIA_DIR = BASE_DIR.joinpath("media")

if os.getenv("SECRET_KEY"):
    ON_PRODUCTION = os.environ.get("ON_PRODUCTION") == "True"
    DJANGO_SECRET_KEY = os.environ.get("SECRET_KEY")
    DJANGO_DEBUG = os.environ.get("DEBUG") == "True"

    # Database configuration
    DJANGO_DB_ENGINE = os.environ.get("DB_ENGINE")
    DJANGO_DB_NAME = os.environ.get("DB_NAME")
    DJANGO_DB_USER = os.environ.get("DB_USER")
    DJANGO_DB_PASSWORD = os.environ.get("DB_PASSWORD")
    DJANGO_DB_HOST = os.environ.get("DB_HOST")
    SECURE_SSL_REDIRECT = os.environ.get("SECURE_SSL_REDIRECT") == "True"
    HOSTS = os.environ.get("ALLOWED_HOSTS").split(",")
    CORS_HOSTS = os.environ.get("CORS_HOSTS").split(",")

    # Email configuration
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_PORT = os.environ.get("EMAIL_PORT")
    EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = os.environ.get("EMAIL_USE_TLS") == "True"
    # EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL') == 'True'
    DEFAULT_FROM_EMAIL = os.environ.get("DEFAULT_FROM_EMAIL")
else:
    env = environ.Env(DEBUG=(bool, False))

    environ.Env.read_env()
    environ.Env.read_env(os.path.join(BASE_DIR, ".env"))

    ON_PRODUCTION = env("ON_PRODUCTION") == "True"
    DJANGO_SECRET_KEY = env("SECRET_KEY")
    DJANGO_DEBUG = env("DEBUG") == "True"

    # Database configuration
    DJANGO_DB_ENGINE = env("DB_ENGINE")
    DJANGO_DB_NAME = env("DB_NAME")
    DJANGO_DB_USER = env("DB_USER")
    DJANGO_DB_PASSWORD = env("DB_PASSWORD")
    DJANGO_DB_HOST = env("DB_HOST")
    SECURE_SSL_REDIRECT = env("SECURE_SSL_REDIRECT")
    HOSTS = env("ALLOWED_HOSTS").split(",")
    CORS_HOSTS = env("CORS_HOSTS").split(",")

    # Email configuration
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = env("EMAIL_HOST")
    EMAIL_PORT = env("EMAIL_PORT")
    EMAIL_HOST_USER = env("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = env("EMAIL_USE_TLS") == "True"
    # EMAIL_USE_SSL = env('EMAIL_USE_SSL') == 'True'
    DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = DJANGO_SECRET_KEY

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = DJANGO_DEBUG

ALLOWED_HOSTS = HOSTS

# Application definition

INSTALLED_APPS = [
    "django.contrib.sites",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Third Party
    "corsheaders",
    "rest_framework",
    "rest_framework.authtoken",
    "rest_framework_simplejwt.token_blacklist",
    "rest_framework_simplejwt",
    "django_cleanup.apps.CleanupConfig",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "dj_rest_auth.registration",
    # Installed Apps
    "user",
]

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework_simplejwt.authentication.JWTAuthentication",
        "dj_rest_auth.jwt_auth.JWTCookieAuthentication",
    ),
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.FormParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FileUploadParser",
    ],
    # 'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}
# If you are not using JWT Authentication system please comment this section
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=90),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "UPDATE_LAST_LOGIN": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "JWK_URL": None,
    "LEEWAY": 0,
    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),
}

REST_AUTH_SERIALIZERS = {"LOGIN_SERIALIZER": "user.serializers.LoginSerializer"}

REST_AUTH_REGISTER_SERIALIZERS = {
    # "REGISTER_SERIALIZER": "user.serializers.RegisterSerializer"
}

REST_USE_JWT = True
JWT_AUTH_COOKIE = "access"
JWT_AUTH_REFRESH_COOKIE = "refresh"
OLD_PASSWORD_FIELD_ENABLED = True
ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "none"
REST_SESSION_LOGIN = False

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # 'user.middleware.AuthorizationMiddleware',
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # create Template directory and set template directory here as -> 'DIRS': [BASE_DIR/'template']
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases


if ON_PRODUCTION:
    DATABASES = {
        "default": {
            "ENGINE": DJANGO_DB_ENGINE,
            "NAME": DJANGO_DB_NAME,
            "USER": DJANGO_DB_USER,
            "PASSWORD": DJANGO_DB_PASSWORD,
            "HOST": DJANGO_DB_HOST,
        }
    }
else:
    # SqliteDB
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"  # change as per your region Ex: 'America/New_York' | 'Europe/Paris' | 'Europe/London' | 'Asia/Dhaka'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = "static"
# STATICFILES_DIRS = [STATIC_DIR]
STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"
WHITENOISE_AUTOREFRESH = True

MEDIA_URL = "/media/"
MEDIA_ROOT = "media"
# DEBUG_PROPAGATE_EXCEPTIONS = True

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

AUTH_USER_MODEL = "user.User"
CORS_ALLOW_ALL_ORIGINS = True
# Turn this on if want to specify hosts
# CORS_ALLOWED_ORIGINS = CORS_HOSTS
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = ["http://127.0.0.1:8000"]
SITE_ID = 1
