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
        assert str(rpc) == 'SerfConnection<counter=0,host=localhost,port=7373>'

    def test_connection_to_bad_socket_throws_exception(self):
        rpc = connection.SerfConnection(port=40000)
        with pytest.raises(connection.SerfConnectionError) as exceptionInfo:
            rpc.handshake()
        assert 'connecting localhost:40000. Connection refused.' \
            in str(exceptionInfo)

    def test_handshake_to_serf_agent(self):
        rpc = connection.SerfConnection()
        assert rpc.handshake() == {b'Seq': 0, b'Error': b''}

    def test_call_throws_exception_if_socket_none(self):
        rpc = connection.SerfConnection()
        with pytest.raises(connection.SerfConnectionError) as exceptionInfo:
            rpc.call('members')
        assert 'handshake must be made first' in str(exceptionInfo)

    def test_handshake_and_call_increments_counter(self):
        rpc = connection.SerfConnection()
        assert str(rpc) == 'SerfConnection<counter=0,host=localhost,port=7373>'
        rpc.handshake()
        assert str(rpc) == 'SerfConnection<counter=1,host=localhost,port=7373>'
        rpc.call('event', {"Name": "foo", "Payload": "test payload", "Coalesce": True})
        assert str(rpc) == 'SerfConnection<counter=2,host=localhost,port=7373>'
