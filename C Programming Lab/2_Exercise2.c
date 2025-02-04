// Write a C program, which takes two integer operands and one operator form the user performs the operation and then prints the
// result.(Consider the operators +,-,*, /, % and use Switch Statement)
// Objective: To calculate addition, subtraction, multiplication, division and remainder of
// the user particular numbers using switch and case statements.

#include <stdio.h>

int main() {
    // Declare variables
    int num1, num2;       // Variables to store two integer operands
    float result;         // Variable to store the result of the operation
    char operator;        // Variable to store the operator entered by the user

    // Take input from the user for the first number
    printf("Enter first number:\n");
    scanf("%d", &num1);

    // Take input from the user for the operator
    printf("Enter operator (+, -, *, /, %%):\n");
    scanf(" %c", &operator);

    // Take input from the user for the second number
    printf("Enter second number:\n");
    scanf("%d", &num2);

    // Perform the operation based on the entered operator
    switch (operator) {
        case '+':  // Addition operation
            result = num1 + num2;
            printf("Result: %d + %d = %.2f\n", num1, num2, result);
            break;

        case '-':  // Subtraction operation
            result = num1 - num2;
            printf("Result: %d - %d = %.2f\n", num1, num2, result);
            break;

        case '*':  // Multiplication operation
            result = num1 * num2;
            printf("Result: %d * %d = %.2f\n", num1, num2, result);
            break;

        case '/':  // Division operation
            // Check if the divisor is not zero
            if (num2 != 0) {
                result = (float)num1 / (float)num2; // Type casting for float division
                printf("Result: %d / %d = %.2f\n", num1, num2, result);
            } else {
                // Handle division by zero error
                printf("Error: Division by zero is not allowed.\n");
            }
            break;

        case '%':  // Modulo operation
            // Check if the divisor is not zero
            if (num2 != 0) {
                result = num1 % num2; // Compute remainder
                printf("Result: %d %% %d = %.2f\n", num1, num2, result);
            } else {
                // Handle division by zero error
                printf("Error: Division by zero is not allowed.\n");
            }
            break;

        default:  // Handle invalid operator input
            printf("Error: Invalid operator.\n");
            break;
    }

    return 0; // Return 0 to indicate successful execution
}
