/*Tyler Scott
March 13, 2013
digitGame.c

Write a C program digitGame.c that reads five positive 3-digits integers 
and prints ONLY last digit of each number in reverse order of the input. 
Each last digit will be printed on the separate line.*/

#include <stdio.h>

int main(){
	
	int num1;
	int num2; 
	int num3;
	int num4; 
	int num5; 
	int ld1, ld2, ld3, ld4, ld5;

	printf("enter first integer\n");
	scanf("%d", &num1);
	printf("enter second integer\n");
	scanf("%d", &num2);
	printf("enter third integer\n");
	scanf("%d", &num3);
	printf("enter fourth integer\n");
	scanf("%d", &num4);
	printf("enter fifth integer\n");
	scanf("%d", &num5);
			
	
	ld1 = num1 % 10;
	ld2 = num2 % 10;
	ld3 = num3 % 10;
	ld4 = num4 % 10;
	ld5 = num5 % 10;
	
	printf("%d, %d, %d, %d, %d\n", ld5, ld4, ld3, ld2, ld1);		
}
