#!/usr/bin/env python3
"""Documented"""
import numpy as np
from numpy.ma.core import diagonal


def specificity(confusion):
    """Documented
    TN / TN + FP
    """
    TP = np.diagonal(confusion)
    TN = np.sum(TP) - TP
    FP = np.sum(confusion, axis=0) - TP
    return TN / (TN+FP)
