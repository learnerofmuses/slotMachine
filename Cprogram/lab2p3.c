/*Tyler Scott
March 20 2013
weekTemp.c
Write a program weekTemp.c that reads 7 real numbers. Each number indicates 
the Fahrenheit temperature for one day. The program finds and prints the 
average Celsius temperature for these 7 days. Use the following formula to 
convert Fahrenheit to Celsius: Celsius = (5/9)*(Fahrenheit-32)

Example 1: 
Input: 44.76 -67 87.5 0 12 86.89 90 
Output: The average Celsius temperature is: 2.392857

Example 2: 
Input: 45 45 45 45 45 45 45 
Output: The average Celsius temperature is: 7.222222

Example 3: 
Input: 32 32 32 32 32 32 32 
Output: The average Celsius temperature is: 0.0

Example 4: 
Input: 87 90 98 87 85 85 90 
Output: The average Celsius temperature is: 31.5873*/

#include <stdio.h>

int main(){
	
	int days, i;
	double Ftemp, Celsius, sum = 0.0, average;

	printf("enter number of days\n");
	
	
	printf("enter %d Fahrenheit temps\n", 7);
	
	for(i=0; i<7; i++){
		scanf("%lf", &Ftemp);
		Celsius = (5.0/9)*(Ftemp-32);
		
		sum = sum + Celsius;
		
	}
	if(days > 0){
		average = (double)(sum)/7;
        	printf("the average Celsius temp is");
		printf("%f\n", average);
	}
	else{
		printf("error\n");
	}
	return 0;
}
	
		
