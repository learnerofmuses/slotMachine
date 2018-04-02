/* Nested Loops Example: program reads 5 integers between 0 and 9 each, 
and prints  
prints 5X5 square of the input numbers in the following way:
ASSUME: ALL INPUTS ARE VALID!
!!!PAY ATTENTION: YOU MUST ENTER INPUTS ON ONE LINE WITH SPACES BETWEEN 
NUMBERS!!!!

Examples:

Input: 3 4 8 9 0
Output:
33333
44444
88888
99999
00000

Input: 7 6 5 1 3
Output:
77777
66666
55555
11111
33333

*/

#include<stdio.h>

int main(){

	int i, j, num;
	printf("enter 5 ints between 0 and 9\n");
	
	for(i=0; i<5; i++){
		scanf("%d", &num);
		for(j=0; j<5; j++){
			printf("%d", num);
		}
		printf("\n");
	}
	return 0;
} 

