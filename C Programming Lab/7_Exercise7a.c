/*a) Write a C program, to find both the largest and smallest number in a list of integers using an Array.
Objective: The objective of this program is to:
Finding largest and smallest number from given integers, Performing matrix
addition and matrix multiplication using array.
*/

//Solving problem a

#include <stdio.h>

int main(){
  int n, i, max, min;

  printf("Enter the number of elements: ");
  scanf("%d", &n);

  int arr[n]; //Declare an array of size n

  printf("Enter %d elements:\n", n);
  for (i = 0; i < n; i++){
    scanf("%d", &arr[i]);
  }

  max = min = arr[0]; //Intialize max and min with the fist element
  for (i = 1; i < n; i++){
    if (arr[i] > max){
      max = arr[i];
    }
    if (arr[i] < min){
      min = arr[i];
    }
  }
  printf("Largest number: %d\n", max);
  printf("Smallest number: %d\n", min);

  return 0;
}