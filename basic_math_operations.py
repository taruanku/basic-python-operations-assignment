# basic_math_operations.py

def main():
    try:
        # Take input from user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Perform basic operations
        addition = num1 + num2
        subtraction = num1 - num2
        multiplication = num1 * num2

        # Division with zero check
        if num2 != 0:
            division = num1 / num2
        else:
            division = "Undefined (Cannot divide by zero)"

        # Display results
        print(f"Addition: {addition}")
        print(f"Subtraction: {subtraction}")
        print(f"Multiplication: {multiplication}")
        print(f"Division: {division}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
