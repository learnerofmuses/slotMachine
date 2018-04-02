#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define ROW 3
#define COL 4


void count(int A[][COL], int num_rows, int num_cols);
void fillRandom(int A[][COL], int num_rows, int num_cols);
void printArray(int A[][COL], int num_rows, int num_cols);


int main(){
	int A[ROW][COL];
	srand(time(NULL));
	fillRandom(A, ROW, COL);
	printArray(A, ROW, COL);
	count(A, ROW, COL);
	return 0;
}

void count(int A[][COL], int num_rows, int num_cols){
	int i, j;
	int count0=0, count1=0, count2=0, count3=0, count4=0;
	for(i=0;i<num_rows; i++){
		for(j=0;j<num_cols;j++){
			if(A[i][j]==0){
				count0++;
			}
			else if(A[i][j]==1){
				count1++;
			}
			else if(A[i][j]==2){
				count2++;
			}
			else if(A[i][j]==3){
				count3++;
			}
			else if(A[i][j]==4){
				count4++;
			}
		}	
	}
	printf("number of 0's %d\n", count0);
	printf("number of 1's %d\n", count1);
	printf("number of 2's %d\n", count2);
	printf("number of 3's %d\n", count3);
	printf("number of 4's %d\n", count4);
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
			printf("%d ", A[i][j]);
		}
		printf("\n");
	}
}
