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

    def event(self, name, payload, coalesce=True):
        return self.connection.call(
            'event',
            {'Name': name, 'Payload': payload, 'Coalesce': coalesce})

    def force_leave(self, name):
        return self.connection.call(
            'force-leave',
            {"Node": name})

    def join(self, location):
        if not isinstance(location, (list, tuple)):
            location = [location]
        return self.connection.call(
            'join',
            {"Existing": location, "Replay": False})
