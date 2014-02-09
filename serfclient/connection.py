class SerfConnection(object):
    """
    Manages RPC communication to and from a Serf agent.
    """

    def __init__(self, host='localhost', port=7373):
        self.host, self.port = host, port

    def __repr__(self):
        return "%(class)s<host=%(host)s,port=%(port)s>" % {
            'class': self.__class__.__name__,
            'host': self.host,
            'port': self.port,
        }
