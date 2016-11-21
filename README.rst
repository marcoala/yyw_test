yyw_test
========

Test app for yoyowallet

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django

Since the task is only a test and that I'm using a free API key with limited access to the data I'm going to implement only one endpoint: the 16 days forecast

http://openweathermap.org/forecast16

Example of call:
http://api.openweathermap.org/data/2.5/forecast/daily?id=2643743&cnt=16&unit=metric&APPID=5e59f877bddafa20efd6b186ccd31032

The endpoint allow you to choose the number of days for the forecast, from 1 to 16. Since the amount of data is very small I'm going to fix the parameter at the maximum (16) and filter the data in the visualisation.
This will allow me to cache the result using the only the city and the current date, limiting the number of the calls to the external system.

Loading the list of city in the database will allow me to build an autocomplete functionality in the system, and to tell to the user when the name of the city is wrong without a call to the external API.


Backend structure
-----------------

The name of the app is yyw_test and this will be internal module structure:

- yyw_test
    - common
    - integrations
        - openweathermap
    - citytemperature

To avoid circular dependency every module can only import form a module above in the list, for example every module can import from `common` but common can't import from any module.

The module `openweathermap` will contain the integration with the external system but the module `citytemperature` will be agnostic on which external service is used, allowing to change service in the future. Nevertheless a excessive abstraction in this case could be a premature optimisation.

Frontend structure
------------------

Only two component should be needed:

- Search box with autocomplete (for the city)
- temperature visualisation

the stretch goals add two more components

- temperature graph visualisation
- data range selection

For the component design I'm going to use the 9 states technique.

Test
----
I've used tox for test (https://tox.readthedocs.io/en/latest/), for the following reasons:

- compatible with circleCI
- possibility to assert a coverage level (test will non pass if coverage is under 100%)
- possibility to assert the use of the standard PEP8 using the linter flake8 (code written under conventions is easier to read)

all the tests are inside the folder `/tests`.


cookiecutter docs
=================

Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run manage.py test
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ py.test

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html
