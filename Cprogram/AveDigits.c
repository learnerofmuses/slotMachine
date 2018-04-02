/*Tyler Scott
March 14 2013
AveDigits.c

Write a C program AveDigits.c that prompts the user to enter one positive 4-digits integer. The program 
finds and prints the integer part of the average of the digits of the input number.
For example, if the inputs is 2357, the output should be: Integer part of the average of the digits is 4.*/

#include <stdio.h>

int main(){

	int num; 
	int d1, d2, d3, d4;	
	int sum;
	int avg; 
	
	printf("enter first integer\n");
	scanf("%d", &num);	
	
	d1 = num % 10;
	d2 = num % 10;
	d3 = num % 10;
	d4 = num % 10; 

	sum = d1+d2+d3+d4; 
	avg = sum/4;
	
	printf("the average of the digits is: %d\n", avg);
		
} 
