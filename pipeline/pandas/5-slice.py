#!/usr/bin/env python3
"""Documented"""


def slice(df):
    """Documented"""
    new_df = df[["High", "Low", "Close", "Volume_BTC"]]
    for i in range(0, new_df.shape[0], 60):
        return df.iloc[i, :]
