/*Write a program that first reads one integer. If the FIRST integer is 
POSITIVE and EVEN the program reads 5 integers and finds the sum of the 
negative input numbers, the amount of negative inputs among the input 
values and their average. YOU HAVE TO USE LOOP FOR IN THIS PART.

If the FIRST integer is NEGATIVE and ODD, the program reads a sequence 
of positive integers, the first non-positive (zero or negative) number 
will terminate the input. The program finds the number of inputs between 
8 and 25 inclusively that are divisible by 7 and their average. YOU HAVE 
TO USE LOOP WHILE IN THIS PART

If the FIRST integer is negative even or positive odd, the program reads 
10 integers. The program finds and prints the maximum and minimum among 
the input numbers. YOU CAN USE THE LOOP OF YOUR CHOICE FOR THIS PART */

#include<stdio.h>
int main(){

	int num, num2, i, c; 
	double sumNeg, negOC, NegAvg;
	double sum, avg; 
	printf("enter an integer:\n");
	scanf("%d", &num);

	if(num > 0 && num%2==0){
		for(i=1; i<=5; i++){
			printf("enter integer:\n");
			scanf("%d", &num2);
			if(num<0){
				sumNeg+=1;
				negOC=num;
			}
		}
		NegAvg=(double)sumNeg/num;
		printf("sum of negative inputs: %d\n", sumNeg);
		printf("amount of negative inputs: %d\n", negOC);
		printf("average of negative inputs: %lf\n", NegAvg);
		scanf("%d", &num);
	}
	if(num2 < 0 && num2 % 2!=0){
		while(num < 0){
			if(num2 >= 8 && num2 <= 25 && num2 % 7==0){
				sum+=1;
				c=num2;
				
			}
		}
		avg=(double)sum/num2;
		printf("average of numbers divisble by 7: %lf\n", avg);
		scanf("%d", &num2);
	}
		else{
			printf("you did not enter a negative odd number\n");
		}
	return 0;
}
