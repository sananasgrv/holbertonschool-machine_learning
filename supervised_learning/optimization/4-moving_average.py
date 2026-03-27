#!/usr/bin/env python3
"""Documented"""
shuffle_data = __import__('2-shuffle_data').shuffle_data


def moving_average(data, beta):
    """
    that calculates the weighted moving average of a data set:

    data is the list of data to calculate the moving average of
    beta is the weight used for the moving average
    Your moving average calculation should use bias correction
    Returns: a list containing the moving averages of data

    """
    v = 0
    averages = []

    for i, x in enumerate(data):
        v = beta * v + (1 - beta) * x
        bias_correction = 1 - beta ** (i + 1)
        averages.append(v / bias_correction)

    return averages