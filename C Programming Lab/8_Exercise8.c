/*Write a C program – using structures for reading the employee details like employee name, date of joining and salary and also to compute Total salary outgo for a month.
Objective: The objective of this program is to: Read the employee details like employee name, date of joining and salary. And display the total salary of the particular month.*/

#include <stdio.h>
#include <string.h>

struct Employee
{
  char name[50];
  int Date_Of_Joining[15];
  float salary;

};


int main(){
  int n, i;
  float total_salary = 0;

  //Read the number of employees
  printf("Enter the number of employess: ");
  scanf("%d", &n);

  //Declare an array of structures
  struct Employee employees[n];

  //Input employees details
  for (i=0; i<n; i++){
    printf("\nEnter details for Employee %d: \n", i +1);

    //Clear input buffer
    getchar();

    // Read employee name
    printf("Name: ");
    fgets(employees[i].name, 50,stdin);
    employees[i].name[strcspn(employees[i].name, "\n")] = '\0'; // Remove new line character

    // read date of joining
    printf("Date of Joining (DD/MM/YYYY): ");
    scanf("%s", &employees[i].Date_Of_Joining);

    // Read salary
    printf("Salary: ");
    scanf("%f", &employees[i].salary);

    //Add Salary to total
    total_salary += employees[i].salary;
  }

  //Display total salary outgo
  printf("\nTotal Salary Outgo for the Month : %.2f\n", total_salary);

  //Display all employee details
  printf("\nEmployee Details:\n");
  for (i = 0; i<n; i++){
    printf("Employee %d:\n", i+1);
    printf("Name: %s\n", employees[i].name);
    printf("Date of Joining: %s\n", employees[i].Date_Of_Joining);
    printf("Salary:%.2f\n", employees[i].salary);
  }
  return 0;
}