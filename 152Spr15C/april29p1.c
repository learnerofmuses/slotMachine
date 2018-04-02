#define<stdio.h>
#define<stdlib.h>
#define<time.h>

#define ROW 2
#define COL 3

void ReadArray(int num_rows, int num_cols);
void PrintArray(int A[][COL], int num_rows, int num_cols); 
void sum_Row(int A[][COL], int rowSize, int colSize, int rowNum);
void sum_Col(int A[][COL], int rowSize, int colSize, int colNum);

void ReadArray(int num_rows, int num_cols){
 


}
void PrintArray(int A[][COL], int num_rows, int num_cols){
	int i, j;
	for(i=0; i<num_rows; i++){
		for(j=0; j<num_cols;j++){
			printf("%d ", A[i][j]);
		}
		printf("\n");
	}
}

void sum_Row(int A[][COL], int rowSize, int colSize, int rowNum){
	int j, sum=0;
	for(j=0;j<colSize;j++){
		sum+=A/*[j]*/[rowNum][j];
	}
	return sum;
}

void sum_Col(int A[][COL], int rowSize, int colSize, int colNum){
	int i, sum=0;
	for(i=0;i<colSize;i++){
		sum+=A[i][colNum]/*[i]*/;
	}
	return sum;
}

int main(){
	srand(time(NULL);
	int rowSize=2+rand()%4, colSize=2+rand()%4;
	int rowA[ROW], colA[COL], i, rowSum=0, colSum=0, j, k;
	ReadArray(A, rowSize, colSize);


}
