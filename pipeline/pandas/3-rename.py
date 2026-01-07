#!/usr/bin/env python3
"""Documented"""
import pandas as pd


def rename(df):
    df.drop(columns=['Unnamed: 0'])
    return df
