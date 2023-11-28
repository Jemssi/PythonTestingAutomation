import unittest
import test

class TestMathMethods(unittest.TestCase):

    def test_add(self):
        self.assertEqual(3, test.add(1, 2))
        self.assertEqual(10, test.add(3, 7))

    def test_multiply(self):
        self.assertTrue(50, test.multiply(5, 10))

    def test_power(self):
        self.assertEqual(256, test.power(2, 8))

if __name__ == '__main__':
    unittest.main()