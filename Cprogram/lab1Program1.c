/*Tyler Scott
March 13,2013
lab1Program1.c

In the file lab1Program1.c you will write a C program that prompts the 
user to enter FIVE integers. If first two integers are EVEN, the program 
will calculate the INTEGER PART of the average of ALL input numbers. The 
output of the program will include: the values of the input numbers and 
the calculated average with the appropriate message. Print your name, 
input numbers and the result on separate lines (the output will consist 
of three lines). If the first two integers are ODD, the program will 
calculate the product of ALL input numbers. The output of the program 
will include: the values of the input numbers and the calculated product 
with the appropriate message. Print your name, input numbers and the 
result on separate lines (the output will consist of three lines). If 
the first integers is ODD and the second is EVEN, the program finds and 
prints the product of LAST digits of ALL inputs. If the first integer is 
EVEN and the second is ODD, the program finds and prints the sum of LAST 
digits of ALL inputs*/ 


#include <stdio.h>

int main()
{
	
	int num1; 
	int num2;
	int num3;  
	int num4;
	int num5; 
	int sum; 
	int avg; 
	int product; 
	int ld1, ld2, ld3, ld4, ld5;

	printf( "enter first integer\n");  
	scanf("%d", &num1);
	printf( "enter second integer\n"); 
	scanf("%d", &num2);
	printf( "enter third integer\n");
	scanf("%d", &num3); 
	printf( "enter fourth integer\n"); 
	scanf("%d", &num4); 
	printf( "enter fifth integer\n"); 
	scanf("%d", &num5); 
	
	if((num1 % 2 == 0) && (num2 % 2 == 0)){
		sum = num1+num2+num3+num4+num5;
		printf("%d\n", sum);
		avg = sum/5; 
		printf("average of inputs are: %d\n", avg);
		printf("Tyler Scott");
		printf("%d, %d, %d, %d, %d\n", num1, num2, num3, num4, num5); 
	}
	else if((num1 % 2 != 0) && (num2 % 2 != 0)){
		product = num1*num2*num3*num4*num5;
		printf("product of inputs are %d, %d, %d, %d, %d\n", num1, num2, num3, num4, num5, product); 
		printf("product is: %d\n", product);
	}
	else if((num1 % 2 != 0) && (num2 % 2 == 0)){
		printf("Tyler Scott");
                printf("%d, %d, %d, %d, %d\n", num1, num2, num3, num4, num5);
		ld1 = num1 % 10;
		ld2 = num2 % 10;
		ld3 = num3 % 10;
		ld4 = num4 % 10;
		ld5 = num5 % 10;
		product = ld1*ld2*ld3*ld4*ld5;
		printf("product of last digits: %d, %d, %d, %d, %d\n", ld1, ld2, ld3, ld4, ld5, product);
	 	printf("product of last digits are: %d\n", product);
	}
	else{
		ld1 = num1 % 10;
		ld2 = num2 % 10;
		ld3 = num3 % 10;
		ld4 = num4 % 10;
		ld5 = num5 % 10;
		sum = ld1+ld2+ld3+ld4+ld5;
		printf("sum of last digits: %d, %d, %d, %d, %d\n", ld1, ld2, ld3, ld4, ld5, sum);
		printf("sum of last digits are: %d\n", sum);
	}
}
