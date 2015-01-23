#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="weightedstats",
    version="0.3",
    description="Mean, weighted mean, median, weighted median",
    author="Jack Peterson",
    author_email="<jack@tinybike.net>",
    maintainer="Jack Peterson",
    maintainer_email="<jack@tinybike.net>",
    license="MIT",
    url="https://github.com/tinybike/weightedstats",
    download_url = "https://github.com/tinybike/weightedstats/tarball/0.3",
    packages=["weightedstats"],
    keywords = ["weights", "mean", "median", "numpy", "statistics"]
)
