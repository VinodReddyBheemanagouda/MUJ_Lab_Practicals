# Write a python program to implement exception handling for ZeroDivision and ValueError.

try:
    # Take input from user
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))

    # Perform division
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except ValueError:
    print("Error: Invalid input. Please enter a valid number.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    print("Execution completed.")
