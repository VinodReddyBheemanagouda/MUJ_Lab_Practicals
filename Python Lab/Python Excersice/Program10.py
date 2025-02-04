# Write a python program for creating user defined exception and raise it when input number is negative.

# Custom exception for negative numbers
class NegativeNumberEroor(Exception):
  #Exception raised when input number is negative.
  def __init__(self, message ="Input number cannot be negative."):
    super().__init__(message)
# Function to validate positive number
def check_positive_number(number):
  if number < 0:
    raise NegativeNumberEroor()
  print(f"The input number {number} is positive.")

  # Main function to handle user input and exceptions
def main():
  try:
    number = float(input("Enter a number: ")) # Get user input
    check_positive_number(number) #Validate number
  except NegativeNumberEroor as e:
    print(f"Error: {e}")
  except ValueError:
    print("Error: Please enter a valid numeric value.")
  else:
    print("No exception occured.")

# Run the script
if __name__ == "__main__":
  main()                