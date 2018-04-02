/* write a program that finds the average number 
of kilometers that the person is traveling during some 
period of time. The user will input the number of days 
for travel and the numbers of miles user traveled each 
day, the program will convert miles to kilometers
and find the average amount of kilometers */

#include<stdio.h>
#define MILETOKM 1.609344 

int main(){
	int days, i;
	double miles, km, sum = 0.0, average;

	printf("enter numbers of days \n");
	scanf("%d", &days);

	printf("enter %d amounts of miles\n", days);
	
	for (i=0; i<days; i++){
		scanf("%lf", &miles);
		km = MILETOKM*miles; 
		
		sum = sum + km;
	}
	if(days > 0){
		average=(double)(sum)/days;
		printf("the average number of km is ");
		printf("%f\n", average);
	}
	else{
		printf("you didn't travel\n");
	}
	return 0;
}
