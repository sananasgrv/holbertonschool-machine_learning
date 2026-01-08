#!/usr/bin/env python3
"""Documented"""
import pandas as pd


def array(df):
    """Documented"""
    new_df = df.tail(10)
    new_df.to_numpy()
    return new_df
