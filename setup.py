#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

from setuptools import setup, Command

version = '1.0.0'

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    print("You probably want to also tag the version now:")
    print("  git tag -a %s -m 'version %s'" % (version, version))
    print("  git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='readable-log-formatter',
    version=version,
    description="""A fault-tolerant pylibmc cache backend for Django""",
    long_description=readme,
    author='Peter Baumgartner',
    author_email='pete@lincolnloop.com',
    url='https://github.com/lincolnloop/django-ft-cache',
    py_modules=['readable_log_formatter'],
    test_suite='tests',
    license="BSD",
    keywords='django-ft-cache',
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
