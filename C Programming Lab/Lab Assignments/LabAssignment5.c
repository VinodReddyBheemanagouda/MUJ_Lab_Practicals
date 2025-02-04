// Write a C program to find factorial of a number using recursion.

#include <stdio.h>

// Function to calculate factorial using recursion
int factorial(int n) {
    // Base case: factorial of 0 or 1 is 1
    if (n == 0 || n == 1) {
        return 1;
    }
    // Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1);
}

int main() {
    int num;

    // Input the number
    scanf("%d", &num);

    // Ensure the number is non-negative
    if (num < 0) {
        printf("Factorial is not defined for negative numbers.\n");
    } else {
        // Call the recursive function and display the result
        printf("%d\n", factorial(num));
    }

    return 0;
}



