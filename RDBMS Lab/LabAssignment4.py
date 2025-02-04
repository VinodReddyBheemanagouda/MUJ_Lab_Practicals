# Write a Pl/SQL program to calculate Area of triangle whose base =100 and height=10.
# -- Program to calculate the area of a triangle in PL/SQL

# DECLARE
#     -- Declare variables to hold the base, height, and area of the triangle
#     base_triangle NUMBER := 100;  -- Base of the triangle
#     height_triangle NUMBER := 10; -- Height of the triangle
#     area_triangle NUMBER;         -- Variable to store the calculated area
# BEGIN
#     -- Calculate the area of the triangle using the formula: (1/2) * base * height
#     area_triangle := (1 / 2) * base_triangle * height_triangle;

#     -- Display the calculated area
#     DBMS_OUTPUT.PUT_LINE('The area of the triangle is: ' || area_triangle);
# END;
# /
