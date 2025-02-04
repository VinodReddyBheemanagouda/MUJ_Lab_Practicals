/*Write a C Program - using if else statements, to find the largest number among the given two integer numbers.*/

#include <stdio.h>

int main() {
    int num1, num2;

    // Prompt user for the first number
    printf("Enter first number:\n");
    scanf("%d", &num1);

    // Prompt user for the second number
    printf("Enter second number:\n");
    scanf("%d", &num2);

    // Check which number is greater or if they are equal
    if (num1 > num2) {
        printf("%d is greater than %d\n", num1, num2);
    } else if (num1 == num2) {
        printf("You entered equal numbers.\n");
    } else {
        printf("%d is greater than %d\n", num2, num1);
    }

    return 0;
}
