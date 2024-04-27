#!/usr/bin/python3

import unittest
from customer import Customer

class TestCustomer(unittest.TestCase):

    def setUp(self):
        self.customer_1 = Customer("Brad", "Pitt", 3000)
        self.customer_2 = Customer("Alex", "Hormozi", 8000)

    def test_mail(self):
        self.assertEqual(self.customer_1.customer_email, 'Brad.Pitt@gmail.com')
        self.assertEqual(self.customer_2.customer_email, 'Alex.Hormozi@gmail.com' )

    def test_name(self):
        self.assertEqual(self.customer_1.customer_full_name, 'Brad Pitt')
        self.assertEqual(self.customer_2.customer_full_name, 'Alex Hormozi')
    
    def test_discount(self):
        self.customer_1.apply_discount()
        self.customer_2.apply_discount()
        
        self.assertEqual(self.customer_1.p, 2850)
        self.assertEqual(self.customer_2.p, 7600)
