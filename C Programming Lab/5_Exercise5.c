// /*Write a C program to find the factorial of a given integer number using both recursive and non-recursive functions.*/
#include <stdio.h>

// // Non-recursive factorial function
// int factorial(int n) {
//     int result = 1; // Initialize result to 1
//     for (int i = 1; i <= n; i++) {
//         result *= i; // Multiply result by the current value of i
//     }
//     return result; // Return the computed factorial
// }

// int main() {
//     int num;
//     printf("Enter a number to find its factorial:\n");
//     scanf("%d", &num);

//     // Handle negative input
//     if (num < 0) {
//         printf("Factorial of a negative number is undefined.\n");
//     } else {
//         int result = factorial(num); // Call the factorial function
//         printf("Factorial of %d is %d\n", num, result);
//     }
//     return 0;
// }


// Recursive factorial function
int factorial(int n) {
    if (n == 0) { // Base case: factorial of 0 is 1
        return 1;
    } else { // Recursive case: n * factorial(n - 1)
        return n * factorial(n - 1);
    }
}

int main() {
    int num;
    printf("Enter a number to find its factorial:\n");
    scanf("%d", &num);

    // Handle negative input
    if (num < 0) {
        printf("Factorial of a negative number is undefined.\n");
    } else {
        int result = factorial(num); // Call the recursive factorial function
        printf("Factorial of %d is %d\n", num, result);
    }
    return 0;
}
