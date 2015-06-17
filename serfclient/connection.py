import socket
import sys
import msgpack
import resource

try:
    from serfclient.result import SerfResult
except ImportError:
    from result import SerfResult


class SerfConnectionError(Exception):
    pass


class SerfTimeout(SerfConnectionError):
    pass


class SerfProtocolError(SerfConnectionError):
    pass


class SerfConnection(object):
    """
    Manages RPC communication to and from a Serf agent.
    """

    # Read from the RPC socket in blocks of this many bytes.
    # (Typically 4k)
    _socket_recv_size = resource.getpagesize()

    def __init__(self, host='localhost', port=7373, timeout=3):
        self.host = host
        self.port = port
        self.timeout = timeout
        self._socket = None
        self._seq = 0

    def __repr__(self):
        return "%(class)s<counter=%(c)s,host=%(h)s,port=%(p)s,timeout=%(t)s>" \
            % {'class': self.__class__.__name__,
               'c': self._seq,
               'h': self.host,
               'p': self.port,
               't': self.timeout}

    def call(self, command, params=None, expect_body=True):
        """
        Sends the provided command to Serf for evaluation, with
        any parameters as the message body.
        """
        if self._socket is None:
            raise SerfConnectionError('handshake must be made first')

        header = msgpack.packb({"Seq": self._counter(), "Command": command})

        if params is not None:
            body = msgpack.packb(params)
            self._socket.sendall(header + body)
        else:
            self._socket.sendall(header)

        # The number of msgpack messages that are expected
        # in response to this command.
        messages_expected = 2 if expect_body else 1

        response = SerfResult()
        unpacker = msgpack.Unpacker()

        # Continue reading from the network until the expected number of
        # msgpack messages have been received.
        while messages_expected > 0:
            try:
                buf = self._socket.recv(self._socket_recv_size)
                if len(buf) == 0:  # Connection was closed.
                    raise SerfConnectionError("Connection closed by peer")
                unpacker.feed(buf)
            except socket.timeout:
                raise SerfTimeout(
                    "timeout while waiting for an RPC response. (Have %s so"
                    "far)", response)

            # Might have received enough to deserialise one or more
            # messages, try to fill out the response object.
            for message in unpacker:
                if response.head is None:
                    response.head = message
                elif response.body is None:
                    response.body = message
                else:
                    raise SerfProtocolError(
                        "protocol handler got more than 2 messages. "
                        "Unexpected message is: %s", message)

                # Expecting one fewer message now.
                messages_expected -= 1

        return response

    def handshake(self):
        """
        Sets up the connection with the Serf agent and does the
        initial handshake.
        """
        if self._socket is None:
            self._socket = self._connect()
        return self.call('handshake', {"Version": 1}, expect_body=False)

    def auth(self, auth_key):
        """
        Performs the initial authentication on connect
        """
        if self._socket is None:
            self._socket = self._connect()
        return self.call('auth', {"AuthKey": auth_key}, expect_body=False)

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
