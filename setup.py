#!/usr/bin/env python3
from setuptools import setup, find_packages


#with open('README.rst') as ff:
#    readme = ff.read()

setup(
    name='constclass',
    version='0.1.0',
    description='Decorators for enforcing const correctness on Python classes',
    #long_description=readme,
    author="Daniel R. D'Avella",
    author_email='ddavella@stsci.edu',
    url='https://github.com/drdavella/constclass',
    python_requires='>=3.3',
    packages=find_packages(),
)
