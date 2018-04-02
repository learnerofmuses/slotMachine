/*Tyler Scott
April 5 2013
Write a program that first reads 1 integer. If the integer is 1 , the 
program reads a series of non-negative integers between 10 and 99. The 
first negative value will terminate the input. The program finds sum and 
average of the numbers with BOTH EVEN digits. USE LOOP WHILE in this part.
If the first input integer is 2, the program reads 10 additional integers 
and finds the amount of inputs that are divisible by 4. USE LOOP FOR in 
this part.
If the first input integer is not 1 or 2, the program prints error 
message.*/

#include <stdio.h.>

int main(){

	int num, sum = 0,n = 0, i = 0,x, y, number;

	printf("enter a number\n");
	scanf("%d", &num);
	
	switch(choice a){

	case 1:
		while(n>10){
			printf("enter a number between 10 and 99\n");
			scanf("%d", &number);
			x = number % 10;
			y = number / 10; 
			if(x%2 == 0 && y%2 == 0){
				sum = sum + number; 
				n++;
			}
		}
	}
	
	switch(choice b){
	case 2:
	
