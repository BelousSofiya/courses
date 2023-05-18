# Create class Worker with fields name and salary. If salary negative raise ValueError
# Create a method get_tax_value() that calculate tax from salary . Tax must be calculate like "progressive tax" with next
# step:
# less then 1000 - 0%
# 1001 - 3000 - 10%
# 3001 - 5000 - 15%
# 5001 - 10000 - 21%
# 10001 - 20000 - 30%
# 20001 - 50000 - 40%
# more than 50000 - 47%
# Please create WorkerTest class with unitest to the class Worker. Try to use setUp and tearDown methods. Don`t use
# assertRaises in tests.

import unittest


class Worker:
    def __init__(self, name, salary=1000):
        if salary < 0:
            raise ValueError
        self.name = name
        self.salary = salary

    def get_tax_value(self):
        if self.salary <= 1000:
            return 0.0
        elif 1000 < self.salary <= 3000:
            return (self.salary - 1000) * 0.1
        elif 3001 < self.salary <= 5000:
            return 0.1 * (3000 - 1000) + 0.15 * (self.salary - 3000)
        elif 5000 < self.salary <= 10000:
            return 0.1 * (3000 - 1000) + 0.15 * (5000 - 3000) + 0.21 * (self.salary - 5000)
        elif 10001 < self.salary <= 20000:
            return 0.1 * (3000 - 1000) + 0.15 * (5000 - 3000) + 0.21 * (10000 - 5000) + 0.3 * (self.salary - 10000)
        elif 20001 < self.salary <= 50000:
            return 0.1 * (3000 - 1000) + 0.15 * (5000 - 3000) + 0.21 * (10000 - 5000) + 0.3 * (20000 - 10000) + 0.4 * (
                        self.salary - 20000)
        elif 50001 < self.salary:
            return 0.1 * (3000 - 1000) + 0.15 * (5000 - 3000) + 0.21 * (10000 - 5000) + 0.3 * (20000 - 10000) + 0.4 * (
                        50000 - 20000) + 0.47 * (self.salary - 50000)

class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("w1")

    def test_salary_1000(self):
        self.assertEqual(self.worker.get_tax_value(), 0)

    def test_salary_10000(self):
        self.worker.salary = 10000
        self.assertEqual(self.worker.get_tax_value(), 1550.0)

    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(self.worker.salary, 10000)

    def tearDown(self):
        self.worker = None

#Tests

print(failures)#Expect 0
print(expectedFailures)#Expect 1

worker = Worker("Vasia")
print(worker.get_tax_value())#Expect 0.0

worker = Worker("Petia", 1000)
print(worker.get_tax_value())#Expect 0.0

worker = Worker("Natasha", 1001)
print(worker.get_tax_value())#Expect 0.1

worker = Worker("Vika", 100000)
print(worker.get_tax_value())#Expect 40050.0