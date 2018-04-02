#include<stdio.h>

int millionaire(float dep, float interest);

int main(){
	int year;
	float dep, interest, res; 
	printf("please enter the deposit and interest:\n");
	scanf("%f %f", &dep, &interest);
	
	while(dep>=0){
		year=millionaire(dep, interest);
		
		printf("enter deposit and interest:\n");
		printf("it will take you %d years to become a millionaire\n", year);
		scanf("%f %f", &dep, &interest);
	}
	return 0;
}

int millionaire(float dep, float interest){
	int year = 0;

	while(dep<1000000){
		dep*=(1+interest);
		year++;	
	}
	return year;
}
