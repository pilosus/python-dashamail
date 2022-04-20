dashamail
=========

`DashaMail`_ API client for Python

Usage
-----

1. Sign up for a DashaMail account
2. Get your API access token: My account -> Integrations
3. Look up `DashaMail API`_ methods you need
4. Use ``dashamail`` client to call the method:

.. code-block:: python

  from dashamail import DashaMailClient

  client = DashaMailClient(api_key="YOUR-API-KEY")
  client.lists_get()


Installation
------------

Just run:

.. code-block:: bash

  pip install -U dashamail


Contributing
------------

See `CONTRIBUTING.rst`_.


.. _DashaMail: https://dashamail.ru/
.. _DashaMail API: https://dashamail.ru/api/
.. _CONTRIBUTING.rst: https://github.com/pilosus/python-dashamail/tree/master/CONTRIBUTING.rst
