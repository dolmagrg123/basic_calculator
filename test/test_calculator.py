import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        # Create a new instance of the Calculator class before each test
        self.calculator = Calculator()

    def test_add(self):
        # Test the add method
        self.assertEqual(self.calculator.add(5, 3), 8)  # Check if 5 + 3 = 8

    def test_subtract(self):
        # Test the subtract method
        self.assertEqual(self.calculator.subtract(10, 3), 7)  # Check if 10 - 3 = 7

    def test_multiply(self):
        # Test the multiply method
        self.assertEqual(self.calculator.multiply(4, 3), 12)  # Check if 4 * 3 = 12

    def test_divide(self):
        # Test the divide method
        self.assertEqual(self.calculator.divide(10, 2), 5)  # Check if 10 / 2 = 5
        self.assertEqual(self.calculator.divide(10, 0), "Error: Division by zero")  # Check division by zero error

if __name__ == '__main__':
    unittest.main()  # Run the unit tests
