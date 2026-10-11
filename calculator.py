import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def power(x, y):
    return x ** y

def modulo(x, y):
    if y == 0:
        raise ValueError("Cannot perform modulo by zero")
    return x % y

def get_number(prompt):
    while True:
        try:
            value = float(input(prompt))
            if not math.isfinite(value):
                print("Error: Please enter a finite number (not infinity or NaN)")
                continue
            return value
        except ValueError:
            print("Error: Please enter a valid number")

def get_operation():
    while True:
        operation = input("Select operation (+, -, *, /, **, %): ").strip()
        if operation in ['+', '-', '*', '/', '**', '%']:
            return operation
        else:
            print("Error: Unsupported operation. Please select +, -, *, /, **, or %")

def calculate(num1, operation, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)
    elif operation == '**':
        return power(num1, num2)
    elif operation == '%':
        return modulo(num1, num2)

def main():
    print("=== Simple Python Calculator ===")
    history = []

    while True:
        num1 = get_number("Enter first number: ")
        operation = get_operation()
        num2 = get_number("Enter second number: ")

        try:
            result = calculate(num1, operation, num2)
            calculation = f"{num1} {operation} {num2} = {result}"
            print(f"\n{calculation}\n")
            history.append(calculation)
        except ValueError as e:
            print(f"Error: {e}\n")

        while True:
            again = input("Calculate again? (y/n): ").strip().lower()
            if again in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'")

        if again == 'n':
            break

    if history:
        print("\n=== Calculation History ===")
        for i, calc in enumerate(history, 1):
            print(f"{i}. {calc}")

if __name__ == "__main__":
    main()
