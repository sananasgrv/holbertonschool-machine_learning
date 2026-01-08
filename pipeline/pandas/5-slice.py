#!/usr/bin/env python3
"""Documented"""


def slice(df):
    """Documented"""
    for i in range(0, df.shape[0], 60):
        new_df =+ df.loc[df.index(i) , ["High", "Low", "Close", "Volume_BTC"]]
    return new_df
