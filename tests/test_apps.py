from django.apps import apps
from django.test import TestCase

from django_http_referrer_policy.apps import DjangoHttpReferrerPolicyConfig


class TestDjangoHttpReferrerPolicyConfig(TestCase):
    def test_apps(self):
        self.assertEqual(DjangoHttpReferrerPolicyConfig.name, 'django_http_referrer_policy')
        self.assertEqual(apps.get_app_config('django_http_referrer_policy').name, 'django_http_referrer_policy')
