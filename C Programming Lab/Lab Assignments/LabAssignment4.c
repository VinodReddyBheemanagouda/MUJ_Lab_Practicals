// Write a C program that defines a structure to store and display student details, including the student's name, ID, and percentage.

#include <stdio.h>

// Define a structure to store student details
struct Student {
    char name[50];  // Student's name
    int id;         // Student's ID
    float percentage;  // Student's percentage
};

int main() {
    // Declare a student variable
    struct Student student;

    // Input the student's name, ID, and percentage
    scanf("%49s", student.name);  // Read name (limit to 49 characters)
    scanf("%d", &student.id);  // Read student ID
    scanf("%f", &student.percentage);  // Read student percentage

    // Display the student's details without decimal places for percentage
    printf("%s\n", student.name);
    printf("%d\n", student.id);

    // If the percentage has no decimal, print it as an integer
    if (student.percentage == (int)student.percentage) {
        printf("%d\n", (int)student.percentage);
    } else {
        printf("%.2f\n", student.percentage);  // Otherwise, print as a float
    }

    return 0;
}



