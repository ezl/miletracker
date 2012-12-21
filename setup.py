#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='miletracker',
    version='1.0',
    description="",
    author="Eric Liu",
    author_email='info@miletracker.com',
    url='',
    packages=find_packages(),
    package_data={'miletracker': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
