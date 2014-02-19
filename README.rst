serfclient
==========

The Python interface to Serf, the decentralised solution for
service discovery and orchestration.

.. image:: https://secure.travis-ci.org/KushalP/serfclient-py.png?branch=master
        :target: http://travis-ci.org/KushalP/serfclient-py

Installation
------------

serfclient requires a running Serf agent. See `Serf's agent documentation
<http://www.serfdom.io/docs/agent/basics.html>`_ for instructions.

To install serfclient, simply:

.. code-block:: bash

    $ sudo pip install serfclient

or alternatively (you really should be using pip though):

.. code-block:: bash

    $ sudo easy_install serfclient

or from source:

.. code-block:: bash

    $ sudo python setup.py install

Getting Started
---------------

.. code-block:: python

    from serfclient.client import SerfClient

    client = SerfClient()
    client.event('foo', 'bar')

Development
------------

serfclient requires a running Serf agent. See `Serf's agent documentation
<http://www.serfdom.io/docs/agent/basics.html>`_ for instructions.

To run the tests, simply:

.. code-block:: bash

    $ python setup.py test
