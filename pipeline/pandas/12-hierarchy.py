#!/usr/bin/env python3
"""Documented"""
import pandas as pd
index = __import__('10-index').index


def hierarchy(df1, df2):
    """Hierarchical DataFrame"""
    df1 = index(df1)
    df2 = index(df2)
    df = pd.MultiIndex.from_product([df2, df1], names=["bitstamp", "coinbase"])
    df = df.sort_index()
    return df
