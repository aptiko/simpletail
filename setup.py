#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="simpletail",
    version="1.0.0",
    license="GPL3",
    description="Read file in reverse order",
    author="Antonis Christofides",
    author_email="antonis@antonischristofides.com",
    url="https://github.com/aptiko/simpletail",
    packages=find_packages(),
    test_suite="tests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Topic :: Text Processing :: General",
    ],
)
