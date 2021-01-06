#!/usr/bin/env python
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(name='numpsy',
      version="0.0.1",
      description='NumpSy - Integrated NumPy, SymPy, Pandas and unit management for scientific programming.',
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/daquintero/numpsy",
      author='Dario Quintero',
      author_email='<darioaquintero> at gmail dot com',
      packages=setuptools.find_packages(),
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
     )
