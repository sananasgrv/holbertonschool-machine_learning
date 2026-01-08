#!/usr/bin/env python3
"""Documented"""


def slice(df):
    """Documented"""
    new_df = df["High", "Low", "Close", "Volume_BTC"].head(60)
    return new_df
