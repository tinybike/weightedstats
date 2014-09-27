#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Tests for weighted stats functions.

"""
from __future__ import division
import os
import sys
import platform
import unittest

HERE = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0, os.path.join(HERE, os.pardir))

from weightedstats import *

class TestWeightedStats(unittest.TestCase):

    def setUp(self):
        self.data = [
            [7, 1, 2, 4, 10],
            [7, 1, 2, 4, 10],
            [7, 1, 2, 4, 10, 15],
            [1, 2, 4, 7, 10, 15],
            [0, 10, 20, 30],
            [1, 2, 3, 4, 5],
            [1, 2, 3, 4, 5],
            [30, 40, 50, 60, 35],
            [2, 0.6, 1.3, 0.3, 0.3, 1.7, 0.7, 1.7, 0.4],
            [3.7, 3.3, 3.5, 2.8],
            [100, 125, 123, 60, 45, 56, 66],
            [2, 2, 2, 2, 2, 2],
            [2.3],
            [-2, -3, 1, 2, -10],
            [1, 2, 3, 4, 5],
        ]
        self.weights = [
            [1, 1/3, 1/3, 1/3, 1],
            [1, 1, 1, 1, 1],
            [1, 1/3, 1/3, 1/3, 1, 1],
            [1/3, 1/3, 1/3, 1, 1, 1],
            [30, 191, 9, 0],
            [10, 1, 1, 1, 9],
            [10, 1, 1, 1, 900],
            [1, 3, 5, 4, 2],
            [2, 2, 0, 1, 2, 2, 1, 6, 0],
            [5, 5, 4, 1],
            [30, 56, 144, 24, 55, 43, 67],
            [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
            [12],
            [7, 1, 1, 1, 6],
            [1, 0, 0, 0, 2],
        ]
        self.median_answers = [7.0,   4.0,  8.5,
                               8.5,  10.0,  2.5,
                               5.0,  50.0,  1.7,
                               3.5, 100.0,  2.0,
                               2.3,  -2.0,  5.0]
        self.mean_answers = [6.444444,  4.800000, 8.583333,
                             8.583333,  9.086956, 2.909091,
                             4.949617, 47.333333, 1.275000,
                             3.453333, 91.782816, 2.000000,
                             2.300000, -4.625000, 3.666667]

    def test_mean(self):
        datum = [7, 1, 1, 1, 6]
        self.assertTrue(weighted_mean(datum) == mean(datum) == 3.2)

    def test_weighted_mean(self):
        for datum, weight, answer in zip(self.data, self.weights, self.mean_answers):
            self.assertTrue(abs(weighted_mean(datum, weights=weight) - answer) <= 1e-6)

    def test_numpy_weighted_mean(self):
        for datum, weight, answer in zip(self.data, self.weights, self.mean_answers):
            self.assertTrue(abs(numpy_weighted_mean(datum, weights=weight) - answer) <= 1e-6)

    def test_median(self):
        datum = [4, 3, 2, 1]
        self.assertTrue(weighted_median(datum) == numpy_weighted_median(datum) == median(datum) == 2.5)
        datum = [7, 1, 1, 1, 6]
        self.assertTrue(weighted_median(datum) == numpy_weighted_median(datum) == median(datum) == 1.0)

    def test_weighted_median(self):
        for datum, weight, answer in zip(self.data, self.weights, self.median_answers):
            self.assertTrue(weighted_median(datum, weights=weight) == answer)
        self.assertTrue(weighted_median([4, 3, 2, 1], weights=[0, 0, 0, 0]) is None)

    def test_numpy_weighted_median(self):
        for datum, weight, answer in zip(self.data, self.weights, self.median_answers):
            self.assertTrue(numpy_weighted_median(datum, weights=weight) == answer)
        self.assertTrue(numpy_weighted_median([4, 3, 2, 1], weights=[0, 0, 0, 0]) is None)


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWeightedStats)
    unittest.TextTestRunner(verbosity=2).run(suite)
