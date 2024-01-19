#!/usr/bin/python3

# The break statement breaks out of the innermost enclosing for or while loop.
# A for or while loop can include an else clause.
# In a for loop, the else clause is executed after the loop reaches its final iteration.
# In a while loop, it’s executed after the loop’s condition becomes false.
# In either kind of loop, the else clause is not executed if the loop was terminated by a break.
# This is exemplified in the following for loop, which searches for prime numbers in the range

for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')


# The continue statement, also borrowed from C, continues with the next iteration of the loop:

for num in range (2, 10):
    if num % 2 == 0:
        print('found an even number', num)
        continue
    print('found an odd number', num)
