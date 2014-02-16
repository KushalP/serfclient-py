#!/usr/bin/env python
import os
import sys

from serfclient import __version__

try:
    from setuptools import setup
    from setuptools.command.test import test as TestCommand

    class PyTest(TestCommand):
        def finalize_options(self):
            TestCommand.finalize_options(self)
            self.test_args = []
            self.test_suite = True

        def run_tests(self):
            import pytest
            errno = pytest.main(self.test_args)
            sys.exit(errno)
except ImportError:
    from distutils.core import setup
    PyTest = lambda x: x

try:
    long_description = open(os.path.join(os.path.dirname(__file__),
                                         'README.rst')).read()
except:
    long_description = None

setup(
    name='serfclient',
    version=__version__,
    description='Python client for the Serf orchestration tool',
    long_description=long_description,
    url='https://github.com/KushalP/serfclient-py',
    author='Kushal Pisavadia',
    author_email='kushal@violentlymild.com',
    maintainer='Kushal Pisavadia',
    maintainer_email='kushal@violentlymild.com',
    keywords=['Serf', 'orchestration', 'service discovery'],
    license='MIT',
    packages=['serfclient'],
    install_requires=['u-msgpack-python'],
    tests_require=['pytest'],
    cmdclass={'test': PyTest}
)
