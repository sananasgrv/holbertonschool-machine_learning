#!/usr/bin/env python3
"""Documented"""


def slice(df):
    """Documented"""
    new_df = df.loc[:60, ["High", "Low", "Close", "Volume_BTC"]]
    return new_df