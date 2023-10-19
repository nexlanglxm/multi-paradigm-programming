#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Employee {
	char name ;
	int age ;
	int salary ;
	int years_worked ;
	char job_title ;
};

struct Manager {
	char name ;
	int age ;
	int salary ;
	struct Employee employees[10] ;
};
	
void printEmployee (struct Employee employee){
	printf("The employee name is %s\n", employee.name);
}

int main(void)
{
	struct Employee employee = { "Adrian" };
	print Employee(employee);
	
	struct Manager manager = {};
	Manager.employee[0] = employee;
	
	struct Employee employee2 = { "Frankie" };
	print Employee(employee);
	
	printEmployee(manager.employee[0]);
	printEmployee(manager.employee[1]);
	
		return 0;
}