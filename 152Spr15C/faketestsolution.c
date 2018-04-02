#include<stdio.h>

int sumSqrt(int n);

int main(){
	int n, sum;
	printf("enter positive int\n");
	scanf("&d", &n);
	while(n>0){
		sum=sumSqrt(n);
		printf("1*1+2*2+...+%d*%d=%d\n", n,n,sum);
		scanf("%d", &n);
	}
	return 0;
}

int sumSqrt(int n){
	int sum= 0, i; 
	for(i=1, i<=n, i++){
		sum = sum+i*i;
	}
	return sum;

}

int sumSqrtWhile(int n){
	int sum=0, i =1;
	while(i<=n){
		sum = sum+i*i;
		i++;
	}
	return sum;

}
