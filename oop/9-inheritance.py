#!/usr/bin/python3
"""Contains Hospital, doctor and patient classes"""


class HospitalMember():
    """Default class for someone in the hospital"""

    def __init__(self, name, age):
        """Initializing members"""
        self.name = name
        self.age = age

    def tell(self):
        """prints the details of hospital member"""
        print(f"Name: {self.name}, Age: {self.age}", end=" ")


class Staff(HospitalMember):
    """Class defining staff roles and salaries"""

    def __init__(self, name, age, role, salary):
        """Initializing staff"""
        HospitalMember.__init__(self, name, age)
        self.role = role
        self.pay = salary
        print(f"Initializing staff {self.name}")

    def tell(self):
        """prints the staff's details"""
        HospitalMember.tell(self)
        print(f"Role: {self.role}, Salary: ${self.pay}")


class Patient(HospitalMember):
    """Initializing patient diagnosis and weight"""

    def __init__(self, name, age, weight, diagnosis):
        """Initializing patients"""
        HospitalMember.__init__(self, name, age)
        self.weight = weight
        self.diag = diagnosis
        print(f"Initializing patient {self.name}")

    def tell(self):
        """prints the patient's details"""
        HospitalMember.tell(self)
        print(f"Weight: {self.weight}kg, Diagnosis: {self.diag}")

def main():
    p1 = Patient("Lanre", 34, 102, "Pancreantitis")
    s1 = Staff("Jared", 28, "Doctor", 150000)
    for a in [p1, s1]:
        a.tell()

if __name__ == '__main__':
    main()

















