"""
Homework 1: Distance functions on vectors
Course    : Data Mining (636-0018-00L)

Auxiliary functions.

This file implements the distance functions that are invoked from the main
program.
"""
# Author: Damian Roqueiro <damian.roqueiro@bsse.ethz.ch>
# September 2015

from __future__ import division
import numpy as np
import math

def manhattan_dist(v1, v2):
    return minkowski_dist(v1, v2, 1)

def hamming_dist(v1, v2):
    t1 = np.ndarray.copy(v1)
    t2 = np.ndarray.copy(v2)
    t1[t1>0] = 1
    t2[t2>0] = 1
    return np.sum(np.abs(t1-t2))

def euclidean_dist(v1, v2):
    return minkowski_dist(v1, v2, 2)

def chebyshev_dist(v1, v2):
    return np.max(np.abs(v1-v2))

def minkowski_dist(v1, v2, d):
    t = np.sum(np.abs(v1-v2)**d)
    return t**(1/d)
