.. :changelog:

History
-------

1.1.1 (2020-11-02)
++++++++++++++++++

* Add deprecation warning about Django v3.0. Django itself has `default support <https://docs.djangoproject.com/en/3.0/ref/middleware/#referrer-policy>`_ of *Referrer-Policy* header in ``SecurityMiddleware`` via setting variable ``SECURE_REFERRER_POLICY``.


1.1.0 (2020-10-27)
++++++++++++++++++

* Set default value to ``'no-referrer-when-downgrade'`` instead of requiring it
* Add Django 3.1 and Python 3.9 for testing

1.0.1 (2019-08-23)
++++++++++++++++++

* Update setup.py
* Update docs for setting value in django-settings.


1.0.0 (2019-08-11)
++++++++++++++++++

* First release on PyPI.
