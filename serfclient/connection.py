import msgpack
import socket
import sys


class SerfConnectionError(Exception):
    pass


class SerfConnection(object):
    """
    Manages RPC communication to and from a Serf agent.
    """

    def __init__(self, host='localhost', port=7373):
        self.host, self.port = host, port
        self._socket = None

    def __repr__(self):
        return "%(class)s<host=%(host)s,port=%(port)s>" % {
            'class': self.__class__.__name__,
            'host': self.host,
            'port': self.port,
        }

    def call(self, command, params=None):
        """
        Sends the provided command to Serf for evaluation, with
        any parameters as the message body.
        """
        if self._socket is None:
            raise SerfConnectionError('handshake must be made first')

        header = msgpack.dumps({"Seq": 0, "Command": command})

        if params is not None:
            body = msgpack.dumps(params)
            self._socket.sendall(header + body)
        else:
            self._socket.sendall(header)

        response = self._socket.recv(4096)
        return msgpack.loads(response)

    def handshake(self):
        """
        Sets up the connection with the Serf agent and does the
        initial handshake.
        """
        if self._socket is None:
            self._socket = self._connect()
        return self.call('handshake', {"Version": 1})

    def _connect(self):
        try:
            return socket.create_connection((self.host, self.port), 3)
        except socket.error:
            e = sys.exc_info()[1]
            raise SerfConnectionError(self._error_message(e))

    def _error_message(self, exception):
        return "Error %s connecting %s:%s. %s." % \
            (exception.args[0], self.host, self.port, exception.args[1])
