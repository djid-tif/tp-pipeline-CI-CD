class SimpleMath:
    @staticmethod
    def addition(a, b):
        return a + b


import unittest


class TestSimpleMath(unittest.TestCase):
    def test_addition(self):
        result = SimpleMath.addition(1, 2)
        self.assertEqual(result, 3)
