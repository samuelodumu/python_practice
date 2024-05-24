#!/usr/bin/python3

class Time:
    def __init__(self, hour=0, minute=0, second=0):
        if type(hour) is not int:
            raise TypeError("Hour must be an int")
        if hour > 23:
            raise ValueError("Hour must be 23 or below")
        else:
            self.hour = hour

        if type(minute) is not int:
            raise TypeError("Minute must be an int")
        if minute > 59:
            raise ValueError("Minute must be 59 or below")
        else:
            self.minute = minute

        if type(second) is not int:
            raise TypeError("Minute must be an int")
        if second > 59:
            raise ValueError("Second must be 59 or below")
        else:
            self.second = second

    def __str__(self):
        return f"{self.hour}:{self.minute:02}:{self.second:02}"

    def __add__(self, other_time):
        new_time = Time()

        if self.second + other_time.second >= 60:
            new_time.second = (self.second + other_time.second) - 60
            self.minute += 1
        else:
            new_time.second = self.second + other_time.second

        if self.minute + other_time.minute >= 60:
            new_time.minute = (self.minute + other_time.minute) - 60
            self.hour += 1
        else:
            new_time.minute = self.minute + other_time.minute

        if self.hour + other_time.hour >= 24:
            new_time.hour = (self.hour + other_time.hour) - 24
        else:
            new_time.hour = self.hour + other_time.hour

        return new_time
        

def main():
    time1 = Time(2, 20, 30)
    time2 = Time(23, 41, 30)
    print(time1)
    print(f"{time1.__str__()} + {time2.__str__()} = {time1 + time2}")


main()
