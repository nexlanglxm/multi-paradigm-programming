# include<stdio.h>
int main() {
	int num1, num2;
	printf("Enter the first integer: ");
	scanf("%d", &num1);
	printf("Enter the second integer: ");
	scanf("%d", &num2);
	
	int sum = num1 + num2;
	
	if (sum >= 10 && sum <= 20) {
		sum = 30;
	}
	
	printf("The sum is %d\n", sum);
	
	return 0;
}
