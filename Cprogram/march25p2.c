/* Nested Loops Example: program reads one integer between 0 and 9 and 
prints 5X5 square of the input number.

Examples:

Input: 3
Output:
33333
33333
33333
33333
33333

Input: 7
Output:
77777
77777
77777
77777
77777

Input: 10
Output: invalid input
*/

#include<stdio.h>

int main(){

	int i, j, num;
	printf("enter int between 0 and 9\n");
	scanf("%d", &num);
	if(num>=0 && num<=9){
		for(i=0; i<5; i++){
			for(j=0; j<5; j++){
				printf("%d", num);
			}
			printf("\n");
		}
	}
	else{
		printf("invalid input\n");
	}
	return 0;
} 

