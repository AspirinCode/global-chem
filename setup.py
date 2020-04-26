#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# package setup
#
# ------------------------------------------------

# imports
# -------
import os

# config
# ------
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

# requirements
# ------------
with open('requirements.txt') as f:
    REQUIREMENTS = f.read().strip().split('\n')

TEST_REQUIREMENTS = [
    'pytest',
    'pytest-runner'
]

if os.path.exists('README.md'):
    long_description = open('README.md').read()
else:
    long_description = 'GlobalChem - Your content variable store for everything chemistry'

# exec
# ----
setup(
    name="global-chem",
    version="0.1.0",
    packages=['global-chem'],
    license='MPL',
    author="Suliman Sharif",
    author_email="sharifsuliman1@gmail.com",
    url="https://www.github.com/Sulstice/global-chem",
    install_requires=REQUIREMENTS,
    long_description=long_description,
    long_description_content_type='text/markdown',
    zip_safe=False,
    keywords='smiles molecules chemistry',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'License :: OSI Approved :: MPL License',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
)