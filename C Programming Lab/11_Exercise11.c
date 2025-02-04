/*Write a program to read data from the keyboard, write it to a file called INPUT, again read the same data from the INPUT file, and copy to that another file and also display it on the screen.
Objective: The objective of this program is to: Create a file and read data from keyboard and copy that data into another file and also display that data on output screen.*/

#include <stdio.h>
#include <stdlib.h>

int main() {
  FILE *fptr1, *fptr2;
  char ch;

  //Open "Input" file in write mode
  fptr1 = fopen("INPUT.txt", "w");
  if (fptr1 == NULL) {
    printf("Error opening file!\n");
    return 1;
  }

  //Read data from the keyboard and write it to the file
  printf("Enter text (Press ctrl+Z) to stop:\n");
  while ((ch = getchar()) != EOF) {
    fputc(ch, fptr1); //Write to INPUT file
  }

  fclose(fptr1); //Close INPUT file after writing

  //Open "INPUT" in read mode and "OUTPUT" in writing mode
  fptr1 = fopen("INPUT.txt", "r");
  fptr2 = fopen("OUTPUT.txt", "w");

  if (fptr1 == NULL || fptr2 == NULL) {
    printf("Error opening file!\n");
    return 1;
  }

  // Read from "INPUT" and copy to "OUTPUT" while displaying on screen
  printf("\nData copied from INPUT.txt and displayed on screen:\n");
  while ((ch = fgetc(fptr1)) != EOF) {
      putchar(ch);  // Display on screen
      fputc(ch, fptr2);  // Copy to OUTPUT file
  }

  // Close both files
  fclose(fptr1);
  fclose(fptr2);

  printf("\nData successfully copied to OUTPUT.txt\n");

  return 0;
}