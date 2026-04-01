#!/usr/bin/env python3
"""Module that performs a convolution on images using multiple kernels."""

import numpy as np


def conv_forward(A_prev, W, b, activation, padding="same", stride=(1, 1)):
    """
    Performs forward propagation over a convolutional layer
    of a neural network.

    A_prev: numpy.ndarray of shape (m, h_prev, w_prev, c_prev)
    W: numpy.ndarray of shape (kh, kw, c_prev, c_new)
    b: numpy.ndarray of shape (1, 1, 1, c_new)
    activation: activation function
    padding: "same" or "valid"
    stride: tuple (sh, sw)

    Returns: output of the convolutional layer
    """

    m, h_prev, w_prev, c_prev = A_prev.shape
    kh, kw, _, c_new = W.shape
    sh, sw = stride

    # Padding hesablanması
    if padding == "same":
        ph = int(np.ceil(((h_prev - 1) * sh + kh - h_prev) / 2))
        pw = int(np.ceil(((w_prev - 1) * sw + kw - w_prev) / 2))
    else:
        ph, pw = 0, 0

    # Output ölçüləri
    oh = int((h_prev + 2 * ph - kh) / sh) + 1
    ow = int((w_prev + 2 * pw - kw) / sw) + 1

    # Padding tətbiqi
    A_prev_pad = np.pad(
        A_prev,
        ((0, 0), (ph, ph), (pw, pw), (0, 0)),
        mode="constant"
    )

    # Output tensor
    Z = np.zeros((m, oh, ow, c_new))

    for i in range(oh):
        for j in range(ow):
            for k in range(c_new):

                vert_start = i * sh
                vert_end = vert_start + kh

                horiz_start = j * sw
                horiz_end = horiz_start + kw

                slice_prev = A_prev_pad[
                    :,
                    vert_start:vert_end,
                    horiz_start:horiz_end,
                    :
                ]

                Z[:, i, j, k] = np.sum(
                    slice_prev * W[:, :, :, k],
                    axis=(1, 2, 3)
                ) + b[0, 0, 0, k]

    return activation(Z)