# Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation without a complex
# solution.
# Write unit tests for this function with QuadraticEquationTest class
# Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0

import unittest


def quadratic_equation(a, b, c):
    if a == 0:
        raise(ValueError)
    D = b * b - 4 * a * c
    if D < 0:
        return None
    x1 = (-b - D ** 0.5) / (2 * a)
    x2 = (-b + D ** 0.5) / (2 * a)
    return (x2, x1) if D > 0 else x1

class QuadraticEquationTest(unittest.TestCase):
    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            quadratic_equation(0, 10, 5)

    def test_D_0(self):
        self.assertEqual(quadratic_equation(1, -6, 9), 3.0)

    def test_D_positive(self):
        self.assertLess(quadratic_equation(1, -8, 12)[1], quadratic_equation(1, -8, 12)[0])

    def test_D_negative(self):
        self.assertFalse(quadratic_equation(5, 3, 7))

#Tests

print(quadratic_equation(2, 1, -1))#Expect (0.5, -1.0)
print(quadratic_equation(1, -4, 4))#Expect 2.0
print(quadratic_equation(4, 1, 2))#Expect None

try:
    quadratic_equation(0, 0, 0)
except ValueError:
    print('error')
#Expect error

print(count_tests > 3)#Expect True
print(failures)#Expect 0
print(errors)#Expect 0
print(cheater)#Expect False
print(skipped)#Expect 0
print(expectedFailures)#Expect 0