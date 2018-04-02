/*write a program that reads 10 ints and finds the number of evens and 
odds

USE LOOP FOR*/

#include<stdio.h>
	
int main(){
	int num, even = 0, odd = 0, i; 
	
	for(i=0; i<10; i++){
		scanf("%d", &num);
		if(num%2==0){
			even++;
		}
		else{
			odd++;
		}
	}
	if(even==0){
		printf("no evens\n");
	}
	else{
		printf("%d evens\n", even);
	}
	if(odd==0){
		printf("no odds"\n);
	}
	else{
		printf("
	
