#!/usr/bin/python3

# A set is an unordered collection with no duplicate elements.
# Basic uses include membership testing and eliminating duplicate entries
# Set objects also support mathematical operations like union (|), intersection(&), difference(-), and symmetric difference:

a = set('utopia')
b = set('dystopia')

print('a = {}'.format(a))
print('b = {}'.format(b))

print("'d' in set(a) = {}".format('d' in a)) # False
print("'d' in set(b) = {}".format('d' in b)) # True


print("a - b = {}".format(a - b))
print("b - a = {}".format(b - a))
print("a | b = {}".format(a | b))
print("a & b = {}".format(a & b))
