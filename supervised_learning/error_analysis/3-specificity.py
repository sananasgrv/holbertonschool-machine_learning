#!/usr/bin/env python3
"""Documented"""
import numpy as np


def specificity(confusion):
    """Documented
    TN / TN + FP
    """
    TP = np.diagonal(confusion)
    TN = np.sum(confusion, axis=1) - TP
    FP = np.sum(confusion, axis=0) - TP
    return TN / (TN+FP)
