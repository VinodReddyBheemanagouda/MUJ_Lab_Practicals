
# Problem Statement

# For a given string "Python Programming", Write a python program to create a dictionary having character as key and number of occurrences as value.


# Instructions

# Write proper comment to make your code readable.
# Use proper naming convention for variables etc in your code.
# Ensure your code compiles without any errors/warning/deprecations 
# Avoid too many & unnecessary usage of white spaces (newline, spaces, tabs, …)
# Always test the code thoroughly, before saving/submitting exercises/project.



# Step 1: Define the input string
input_string = "Python Programming"

# Step 2: Initialize an empty dictionary to store character counts
char_count_dict = {}

# Step 3: Loop through each character in the string
for char in input_string:
    # Count spaces if required by the test case
    if char in char_count_dict:
        char_count_dict[char] += 1
    else:
        char_count_dict[char] = 1

# Step 4: Output the resulting dictionary (no extra text)
print(char_count_dict)
