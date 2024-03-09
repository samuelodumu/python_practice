#!/usr/bin/python3

class Room():
    
    people = 0

    def __init__(self, name):
        self.name = name

        print(f"{self.name} has entered the lobby")
        Room.people += 1
    
    def say_hi(self):
        print(f"Hi, they call me {self.name}")
    
    def exit(self):
        print(f"{self.name} has left the lobby")
        Room.people -= 1

        if Room.people == 0:
            print("There is no one left in the lobby")
        elif Room.people == 1:
            print(f"There is {Room.people} person in the lobby")
        else:
            print(f"There are {Room.people} people in the lobby")
        
    @classmethod
    def how_many(cls):
        print(f"There are {Room.people} people in the lobby")


person1 = Room("Andy")
person2 = Room("Simone")
person3 = Room("Dina")
person4 = Room("Daniel")
Room.how_many()
print("===============================")
person1.say_hi()
person2.say_hi()
person3.say_hi()
person4.say_hi()
print("===============================")
person1.exit()
person3.exit()
print("===============================")
person5 = Room("Jake")
Room.how_many()
