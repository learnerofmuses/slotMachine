/* Tyler Scott
/* March 13 2013

#include<stdio.h>

int main(){

	int num1, num2, num3, num4; /*input numbers*/
	
	/* input session*/

	printf("enter 4 integer numbers") /*user prompt*/; 
	scanf("%d%d%d%d", &num1, &num2, &num3, &num4); 
	sum = num2+num3+num4;
	
	if(num2%num3%num4 == 0) { 
		ave = sum/3.0;
	}
	else{
		product = num2*num3*num4;	
	}

	return 0; 
}
	
