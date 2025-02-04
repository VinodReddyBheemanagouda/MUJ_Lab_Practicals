/*
Write a C Program – using pointers To Swap the Values of Two Variables.
Objective: The objective of this program is to: Swapping the two variables.*/
#include <stdio.h>

//Function to swap two numbers using pointers

void swap(int *x, int *y) {
  int temp = *x; //Store the value of x in temp
  *x = *y;       //Assign y's value to x
  *y = temp;    //Assign temp (old x value) tp y
}
int main(){
  int a = 3, b = 5; //Initialize variables

  printf("Assigned Value: a = %d, b = %d\n", a, b);

  //Call the swap function
  swap(&a, &b);

  printf("After Swapping: a = %d, b = %d\n", a, b);

  return 0;
}