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

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number")

def get_operation():
    while True:
        operation = input("Select operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Error: Unsupported operation. Please select +, -, *, or /")

def calculate(num1, operation, num2):
    if operation == '+':
        return add(num1, num2)
    elif operation == '-':
        return subtract(num1, num2)
    elif operation == '*':
        return multiply(num1, num2)
    elif operation == '/':
        return divide(num1, num2)

def main():
    print("=== Simple Python Calculator ===")

    num1 = get_number("Enter first number: ")
    operation = get_operation()
    num2 = get_number("Enter second number: ")

    try:
        result = calculate(num1, operation, num2)
        print(f"\n{num1} {operation} {num2} = {result}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
