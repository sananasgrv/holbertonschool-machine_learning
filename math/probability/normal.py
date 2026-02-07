#!/usr/bin/env python3
"""Documented"""


class Normal:
    """docstring for Exponential"""

    def __init__(self, data=None, mean=0., stddev=1.):
        if data is None:
            self.mean = float(mean)
            if stddev < 0:
                raise ValueError("stddev must be a positive value")
            self.stddev = float(stddev)
        else:
            if isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            mean = sum(data) / len(data)
            stddev = sum((data[i]-self.mean)**2 for i in range(len(data))) / len(data)
