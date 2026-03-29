#!/usr/bin/env python3
"""Same convolution on grayscale images"""

import numpy as np

def convolve_grayscale_same(images, kernel):
    """
    Performs a same convolution on grayscale images

    Args:
        images: numpy.ndarray of shape (m, h, w)
        kernel: numpy.ndarray of shape (kh, kw)

    Returns:
        numpy.ndarray containing the convolved images
    """
    m, h, w = images.shape
    kh, kw = kernel.shape

    # Compute padding for "same" convolution
    pad_h = (kh - 1) // 2
    pad_w = (kw - 1) // 2

    # Pad images with zeros
    images_padded = np.pad(
        images,
        pad_width=((0, 0), (pad_h, kh - pad_h - 1), (pad_w, kw - pad_w - 1)),
        mode='constant',
        constant_values=0
    )

    # Output shape is same as original image
    output = np.zeros((m, h, w))

    # Convolution using 2 loops
    for i in range(h):
        for j in range(w):
            current_slice = images_padded[:, i:i+kh, j:j+kw]
            output[:, i, j] = np.sum(current_slice * kernel, axis=(1, 2))

    return output
