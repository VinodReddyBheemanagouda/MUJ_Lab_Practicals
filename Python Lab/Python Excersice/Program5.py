# Write a python program to create Simple Calculator by Using Functions.

# Function for addition
def add(x,y):
  return x + y

#Function for multiplication
def multiply(x,y):
  return x * y

#Function for subtraction
def subtract(x,y):
  return x-y

#Function for division
def divide(x,y):
  return x/y

# print("Select Operation.")
# print("1 for Addition")
# print("2 for Subtraction")
# print("3 for Multiplication")
# print("4 for Division")

while True:
  #Take input from user
  choice=input("Enter your choice\n1 for Addition\n2 for Subtraction\n3 for Multiplication\n4 for Division):\n")

  #validate the input
  if choice in('1','2','3','4'):
    try:
      num1 = float(input("Input first number: "))
      num2 = float(input("Input second number: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue
    if choice == '1':
      print(num1,"+",num2,"=",add(num1,num2))  
    elif choice == '2':
      print(num1,"-",num2,"=",subtract(num1,num2))  
    elif choice == '3':
      print(num1,"*",num2,"=",multiply(num1,num2))  
    elif choice == '4':
      print(num1,"/",num2,"=",divide(num1,num2))  

    #Check if user want another calculation
    next_calculation = input("Let's do next calculation?(yes/no)")
    if next_calculation =='no':
      break
  else:
    print("Invalid Input")  