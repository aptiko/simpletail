#!/usr/bin/env python

from setuptools import setup, find_packages


setup(
    name="simpletail",
    version="0.1.1",
    license="GPL3",
    description="Read file in reverse order",
    author="Antonis Christofides",
    author_email="anthony@itia.ntua.gr",
    url="https://github.com/aptiko/simpletail",
    packages=find_packages(),
    test_suite="tests",
    install_requires=[
    ],
)
