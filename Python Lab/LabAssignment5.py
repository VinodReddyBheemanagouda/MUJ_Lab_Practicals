
# Problem Statement

# Write a Program to Convert Decimal to Binary Using Recursion.


# Instructions

# Write proper comment to make your code readable.
# Use proper naming convention for variables etc in your code.
# Ensure your code compiles without any errors/warning/deprecations 
# Avoid too many & unnecessary usage of white spaces (newline, spaces, tabs, …)
# Always test the code thoroughly, before saving/submitting exercises/project.

# Example

# Sample Input:- 4

# Sample output:- 100

# Function to convert decimal to binary using recursion
def decimal_to_binary(decimal_number):
    # Base case: If the number is 0, return an empty string
    if decimal_number == 0:
        return ""
    else:
        # Recursively call the function to process the next digit
        return decimal_to_binary(decimal_number // 2) + str(decimal_number % 2)

# Main function to handle the input and output
def main():
    # Prompt the user to enter a decimal number
    decimal_number = int(input())
    
    # Handle the special case where the decimal number is 0
    if decimal_number == 0:
        print("0")
    else:
        # Call the recursive function and print the result
        binary_result = decimal_to_binary(decimal_number)
        print(binary_result)

# Call the main function to run the program
if __name__ == "__main__":
    main()