#!/usr/bin/python3

# The map(func, seq) function takes two arguments: the first being a function or a
# lambda operation and the second being a sequence e.g. a list
# map() returns a new list or iterable whose elements are the result of performing
# the function on each element of the sequence:

op = lambda x: x**3
num = [2, 4, 5, 6, 8]
cubes = list(map(op, num))
print(cubes)

# map can also work with multiple lists as sequences like so:
a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]

new_list = list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))
print(new_list)

# If one list has fewer elements than the others, map will stop when the shortest list has been consumed
a.pop()

new_list = list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))
print(new_list)
 
# In the examples above the parameter x gets its values from the list a, while y gets its values from b, and z from list c.
