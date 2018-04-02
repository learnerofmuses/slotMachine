/*lab 4 problem 3 */

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define SIZE 6

int count_digit(int num);
void make_array(int A[], int size);
void print_array(int A[], int size); 
void process_plates(int A[], int size); 


int main(){
	int num(SIZE)={0}, real_size;
	printf("please enter the number of cars in parking lot:\n");
}

int count_digit(int num){
	int i, count; 
	for(i=0; i<num; i++){
		count=make_array(A[i]); 
		if(A[0]>=1 || A[0]<=5 && num==6){
			printf("this is a NJ plate\n");
		}
		if(A[0]>=6 || A[0]<=9 && num==6){
			printf("this is a NC plate\n");
		}
		if(A[8]>=1 || A[8]<=5 && num==7){
			printf("this is a NY plate\n");
		}
 		if(A[8]>=6 || A[8]<=9 && num==7){
			printf("this is a MA plate\n");
		}
		if(A[

		if(num=4 || num=6
}
void make_array(int array[], int size){
	int i; 
	for(i=0; i<size; i++){
		if(A[i]<4 && A[i]>7){
			printf("this is not a state license plate\n");
		}
		else{
			printf("please enter the license plate:\n");
			printf("%d\n" &A[i]);
		}
		printf("\n"); 
}


void print_array(int A[], int size){ 
	int i; 
	for(i=0; i<size; i++){
		printf("%d\n", (A[i]));
	}
	printf("\n");
}


void process_plates(int A[], int size){
	int i; 

}
