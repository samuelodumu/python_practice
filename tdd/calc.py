#!/usr/bin/python3

"""This module defines functions for basic arithmetic 
(addition, subtraction, multiplication and division)"""

def add_num(a, b):
    """Adds the numbers a and b
    >>> add_num(10, 24)
    34
    >>> add_num(2.5, 2)
    4.5
    >>> add_num('a', 42)
    Traceback (most recent call last)
        ...
    TypeError("Number must be an integer")
    """
    if not isinstance(any(x for x in a, b), float):
        raise TypeError("Number must be an integer")
    result = a + b
    return result

def main():
    num = add_num(23.4, 50)
    print(num)
