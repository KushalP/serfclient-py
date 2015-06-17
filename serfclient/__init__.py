from pkg_resources import get_distribution
from serfclient.client import SerfClient
from serfclient.environment_config import EnvironmentConfig

__version__ = get_distribution('serfclient').version

__all__ = ['SerfClient', 'EnvironmentConfig']
