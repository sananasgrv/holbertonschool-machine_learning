#!/usr/bin/env python3
"""Documented"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """Documented"""
    index(df1)
    index(df2)
    df2 = df2.loc[:1417411920, :]
    df = pd.concat([df2, df1], keys=["bitstamp", "coinbase"])
    return df
