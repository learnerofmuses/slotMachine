/*write a program that reads three integers  and finds 
the sum and product */

#include <stdio.h>

int main(){
	int a, b, c, sum, product;
	
	printf("enter 3 integers\n"); 
	scanf("%d%d%d", &a, &b, &c);
	
	sum = a+b+c;
	product = a*b*c;
	printf("sum is %d\n", sum);
	printf("product is %d\n", product);
	return 0;
	
}



