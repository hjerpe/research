"""
Bug Fix Challenge: Simple Calculator with Edge Cases

This module contains a calculator with several bugs that both
Jules and Claude Code should be able to identify and fix.

Expected bugs:
1. Division by zero not handled
2. Integer division loses precision
3. Negative number square root crashes
4. Input validation missing
"""

import math


class Calculator:
    """A simple calculator with some bugs to fix."""

    def add(self, a, b):
        """Add two numbers."""
        return a + b

    def subtract(self, a, b):
        """Subtract b from a."""
        return a - b

    def multiply(self, a, b):
        """Multiply two numbers."""
        return a * b

    def divide(self, a, b):
        """Divide a by b."""
        # BUG: No division by zero check
        return a / b

    def power(self, a, b):
        """Raise a to the power of b."""
        return a ** b

    def square_root(self, a):
        """Calculate square root of a."""
        # BUG: No check for negative numbers
        return math.sqrt(a)

    def percentage(self, value, percent):
        """Calculate percentage of a value."""
        return (value * percent) / 100


def main():
    """Test the calculator with various inputs."""
    calc = Calculator()

    # Test basic operations
    print("Addition: 5 + 3 =", calc.add(5, 3))
    print("Subtraction: 10 - 4 =", calc.subtract(10, 4))
    print("Multiplication: 6 * 7 =", calc.multiply(6, 7))

    # These will cause errors:
    print("Division: 10 / 2 =", calc.divide(10, 2))
    # print("Division by zero:", calc.divide(10, 0))  # Uncomment to test bug

    print("Power: 2^8 =", calc.power(2, 8))
    print("Square root of 16 =", calc.square_root(16))
    # print("Square root of -4 =", calc.square_root(-4))  # Uncomment to test bug

    print("25% of 200 =", calc.percentage(200, 25))


if __name__ == "__main__":
    main()
