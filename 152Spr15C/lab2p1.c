/*Write a C program that reads a sequence of non-negative integers, the 
first negative integer terminates the input. For each input value, find 
and print the square root of the input number. Use function sqrt from 
math.h library.*/
#include<stdio.h>
#include<math.h>


int sumSqr(int n);

int main(){
	int n;
	printf("enter positive integer:\n");
	scanf("%d", &n);
	while(n>=0){
		printf("square root of %d is, %d\n", (sqrt(n)));
		scanf("%f", &n);
	}	
	return 0;
}


