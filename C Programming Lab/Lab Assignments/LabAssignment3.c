// Write a C Program – using pointers To Swap the Values of Two Variables

#include <stdio.h>

void swap(int *a, int *b) {
    int temp;

    // Swap the values using a temporary variable
    temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x, y;

    // Get input for the two variables
    scanf("%d %d", &x, &y);

    // Call the swap function using pointers
    swap(&x, &y);

    // Print the swapped values directly
    printf("%d %d\n", x, y);

    return 0;
}



