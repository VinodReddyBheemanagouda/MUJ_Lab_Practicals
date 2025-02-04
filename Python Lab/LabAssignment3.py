# Statement
# Write a python program to print prime numbers between 10 to 20.

# Instructions
# Write proper comment to make your code readable.
# Use proper naming convention for variables etc in your code.
# Ensure your code compiles without any errors/warning/deprecations 
# Avoid too many & unnecessary usage of white spaces (newline, spaces, tabs, …)
# Always test the code thoroughly, before saving/submitting exercises/project.
# Method 1 

def is_prime(number):
    """Checks if a number is prime (only divisible by 1 and itself)."""
    if number < 2:  # Numbers less than 2 are not prime.
        return False
    for divisor in range(2, int(number ** 0.5) + 1):  # Check for divisors up to the square root.
        if number % divisor == 0:  # If divisible, it's not prime.
            return False
    return True  # If no divisors found, it's prime.

# Find and print prime numbers between 10 and 20 in the correct format.
prime_numbers = []  # Create an empty list to store prime numbers.
for num in range(10, 21):  # Loop from 10 to 20 (inclusive).
    if is_prime(num):  # Check if the current number is prime.
        prime_numbers.append(str(num))  # Add the prime number (as a string) to the list.

print(" ".join(prime_numbers)) # Join the numbers with spaces and print on one line.


# Method 2- Using Loop
# Iterate through numbers between 10 and 20
# print("Prime numbers between 10 and 20 are:")
# for number in range(10, 21):
#     # Check if the number is prime
#     if all(number % divisor != 0 for divisor in range(2, int(number ** 0.5) + 1)):
#         print(number)