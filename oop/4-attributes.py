#!/usr/bin/python3

class Robot:
    pass

x = Robot()
x.name =  "Dame"
x.build_year = "1956"

print(x.name)
print(x.build_year)
print(x.__dict__)
Robot.name = "Charles"
print(Robot.name)
print(getattr(x, "energy", 100))
print(Robot.__dict__)

def f(x):
    f.counter = getattr(f, 'counter', 0) + 1
    return "monty"
for i in range(10):
    f(i)
print(f.counter)
