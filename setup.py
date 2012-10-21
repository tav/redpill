#! /usr/bin/env python

# Public Domain (-) 2004-2012 The Redpill Authors.
# See the Redpill UNLICENSE file for details.

from redpill.version import __release__
from setuptools import setup

# ------------------------------------------------------------------------------
# Run Setup
# ------------------------------------------------------------------------------

setup(
    name="redpill",
    author="tav",
    author_email="tav@espians.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: Public Domain",
        "Operating System :: OS Independent",
        "Programming Language :: Python"
        ],
    description="A cross-plaform package management framework",
    entry_points=dict(console_scripts=[
        "redpill = redpill.main:main"
        ]),
    install_requires=[
        "PyYAML >= 3.10",
        "requests >= 0.14.1",
        "simplejson >= 2.6.2",
        "tavutil >= 1.0.2"
        ],
    keywords=["package management", "dependency management"],
    license="Public Domain",
    long_description=open('README.rst').read(),
    packages=["redpill"],
    url="https://github.com/tav/redpill",
    version=__release__,
    zip_safe=True
    )
