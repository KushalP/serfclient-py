try:
    from serfclient.connection import SerfConnection
except ImportError:
    from connection import SerfConnection


class SerfClient(object):
    def __init__(self, host='localhost', port=7373, timeout=3):
        self.host = host
        self.port = port
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
            {'Name': name, 'Payload': payload, 'Coalesce': coalesce})

    def force_leave(self, name):
        """
        Force a node to leave the cluster.
        """
        return self.connection.call(
            'force-leave',
            {"Node": name})

    def join(self, location):
        """
        Join another cluster by provided a list of ip:port locations.
        """
        if not isinstance(location, (list, tuple)):
            location = [location]
        return self.connection.call(
            'join',
            {"Existing": location, "Replay": False})
