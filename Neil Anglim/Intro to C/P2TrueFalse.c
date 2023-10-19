#include <stdio.h>

int checkIf30(int, num1, int num2) {
	return (num1 == 30 || num1 == 30 || num1 + num2 == 30);
}

int main() {
	int num1, num2;
	printf("Enter two integers: ");
	scanf("%d %d" &num1, &num2);
	
	if(checkIf30(num1, num2)) {
		printf("True\n");
	}else {
		printf("False\n");
	}
	
	return 0;
}