#!/usr/bin/python3

while True:
    try:
        a = int(input("Enter a number "))
        break
    except ValueError:
        print("Please enter a number (0 and above)...")

# Classes with an except clause 
# You can catch a specific exception and all its subclasses with a single except clause,
# but you cannot catch a more general exception with an except clause meant for a derived (more specific) exception:
class b(Exception):
    pass
class c(b):
    pass
class d(c):
    pass

for cls in [b, c, d]:
    try:
        raise cls()
    except d:
        print('d')
    except c:
        print('c')
    except b:
        print('b')
# if the except clauses were reversed (with except B first),
# it would have printed B, B, B — the first matching except clause is triggered
