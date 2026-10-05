# Python Calculator

A beginner-friendly console calculator application that performs basic arithmetic operations.

## Features

- **Basic Operations**: Addition (+), Subtraction (-), Multiplication (*), Division (/)
- **Input Validation**: Validates numeric input with user-friendly error messages
- **Error Handling**: 
  - Handles non-numeric input gracefully
  - Prevents division by zero
  - Rejects unsupported operations
- **Simple & Readable**: Designed for beginners to understand and learn from

## Requirements

- Python 3.x

## Usage

Run the calculator from the command line:

```bash
python3 calculator.py
```

### Example Session

```
=== Simple Python Calculator ===
Enter first number: 10
Select operation (+, -, *, /): +
Enter second number: 5

10.0 + 5.0 = 15.0
```

## Supported Operations

| Operation | Symbol | Example |
|-----------|--------|---------|
| Addition | + | 10 + 5 = 15 |
| Subtraction | - | 10 - 5 = 5 |
| Multiplication | * | 10 * 5 = 50 |
| Division | / | 10 / 5 = 2 |

## Error Handling

The calculator handles the following error scenarios:

1. **Non-numeric Input**: If you enter text instead of a number, you'll be prompted to try again
   ```
   Enter first number: abc
   Error: Please enter a valid number
   Enter first number: 10
   ```

2. **Unsupported Operation**: Only +, -, *, / are allowed
   ```
   Select operation (+, -, *, /): %
   Error: Unsupported operation. Please select +, -, *, or /
   Select operation (+, -, *, /): +
   ```

3. **Division by Zero**: Attempting to divide by zero displays an error
   ```
   Enter first number: 10
   Select operation (+, -, *, /): /
   Enter second number: 0
   Error: Cannot divide by zero
   ```

## Code Structure

- `add(x, y)`: Returns the sum of two numbers
- `subtract(x, y)`: Returns the difference of two numbers
- `multiply(x, y)`: Returns the product of two numbers
- `divide(x, y)`: Returns the quotient of two numbers (with zero-check)
- `get_number(prompt)`: Handles user input validation for numbers
- `get_operation()`: Handles operation selection validation
- `calculate(num1, operation, num2)`: Performs the calculation
- `main()`: Main program flow

## License

Open source - Feel free to use and modify as needed for learning purposes.
