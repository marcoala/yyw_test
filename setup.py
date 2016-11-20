#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import yyw_test
version = yyw_test.__version__

setup(
    name='yyw_test',
    version=version,
    author='Marco Alabruzzo',
    author_email='marco.alabruzzo@gmail.com',
    packages=[
        'yyw_test',
    ],
    include_package_data=True,
    zip_safe=False,
    scripts=['manage.py'],
)
