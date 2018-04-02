/*Write a program that inputs one integer between 0 and 100 which indicates 
student's grade. The program outputs the letter equivalent for numeric 
grade according to the following table: 
A: 100 - 90 
B: 89 - 75 
C: 74 - 65 
D: 64 - 60 
F: 59 - 0 
Your program must print error message if the input is outisde of the valid 
range.*/

#include <stdio.h>

int main(){

	int num;
	
	printf("enter your integer\n");
	scanf("%d", &num);
	
	if(
