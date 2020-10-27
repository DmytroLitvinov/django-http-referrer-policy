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

Optional: provide variable `REFERRER_POLICY` to your settings with valid value if default value ``'no-referrer-when-downgrade'`` does not suit to you:

.. code-block:: python

    REFERRER_POLICY = 'no-referrer'

More details about valid referrer policies:
https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy#Syntax
