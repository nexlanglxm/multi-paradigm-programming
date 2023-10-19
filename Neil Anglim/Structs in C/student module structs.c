#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct Module {
	char name ;
	int credits ;
};

struct Student {
	char name ;
	int age ;
	struct Module modules[10] ;
};

void printModule (struct Module module){
	printf("The module name is %s\n", module.name);
}

int main(void)
{
	struct Module module = { "Multi-paradigm Programming" };
	print Module(module);
	
	struct Student student = {};
	student,modules[0] = module;
	
	struct Module module2 = { "Intro to Programming" };
	print Module(module);
	
	printModule(student.modules[0]);
	printModule(student.modules[1]);
	
		return 0;
}

void printStudent (struct Student student) {
	printf("The students name is %s\n", student.name);
}