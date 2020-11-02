# -*- coding: utf-8
import warnings

import django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DjangoHttpReferrerPolicyConfig(AppConfig):
    name = 'django_http_referrer_policy'

    def ready(self):
        if django.VERSION >= (3, 0):
            message = _('Deprecated, use settings.SECURE_REFERRER_POLICY variable instead. '
                        'More details: https://docs.djangoproject.com/en/3.0/ref/middleware/#referrer-policy')
            warnings.warn(message, DeprecationWarning, stacklevel=3)
