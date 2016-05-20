import pytest

from serfclient import result


class TestSerfResult(object):
    @pytest.fixture
    def head_and_body_result(self):
        return result.SerfResult(head=1, body=2)

    def test_initialises_to_none(self):
        r = result.SerfResult()
        assert r.head is None
        assert r.body is None

    def test_provides_a_pretty_printed_form_for_repl_use(self):
        r = result.SerfResult(head={"a": 1}, body=('foo', 'bar'))
        assert str(r) == \
            "SerfResult<head={'a': 1},body=('foo', 'bar')>"

    def test_can_convert_to_list_and_tuple(self, head_and_body_result):
        for structure in [list, tuple]:
            assert sorted(structure(head_and_body_result)) == [1, 2]
