#!/usr/bin/python3

from math import sin, cos, tan


def map_functions(x, func):
    """ map an iterable of functions on the the object x """
    result = []
    for i in func:
        result.append("{:.3f}".format(i(x)))
    return result


functions = (sin, cos, tan)
print(map_functions(45, functions))
