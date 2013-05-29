pyconomic for Django
====================

``django_pyconomic`` easily integrates Iconfinder's e-conomic Python library, ``pyconomic``, into your Django applications by allowing easy configuration from your Django settings.


Quick start
-----------

1.  Install ``django_pyconomic`` from PyPI:

    ::
    
       $ pip install django_pyconomic

2.  Update your project's ``settings.py``:

    ::
    
       INSTALLED_APPS = (
           ..
           'django_pyconomic',
       )
       
       PYCONOMIC_AGREEMENT_NUMBER = ..
       PYCONOMIC_USERNAME = '..'
       PYCONOMIC_PASSWORD = '..'

3.  Start using the global e-conomic client instance in your code:

    ::
    
       from django_pyconomic import client
       
       ..


Configuration options
---------------------

``PYCONOMIC_AGREEMENT_NUMBER``
    e-conomic agreement number as an integer.
``PYCONOMIC_USERNAME``
    e-conomic username.
``PYCONOMIC_PASSWORD``
    e-conomic password.
``PYCONOMIC_MOCK``
    Optional setting that when ``True`` uses the ``pyconomic.mock_client.MockClient`` rather than the actual client.
