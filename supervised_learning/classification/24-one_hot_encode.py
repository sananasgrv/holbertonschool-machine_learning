#!/usr/bin/env python3
"""Documented"""
import numpy as np


def one_hot_encode(Y, classes):
    """Documented"""

    if (not isinstance(Y, np.ndarray) or
            not isinstance(classes, int) or
            classes <= 0):
        return None

    m = Y.shape[0]

    try:
        one_hot = np.zeros((classes, m))
        one_hot[Y, np.arange(m)] = 1
        return one_hot
    except Exception:
        return None
