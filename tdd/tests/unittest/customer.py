#!/usr/bin/python3


class Customer:
    """A simple customer class"""

    discount = 0.95
    
    def __init__(self, first_name, last_name, purchase):
        self.f_n = first_name
        self.l_n = last_name
        self.p = purchase

    @property
    def customer_email(self):
        return f"{self.f_n}.{self.l_n}@gmail.com"

    @property
    def customer_full_name(self):
        return f"{self.f_n} {self.l_n}"

    def apply_discount(self):
        self.p = int(self.p * self.discount)

