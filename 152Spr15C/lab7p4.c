#include<stdio.h>
#include<stdlib.h>
#define ROW 4
#define COL 4

void fillRandom(int A[ ][COL], int num_rows, int num_cols);
void printArray(int A[ ][COL], int num_rows, int num_cols);
int numNonZero(int A[][COL], int num_rows, int num_cols);


int main(){
	int A[ROW][COL];
	srand(time(NULL));
	fillRandom(A, ROW, COL);
	printArray(A, ROW, COL);
	numNonZero(A, ROW, COL);
	/*if(zcount<0*/	
	return 0;
}

void fillRandom(int A[ ][COL], int num_rows, int num_cols){
	int i, j;
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			A[i][j]=(-3+rand() % 7);
		}
	}
}

void printArray(int A[ ][COL], int num_rows, int num_cols){
	int i, j;
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			printf ("%d ", A[i][j]);
		}
		printf("\n");
	}
}
int numNonZero(int A[][COL], int num_rows, int num_cols);
	int i, j, cnt=0;
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			if(a[i][j]!=0){
				cnt++;
			}
		}
	}
}
