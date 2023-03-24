from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        self.assertEqual(calc.add(1,2),3)

    def test_subtract(self):
        self.assertEqual(calc.subtract(10,15),5)