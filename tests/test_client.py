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
