import os


class EnvironmentConfig(object):
    """
    Reads environment variables that Serf understands and parses
    them into a easily consumable object.

    Currently supports reading the following environment variables:

     - SERF_RPC_AUTH
     - SERF_RPC_ADDR

    and sets attributes:

     - host
     - port
     - auth_key
    """

    def __init__(self):
        self.host = 'localhost'
        self.port = 7373
        self.auth_key = None

        rpc_addr = os.getenv('SERF_RPC_ADDR')
        if rpc_addr:
            self.host, self.port = rpc_addr.split(':')
            self.port = int(self.port)

        rpc_auth = os.getenv('SERF_RPC_AUTH')
        if rpc_auth:
            self.auth_key = rpc_auth
