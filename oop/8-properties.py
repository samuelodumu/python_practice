#!/usr/bin/python3

class P:
    def __init__(self, x):
        self.x = x

    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        elif x > 1000:
            self.__x = 1000
        else:
            self.__x = x


# New class to show that a property could be based on two or more attributes
class Robot():
    def __init__(self, name="", build_year=1990, p_phy=0.5, p_psy=0.5):
        self.name = name
        self.b_y = build_year
        self.__p_phy = p_phy
        self.__p_psy = p_psy

    @property
    def condition(self):
        s = self.__p_phy + self.__p_psy
        if s <= -1:
            return "I feel miserable!"
        if s <= 0:
            return "I feel bad!"
        if s <= 0.5:
            return "Could be worse!"
        if s <= 1:
            return "Seems to be okay!"
        else:
            return "Great!"

def main():
    if __name__ == "__main__":
        x = Robot("Marv", 2003, 0.2, 0.5)
        y = Robot("Joli", 1983, -0.4, 0.6)
        print(x.condition)
        print(y.condition)


        p1 = P(1032)
        print(p1.x)
        p2 = P(43)
        print(p2.x)
        p3 = P(-29)
        print(p3.x)
        p3.x = 200
        print(p3.x)

main()
