import pytest

from serfclient import connection


class TestConnection(object):
    """
    Tests for the RPC communication object.
    """

    def test_has_a_default_host_and_port(self):
        rpc = connection.RPCConnection()
        assert rpc.host == 'localhost'
        assert rpc.port == 7373

    def test_representation(self):
        rpc = connection.RPCConnection()
        assert str(rpc) == 'RPCConnection<host=localhost,port=7373>'
