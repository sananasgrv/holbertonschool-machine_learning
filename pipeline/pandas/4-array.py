#!/usr/bin/env python3
"""Documented"""


def array(df):
    """Documented"""
    new_df = df.column(["High", "Close"])
    new_df = new_df.tail(10)
    new_df.to_numpy()
    return new_df
