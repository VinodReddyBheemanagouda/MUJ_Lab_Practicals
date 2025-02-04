// Write a C Program to extract a portion of a string from a character string
// Objective: The objective of this program is to: Finding the position of the character and number of characters from the given string.

#include <stdio.h>
#include <string.h>

int main() {
    char str[100], substr[100]; // Declare arrays for the main string and substring
    int start, length, i, j = 0;

    // Step 1: Input the main string
    printf("Enter a string:\n");
    fgets(str, sizeof(str), stdin); // fgets allows spaces in input

    // Remove trailing newline character if present
    str[strcspn(str, "\n")] = '\0';

    // Step 2: Input starting position and number of characters to extract
    printf("Enter the starting position (0-based index):\n");
    scanf("%d", &start);
    printf("Enter the number of characters to extract:\n");
    scanf("%d", &length);

    // Step 3: Validate inputs
    int strLength = strlen(str); // Get the length of the input string
    if (start < 0 || start >= strLength || length < 0 || (start + length) > strLength) {
        printf("Error: Invalid starting position or length.\n");
        return 1; // Exit with an error if inputs are invalid
    }

    // Step 4: Extract the substring
    for (i = start; i < start + length; i++) {
        substr[j++] = str[i]; // Copy characters from str to substr
    }
    substr[j] = '\0'; // Null-terminate the substring

    // Step 5: Display the extracted substring
    printf("Extracted substring: \"%s\"\n", substr);

    return 0;
}
