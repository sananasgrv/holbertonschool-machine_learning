#!/usr/bin/env python3
"""Documented"""


def slice(df):
    """Documented"""
    new_df = df.loc["High", "Low", "Close", "Volume_BTC"]
    return new_df.head(60)
