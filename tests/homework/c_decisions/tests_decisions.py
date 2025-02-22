import unittest
from src.homework.c_decisions.decisions import get_options_ratio
from src.homework.c_decisions.decisions import get_faculty_rating

class Test_Config(unittest.TestCase):

def test_get_options_ratio(self):
    self.assertEqual(get_options_ratio( 5, 20), 0.25)
    self.assertEqual(get_options_ratio( 10, 20), 0.5)

def get_faculty_rating(self):
    result = (If get_options_ratio >=.9 <1, excellent)
    result = (if get_options_ratio >.8, Very Good)
    result = (if get_options_ratio >.7, Good)
    result = (if get_options_ratio >.6, Needs improvement)
    result = (if get_options_ratio >=0 <.59, Unacceptable)