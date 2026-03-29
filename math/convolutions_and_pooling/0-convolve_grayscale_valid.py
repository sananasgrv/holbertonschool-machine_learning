#!/usr/bin/env python3
"""Documented"""
import numpy as np


def convolve_grayscale_valid(images, kernel):
    """
    that performs a valid convolution on grayscale images:
    images is a numpy.ndarray with shape (m, h, w) containing multiple grayscale images
        m is the number of images
        h is the height in pixels of the images
        w is the width in pixels of the images
    kernel is a numpy.ndarray with shape (kh, kw) containing the kernel for the convolution
        kh is the height of the kernel
        kw is the width of the kernel
    You are only allowed to use two for loops; any other loops of any kind are not allowed
    Returns: a numpy.ndarray containing the convolved images
    """
        m, h, w = images.shape
        kh, kw = kernel.shape

        output_h = h - kh + 1
        output_w = w - kw + 1

        output = np.zeros((m, output_h, output_w))

        for i in range(output_h):
            for j in range(output_w):
                current_slice = images[:, i:i + kh, j:j + kw]

                output[:, i, j] = np.sum(current_slice * kernel, axis=(1, 2))

        return output
