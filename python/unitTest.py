import unittest

# import calculator
# class calculator:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     @classmethod
#     def plus(cls, x, y):
#         return x + y
#
#     @classmethod
#     def minus(cls, x, y):
#         return x - y
c = calculator
class CalculatorTestCase(unittest.TestCase):
    def setUp(self):
        self.args = (3, 2)

    def tearDown(self):
        self.args = None

    def test_plus(self):
        expected = 5
        result = plus(*self.args);
        self.assertEqual(expected, result)

    def test_minus(self):
        expected = 1
        result = minus(*self.args);
        self.assertEqual(expected, result)

def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

suite = (unittest.TestLoader().loadTestsFromTestCase(CalculatorTestCase))
unittest.TextTestRunner(verbosity=2).run(suite)

