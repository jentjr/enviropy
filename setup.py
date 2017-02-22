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
version = '0.0.1'

def read(f):
    return open(f, encoding='utf-8').read()

setup(
    name='enviropy',
    version=version,
	description='Statistical methods and plotting tools for environmental data',
	long_description=read('README.rst'),
	author='Justin R. Jent',
	author_email='jentjr@gmail.com',
    download_url='https://github.com/jentjr/enviropy/',
	install_requires=requires,
	packages=['enviropy', 'enviropy.external']
	)
