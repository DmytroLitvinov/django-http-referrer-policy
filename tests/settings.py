# -*- coding: utf-8
import django  # noqa

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "+m6#58qph==@kyhte)yj4p6e&*8m4v9ld!5w&uu+ob@)_0eg78"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
]

SITE_ID = 1

MIDDLEWARE = (
    'django_http_referrer_policy.middleware.ReferrerPolicyMiddleware',
)
