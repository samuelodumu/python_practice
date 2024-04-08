#!/usr/bin/python3


class Numbers:
    def __init__(self):
        self.n = []

    def add_items(self, num):
        self.n.append(num)


# print(dir(Numbers))

odd = Numbers()
even = Numbers()
print(odd.__dir__())

print(even.n)

odd.add_items(1)
odd.add_items(3)
print(odd.n)

even.add_items(2)
even.add_items(4)
print(even.n)
