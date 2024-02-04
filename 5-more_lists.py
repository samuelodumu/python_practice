#!/usr/bin/python3

# More list methods and list comprehension

fruits = ['Banana', 'Carrot', 'Orange', 'Pawpaw', 'Guava', 'Orange', 'Garden egg', 'Apple']
print(fruits)

fruits.pop() # Removes the last element of the list and returns it.
             # When given an index argument it removes the element at that index.
print(fruits)

fruits.reverse() # reverses the list
print(fruits)

fruits.insert(3, 'Apple') # inserts 'Apple' element before index 3
print(fruits)

fruits.sort() # sorts the elements of the string (alphabetically in this case because we're dealing with strings)
print(fruits)

print(fruits.count('Orange')) # returns how many times 'Orange' occours in list

fruits.remove('Carrot') # removes the 'Carrot' element

print(fruits, '\n')

# List comprehension AKA list shorthand
squares = [(x, x**2) for x in range(2, 11)]
print(squares)
from math import pi
digits_of_pi = [str(round(pi, x)) for x in range(1, 6)]
print(digits_of_pi)
