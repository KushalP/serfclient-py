from pkg_resources import get_distribution

__version__ = get_distribution('serfclient').version

from serfclient.client import SerfClient
