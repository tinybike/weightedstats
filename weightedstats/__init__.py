#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Mean, weighted mean, median, and weighted median.

WeightedStats includes four functions (mean, weighted_mean, median,
weighted_median) which accept lists as arguments, and two functions
(numpy_weighted_mean, numpy weighted_median) which accept either lists
or numpy arrays.

Example:

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

"""
from __future__ import division
import sys

__title__      = "WeightedStats"
__version__    = "0.4"
__author__     = "Jack Peterson"
__email__      = "jack@tinybike.net"
__license__    = "MIT"

def mean(data):
    """Calculate the mean of a list."""
    return sum(data) / float(len(data))

def weighted_mean(data, weights=None):
    """Calculate the weighted mean of a list."""
    if weights is None:
        return mean(data)
    total_weight = float(sum(weights))
    weights = [weight / total_weight for weight in weights]
    w_mean = 0
    for i, weight in enumerate(weights):
        w_mean += weight * data[i]
    return w_mean

def numpy_weighted_mean(data, weights=None):
    """Calculate the weighted mean of an array/list using numpy."""
    import numpy as np
    weights = np.array(weights).flatten() / float(sum(weights))
    return np.dot(np.array(data), weights)

def median(data):
    """Calculate the median of a list."""
    data.sort()
    num_values = len(data)
    half = num_values // 2
    if num_values % 2:
        return data[half]
    return 0.5 * (data[half-1] + data[half])

def weighted_median(data, weights=None):
    """Calculate the weighted median of a list."""
    if weights is None:
        return median(data)
    midpoint = 0.5 * sum(weights)
    if any([j > midpoint for j in weights]):
        return data[weights.index(max(weights))]
    if any([j > 0 for j in weights]):
        sorted_data, sorted_weights = zip(*sorted(zip(data, weights)))
        cumulative_weight = 0
        below_midpoint_index = 0
        while cumulative_weight <= midpoint:
            below_midpoint_index += 1
            cumulative_weight += sorted_weights[below_midpoint_index-1]
        cumulative_weight -= sorted_weights[below_midpoint_index-1]
        if abs(cumulative_weight - midpoint) < sys.float_info.epsilon:
            bounds = sorted_data[below_midpoint_index-2:below_midpoint_index]
            return sum(bounds) / float(len(bounds))
        return sorted_data[below_midpoint_index-1]

def numpy_weighted_median(data, weights=None):
    """Calculate the weighted median of an array/list using numpy."""
    import numpy as np
    if weights is None:
        return np.median(np.array(data).flatten())
    data, weights = np.array(data).flatten(), np.array(weights).flatten()
    if any(weights > 0):
        sorted_data, sorted_weights = map(np.array, zip(*sorted(zip(data, weights))))
        midpoint = 0.5 * sum(sorted_weights)
        if any(weights > midpoint):
            return (data[weights == np.max(weights)])[0]
        cumulative_weight = np.cumsum(sorted_weights)
        below_midpoint_index = np.where(cumulative_weight <= midpoint)[0][-1]
        if np.abs(cumulative_weight[below_midpoint_index] - midpoint) < sys.float_info.epsilon:
            return np.mean(sorted_data[below_midpoint_index:below_midpoint_index+2])
        return sorted_data[below_midpoint_index+1]
