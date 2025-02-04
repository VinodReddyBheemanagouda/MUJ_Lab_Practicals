// Write a C program to find the sum of individual digits of a positive integer.

#include <stdio.h>

int main(){
  int num, sum = 0;

  //take input from user
  printf("Enter a number:\n");
  scanf("%d", &num);

  //Loop to calculate the sum of digits
  while (num !=0)
  {
    sum = sum + (num % 10); // Extract and add the last digit
    num = num / 10; // Remove the last digit
  }
  
  //print the result
  printf("sum of the digits: %d\n", sum);
  return 0;
}