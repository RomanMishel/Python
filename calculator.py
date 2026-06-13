def calculator():
    print("Choose your operation:")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    operation = int(input())
    print("Enter your first number:")
    a = int(input())
    print("Enter your second number:")
    b = int(input())

    if operation == 1:
        result = a + b
        operation = "+"

    elif operation == 2:
        result = a - b
        operation = "-"

    elif operation == 3:
        result = a * b
        operation = "*"

    elif operation == 4:
        result = a / b
        operation = "/"

    else:
        print("Invalid operation.")
        return

    print(f"{a} {operation} {b} = {result}")
calculator()