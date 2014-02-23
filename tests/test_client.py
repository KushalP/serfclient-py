import pytest

from serfclient import client


class TestSerfClientCommands(object):
    """
    Common commands for the library
    """
    @pytest.fixture
    def serf(self):
        return client.SerfClient()

    def test_has_a_default_host_and_port(self, serf):
        assert serf.host == 'localhost'
        assert serf.port == 7373

    def test_initialises_a_serf_connection_on_creation(self, serf):
        assert serf.connection is not None

    def test_sending_a_simple_event(self, serf):
        assert serf.event('foo', 'bar') == {b'Error': b'', b'Seq': 1}

    def test_sending_a_non_coalescing_event(self, serf):
        assert serf.event('foo', 'bar') == {b'Error': b'', b'Seq': 1}

    def test_event_payload_is_optional(self, serf):
        assert serf.event('foo') == {b'Error': b'', b'Seq': 1}
        assert serf.event('bar', coalesce=False) == {b'Error': b'', b'Seq': 2}

    def test_force_leaving_of_a_node(self, serf):
        assert serf.force_leave('bad-node-name') == {b'Error': b'', b'Seq': 1}

    def test_joining_a_non_existent_node(self, serf):
        assert serf.join(['127.0.0.1:23000']) == \
            {b'Error': b'dial tcp 127.0.0.1:23000: connection refused',
             b'Seq': 1}

    def test_joining_an_existing_node_fails(self, serf):
        assert serf.join(['127.0.0.1:7373']) == \
            {b'Error': b'Reading remote state failed: EOF', b'Seq': 1}

    def test_providing_a_single_value_should_put_it_inside_a_list(self, serf):
        assert serf.join('127.0.0.1:7373') == \
            {b'Error': b'Reading remote state failed: EOF', b'Seq': 1}
