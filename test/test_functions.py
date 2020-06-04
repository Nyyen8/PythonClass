"""
Program: test_functions.py
Author: Paul Elsea
Last Modified: 06/04/2020

The purpose of this program is to test the
convert_to_months functions in campter_age_input.py.
"""

import unittest
from main import camper_age_input
'''These allow the tests to access the function'''

class FunctionTestCase(unittest.TestCase):

    def test_convert_to_months_pass(self):
        self.assertEqual(36, camper_age_input.convert_to_months(3))
        '''This test checks to see if the functions returns a result of 36, and passes if that is true'''

    def test_convert_to_months_fail(self):
        self.assertNotEqual(36, camper_age_input.convert_to_months(1))
        '''This test checks to see if the functions doesn't return 36, and passes if that is true'''

if __name__ == '__main__':
    unittest.main()