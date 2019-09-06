Changelog
=========

1.3.0 (WIP)
-----------

- Implemented `client.set_tag()` and `client.delete_tag()` - `#38
  <https://github.com/KushalP/serfclient-py/pull/38>`_
- Implemented `client.get_coordinate()` - `#39
  <https://github.com/KushalP/serfclient-py/pull/39>`_

1.2.0
-----

- Deprecate support for Python 2.6
- Implemented `client.stream()` - `#34
  <https://github.com/KushalP/serfclient-py/pull/34>`_
- Added support for Python 3.5 and 3.6 - `#35
  <https://github.com/KushalP/serfclient-py/pull/35>`_
- Change msgpack-python requirement to msgpack - `#36
  <https://github.com/KushalP/serfclient-py/pull/36>`_

1.1.0
-----

- Provide a way to close connections - `#31
  <https://github.com/KushalP/serfclient-py/issues/29>`_
- Add `mock` as a test dependency - `#30
  <https://github.com/KushalP/serfclient-py/issues/30>`_

1.0.0
-----

- Support serf v0.7 - `#28
  <https://github.com/KushalP/serfclient-py/issues/28>`_
- Breaking change with v0.7.1 which can be seen in the issue above

0.7.1
-----

- Bugfix for packed IPv4 addresses - `#25
  <https://github.com/KushalP/serfclient-py/pull/25>`_

0.7.0
-----

- Add a `stats` command, which provides debugging information about
  the running serf agent - `#22
  <https://github.com/KushalP/serfclient-py/pull/22>`_

0.6.0
-----

- Add a custom msgpack data unpacker for the `Addr` field - `#21
  <https://github.com/KushalP/serfclient-py/pull/21>`_

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
