/*lab 4 problem 2*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define SIZE 20
 
void make_array(int A[], int real_size);
void print_array(int A[], int real_size);	 
int count_even_divisor(int num); 
int array_even_divisor(int array, int real_size);

int main(){
	
	
	int num[SIZE]={0}, real_size; 
	srand(time(NULL)); 
	real_size=5+rand()%16;
	printf("real size is: %d\n", real_size);
	printf("array before make_array\n");
	print_array(num, real_size);
	printf("array after make_array\n");
	make_array(num, real_size);
	print_array(num, real_size);
	array_even_divisor(num, real_size);
	return 0;
}		
void make_array(int A[], int real_size){
	int i; 
	for(i=0; i<real_size; i++){
		A[i]=rand()%101;
	}	
}

void print_array(int A[], int real_size){
	int i; 
	for(i=0;  i<real_size; i++){
		printf("%d\n", (A[i]));
	} 
	printf("\n");
}


int count_even_divisor(int num){
	int i, count=0; 
	for(i=2; i<=num; i=i+2){
		if(num%i==0);
			count++;
	
	{
	return count;
}

int array_even_divisor(int array, int real_size){
	int i, count; 
	for(i=0; i<real_size; i++){
		count=count_even_divisor(A[i]);
		if(count==0){
			printf("no even divisors\n");
		}
		else{
			printf("even divisors %d\n", count);
		}
	}

