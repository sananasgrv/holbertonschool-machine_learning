#!/usr/bin/env python3
import numpy as np
"""Documented"""


def np_cat(mat1, mat2, axis=0):
    """Documented"""
    new_mat = np.concatenate((mat1, mat2), axis=axis)
    return new_mat
