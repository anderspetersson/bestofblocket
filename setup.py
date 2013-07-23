#!/usr/bin/env python
from setuptools import setup, find_packages
try:
    from bestofblocket import get_version
    version = get_version()
except ImportError:
    version = '0.0.1'


setup(
    name='bestofblocket',
    version=version,
    author='Anders Petersson',
    author_email='me@anderspetersson.se',
    url='http://www.bestofblocket.se',
    description='bestofblocket',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
