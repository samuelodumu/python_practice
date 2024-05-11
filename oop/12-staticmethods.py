#!/usr/bin/python3

# In the python datetime module we have weekday methods where Monday equals 0 and Sunday equals 6 
# and all the other days are in between

class Employee:
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

    @classmethod # declaration of a class method
    def set_raise_amt(cls, value):
        cls.raise_amt = value

    @staticmethod # declaration of a static method
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True

if __name__ == '__main__':
    import datetime
    
    my_date = datetime.date(2024, 5, 10)
    
    print(Employee.is_workday(my_date))
