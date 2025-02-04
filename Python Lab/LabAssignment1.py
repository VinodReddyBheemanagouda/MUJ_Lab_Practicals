
# Problem Statement
# Write a python program to create data frame from dictionary { 'A': [1, 2, np.nan, 4], 'B': [np.nan, 5, 6, np.nan],   'C': [np.nan, np.nan, 9, 10] }, apply backward fill to fill missing values.

# Instructions

# Write proper comment to make your code readable.
# Use proper naming convention for variables etc in your code.
# Ensure your code compiles without any errors/warning/deprecations 
# Avoid too many & unnecessary usage of white spaces (newline, spaces, tabs, …)
# Always test the code thoroughly, before saving/submitting exercises/project.

# Import necessary library
import pandas as pd
import numpy as np

# Create a dictionary with the given data
data = {
    'A': [1, 2, np.nan, 4],
    'B': [np.nan, 5, 6, np.nan],
    'C': [np.nan, np.nan, 9, 10]
}

# Create a DataFrame from the dictionary
data_frame = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(data_frame)

# Apply backward fill to fill missing values
filled_data_frame = data_frame.fillna(method='bfill')

# Display the DataFrame after backward fill
print("\nDataFrame after Backward Fill:")
print(filled_data_frame)
