#!/usr/bin/python3

class SchoolMember():
    """Remember members of the school"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(f"Initialized school member {self.name}")

    def tell(self):
        """Prints the details of a school member"""
        print(f"Name:{self.name} Age:{self.age}", end = " ")

class Teacher(SchoolMember):
    """Represents a teacher"""
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print(f"Initialized teacher {self.name}")

    def tell(self):
        """Prints details of a teacher"""
        SchoolMember.tell(self)
        print(f"Salary: {self.salary}")

class Student(SchoolMember):
    """Represents a student"""
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print(f"Initialized student {self.name}")

    def tell(self):
        SchoolMember.tell(self)
        print(f"Marks: {self.marks}")


t = Teacher("Mr. Shakriar", 30, 50000)
s = Student("Hans", 14, 80)

print()

members = [t, s]
for member in members:
    member.tell()
