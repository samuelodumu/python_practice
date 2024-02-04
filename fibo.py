#!/usr/bin/python3

def fib(n):
    """Return a list containing the Fibonacci series up to n."""
    a, b = 0, 1
    result = []
    while a < n:
        result.append(a)
        a, b = b, a+b
    print(result)

if __name__ == '__main__':
    import sys
    fib(int(sys.argv[1]))

