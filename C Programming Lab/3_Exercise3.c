/*Write a C program - using gets() and puts() do display the input character.
Objective: The objective of this program is show the use of GETS and PUTS functions*/
#include <stdio.h>

int main() {

  char str[100];// Declare a character array to store the input string

  //use gets() to take input from the user
  printf("Enter a string:\n");
  fgets(str, sizeof(str), stdin); // Accepts a string input, including spaces, safely

  // Use puts() to display the entered string
  printf("You entered:\n");
  puts(str);//Display the string with a newline automatically
  return 0;
}


/*
Note:-
gets(str):

The gets() function is used to take the input string. It allows reading a line of text, including spaces, until a newline (\n) is encountered.
Note: The gets() function does not check for buffer overflow, so it is generally considered unsafe. It is recommended to use fgets() in modern C programs.
puts(str):

The puts() function is used to display the string. It automatically appends a newline character (\n) after the output.
Why fgets() is Preferred:
Buffer Overflow Protection:
Unlike gets(), fgets() limits the input to the size of the buffer specified (sizeof(str) in this case).
Usage:
fgets(str, sizeof(str), stdin) reads a string of at most sizeof(str) - 1 characters, ensuring it doesn't exceed the buffer size.*/