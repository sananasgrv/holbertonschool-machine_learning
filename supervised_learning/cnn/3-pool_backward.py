#!/usr/bin/env python3
"""Documented"""
import numpy as np


def pool_backward(dA, A_prev, kernel_shape, stride=(1, 1), mode='max'):
    """Documented"""

    m, h_new, w_new, c = dA.shape
    m, h_prev, w_prev, c = A_prev.shape
    kh, kw = kernel_shape
    sh, sw = stride

    dA_prev = np.zeros_like(A_prev)

    for i in range(h_new):
        for j in range(w_new):
            h_start = i * sh
            w_start = j * sw
            if mode == 'max':
                region = A_prev[
                    :, h_start:h_start + kh, w_start:w_start + kw, :
                ]
                mask = (region == np.max(
                    region, axis=(1, 2), keepdims=True
                ))
                dA_prev[
                    :, h_start:h_start + kh, w_start:w_start + kw, :
                ] += mask * dA[:, i, j, :][:, np.newaxis, np.newaxis, :]
            else:
                avg = dA[:, i, j, :] / (kh * kw)
                dA_prev[
                    :, h_start:h_start + kh, w_start:w_start + kw, :
                ] += (np.ones((m, kh, kw, c)) *
                      avg[:, np.newaxis, np.newaxis, :])

    return dA_prev
