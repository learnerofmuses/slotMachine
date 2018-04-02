/*float double ints example */


#include<stdio.h>

int main(){
	int n1, n2, n3; 
	double ave;

	printf("enter 3 ints \n");
	scanf("%d%d%d", &n1, &n2, &n3);
	ave=(n1+n2+n3)/3;
	printf("bad truncated ave is %f\n", ave);
	ave=(n1+n2+n3)/3.0;
	printf("good average is %f\n", ave);
	printf("ave with only 2 decimals %.2f\n", ave);
	printf("using casting to find average\n");
	ave=(n1+n2+n3)/((double)(3));
	printf("ave is %f\n", ave);
	return 0;
}		
