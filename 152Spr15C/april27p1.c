/*find number of odd elements in the 2D array of ints */

#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define ROW 3
#define COL 4

void fillRandom(int A[][COL], int num_rows, int num_cols);
void printArray(int A[][COL], int num_rows, int num_cols);
int odd(int A[][COL], int num_rows, int num_cols);

int main(){
	
	int the_array[ROW][COL];
	int num_odd=0;
	srand(time(NULL));
	fillRandom(the_array, ROW, COL);
	printArray(the_array, ROW, COL);
	num_odd=odd(the_array, ROW, COL);
	if(num_odd>0){

		printf("the num of odds in the array are %d\n", num_odd);
	}
	else{	
		printf("no odds found in the array\n");
	}
	return 0;
}

void fillRandom(int A[][COL], int num_rows, int num_cols){
	int i, j;
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			A[i][j]=(rand() % 5);
		}
	}
}


void printArray(int A[][COL], int num_rows, int num_cols){
	int i, j; 
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			printf("%d ",A[i][j]);
		}
		printf("\n");
	} 
}


int odd(int A[][COL], int num_rows, int num_cols){
	int i, j, oddC=0;
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			if(A[i][j]%2==0){
				oddC++;
			}
		}
	}
}	
