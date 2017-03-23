import unittest
import rpn
class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate('1 1 +')
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate('5 3 -')
        self.assertEqual(2, result)
    def test_exponent(self):
        result = rpn.calculate('5 2 ^')
        self.assertEqual(25, result)
    def test_multiply(self):
        result = rpn.calculate('5 2 *')
        self.assertEqual(10, result)
