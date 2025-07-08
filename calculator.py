print("Simple Calculator")
print("Choose operation: +, -, *, /")

operation = input("Enter operation: ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '+':
    print(f"Result: {num1 + num2}")
elif operation == '-':
    print(f"Result: {num1 - num2}")
elif operation == '*':
    print(f"Result: {num1 * num2}")
elif operation == '/':
    if num2 != 0:
        print(f"Result: {num1 / num2}")
    else:
        print("Cannot divide by zero.")
else:
    print("Invalid operation.")
