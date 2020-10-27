from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:  # pragma: no cover
    MiddlewareMixin = object


class ReferrerPolicyMiddleware(MiddlewareMixin):
    """
    A middleware implementing the Referrer-Policy header.
    The value of the header will be read from the REFERRER_POLICY
    setting, which must be set to one of the string values
    contained in the attribute VALID_REFERRER_POLICIES
    on this class.
    """
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy#Syntax
    VALID_REFERRER_POLICIES = {
        'no-referrer',
        'no-referrer-when-downgrade',
        'origin',
        'origin-when-cross-origin',
        'same-origin',
        'strict-origin',
        'strict-origin-when-cross-origin',
        'unsafe-url',
    }

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.
        referrer_policy = getattr(settings, 'REFERRER_POLICY', 'no-referrer-when-downgrade')

        if referrer_policy not in self.VALID_REFERRER_POLICIES:
            raise ImproperlyConfigured(
                "settings.REFERRER_POLICY has an illegal value."
            )

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        response['Referrer-Policy'] = settings.REFERRER_POLICY

        return response
