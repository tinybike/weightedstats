WeightedStats
=============

.. image:: https://travis-ci.org/tinybike/weightedstats.svg?branch=master
    :target: https://travis-ci.org/tinybike/weightedstats

.. image:: https://coveralls.io/repos/tinybike/weightedstats/badge.svg?branch=master :target: https://coveralls.io/r/tinybike/weightedstats?branch=master

.. image:: https://badge.fury.io/py/weightedstats.svg
    :target: http://badge.fury.io/py/weightedstats

Python functions to calculate the mean, weighted mean, median, and weighted median.

Installation
^^^^^^^^^^^^

The easiest way to install WeightedStats is to use pip::

    $ pip install weightedstats

Usage
^^^^^

WeightedStats includes four functions (mean, weighted_mean, median, weighted_median) which accept lists as arguments, and two functions (numpy_weighted_mean, numpy weighted_median) which accept either lists or numpy arrays.

Example::

    import weightedstats as ws

    my_data = [1, 2, 3, 4, 5]
    my_weights = [10, 1, 1, 1, 9]

    # Ordinary (unweighted) mean and median
    ws.mean(my_data)    # equivalent to ws.weighted_mean(my_data)
    ws.median(my_data)  # equivalent to ws.weighted_median(my_data)
    
    # Weighted mean and median
    ws.weighted_mean(my_data, weights=my_weights)
    ws.weighted_median(my_data, weights=my_weights)

    # Special weighted mean and median functions for use with numpy arrays
    ws.numpy_weighted_mean(my_data, weights=my_weights)
    ws.numpy_weighted_median(my_data, weights=my_weights)

Tests
^^^^^

Unit tests are in the test/ directory.
