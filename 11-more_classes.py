#!/usr/bin/python3

class Person:
    def __init__(self, name = None, age = None):
        self.name = name
        self.age = age

    def set_details(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f'person name is {self.name} and person age is {self.age}'

p1 = Person()
p1.set_details("George", 50)
print(p1.get_details())
p1.name = "evans"
print(p1.__dict__)
print(p1.__dir__())
