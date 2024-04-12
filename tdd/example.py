#!/usr/bin/python3

"""Module that supplies one function, factorial
>>> factorial(6)
720
"""

def factorial(n):
    """Returns the factorial of a n, an exact integer >= 0
    >>> [factorial(x) for x in range(6)]
    [1, 1, 2, 6, 24, 120]

    >>> factorial(-2)
    Traceback (most recent call last):
        ...
    ValueError: n must be >= 0

    Floats are ok, but the float must be an exact integer:
    >>> factorial(5.1)
    Traceback (most recent call last):
        ...
    ValueError: n must be exact integer

    >>> factorial(1e100)
    Traceback (most recent call last):
        ...
    OverflowError: n is too large
    """
    import math
    if not n >= 0:
        raise ValueError("n must be >= 0")
    if math.floor(n) != n:
        raise ValueError("n must be exact integer")
    if n + 1 == n:
        raise OverflowError("n is too large")
    result = 1
    factor = 2

    while factor <= n:
        result *= factor
        factor += 1
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()
