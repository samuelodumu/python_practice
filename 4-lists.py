#!/usr/bin/python3

# Lists might contain items of different types, but usually the items all have the same type
print('SQUARES')
squares = [1, 4, 9, 16, 25, 36, 49, 64, 80, 100]
print(squares)
print(squares[-4:]) # makes new list of sub elements
print(squares[3]) # gets element at index number
print(squares[:], '\n') # returns a shallow copy of the list

print("But 9^2 is 81 not 80, and let's add the square of 11 while at it\n")
squares.append(121) # adds another element to the end of the list
squares[8] = 81 # changes element at given index (unlike in strings where characters are immutable)
print(squares, '\n')

print('LETTERS')
letters = ['a', 'b', 'c', 'd', 'e']
print(letters)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:

letters[1:3] = ['B', 'C']
print(letters)

letters[1:3] = [] # deletes the elements fom index 1 - 3
print(letters)

# Lists can also be nested; a list can contain one or more lists inside it
x = [squares, letters]
print(x)
print(x[0][6]) # prints the 7th element of the 1st nested list
print(x[1][1]) # prints the 2nd element of the 2nd nested list
