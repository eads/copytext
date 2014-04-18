#!/usr/bin/env python

from setuptools import setup

setup(
    name='copytext',
    version='0.1.0',
    description='A tool for accessing a spreadsheet as a series of nested keys.',
    long_description=open('README').read(),
    author='NPR Visuals Team',
    author_email='nprapps@npr.org',
    url='http://blog.apps.npr.org/',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=[
        'copytext'
    ],
    install_requires = [
        'openpyxl>=1.8.5',
    ]
)
