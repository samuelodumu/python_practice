#!/usr/bin/python3

# When you call a method of this object as myobject.method(arg1, arg2),
# this is automatically converted by Python into MyClass.method(myobject, arg1, arg2)
# - this is all the special self is about.

class Person:
    def say_hi(self):
        print('Hi, how are you?')

p = Person()
p.say_hi() # or we could say Person().say_hi()
