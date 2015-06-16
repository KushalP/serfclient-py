import os

try:
    from serfclient.connection import SerfConnection
except ImportError:
    from connection import SerfConnection


def _get_env_host_and_port():
    env_host, env_port = None, None
    serf_rpc_addr = os.getenv('SERF_RPC_ADDR')
    if serf_rpc_addr:
        env_host, env_port = serf_rpc_addr.split(':')
    return env_host, env_port


class SerfClient(object):
    def __init__(self, host=None, port=None, timeout=3):
        env_host, env_port = _get_env_host_and_port()
        self.host = host or env_host or 'localhost'
        self.port = port or env_port or 7373
        self.timeout = timeout
        self.connection = SerfConnection(
            host=self.host, port=self.port, timeout=self.timeout)
        self.connection.handshake()

    def event(self, name, payload=None, coalesce=True):
        """
        Send an event to the cluster. Can take an optional payload as well,
        which will be sent in the form that it's provided.
        """
        return self.connection.call(
            'event',
            {'Name': name, 'Payload': payload, 'Coalesce': coalesce},
            expect_body=False)

    def members(self, name=None, status=None, tags=None):
        """
        Lists members of a Serf cluster, optionally filtered by one or more
        filters:

        `name` is a string, supporting regex matching on node names.
        `status` is a string, supporting regex matching on node status.
        `tags` is a dict of tag names and values, supporting regex matching
        on values.
        """
        filters = {}

        if name is not None:
            filters['Name'] = name

        if status is not None:
            filters['Status'] = status

        if tags is not None:
            filters['Tags'] = tags

        if len(filters) == 0:
            return self.connection.call('members')
        else:
            return self.connection.call('members-filtered', filters)

    def force_leave(self, name):
        """
        Force a node to leave the cluster.
        """
        return self.connection.call(
            'force-leave',
            {"Node": name}, expect_body=False)

    def join(self, location):
        """
        Join another cluster by provided a list of ip:port locations.
        """
        if not isinstance(location, (list, tuple)):
            location = [location]
        return self.connection.call(
            'join',
            {"Existing": location, "Replay": False})
