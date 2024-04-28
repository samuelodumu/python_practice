#!/usr/bin/python3

class Robot:
    def __init__(self, name, build_year):
        self.name = name
        self.by = build_year
    def __repr__(self):
        return f"Robot('{self.name}', {self.by})"
    def __str__(self):
        return f"Name: {self.name}, Build Year: {self.by}"

if __name__ == "__main__":
    x = Robot("Dame", 1956)
    x_str = str(x)
    x_repr = repr(x)
    print(x_repr, type(x_repr))
    new = eval(x_repr)
    print(f"Type of new 'eval(x_repr)': {type(new)}")
    # gettatr retrieves the attribute from an object, in this case 'energy' from 'x'. 
    # If the attribute doesn't exist it raises an error except a third parameter is 
    # specified which would be printed instead.
    print(getattr(x, "energy", 'energy is not an attribute in x'))
    print(x.__dict__)
    print(Robot.__dict__)
