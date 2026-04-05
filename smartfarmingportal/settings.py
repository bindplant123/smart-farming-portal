from pathlib import Path
import os
from django.utils.translation import gettext_lazy as _

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-smart-farming-key-2026")

DEBUG = os.getenv("DEBUG", "False") == "True"

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

ROOT_URLCONF = "smartfarmingportal.urls"
WSGI_APPLICATION = "smartfarmingportal.wsgi.application"


# ✅ INSTALLED APPS
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portal",
    "ckeditor",   # ✅ CKEditor added
]


# ✅ MIDDLEWARE
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # ✅ Whitenoise for static files
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# ✅ LANGUAGE SETTINGS
LANGUAGE_CODE = "en"

LANGUAGES = [
    ("en", _("English")),
    ("hi", _("Hindi")),
    ("mr", _("Marathi")),
    ("gu", _("Gujarati")),
    ("ta", _("Tamil")),
    ("te", _("Telugu")),
    ("kn", _("Kannada")),
    ("pa", _("Punjabi")),
    ("bn", _("Bengali")),
]

# ✅ Language cookie settings
LANGUAGE_COOKIE_NAME = "django_language"
LANGUAGE_COOKIE_AGE = 365 * 24 * 60 * 60  # 1 year

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

TIME_ZONE = "Asia/Kolkata"

USE_I18N = True
USE_TZ = True


# ✅ TEMPLATES
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",  # ✅ for images
            ],
        },
    },
]


# ✅ DATABASE
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# ✅ STATIC FILES
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

STATICFILES_DIRS = [
    BASE_DIR / "portal" / "static",
]


# ✅ MEDIA FILES
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


# ✅ AUTH REDIRECTS
LOGIN_URL = "portal:login"
LOGIN_REDIRECT_URL = "portal:home"
LOGOUT_REDIRECT_URL = "portal:login"


# ✅ WEATHER API
WEATHER_API_KEY = "your-api-key-here"


# ✅ DEFAULT FIELD
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"