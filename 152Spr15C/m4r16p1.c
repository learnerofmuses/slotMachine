/*nested loops

write a program that reads one integer and prints the following square
***....***
***....***
....
**********

the number of rows and columns equal to the input num*/

#include<stdio.h>

int main(){
	int num, i, j; 

	printf("enter integer \n");
	scanf("%d", &num);
	for(i=1; i<=num; i++){
		for(j=1; j<=num; j++){
			printf("*");
		}
		printf("\n");
	}
	
	return 0; 
	
}
