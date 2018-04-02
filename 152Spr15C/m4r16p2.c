/*nested loop example 2

write a program that reads one integer 
and prints the following triangles 

******
*****
****
...
*

otherwise:
*
**
....
****** */


#include<stdio.h>

int main(){
	int num, i, j; 

	printf("enter integer \n");
	scanf("%d", &num);
	if(num%2==0){
	for(i=num; i>=1; i--){
		for(j=1; j<=i; j++){
			printf("*"); 
		}
		printf("\n");
	}
	}
	else{
	
		for(i=1; i<=num; i++){
			for(j=1; j<=i; j++){
				printf("*");
			}
			printf("\n");
		
		}
	}
	return 0;
}
