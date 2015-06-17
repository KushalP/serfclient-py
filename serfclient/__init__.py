from pkg_resources import get_distribution
from serfclient.client import SerfClient

__version__ = get_distribution('serfclient').version

__all__ = ['SerfClient']
