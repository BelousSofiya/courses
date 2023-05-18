# You have function divide
def divide(num_1, num_2):
    return float(num_1)/num_2
# Please, write the code with unit tests for the function "divide":
# minimum 3 tests
# must chek all flows
# all test must be pass
# no failures
# no skip

import unittest

class DivideTest(unittest.TestCase):
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)

    def test_division_string(self):
        with self.assertRaises(ValueError):
            divide("fghfg", 1)

    def test_division_by_string(self):
        with self.assertRaises(TypeError):
            divide(2, "cbc")

    def test_division_normal(self):
        self.assertEqual(divide(10, 5), 2)

#Tests

# count_tests >= 3#Expect True
# failures#Expect 0
# errors#Expect 0
# skipped#Expect 0
# expectedFailures#Expect 0
# expectRaisesError#Expect True

