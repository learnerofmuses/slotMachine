/*write a program that generates random numbers and finds percentage of 
evens and odds
make the size - user input*/

#include<stdio.h>
#include<stdlib.h>

int main(){
	int num, evenCounter=0, oddCounter=0, i, size;
	double even, odd; 
	srand(time(NULL));
	printf("enter number of ints to generate\n");
	scanf("%d", &size);
	for(i=1; i<=size; i++){
		num=rand();
		printf("%d\n", num);
		if(num%2==0){
			evenCounter++;
		}
		else{
			oddCounter++;
		}
	}
	
	even=((double)(evenCounter)/size)*100;
	odd=((double)(oddCounter)/size)*100;

	printf("evenPercent=%f\n"), even);
	printf("oddPercent=%f\n"), odd);
	return 0;

}
	
