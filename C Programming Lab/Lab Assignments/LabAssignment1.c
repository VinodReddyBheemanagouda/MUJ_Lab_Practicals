// Write a C program to check whether the entered year is leap year or not

#include <stdio.h>

int main() {
    int year;

    // Prompt the user to enter a year
    scanf("%d", &year);

    // Check if the year is a leap year
    if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
        // If the conditions are true, print "Leap Year"
        printf("Leap Year\n");
    } else {
        // If the conditions are false, print "Non Leap Year"
        printf("Non Leap Year\n");
    }

    return 0;
}



