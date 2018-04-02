/* Tyler Scott
March 25 2013
Problem 1 Write a program that reads 2 integers, m and n, and prints the m 
X n rectangle of stars: m rows and n columns.
For example, for m = 3 and n = 5 the output will be:
*****
*****
******/

#include <stdio.h>

int main() 

	int m, n, i, j;
	printf("enter 2 integers\n");
	scanf("%d", &m);
	scanf("%d", &n);
	if(m <= 0 || n <= 0){
		printf("invalid input\n");
	}
	else{
	
		for(i=0; i<=m; i++){
			for(j=0; j<= n; j++){
				printf("*");
			}
			printf("\n");
		}
	}
	return 0;
}
