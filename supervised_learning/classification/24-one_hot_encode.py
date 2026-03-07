#!/usr/bin/env python3
""""Documented"""
import numpy as np

def one_hot_encode(Y, classes):
    """Documented"""
    if (not isinstance(Y, np.ndarray) or
            not isinstance(classes, int) or
            classes <= 0):
        return None

    m = Y.shape[0]

    try:
        onehot = np.zeros((classes, m))
        onehot[np.arange(classes), Y] = 1
        return onehot
    except ValueError:
        return None
