#!/usr/bin/python3

# every object refers to its class via the self.__class__ attribute
class Robot():
    """Represents a robot, with a name."""

    #class variable to count the number of robots
    population = 0

    def __init__(self, name):
        """Initializes robots"""
        
        self.name = name

        print(f"Initializing {self.name}")
        Robot.population += 1

    def kill_bot(self):
        """Delete a bot"""

        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print("That was the last one")
        else:
            print("We have {:d} bots left".format(Robot.population))

    def say_hi(self):
        """Make a bot say hi"""

        print(f"Hello, I'm {self.name}")

    @classmethod
    def how_many(cls):
        """Tracks how many bots are left"""
        print(f"There are {cls.population} robots active")


"""
droid1 = Robot('DR 47')
droid2 = Robot('APA 1')
droid3 = Robot('JB 007')

Robot.how_many()
droid1.say_hi()
droid1.kill_bot()
droid3.kill_bot()
droid4 = Robot('Arian')
Robot.how_many()
"""
help(Robot)
