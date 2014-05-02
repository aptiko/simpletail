#!/usr/bin/env python

from setuptools import setup, find_packages


kwargs = {
    'name': "simpletail",
    'version': "dev",
    'license': "GPL3",
    'description': "Read file in reverse order",
    'author': "Antonis Christofides",
    'author_email': "anthony@itia.ntua.gr",
    'packages': find_packages(),
    'test_suite': "tests",
    'install_requires': [
    ],
}
setup(**kwargs)
