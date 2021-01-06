#!/usr/bin/env python
import os
import sys
import warnings
import builtins
from distutils.core import setup

# Python supported version checks. Keep right after stdlib imports to ensure we
# get a sensible error for older Python versions
if sys.version_info[:2] < (3, 7):
    raise RuntimeError("Python version >= 3.7 required.")


import versioneer
# Taken from NumPy:
# This is a bit hackish: we are setting a global variable so that the main
# numpy __init__ can detect if it is being loaded by the setup routine, to
# avoid attempting to load components that aren't built yet.  While ugly, it's
# a lot more robust than what was previously being used.
builtins.__NUMPY_SETUP__ = True

# Needed for backwards code compatibility below and in some CI scripts.
# The version components are changed from ints to strings, but only VERSION
# seems to matter outside of this module and it was already a str.
FULLVERSION = versioneer.get_version()
ISRELEASED = 'dev' not in FULLVERSION
MAJOR, MINOR, MICRO = FULLVERSION.split('.')[:3]
VERSION = '{}.{}.{}'.format(MAJOR, MINOR, MICRO)


# The first version not in the `Programming Language :: Python :: ...` classifiers above
if sys.version_info >= (3, 10):
    fmt = "NumPy {} may not yet support Python {}.{}."
    warnings.warn(
        fmt.format(VERSION, *sys.version_info[:2]),
        RuntimeWarning)
    del fmt

setup(name='numpsy',
      version=versioneer.get_version(),
      description='NumpSy - Integrated NumPy, SymPy, Pandas and unit management for scientific programming.',
      author='Dario Quintero',
      author_email='<darioaquintero> at gmail dot com',
      url='',
      packages=['numpsy'],
     )
