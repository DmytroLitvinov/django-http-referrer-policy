=====
Usage
=====

To use Django HTTP Referrer Policy in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_http_referrer_policy',
        ...
    )

Add Django HTTP Referrer Policy Middleware to your settings:

.. code-block:: python

    MIDDLEWARE = [
        ...
        'django_http_referrer_policy.middleware.ReferrerPolicyMiddleware',
        ...
    ]
