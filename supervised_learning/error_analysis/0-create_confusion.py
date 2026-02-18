#!/usr/bin/env python3
"""Documented"""
import numpy as np


def create_confusion_matrix(labels, logits):
    """Documented"""
    m, classes = labels.shape
    true_classes = np.argmax(labels, axis=1)
    pred_classes = np.argmax(logits, axis=1)

    conf = np.zeros(shape=(classes, classes))

    for i in range(classes):
        conf[true_classes[i], pred_classes[i]] = true_classes[i]

    return conf
