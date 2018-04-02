/*Write a program that reads 10 integers and finds amount of ints 
divisible by 3, their sum, product and average. Use loop FOR*/

#include<stdio.h>

int main(){

	int num, i, sum = 0, product = 1, counter = 0;
	double average;
	printf("enter 10 integers\n");

	for (i = 1; i<=10; i++){
		scanf("%d", &num);
		if(num%3 == 0){
			counter++;
			sum = sum + num;
			product=product*num;
		}
	}
	
	if (counter > 0){
		average=(double)(sum)/counter;
		printf("%d ints divisible by 3\n", counter);
		printf("the average is %.4f\n",average);
		printf("sum is %d\n product is %d\n", sum, product);
			
	}
	else{
		printf("no ints divisible by 3\n");
	}
	return 0;
}

