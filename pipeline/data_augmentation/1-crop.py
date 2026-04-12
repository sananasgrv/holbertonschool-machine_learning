#!/usr/bin/env python3
"""Documented"""
import tensorflow as tf

def crop_image(image, size):
    """Documented"""
    crop_height, crop_width = size

    # get number of channels from the image
    channels = tf.shape(image)[-1]

    # perform random crop
    cropped = tf.image.random_crop(image, size=[crop_height, crop_width, channels])

    return cropped
