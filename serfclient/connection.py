import socket
import sys
import umsgpack


class SerfConnectionError(Exception):
    pass


class SerfConnection(object):
    """
    Manages RPC communication to and from a Serf agent.
    """

    def __init__(self, host='localhost', port=7373, timeout=3):
        self.host = host
        self.port = port
        self.timeout = timeout
        self._socket = None
        self._seq = 0
        umsgpack.compatibility = True

    def __repr__(self):
        return "%(class)s<counter=%(c)s,host=%(h)s,port=%(p)s,timeout=%(t)s>" \
            % {'class': self.__class__.__name__,
               'c': self._seq,
               'h': self.host,
               'p': self.port,
               't': self.timeout}

    def call(self, command, params=None):
        """
        Sends the provided command to Serf for evaluation, with
        any parameters as the message body.
        """
        if self._socket is None:
            raise SerfConnectionError('handshake must be made first')

        header = umsgpack.dumps({"Seq": self._counter(), "Command": command})

        if params is not None:
            body = umsgpack.dumps(params)
            self._socket.sendall(header + body)
        else:
            self._socket.sendall(header)

        response = self._socket.recv(4096)
        return umsgpack.loads(response)

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
            return socket.create_connection(
                (self.host, self.port), self.timeout)
        except socket.error:
            e = sys.exc_info()[1]
            raise SerfConnectionError(self._error_message(e))

    def _counter(self):
        """
        Returns the current value of the iterator and increments it.
        """
        current = self._seq
        self._seq += 1
        return current

    def _error_message(self, exception):
        return "Error %s connecting %s:%s. %s." % \
            (exception.args[0], self.host, self.port, exception.args[1])
