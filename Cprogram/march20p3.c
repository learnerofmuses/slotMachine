/*write a program that reads one integer and finds the number, sum and 
average of all divisors that are divisible by 3 of the input number 
example: input 24 all divisors: 1, 2, 3, 4, 6, 8, 12, 24 divisors that are 
divisble by 3: 3, 6, 12, 24 their sum = 45 average= 45/4.0 = 11.25*/

#include <stdio.h>
#define THREE 3
int main(){
	
	int num, sum = 0, divisor, counter = 0;
	double average;

	printf("enter int \n");
	scanf("%d", &num);
	
	for (divisor = 1; divisor<=num; divisor++){
		if((num % divisor == 0) && (divisor%3==0)){  
	   		printf("%d ", divisor);
			counter++;
			sum=sum+divisor;
		}
	}
	printf("\n");
	if(counter > 0){
		
		average=(double)(sum)/counter;
		printf("\nsum is %d\n", sum);
		printf("average is %.3f\n", average);
	}
	else{
		printf("no divisors divisible by 3\n");
	}
	return 0;
}

	
