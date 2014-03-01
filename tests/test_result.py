import pytest

from serfclient import result


class TestSerfResult(object):
    def test_initialises_to_none(self):
        r = result.SerfResult()
        assert r.head is None
        assert r.body is None

    def test_provides_a_pretty_printed_form_for_repl_use(self):
        r = result.SerfResult(head={"a": 1, "b": 2}, body=('foo', 'bar'))
        assert str(r) == \
            "SerfResult<head={'a': 1, 'b': 2},body=('foo', 'bar')>"
