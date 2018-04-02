/*lab 4*/ 

#include<stdio.h>
#include<stdlib.h>
#include<time.h>

#define SIZE 20 

int sumEven(int A[], int array_size);
int countEven(int A[], int array_size);
int averageEven(int A[], int array_size);
int main(){
	srand(time(NULL)); 
	int num[SIZE], i, realSize, sum=0, count;  
	realSize=5+rand()%16;
	printf("real size is %d\n", realSize); 
	for(i=0; i<realSize; i++){
		num[i]=rand()%10; 
		printf("%d", &num[i]); 
	}
	printf("\n");
	sum=sum_Even(num, realSize);
	if(sum==-1){
		printf("no evens\n");
	}
	else{
		printf("sum of evens is %d\n", sum);
	}
	if(count==-1){
		printf("no evens\n");
	}
	else{
		printf("average is %f\n");
	}
	return 0; 
}

int sumEven(int A[], int array_size){
	int i, sum_Even=0, countEven=0;
	for(i=0; i<array_size; i++){
		if(A[i]%2==0){
			sum_Even+=A[i];
			countEven++;
		}
	}
	printf("sum is %d\n", sum_Even);
	printf("counter is %d\n", countEven);
	if(countEven>0){		
		return sum_Even;
	}
	else{
		return -1;
	}
}

int countEven(int A[], int array_size){
        int i, sum_Even=0, countEven=0;
        for(i=0; i<array_size; i++){
                if(A[i]%2==0){
                        countEven++;
                }
        }
        printf("counter is %d\n", countEven);
        if(countEven>0){
                return sum_Even;
        }
        else{
                return -1;
        }
}

int averageEven(int A[], int array_size){
        int i, sum_Even=0, countEven=0;
        for(i=0; i<array_size; i++){
                if(A[i]%2==0){
                        countEven++;
                }
        }
        printf("counter is %d\n", countEven);
        if(countEven>0){
                return sum_Even;
	}
	else{
		return -1;
	}
}
