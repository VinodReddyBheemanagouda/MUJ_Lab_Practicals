
# Problem Statement

# Write a Program to print list of duplicates from a list of integers [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20].


# Instructions

# Write proper comment to make your code readable.
# Use proper naming convention for variables etc in your code.
# Ensure your code compiles without any errors/warning/deprecations 
# Avoid too many & unnecessary usage of white spaces (newline, spaces, tabs, …)
# Always test the code thoroughly, before saving/submitting exercises/project.

def find_duplicates(integer_list):
    """
    Finds and returns a list of duplicate integers from a given list.

    Args:
        integer_list: A list of integers.

    Returns:
        A list containing the duplicate integers. Returns an empty list if no duplicates are found.
    """

    seen = {}  # Dictionary to store counts of each number
    duplicates = []  # List to store duplicate numbers

    for number in integer_list:
        if number in seen:
            seen[number] += 1
            if seen[number] == 2: #Add to duplicate list only on its first re-occurrence
                duplicates.append(number)
        else:
            seen[number] = 1

    return duplicates


if __name__ == "__main__":
    numbers = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
    duplicate_numbers = find_duplicates(numbers)

    print(duplicate_numbers) #Directly print the list of duplicates.