#!/usr/bin/python3

def print_name(obj):
    print(f"Hi, I am {obj.name}!")

class Robot:
    sayhi = print_name
x = Robot()
x.name = "Jonas"
# print_name(x)
Robot.sayhi(x) # same as x.sayhi()
x.sayhi()
