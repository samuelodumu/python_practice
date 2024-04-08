#!/usr/bin/python3

class Robot:
    def __init__(self, name=None, build_year=2000):
        self.__name = name
        self.__build = build_year
    def say_hi(self):
        if self.__name:
            print(f"Hi, my name is {self.__name}")
        else:
            print("Hi, I'm without a name for now")

    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name

    def set_build(self, b_y):
        self.__build = b_y
    def get_build(self):
        return self.__build

if __name__ == "__main__":
    x = Robot("Milan", 1940)
    y = Robot("Casper", 2003)
    for a in [x, y]:
        a.say_hi()
        if a.get_name() == "Casper":
            a.set_build(2005)
        print(f"I was made in the year {a.get_build()}!")
