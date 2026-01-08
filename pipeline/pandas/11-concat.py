#!/usr/bin/env python3
"""Documented"""
import pandas as pd
index = __import__('10-index').index


def concat(df1, df2):
    """Documented"""
    pd.merge(df1, df2, )
    return df1,df2
