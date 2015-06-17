from serfclient import result


class TestSerfResult(object):
    def test_initialises_to_none(self):
        r = result.SerfResult()
        assert r.head is None
        assert r.body is None

    def test_provides_a_pretty_printed_form_for_repl_use(self):
        r = result.SerfResult(head={"a": 1}, body=('foo', 'bar'))
        assert str(r) == \
            "SerfResult<head={'a': 1},body=('foo', 'bar')>"

    def test_can_convert_to_list(self):
        r = result.SerfResult(head=1, body=2)
        assert sorted(list(r)) == [1, 2]

    def test_can_convert_to_tuple(self):
        r = result.SerfResult(head=1, body=2)
        assert sorted(tuple(r)) == [1, 2]
