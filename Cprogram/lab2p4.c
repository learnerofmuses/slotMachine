/*Tyler Scott
March 20 2013
Write a program that inputs a sequence of positive integers, the first 
non-positive (zero or negative) number will terminate the input. The 
program finds the number of inputs between 10 and 20 inclusively and their 
average.
Example:
Input: 7 18 2 3 10 19 -6
Output:
There are 3 numbers between 10 and 20 inclusively
Their average is: 15.333333*/ 

#include <stdio.h>

int main(){

	int num;
	int sum;
	int average;
	
	printf("enter a sequence of positive ints\n");
	scanf("%d", &num);
	
	if(num <= 0){
	
