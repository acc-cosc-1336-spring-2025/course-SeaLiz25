#
import unittest
from src.homework.d_repetition.repetition import get_factorial
from src.homework.d_repetition.repetition import sum_odd_numbers
class Test_Config(unittest.TestCase):

    def test_get_factorial(self):
        self.assertEquals (get_factorial(4),24)
        self.assertEquals (get_factorial(5),120)
        self.assertEquals (get_factorial(6),120)

    def test_sum_odd_numbers(self):
        self.assertEquals (sum_odd_numbers(7), 15)
        self.assertEquals (sum_odd_numbers(9), 25)
        self.assertEquals (sum_odd_numbers(10), 25)


