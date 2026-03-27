#!/usr/bin/env python3
"""Documented"""
shuffle_data = __import__('2-shuffle_data').shuffle_data


ef moving_average(data, beta):
    """
    that calculates the weighted moving average of a data set:

    data is the list of data to calculate the moving average of
    beta is the weight used for the moving average
    Your moving average calculation should use bias correction
    Returns: a list containing the moving averages of data

    """

    X, Y=shuffle_data(X, Y)
    mini_batches=[]

    for i in range(0, X.shape[0], batch_size):
        X_batch = X[i:i+batch_size]
        Y_batch = Y[i:i+batch_size]
        mini_batches.append((X_batch, Y_batch))

    return mini_batches
