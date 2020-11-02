=============================
Django HTTP Referrer Policy
=============================

.. image:: https://badge.fury.io/py/django-http-referrer-policy.svg
    :target: https://badge.fury.io/py/django-http-referrer-policy

.. image:: https://travis-ci.org/DmytroLitvinov/django-http-referrer-policy.svg?branch=master
    :target: https://travis-ci.org/DmytroLitvinov/django-http-referrer-policy

.. image:: https://readthedocs.org/projects/django-http-referrer-policy/badge/?version=latest
    :target: https://django-http-referrer-policy.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

.. image:: https://codecov.io/gh/DmytroLitvinov/django-http-referrer-policy/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/DmytroLitvinov/django-http-referrer-policy

django-referrer-policy provides a middleware class implementing `the Referrer-Policy header <https://www.w3.org/TR/referrer-policy/>`_ for
`Django <https://www.djangoproject.com/>`_-powered sites.

**Note**: Starting from Django v3.0, Django itself has `default support <https://docs.djangoproject.com/en/3.0/ref/middleware/#referrer-policy>`_
 of *Referrer-Policy* header in ``SecurityMiddleware`` via setting variable ``SECURE_REFERRER_POLICY``.

Documentation
-------------

The full documentation is at https://django-http-referrer-policy.readthedocs.io.

Quickstart
----------

Install Django HTTP Referrer Policy::

    pip install django-http-referrer-policy


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


Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Maintainable version of `original library <https://github.com/ubernostrum/django-referrer-policy/>`_.

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _`origin library`: https://google.com
