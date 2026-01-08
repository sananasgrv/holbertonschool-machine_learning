#!/usr/bin/env python3
"""Documented"""
import pandas as pd


def visualize(df):
    """Documented"""

    df = df.drop(columns=["Weighted_Price"])
    df = df.rename(columns={"Timestamp": "Date"})
    df["Date"] = pd.to_datetime(df["Date"], unit="s")
    df = df.set_index("Date")
    df["Close"] = df["Close"].ffill()
    df[["High", "Low", "Open"]] = df[["High", "Low", "Open"]].fillna(df["Close"])
    df[["Volume_(BTC)", "Volume_(Currency)"]] = (
        df[["Volume_(BTC)", "Volume_(Currency)"]].fillna(0)
    )
    df = df.loc["2017-01-01":]
    df = df.resample("D").agg({
        "High": "max",
        "Low": "min",
        "Open": "mean",
        "Close": "mean",
        "Volume_(BTC)": "sum",
        "Volume_(Currency)": "sum",
    })
    return df
