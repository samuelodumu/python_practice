#!/usr/bin/bash

def div(a, b):
    result = 0
    try:
        result = a / float(b)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    return result

print(div(10, 2)) # Should print 5.0
print(div(10, 0)) # Should print an error message
