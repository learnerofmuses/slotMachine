#include <stdio.h>

int main(){
	int num1;      /* first input number */ 
    	int num2;       /* second input number */ 
    	int sum;      /* sum of two input numbers */ 
	
	printf("Please enter first integer "); 
    	scanf ("%d", &num1);

    	printf("Please enter second integer "); 
    	scanf("%d", &num2); 
	
	
        sum = num1 + num2;

        printf("Sum is %d\n", sum);

        return 0; 

} 
