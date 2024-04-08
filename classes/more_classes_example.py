#!/usr/bin/python3

class Car:

    countCars = 0
    def __init__(self, brand, model, color, weight):
        print(f"This is a {color} {brand} {model}")
        self.brand = brand
        self.model =  model
        self.color = color
        self.weight = weight
        countCars += 1

    def drive(self):
        print(f"driving the {self.brand} {self.model} now...")

    def getprice(self, discount=1):
        print(f"The price of the {self.brand} {self.model} is ${self.weight * 100 * discount}")

c1 = Car("Toyota", "Corolla", "Grey", 3239)
c2 = Car("Vibe", "Pontiac", "Red", 9402)
c3 = Car("Mercedes", "Benz", "White", 5889)
c2.drive()
c3.getprice(0.9)
print(f"")Car.countCars

# print(c1.__dir__())
