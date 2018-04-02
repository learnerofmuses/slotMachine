/* lab 4*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define SIZE 20 

int main(){
	

	int num[SIZE], i, realSize, sEven=0, cEven=0; 
	double aEven;  
	srand(time(NULL));
	realSize = 5+rand() % 16; 
	
	for(i=0; i<realSize; i++){
		sEven[i];
		if(num[i]%2==0){
			sEven+=num[i];	
			cEven++;
		}
	}
	for(i=0; i<realSize; i++){
		printf("%d", &num[i]);
	}
	printf("\n");
	if(cEven>0){
		aEven=(double)(sEven)/cEven;
		printf("the average of even integers is%f\n", aEven);
	}
	else{
		printf("there are no even numbers \n"); 
	}
	return 0; 

}
