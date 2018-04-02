#include<stdio.h>

int sumSqr(int n);

int main(){
	int n, i =1, sum, tf=0;
	printf("please enter non-negative integers:\n");
	scanf("%d", &n);

	if(i=0){
		printf("the program has been terminated");
		tf=-1;
	}
	while(tf=0){
		sum=sumSqr(n);
		printf("sum squares of %d is: %d\n", n, sum);
		scanf("%d", &n);
	}
}

int sumSqr(int n){
	int i, sum = 0;
	for(i=1, i<=n, i++){
		sum = i+1;
	}
	return sum;
}
