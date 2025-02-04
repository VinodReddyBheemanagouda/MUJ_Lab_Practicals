/*c) Write a C program, to multiply two matrices using an Array.
Objective: The objective of this program is to:
Finding largest and smallest number from given integers, Performing matrix
addition and matrix multiplication using array.*/

#include <stdio.h>

int main(){
  int rows, cols, i, j ;
  printf("Enter size of matrix (rows and columns)\n");
  scanf("%d %d", &rows, &cols);
  int matrix1[rows][cols], matrix2[rows][cols], result[rows][cols];

  printf("Enter elements of first matrix: \n");
  
  for (i=0; i<rows; i++) {
    for (j=0; j<cols; j++) {
      scanf("%d",&matrix1[i][j]);
    }
    
  }

  printf("Enter elements of second matrix: \n");
  
  for (i=0; i<rows; i++) {
    for (j=0; j<cols; j++) {
      scanf("%d",&matrix2[i][j]);
    }
    
  }
  
  //Perform multiplication
  for (i=0; i<rows; i++){
    for (j=0; j<cols; j++){
      result[i][j] = matrix1[i][j] * matrix2[i][j];
    }
  }

  printf("Resultant matrix is:\n");
  for (i=0; i<rows; i++){
    for(j=0; j<cols; j++){
      printf("%d",result[i][j]);
    }
    printf("\n");
  }

  return 0;
}