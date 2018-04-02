/*Write a function int power ( int base, int exponent) that returns the 
value of base ^ exponent. For example if the base is 2 and exponent is 3 
the power function returns 8. Write a main program that reads the 
sequence of non-negative numbers. The first negative number indicates 
the end of the input sequence. Assume that the amount of input numbers 
is even. Starting from the first input number, consider the pair of 
inputs as base and exponent and find the base ^ exponent for each pair. 
The program prints the results on different lines printing the value of 
base and exponent as well as the value of base^exponent. If both numbers 
in the pair are 0, the program will print the error message "0^0 is not 
defined" For example if the input is: 2, 3, 1, 4, 2, 0, 0, 5, 0, 0, 5, 
2, 3, 3, -4. The program will print:
2^3 = 8
1^4 = 1
2^0 = 1
0^5 = 0
0^0 is not defined
5^2 = 25
3^3 = 9 
*/
#include<stdio.h>

int power(int base, int exponent);

int main(){
	int base, ex, res;
	printf("enter a positive integer:\n");
	scanf("%d %d", &base, &ex);
	while(base>=0){
		res=power(base, ex);
		if(res==-1){
			printf("try again:\n");
		}
		else{
			printf("%d, %d equals %d\n", base, ex, res);
		}
		scanf("%d %d", &base, &ex);
	}
	return 0;
		
}

int power(int base, int exponent){
	int res, count;

	if(base>0 && exponent==0){ 
		res=1;
	}
	else if(base==0 && exponent==0){
		res=0;
	}
	else{
		res=1;
		for(count=1; count<=exponent; count++){
			res=res*base;
		}
	}	
	return res;
}
