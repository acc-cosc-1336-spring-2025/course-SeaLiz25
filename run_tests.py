from tests.homework.c_decisions import tests_decisions

suite = unittest.TestLoader().loadTestsFromModule(tests_decisions)
unittest.TextTestRunner(verbosity=2).run(suite)

import unittest
from tests.homework.c_decisions import tests_decisions
from src.homework.c_decisions.decisions import get_faculty_rating, get_options_ratio

class Test_Config(unittest.TestCase):

 def test_get_options_ratio(self):
        self.assertEqual(get_options_ratio(5, 20), 0.25)
        self.assertEqual(get_options_ratio(10, 20), 0.5)


