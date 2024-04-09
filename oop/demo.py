#!/usr/bin/python3

class Our_class():  
    def __init__(self, a):
        self.ourAtt = a

    @property
    def ourAtt(self):
        return self.__ourAtt

    @ourAtt.setter
        def ourAtt(self, a):
        if a < 0:
            self.__ourAtt = 0
        elif a > 1000:
            self.__ourAtt = 1000
        else:
            self.__ourAtt = a


x = Our_class(100090)
print(x.ourAtt)
