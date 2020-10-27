from django.core.exceptions import ImproperlyConfigured
from django.test import TestCase
from django.urls import reverse

from django_http_referrer_policy.middleware import ReferrerPolicyMiddleware


class TestReferrerPolicyMiddleware(TestCase):
    """
    Test ReferrerPolicyMiddleware.
    """
    test_url = reverse('test-referrer-policy-middleware')

    def test_valid_values(self):
        """
        Each valid value of the header is accepted, and properly sent.
        """
        for value in ReferrerPolicyMiddleware.VALID_REFERRER_POLICIES:
            with self.settings(REFERRER_POLICY=value):
                response = self.client.get(self.test_url)
                self.assertTrue('Referrer-Policy' in response)
                self.assertEqual(response['Referrer-Policy'], value)

    def test_invalid_value(self):
        """
        An invalid header value is a configuration error.
        """
        with self.assertRaises(ImproperlyConfigured):
            with self.settings(REFERRER_POLICY='invalid'):
                self.client.get(self.test_url)
