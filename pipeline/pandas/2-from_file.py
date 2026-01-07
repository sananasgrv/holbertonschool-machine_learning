#!/usr/bin/env python3
"""Documented"""
import pandas as pd


def from_file(filename, delimiter):
    """Documented"""
    df = pd.read_csv(filename, delimiter=delimiter)
    return df
