#!/usr/bin/python3


class Customer:
    """
    A sample customer class

    >>> from doctest_customer import Customer as C
    >>> c1 = C('Alex', 'Jay', 300)
    >>> c2 = C('Dan', 'Imba', 23500)
    >>> c1.customer_mail
    'Alex.Jay@email.com'
    >>> c2.customer_mail
    'Dan.Imba@email.com'
    >>> c1.customer_fullname
    'Alex Jay'
    >>> c2.customer_fullname
    'Dan Imba'
    >>> c1.p
    300
    >>> c2.p
    23500
    >>> c1.apply_discount()
    285.0
    >>> c2.apply_discount()
    22325.0
    """
    
    discount = 0.95

    def __init__(self, first_name, last_name, purchase):
        self.fn = first_name
        self.ln = last_name
        self.p = purchase

    @property
    def customer_mail(self):
        return f"{self.fn}.{self.ln}@email.com"
    @property
    def customer_fullname(self):
        return f"{self.fn} {self.ln}"

    def apply_discount(self):
        self.p = round(self.p * self.discount, 2)
        return self.p


if __name__ == "__main__":
    import doctest
    doctest.testmod()
