#!/usr/bin/python3

while True:
    print("Enter your age: ")

    age = input()

    try:
        age = int(age)
    except:
        print("age must be a number")
        continue
    if age < 1:
        print("age must be positive")
        continue
    if age > 120:
        print("please enter a human age")
        continue
    break
