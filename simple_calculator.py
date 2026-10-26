
# Simple Calculator
# This program performs basic arithmetic operations.

try:
    # Take two numbers as input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Display the available operations
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Accept the user's choice
    choice = input("Enter your choice (1-4): ")

    # Perform the selected operation
    if choice == "1":
        result = num1 + num2
        print("Result:", result)

    elif choice == "2":
        result = num1 - num2
        print("Result:", result)

    elif choice == "3":
        result = num1 * num2
        print("Result:", result)

    elif choice == "4":
        # Check whether the divisor is zero
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print("Result:", result)

    else:
        print("Invalid choice. Please select 1-4.")

# Handle invalid numerical input
except ValueError:
    print("Error: Please enter valid numbers.")
