# Write a python program to find largest number among three numbers.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter Second number: "))
num3 = int(input("Enter Third number: "))

if (num1 >= num2) & (num1 >=num3):
  largest =  num1

elif (num2 >= num1) & (num2 >=num3):
  largest = num2

else:
  largest = num3

print ("The largest number is", largest)    