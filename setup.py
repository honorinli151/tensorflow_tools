#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='tensorflow_tools',
    version=0.1,
    description=(
        'personal tensorflow packages.'
    ),
    author='Chenle Li',
    author_email='chenle.li@student.ecp.fr',
    packages=find_packages(),
    platforms=["all"],
    url='https://github.com/honorinli151/tensorflow_tools',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries'
    ],
)