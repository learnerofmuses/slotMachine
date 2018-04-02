/*Write a C program that reads a sequence of positive numbers, the first 
non-positive integer terminates the input. The program prints for each 
input number the corresponded sum of squares, using function sumSqr. */

#include<stdio.h>

int count_even_divisor(int num);

int main(){
	int num, c;
	scanf("%d", &num);
	while(n>0){
		c=count_even_divisor(n);
		if(c==0){
			printf("no even divisors\n");
		}
		else{
			printf("%d even divisors\n", c);
		}
			scanf("%d", &num);
	
}

int count_even_divisor(int num){
	int counter = 0, i; 
	for(i=2, i<=n, i+2){
		if(n%i==0){
			counter++;
		}
	}
	return counter;
}


