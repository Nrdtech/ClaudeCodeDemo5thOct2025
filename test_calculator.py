import unittest
import math
from calculator import (
    add, subtract, multiply, divide, power, modulo,
    get_number, get_operation, calculate
)


class TestArithmeticOperations(unittest.TestCase):
    """Test basic arithmetic operation functions."""

    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(2.5, 1.5), 4.0)

    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-5, 3), -8)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(5.5, 2.5), 3.0)

    def test_multiply(self):
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-5, 3), -15)
        self.assertEqual(multiply(0, 100), 0)
        self.assertEqual(multiply(2.5, 4), 10.0)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(7, 2), 3.5)
        self.assertAlmostEqual(divide(1, 3), 0.333333, places=5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError) as context:
            divide(10, 0)
        self.assertEqual(str(context.exception), "Cannot divide by zero")

    def test_power(self):
        self.assertEqual(power(2, 3), 8)
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(2, -1), 0.5)
        self.assertEqual(power(10, 2), 100)

    def test_modulo(self):
        self.assertEqual(modulo(10, 3), 1)
        self.assertEqual(modulo(7, 2), 1)
        self.assertEqual(modulo(10, 5), 0)
        self.assertEqual(modulo(-10, 3), 2)

    def test_modulo_by_zero(self):
        with self.assertRaises(ValueError) as context:
            modulo(10, 0)
        self.assertEqual(str(context.exception), "Cannot perform modulo by zero")


class TestCalculate(unittest.TestCase):
    """Test the calculate dispatcher function."""

    def test_calculate_add(self):
        self.assertEqual(calculate(5, '+', 3), 8)

    def test_calculate_subtract(self):
        self.assertEqual(calculate(10, '-', 4), 6)

    def test_calculate_multiply(self):
        self.assertEqual(calculate(6, '*', 7), 42)

    def test_calculate_divide(self):
        self.assertEqual(calculate(15, '/', 3), 5)

    def test_calculate_power(self):
        self.assertEqual(calculate(2, '**', 4), 16)

    def test_calculate_modulo(self):
        self.assertEqual(calculate(17, '%', 5), 2)

    def test_calculate_invalid_operation(self):
        result = calculate(5, '&', 3)
        self.assertIsNone(result)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions."""

    def test_large_numbers(self):
        self.assertEqual(add(1e10, 1e10), 2e10)
        self.assertEqual(multiply(1e5, 1e5), 1e10)

    def test_very_small_numbers(self):
        result = add(1e-10, 1e-10)
        self.assertAlmostEqual(result, 2e-10, places=15)

    def test_mixed_integer_float(self):
        self.assertEqual(add(5, 3.5), 8.5)
        self.assertEqual(multiply(4, 2.5), 10.0)


if __name__ == '__main__':
    unittest.main()
