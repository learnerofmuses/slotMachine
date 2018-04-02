/* write a program that reads one integer and prints the 
following square:
*****...*
*****...*
.........
*********

the number of stars in the line equals to input number
and the number of lines in the square equals to input 
number
 
if int is 5 the results will be
*****
*****
*****
*****
*****

use nested loop for
*/

#include<stdio.h>
int main(){
	int num, i, j; 
	printf("enter int \n");
	scanf("%d", &num);
	if(num<=0){
		printf("nothing to print\n");
	}
	else{

		for (i = 1; i<=num; i++){
			for(j = 1; j<= num; j++){
				printf("*");
			}
			printf("\n");
		}
	}
	return 0;
}	
