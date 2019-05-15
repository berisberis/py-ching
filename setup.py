#!/usr/bin/env python
# -*- coding: utf-8 -*-
import io
from setuptools import find_packages, setup

with io.open("README.md", "rt", encoding="utf8") as f:
    readme = f.read()

setup(
    name='iching',
    version='0.2.1',
    url='https://github.com/berisberis/py-ching',
    license='MIT',
    maintainer='berisberis',
    description='Random i-ching trigram generator that iterates and graphs results.',
    long_description=readme,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
        'flask_restful',
        'pygal',
    ],
    extras_require={
        'test': [
            'pytest',
            'coverage',
        ],
    },
)