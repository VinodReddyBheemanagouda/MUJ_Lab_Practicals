# Write a python program to add and delete key-value pairs in dictionary in different ways.

# Create an empty dictionary
my_dict = {}
print("Empty dictionary:",my_dict)
# Adding key-value pairs using assignment
my_dict["name"] = "Aamir"
my_dict["age"] = 29
print("Dictionary after adding using assignment:", my_dict)

# Adding multiple key-value pairs using update()
my_dict.update({"city":"New Delhi", "country":"India" })
print("Dictionary after using update()",my_dict)

# Deleting a key-value pair using del
del my_dict["age"]
print("Dictionary after deleting 'age' using del:", my_dict)

# Deleting key-value pairs using pop()
removed_value=my_dict.pop("city") #pop() returns the removed value
print(f"removed value:{removed_value}")
print("Dictionary afetr deleting 'city' using pop()", my_dict)

#Deleting the last key-value pair using popitem()
my_dict.popitem()
print("Dictionary after deleting last item using popitem():", my_dict)

#Clearing all key_value pairs using clear()
my_dict.clear()
print("Dictionary after clearing all items:",my_dict)