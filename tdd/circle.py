#!/usr/bin/python3

from math import pi

def circle_area(r):
    if r < 0:
        raise ValueError("The radius cannot be negative")
    if type(r) not in [int, float]:
        raise TypeError("Radius must be an integer or decimal")
    area = pi * (r ** 2)
    return area
