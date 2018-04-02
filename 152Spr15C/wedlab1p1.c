/*Write a program that reads 7 real numbers. Each number indicates the 
Fahrenheit temperature for one day. The program finds and prints the 
average Celsius temperature for these 7 days. Use the following formula 
to convert Fahrenheit to Celsius: Celsius = (5/9)*(Fahrenheit-32) */

#include<stdio.h>

int main(){

	int i; 

	double num, sum;
	
	double avg;
	
	
	for(i=1; i<=7; i++){
		printf("what is the Farenheit temp:\n");
		scanf("%lf", &num);		
		num = (double)(5.0/9)*(num-32);
		sum = sum+num;
	}
	avg = (double)sum/7;
	printf("average is %f\n", avg);
	return 0;
}
