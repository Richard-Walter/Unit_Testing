import unittest
import calc


class TestCalc(unittest.TestCase):

    # Test cases must start with test_
    def test_add(self):

        # result = calc.add(10, 5)
        self.assertEqual(calc.add(10, 5), 15)
        # Test some edge cases
        self.assertEqual(calc.add(-1, 1), 0)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_divide(self):
        self.assertEqual(calc.divide(10, 5), 2)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        self.assertEqual(calc.divide(5, 2), 2.5)
        # Test exception raised wen dividing by zero
        # self.assertRaises(ValueError, calc.divide, 10, 2)
        # Better to use context manager
        with self.assertRaises(ValueError):
            calc.divide(10, 0)

    def test_subtract(self):

        self.assertEqual(calc.subtract(10, 5), 5)
        self.assertEqual(calc.subtract(-1, 1), -2)
        self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):

        self.assertEqual(calc.multiply(10, 5), 50)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)


# Must include this directing the interpreter to use the main function built into unittest
if __name__ == '__main__':
    unittest.main()










