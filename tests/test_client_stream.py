import mock
import pytest
import re

from contextlib import closing
from serfclient import client


class TestSerfClientStream(object):
    """
    Common commands for the library
    """
    @pytest.yield_fixture
    def serf(self):
        with closing(client.SerfClient(timeout=None)) as serf:
            yield serf

    def test_sending_a_simple_event(self, serf):
        assert serf.event('foo', 'bar').head == {b'Error': b'', b'Seq': 1}
        assert serf.event('bill', 'gates').head == {b'Error': b'', b'Seq': 2}

    def test_stream(self, serf):
        response = serf.stream()
        assert response.head == {b'Error': b'', b'Seq': 1}
        expected_data = sorted([
            [b'bill', b'gates'],
            [b'foo', b'bar'],
        ])
        all_responses = []
        count = 0
        for response in response.body:
            if response.body[b'Event'] == b'user':
                all_responses.append(response)
                if len(all_responses) == 2:
                    serf.close()

        sorted_responses = sorted([
            [
                res.body[b'Name'],
                res.body[b'Payload'],
            ] for res in all_responses
        ])
        for i, res in enumerate(sorted_responses):
            expected = expected_data[i]
            assert res[0] == expected[0]
            assert res[1] == expected[1]
