#!/usr/bin/env python

"""
Setup script for NewPyProj.
"""

import setuptools

from npp import __project__, __version__, CLI

import os
if os.path.exists('README.rst'):
    README = open('README.rst').read()
else:
    README = ""  # a placeholder, readme is generated on release
CHANGES = open('CHANGES.md').read()


setuptools.setup(
    name=__project__,
    version=__version__,

    description="NewPyProj is a utility for creating a Python 3 package from a template.",
    url='http://pypi.python.org/pypi/NewPyProj',
    author='Jeff Kloosterman',
    author_email='kloosterman.jeff@gmail.com',

    packages=setuptools.find_packages(),

    entry_points={'console_scripts': [CLI + ' = npp.cli:main']},

    long_description=(README + '\n' + CHANGES),
    license='WTFPL',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.3',
    ],

    install_requires=[],
)
