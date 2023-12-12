#include <stdio.h>
#include <stdlib.h>
int main(){
	int n;
	printf("Enter a number: ");
	scanf("%d", &n);
	
	int difference = abs(n - 51);
	
	if (n > 51) {
		difference *= 3;
	}
	
	printf("The absolute difference (x3 if n > 51) between %d and 51 is %d\n", n, difference);
	
	return 0;