import pytest

from serfclient import client


class TestSerfClientCommands(object):
    """
    Common commands for the library
    """

    def test_has_a_default_host_and_port(self):
        serf = client.SerfClient()
        assert serf.host == 'localhost'
        assert serf.port == 7373

    def test_initialises_a_serf_connection_on_creation(self):
        serf = client.SerfClient()
        assert serf.connection is not None

    def test_sending_a_simple_event(self):
        serf = client.SerfClient()
        assert serf.event('foo', 'bar') == {b'Error': b'', b'Seq': 1}

    def test_sending_a_non_coalescing_event(self):
        serf = client.SerfClient()
        assert serf.event('foo', 'bar', False) == {b'Error': b'', b'Seq': 1}
