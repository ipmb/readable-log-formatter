#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import sys

from setuptools import setup

version = '0.1.4'

readme = open('README.rst').read()

setup(
    name='readable-log-formatter',
    version=version,
    description="""A human readable log formatter for Python""",
    long_description=readme,
    author='Peter Baumgartner',
    author_email='pete@lincolnloop.com',
    url='https://github.com/ipmb/readable-log-formatter',
    py_modules=['readable_log_formatter'],
    test_suite='tests',
    license="BSD",
    keywords='readable-log-formatter',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
