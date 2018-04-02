/*arrays and functions 

write a function void make_zero(int A[], int real_size)

the function will replace all even elements of the array with 0 

write a function void make_array(int A[], int real_size, int low, int 
upper) that 
randomly generates array of ints between low and upper 

write a function void print_array(int A[], int real_size)
the size of the array will be randomly generated int main 
between 5 and 20
*/

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define SIZE 100 
#define SIZE_MAX 20 
#define SIZE_MIN 5

void make_array(int A[], int real_size, int low, int upper);
void print_array(int A[], int real_size);
void make_zero(int A[], int real_size);
int main(){
 	
	srand(time(NULL));
	int real_size, A[SIZE], low, upper; 
	real_size=SIZE_MIN+rand()%(SIZE_MAX-SIZE_MIN+1);
	printf("enter low and upper bounds for the elements\n"); 
	scanf("%d%d", &low, &upper); 
	printf("array BEFORE function make_array\n"); 
	print_array(A, real_size); 
	make_array(A, real_size, low, upper); 
	printf("array AFTER function make_array\n"); 
	print_array(A, real_size);	
	make_zero(A, real_size);
	printf("array after function make_zero\n");
	print_array(A, real_size);
	return 0;
}

void make_array(int A[], int real_size, int low, int upper){
	int i;
	for(i=0; i<real_size; i++){
		A[i]=low+rand()%(upper-low+1);
	}
}
void print_array(int A[], int real_size){
	int i; 
	for(i=0; i<real_size; i++){
		printf("%d ", A[i]); 
	}
	printf("\n"); 
}
void make_zero(int A[], int real_size){
	int i; 
	for(i=0; i<real_size; i++){
		if(A[i]%2==0){
			
}
	
