#!/usr/bin/python3

class Employee:

    num_of_emps = 0
    raise_amt = 1.1

    def __init__(self, first_name, last_name, salary):
        self.first = first_name
        self.last = last_name
        self.pay = salary
        self.fullname = f"{self.first} {self.last}"
        self.num_of_emps += 1
        print(f"I am {self.fullname} and {self.pay} is my salary")

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
        print(f"{self.fullname}'s new pay is {self.pay}")
    
    def email(self):
        print(f"{self.first}.{self.last}@email.com")
        
    @classmethod
    def set_raise_amt(cls, value):
        cls.raise_amt = value

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)


if __name__ == "__main__":
    
    emp1 = Employee('Janet', 'Moore', 32000)
    emp2 = Employee('Jordan', 'Greenwood', 20000)
    emp2.apply_raise()
    print(f"Current raise amount: {emp1.raise_amt}")
    Employee.set_raise_amt(1.3)
    print(f"changing raise amount changed to 1.3...")
    print(f"emp1.raise_amt: {emp1.raise_amt}")
    print(f"emp2.raise_amt: {emp2.raise_amt}")
    print('================================')
    emp_str1 = 'John-Doe-70000'
    emp_str2 = 'Steve-Smith-30000'
    emp_str3 = 'Jane-Doe-90000'
    new_emp_1 = Employee.from_string(emp_str1)
    new_emp_1.email()
    new_emp_2 = Employee.from_string(emp_str2)
    new_emp_2.email()
    new_emp_3 = Employee.from_string(emp_str3)
    new_emp_3.email()

