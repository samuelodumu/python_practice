#!/usr/bin/python3

"""This module defines functions for basic arithmetic 
(addition, subtraction, multiplication and division)"""

def add_num(a, b):
    """Adds the numbers a and b
    >>> add_num(10, 24)
    34
    >>> add_num(2.5, 2)
    4.5
    >>> add_num('x', 42)
    Traceback (most recent call last):
        ...
    TypeError: a must be an int or float
    
    >>> add_num(5, True)
    Traceback (most recent call last):
        ...
    TypeError: b must be an int or float

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an int or float")
    if type(b) not in [int, float]:
        raise TypeError("b must be an int or float")
    result = a + b
    return result

def main():
    num = add_num(23.4, 50)
    print(num)
    num2 = add_num(10, num)
    print(num2)

main()
