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

    def test_connection_to_bad_socket_throws_exception(self):
        rpc = connection.SerfConnection(port=40000)
        with pytest.raises(connection.SerfConnectionError) as exception:
            rpc.handshake()
        assert exception.value.message == \
            'Error 61 connecting localhost:40000. Connection refused.'

    def test_connection_to_serf_agent(self):
        rpc = connection.SerfConnection()
        assert rpc.handshake() == True
