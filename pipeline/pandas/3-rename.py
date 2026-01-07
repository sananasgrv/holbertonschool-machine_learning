#!/usr/bin/env python3
"""Documented"""
import pandas as pd


def rename(df):
    """Documented"""
    df.index = pd.to_datetime(df.index)
    return df
