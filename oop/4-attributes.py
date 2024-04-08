#!/usr/bin/python3

class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.by = build_year
    def __repr__(self):
        return f"Robot('{self.name}', {self.by})"

if __name__ == "__main__":
    x = Robot("Dame", 1956)
    x_str = str(x)
    print(x_str)
    print(f"Type of x_str: {type(x_str)}")
    new = eval(x_str)
    print(f"Type of new 'eval(x_str)': {type(new)}")

    print(getattr(x, "energy", 100))
    print(x.__dict__)
    print(Robot.__dict__)
