#!/usr/bin/env python3
import pandas as pd
"""Documented"""


def from_file(filename, delimiter):
    """Documented"""
    df = pd.read_csv(filename, delimiter=delimiter)
    return df