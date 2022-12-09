#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


base_packages = ["pytest>=3.5.0"]

only_test_packages = [
    "black>=19.10b0",
    "flake8>=3.8.3",
]
test_packages = only_test_packages + base_packages

util_packages = ["pre-commit>=2.6.0", "ipykernel>=6.15.1", "twine"] + base_packages

docs_packages = [
    "mkdocs==1.2.3",
    "mkdocs-material==8.0.0",
    "mkdocstrings==0.18.0",
    "jinja2<3.1.0",
]

dev_packages = test_packages + util_packages + docs_packages

setup(
    name="pytest-slow-last",
    version="0.1.0",
    author="David Masip Bonet",
    author_email="david26694@gmail.com",
    maintainer="David Masip Bonet",
    maintainer_email="david26694@gmail.com",
    license="MIT",
    url="https://github.com/david26694/pytest-slow-last",
    description="Run tests in order of execution time (faster tests first)",
    long_description=read("README.rst"),
    py_modules=["pytest_slow_last"],
    python_requires=">=3.5",
    install_requires=base_packages,
    extras_require={
        "test": test_packages,
        "util": util_packages,
        "docs": docs_packages,
        "dev": dev_packages,
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={
        "pytest11": [
            "slow-last = pytest_slow_last",
        ],
    },
)
