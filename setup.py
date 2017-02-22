#!/usr/bin/env python
import os
import sys
from codecs import open

from setuptools import setup

if sys.argv[-1] == 'publish':
    os.system('python setup.py register')
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload --universal')
    sys.exit()

requires = ['pyodbc', 'pandas']
from enviropy import __version__, __name__, __author__ 

def read(f):
    return open(f, encoding='utf-8').read()

setup(
    name=__name__,
    version=__version__,
	description='Statistical methods and plotting tools for environmental data',
	long_description=read('README.rst'),
	author=__author__,
	author_email='jentjr@gmail.com',
    download_url='https://github.com/jentjr/enviropy/',
	license='MIT',
	install_requires=requires,
	packages=['enviropy']
	)
