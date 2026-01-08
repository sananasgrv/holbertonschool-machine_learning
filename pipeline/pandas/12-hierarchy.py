#!/usr/bin/env python3
"""Documented"""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Hierarchical DataFrame"""
    df1 = index(df1)
    df2 = index(df2)
    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    df = df.sort_index()
    col = list(df.columns)
    return df
