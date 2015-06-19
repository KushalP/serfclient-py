Changelog
=========

0.5.0
-----

- Support `RPC
  auth <https://serfdom.io/docs/agent/options.html#rpc_auth>`_ token
  when communicating with secure serf members -
  `#12 <https://github.com/KushalP/serfclient-py/pull/12>`_
- Added `EnvironmentConfig` object that can read Serf environment
  variables in an easy way -
  `#17 <https://github.com/KushalP/serfclient-py/pull/17>`_

0.4.0
-----

- Fix for spinning forever doing a socket recv after serf
  stops/restarts - `#7
  <https://github.com/KushalP/serfclient-py/pull/7>`_
- Fixing dependency on `serfclient.__version__` in setup.py - `#8
  <https://github.com/KushalP/serfclient-py/pull/8>`_

0.3.0
-----

- SerfClient object available as `serfclient.SerfClient` instead of
  `serfclient.client.SerfClient` - `#4 <https://github.com/KushalP/serfclient-py/pull/4>`_
- No longer using a fixed size to read from the RPC socket - `#5 <https://github.com/KushalP/serfclient-py/pull/5>`_
- Add support for filtering the members list - `#6 <https://github.com/KushalP/serfclient-py/pull/6>`_

0.2.0
-----

- Added SerfClient.members() function to provide member information

0.1.0
-----

- SerfClient returns bounded SerfResult objects to hold the head
  and body of the response

0.0.3
-----

- Fix for issue #1: event payloads can be optional

0.0.2
-----

Two changes to the README:

- Explained how to install serfclient
- Showed how to use the `SerfClient` class
