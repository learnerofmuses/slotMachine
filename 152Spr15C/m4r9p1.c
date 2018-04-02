/*first program in C read 3 ints and finds 
sum and product */


#include<stdio.h>

int main(){
	int n1, n2, n3, s=0, p=1;
	printf("enter 3 ints\n");
	scanf("%d%d%d", &n1, &n2, &n3);
	s=n1+n2+n3; 
	p=n1*n2*n3;
	printf("sum is %d, product is %d", s, p);
	return 0;
}
