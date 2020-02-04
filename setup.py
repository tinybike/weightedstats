#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()

setup(
    name="weightedstats",
    version="0.4.1",
    description="Mean, weighted mean, median, weighted median",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Jack Peterson",
    author_email="<jack@tinybike.net>",
    maintainer="Jack Peterson",
    maintainer_email="<jack@tinybike.net>",
    license="MIT",
    url="https://github.com/tinybike/weightedstats",
    download_url = "https://github.com/tinybike/weightedstats/tarball/0.4.1",
    packages=["weightedstats"],
    keywords = ["weights", "mean", "median", "numpy", "statistics"]
)
