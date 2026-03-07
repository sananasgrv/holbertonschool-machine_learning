#!/usr/bin/env python3
"""Documented"""
import numpy as np


def one_hot_decode(one_hot):
    """Documented"""

    if not isinstance(one_hot, np.ndarray):
        return None

    if len(one_hot.shape) != 2:
        return None

    try:
        return np.argmax(one_hot, axis=0)
    except Exception:
        return None
