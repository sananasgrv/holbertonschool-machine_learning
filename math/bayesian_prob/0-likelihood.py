#!/usr/bin/env python3
"""Documented"""
import numpy as np


def likelihood(x, n, P):
    """Calculate the likelihood of a given probability distribution"""
    if not isinstance(n, int) or n <= 0 :
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(x, np.ndarray) or P.ndim != 1:
        raise ValueError("P must be a 1D numpy.ndarray")
    for i in P:
        if i > 1 or i<0:
            raise ValueError("All values in P must be in the range [0, 1]")

