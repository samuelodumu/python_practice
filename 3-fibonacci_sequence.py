#!/usr/bin/python3

def fib(n):
    """Return a list containing the Fibonacci series up to n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    print(result)
        
fib(200)