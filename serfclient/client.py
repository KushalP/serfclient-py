try:
    from serfclient.connection import SerfConnection
except ImportError:
    from connection import SerfConnection


class SerfClient(object):
    def __init__(self, host='localhost', port=7373, rpc_auth=None, timeout=3):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.connection = SerfConnection(
            host=self.host, port=self.port, timeout=self.timeout)
        self.connection.handshake()
        if rpc_auth:
            self.connection.auth(rpc_auth)

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
