/*Tyler Scott
March 27 2013
Write a program that first reads one integer. (40 points) If the FIRST 
integer is POSITIVE and ODD the program reads 5 integers and finds the sum 
of the positive input numbers, the amount of positive inputs among the 
input values and their average. YOU HAVE TO USE LOOP FOR IN THIS PART.

(40 points) If the FIRST integer is NEGATIVE and EVEN, the program reads a 
sequence of NON-ZERO integers, the first ZERO number will terminate the 
input. The program finds the number of inputs between -8 and 10 
inclusively that are divisible by 4 and their average. YOU HAVE TO USE 
LOOP WHILE IN THIS PART

(20 points) If the FIRST integer is negative odd or positive even, the 
program reads 5 integers between 10 and 99. The program finds and prints 
the sum of digits for each input number and the average if digits for each 
input number YOU CAN USE THE LOOP OF YOUR CHOICE FOR THIS PART*/

#include <stdio.h>
int main(){

	int i, num, posn, nums, d1,
	int sum = 0, count = 0, average; 
	
	printf("enter an integer\n");
	scanf("%d", &num);

	if(num > 0 && num % 2 != 0){
		for(i = 0, i<=5, i++){ 
			scanf("%d", &posn);
			count++;
			sum = sum + posn;
		}
		scanf("%d", &posn);
	
		if(count>0){
			average = (float)(sum)/count;
			printf("%f\n", posn);
		}
		else{
			printf("no odd numbers\n");
		}
	}
	else if(num < 0 && num % 2 == 0){
		printf("enter sequence of non-zero integers\n");
		scanf("%d", &num);
		while(num >= -8 && num <= 10){
			if(num % 4 == 0){
				count++;
				sum = sum + nums;
			}
			scanf("%d", &nums);
		}
		if(count > 0){
			average = (float)(sum)/count;
			printf("%f", &nums);
		}
		else{
			printf("no negative or even numbers\n");
	 	}
	else if(num < 0 && num % 2 != 0 || num > 0 && num % 2 == 0){
		for(i = 0, i<=5, i++){
			scanf("%d", posn);
			count++;
			sum = sum + posn;	
			
		}
	}
	return 0;
}
