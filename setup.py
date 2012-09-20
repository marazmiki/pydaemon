#!/usr/bin/env python
# coding: utf-8

import setuptools
import os
import pydaemon


def rel(*x):
    return os.path.normpath(os.path.join(os.path.dirname(__file__), *x))


PACKAGE_NAME = 'pydaemon'


CLASSIFIERS = [
    'Intended Audience :: Developers',
    'Programming Language :: Python',
    'Operating System :: POSIX',
    'Operating System :: Unix',
    'Topic :: Software Development :: Libraries :: Python Modules',
]

setuptools.setup(name=PACKAGE_NAME,
    version= pydaemon.get_version(),
    description= 'A simple class that allows to create daemon in UNIX and Linux',
    long_description=open(rel('README.md')).read(),
    author='marazmiki',
    author_email='marazmiki@gmail.com',
    classifiers=CLASSIFIERS,
    license= 'MIT license',
    url= 'http://pypi.python.org/pypi/pydaemon',
    download_url='https://github.com/marazmiki/pydaemon/zipball/master',
    packages=setuptools.find_packages(exclude=['examples']),
    include_package_data=True,
    zip_safe=False)
