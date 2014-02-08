class RPCConnection(object):
    """
    Manages RPC communication to and from a Serf agent.
    """

    def __init__(self, host='localhost', port=7373):
        self.host, self.port = host, port

    def __repr__(self):
        return "RPCConnection<host=%(host)s,port=%(port)s>" % {
            'host': self.host,
            'port': self.port,
        }
