#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="weightedstats",
    version="0.1",
    description="Weighted mean, median, and weighted median",
    author="Jack Peterson",
    author_email="<jack@tinybike.net>",
    maintainer="Jack Peterson",
    maintainer_email="<jack@tinybike.net>",
    license="MIT",
    url="https://github.com/tensorjack/weightedstats",
    download_url = "https://github.com/tensorjack/weightedstats/tarball/0.1",
    packages=["weightedstats"],
    keywords = ["weights", "statistics"]
)
