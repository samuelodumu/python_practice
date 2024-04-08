#!/usr/bin/python3

class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def say_hi(self):
        print(f'Hello, you must be {self.name} and you are {self.age}!')

p1 = Person('Samuel', 19).say_hi()
