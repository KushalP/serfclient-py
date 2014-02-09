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
