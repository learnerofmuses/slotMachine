/* Tyler Scott
/* scott@suzy.cs.widener.edu
/* MARCH 11 2013
/* lab1p1.c

/*In the file Average.c you will write a C program that prompts the user to 
/*enter three integers. The program will calculate the INTEGER PART of the 
/*average of the input numbers. The output of the program will include: the 
/*values of the input numbers and the calculated average with the 
/*appropriate message. Print your name, input numbers and the result on 
/*separate lines 
/*(the output will consist of three lines). For example, if the input was 
/*1, 2 and 4. The output should be

/*Input numbers are: 1, 2, and 4 
/*The integer part of the average of the input numbers is 2

#include <stdio.h>

int main()
{

	int num1;     /*first input number*/
	int num2;     /*second input number*/
	int num3;     /*third input number*/
	int sum;     /*variable in which sum will be stored*/
	int average; /*average of the three numbers*/
	
	printf("enter first int\n");     /*prompt*/
	scanf( "%d", &num1); /*read int*/
	printf("enter second int\n");    /*prompt*/
	scanf( "%d", &num2); /*read int*/
	printf("enter third int\n");     /*prompt*/
	scanf( "%d", &num3); /*read int*/

	sum = num1 + num2 + num3; /*assign total to sum*/
	printf("Sum is %d\n", sum); /*print sum*/

}
