#!/usr/bin/env python3
"""Documented"""


def array(df):
    """Documented"""
    new_df = df[["Datetime", "Close"]].to_numpy()
    new_df = new_df.tail(10)
    return new_df
