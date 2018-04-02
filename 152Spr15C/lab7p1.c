/*Write a function void ReadArray (int A[ ][COL], int num_row, int 
num_col) that reads a two dimensional array, COL - is the number of 
columns in array A. Write a function int even (int A[][COL], int 
num_rows, int num_cols) that finds and returns the amount of the even 
elements among the elements of the array A. Write a program that reads 
five two-dimensional arrays of size 3X4 (3 rows and 4 columns) each and 
find an array that has a maximal amount of the even elements. Use 
function even to count the amount of even elements in each array and use 
function ReadArray to read an input. Try to declare only one 
two-dimensional array and re-use this memory space 5 times by using loop 
structure.*/

#include<stdio.h>
#include<stdlib.h>
#define ROW 3
#define COL 4

void fillUser(int A[][COL], int num_rows, int num_cols);
void printArray(int A[][COL], int num_rows, int num_cols);
int even(int A[][COL], int num_rows, int num_cols);

int main(){
	int A[ROW][COL], i=0, max, which=1; 
	int num_even=0;
	srand(time(NULL));
	fillUser(A, ROW, COL);
	printArray(A, ROW, COL);
	num_even=even(A, ROW, COL);
	max=num_even;
	
	while(i<4){
		fillUser(A, ROW, COL);
		printArray(A, ROW, COL);	
		num_even=even(A, ROW, COL);
		if(num_even>max){
			max=num_even;
			which=(i+2);
		}
	}	
	if(num_even>0){
	
		printf("the num of evens in the array are %d\n", num_even); 
	}
	else{
		printf("no evens found in the array\n");
	}
	printf("the maximum of evens is %d\n", max);
	printf(" ", which);
	return 0;
}

void fillUser(int A[][COL], int num_rows, int num_cols){
	int i, j;
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			scanf("%d ", A[i][j]);
		}
	}
}
void printArray(int A[][COL], int num_rows, int num_cols){
	int i, j;
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			printf("%d ", A[i][j]);
		}
		printf("\n");
	}
}

int even(int A[][COL], int num_rows, int num_cols){
	int i, j, countE=0;
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			if(A[i][j]%2!=0){
				countE++;
			}
		}
	}
	return countE;
}
