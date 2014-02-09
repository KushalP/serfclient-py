import pytest

from serfclient import connection


class TestSerfConnection(object):
    """
    Tests for the Serf RPC communication object.
    """

    def test_has_a_default_host_and_port(self):
        rpc = connection.SerfConnection()
        assert rpc.host == 'localhost'
        assert rpc.port == 7373

    def test_representation(self):
        rpc = connection.SerfConnection()
        assert str(rpc) == 'SerfConnection<host=localhost,port=7373>'
