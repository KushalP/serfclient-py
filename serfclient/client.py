from connection import SerfConnection

class SerfClient(object):
    def __init__(self, host='localhost', port=7373):
        self.host, self.port = host, port
        self.connection = SerfConnection(host=self.host, port=self.port)
        self.connection.handshake()

    def event(self, name, payload):
        return self.connection.call(
            'event',
            {"Name": name, "Payload": payload, "Coalesce": True})
