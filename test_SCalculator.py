import unittest
import SCalculator
class Test(unittest.TestCase):
    def test_addition(self):
        result = SCalculator.addition(10, 20)
        self.assertEqual(result, 30)


    def test_subtraction(self):
        result = SCalculator.subtraction(10, 5)
        self.assertEqual(result, 5)


    def test_multiplication(self):
        result = SCalculator.multiplication(10, 20)
        self.assertEqual(result, 200)


    def test_division(self):
        result = SCalculator.division(10, 2)
        self.assertEqual(result, 5)


