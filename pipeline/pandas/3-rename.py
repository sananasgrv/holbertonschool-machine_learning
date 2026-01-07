#!/usr/bin/env python3
"""Documented"""
import pandas as pd


def rename(df):
    """Documented"""
    new_df = df.copy(["Timestamp", "Close"],)
    return df
