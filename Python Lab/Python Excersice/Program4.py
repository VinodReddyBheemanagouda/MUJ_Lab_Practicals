# Write a program to double a given number and add two numbers using lambda() function.

# Lambda function to double a number
double = lambda x: 2 * x
print("Double of 5 is:", double(5))

# Lambda function to add two numbers
add = lambda x, y: x + y
print("Sum of 5 and 4 is:", add(5, 4))



# Note for Lambda
'''
Lambda Function in Python – A Quick Refresher
A lambda function in Python is an anonymous (nameless), single-line function that can have any number of arguments but only one expression. It is often used for short, simple operations where defining a full function would be unnecessary.

Syntax:
python
Copy
Edit
lambda arguments: expression
The expression is evaluated and returned when the lambda function is called.
Where is Lambda Used?
Lambda functions are used in various scenarios, including:

Short, One-Time Functions

When you need a simple function without formally defining it using def.
python
Copy
Edit
square = lambda x: x ** 2
print(square(4))  # Output: 16
Used with Built-in Functions (map(), filter(), reduce())

map() → Apply a function to all elements in an iterable.
python
Copy
Edit
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16]
filter() → Filter elements based on a condition.
python
Copy
Edit
nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)  # Output: [2, 4, 6]
reduce() → Perform cumulative operations (requires functools.reduce).
python
Copy
Edit
from functools import reduce
product = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(product)  # Output: 24
Used in Sorting (sorted() with custom keys)
Sort a list of tuples by the second element.
python
Copy
Edit
students = [("Alice", 25), ("Bob", 20), ("Charlie", 22)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)  
# Output: [('Bob', 20), ('Charlie', 22), ('Alice', 25)]
Used in GUI Programming (Tkinter)

Useful in GUI frameworks like Tkinter for short event-handling functions.
python
Copy
Edit
from tkinter import Button, Tk
root = Tk()
button = Button(root, text="Click Me", command=lambda: print("Button Clicked"))
button.pack()
root.mainloop()
Used in Data Science & Pandas (apply())

Lambda functions are useful for modifying and transforming data.
python
Copy
Edit
import pandas as pd
df = pd.DataFrame({'A': [1, 2, 3, 4]})
df['B'] = df['A'].apply(lambda x: x * 2)
print(df)
# Output:
#    A  B
# 0  1  2
# 1  2  4
# 2  3  6
# 3  4  8
'''