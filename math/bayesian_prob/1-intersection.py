#!/usr/bin/env python3
"""Documented"""
import numpy as np
from numpy.ma.core import shape


def intersection(x, n, P, Pr):
    """ that calculates the intersection of
    obtaining this data
     with the various hypothetical probabilities"""
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that"
                         " is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray):
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or shape(Pr) != shape(n):
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if P.ndim != 1 or Pr.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")