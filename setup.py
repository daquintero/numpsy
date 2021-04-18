#!/usr/bin/env python
import setuptools

with open("README_RAW.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="numpsy",
    version="0.0.5",
    description="NumpSy - Integrated NumPy, SymPy, SciPy and Pandas with unit management for scientific programming with IPython.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daquintero/numpsy",
    author="Dario Quintero",
    author_email="darioaquintero@gmail.com",
    packages=setuptools.find_packages(),
    install_requires=[
        "ipython",
        "numpy",
        "pandas",
        "sympy",
        "scipy",
        "tabulate"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
