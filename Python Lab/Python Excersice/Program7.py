# Write a python program to calculate area of rectangle using class and object concepts.

class Rectangle:
    """Class to calculate the area of a rectangle."""

    def __init__(self, length: float, width: float):
        """Initialize the rectangle with length and width."""
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """Calculate and return the area of the rectangle."""
        return self.length * self.width

# Take user input for length and width
try:
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))

    # Create an instance of Rectangle
    rectangle = Rectangle(length, width)

    # Display the area of the rectangle
    print(f"Area of Rectangle: {rectangle.calculate_area():.2f}")

except ValueError:
    print("Invalid input! Please enter numeric values.")
