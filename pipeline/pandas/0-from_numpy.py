#!/usr/bin/env python3
"""Documented"""
import pandas as pd

def from_numpy(array):
    """Documented"""
    i = 65
    df = pd.DataFrame(array, columns=[for i in range(df.shape[1])])
    return df