/*Write a C Program – to use structure within union, display the structure and length of union elements
Objective: The objective of this program is to: display the structure and length of union elements*/

#include <stdio.h>
#include <string.h>

//Define a structure
struct Employee{
  char name[20];
  int id;
  float salary;
};

//Define a union containing an int, float, and Employee structure
union Data {
  int num;
  float decimal;
  struct Employee emp;
};

int main() {
  //Declare a union variable
  union Data data;

  //Assigning values to the structure inside the union
  strcpy(data.emp.name, "Aamir Sohail");
  data.emp.id = 101;
  data.emp.salary = 45000.50;

  //Display the structure data
  printf("Employee Details:\n");
  printf("Name: %s\n", data.emp.name);
  printf("ID: %d\n", data.emp.id);
  printf("Salary: %.2f\n", data.emp.salary);

  //Display the sizes of the structure and union
  printf("\nSize of structure Employee: %lu bytes\n", sizeof(struct Employee));
  printf("Size of Union Data: %lu bytes\n", sizeof(union Data));

  return 0;
}