=====
Usage
=====


Add Django HTTP Referrer Policy Middleware to your settings:

.. code-block:: python

    MIDDLEWARE = [
        ...
        'django_http_referrer_policy.middleware.ReferrerPolicyMiddleware',
        ...
    ]

Add variable `REFERRER_POLICY` to your settings with valid value:

.. code-block:: python

    REFERRER_POLICY = 'no-referrer'

More details about valid referrer policies:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy#Syntax
