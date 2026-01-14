#!/usr/bin/env python3
"""
Write a function def poly_derivative(poly): that calculates the derivative of a polynomial:
"""


def poly_derivative(poly):
    """
    poly is a list of coefficients representing a polynomial

    the index of the list represents the power of x that the coefficient belongs to
    Example: if <img src=“https://latex.codecogs.com/gif.latex?f(x)&space;=&space;x^3&space;&plus;&space;3x&space;&plus;5” title=“f(x) = x^3 + 3x +5” />, poly is equal to [5, 3, 0, 1]
    If poly is not valid, return None
    If the derivative is 0, return [0]
    Return a new list of coefficients representing the derivative of the polynomial
    """
    if type(poly) is not list or poly == [] :
        return None
    elif poly[0] == 0 and len(poly) == 1:
        return [0]
    else:
        result = []
        for i in range(len(poly)):
                result.append(poly[i] * i)
        if result[0] == 0 :
            result.pop(0)
        return result

poly = [0]
print(poly_derivative(poly))