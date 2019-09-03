#!/usr/bin/env python
from setuptools import find_packages, setup

setup(
    name='extended_int',
    version='0.6',
    description=(
        'Python classes that provides support for extended integers (the set '
        'of integers, and infinity).'),
    author='Neil Girdhar',
    author_email='mistersheik@gmail.com',
    project_urls={
        "Bug Tracker": "https://github.com/NeilGirdhar/extended_int/issues",
        "Source Code": "https://github.com/NeilGirdhar/extended_int",
    },
    download_url="https://pypi.python.org/pypi/extended_int",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    keywords=[],
    python_requires='>=3.7',
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
