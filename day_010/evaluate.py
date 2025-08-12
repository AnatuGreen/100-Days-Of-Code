import sys
from unittest import TestCase
from exercise import is_leap_year  # Import is_leap_year function only (will fail if not declared)

class Evaluate(TestCase):

    def test_leap_year_2400(self):
        self.assertEqual(True, is_leap_year(2400), "2400 is a leap year")

    def test_not_leap_year_1989(self):
        self.assertEqual(False, is_leap_year(1989), "1989 is not a leap year")

    def test_leap_year_2000(self):
        self.assertEqual(True, is_leap_year(2000), "2000 is a leap year")

    def test_not_leap_year_2100(self):
        self.assertEqual(False, is_leap_year(2100), "2100 is not a leap year")