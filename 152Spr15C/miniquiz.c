#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define ROW 4
#define COL 3



void process(int A[][COL], int row, int col, int grades[]); 
void fillRandom(int A[][COL], int num_rows, int num_cols);
void printArray(int A[][COL], int num_rows, int num_cols);
int maxPosition(int A[], int Nrows);


int main(){
	int A[ROW][COL];
	int grades[100];
	int freq=0;
	srand(time(NULL));
	fillRandom(A, ROW, COL);
	printArray(A, ROW, COL);
	process(A, ROW, COL, grades);
	maxPosition(grades, ROW);
	freq=maxPosition(grades, ROW);
	/*freq=grades(max)*/
	if(freq==0){
		printf("frequent grade is A\n");
	}
	else if(freq==1){
		printf("frequent grade is B\n");
	} 
	else if(freq==2){
		printf("frequent grade is C\n");
	}
	else if(freq==3){
		printf("frequent grade is D\n");
	}
	else if(freq==4){
		printf("frequent grade is F\n");
	}
	return 0;
}



void process(int A[][COL], int row, int col, int grades[]){
	int i, j;
	int countA=0, countB=0, countC=0, countD=0, countF=0;
	for(i=0;i<row;i++){
		for(j=0;j<col;j++){
			if(A[i][j]>=0 && A[i][j]<=59){
				grades[4]++;
			}
			else if(A[i][j]>=60 && A[i][j]<=69){
				grades[3]++;
			}
			else if(A[i][j]>=70 && A[i][j]<=79){
				grades[2]++;
			}
			else if(A[i][j]>=80 && A[i][j]<=89){
				grades[1]++;
			}
			else if(A[i][j]>=90 && A[i][j]<=100){
				grades[0]++;
			}
		}
	}
	
}
void fillRandom(int A[][COL], int num_rows, int num_cols){
	int i, j; 
	for(i=0;i<num_rows;i++){
		for(j=0;j<num_cols;j++){
			A[i][j]=(rand() %101);
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

int maxPosition(int A[], int Nrows){
	int i, max, index;
	max=A[0];
	index=0;
	for(i=0;i<Nrows;i++){
		if(A[i]>max){
			index=1;
			max=A[i];
		}
	}
	return index;
}
