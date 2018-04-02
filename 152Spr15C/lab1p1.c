/*Write a program that inputs 10 integers between 0 and 100 which 
indicates student's grade. The program outputs the letter equivalent for 
numeric grade for each input according to the following table:
A: 100 - 90
B: 89 - 75
C: 74 - 65
D: 64 - 60
F: 59 - 0
Your program must print error message if the input is outisde of the 
valid range.*/

#include<stdio.h>

int main(){
	int num, grade;

	printf("enter number of grades you want to be calculated:\n");
	scanf("%d", &num);
	
	printf("enter %d grades\n", num);
	
	if(grade<=100 && grade >=90){
