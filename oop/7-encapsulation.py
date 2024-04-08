#!/usr/bin/python3

class Robot:
    def __init__(self, name=None, build=None):
        self.name = name
        self.build = build
    def say_hi(self):
        if self.name:
            print(f"Hi, my name is {self.name}")
        else:
            print("Hi, I'm without a name for now")
        if self.build:
            print(f"I was made in {self.build}")
        else:
            print("My build year is not currently available")

    def set_name(self, name):
        self.name = name
    def get_name(self):
        return self.name

    def set_build(self, b_y):
        self.build = b_y
    def get_build(self):
        return self.build
x = Robot()
x.say_hi()
x.set_name('Matt')
x.set_build(1930)
x.say_hi()
