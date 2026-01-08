#!/usr/bin/env python3
"""Documented"""
import pandas as pd


def rename(df):
    """Documented"""
    new_df = df.loc[:, ["Timestamp", "Close"]]
    new_df = new_df.rename(columns={"Timestamp": "Datetime"})
    return new_df
