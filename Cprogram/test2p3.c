/*Tyler Scott
March 22 2013*/

#include <stdio.h>

int main(){
	
	int num1;
	int d1, d2, d3, d4, d5;
	int sum;
	int avg;
	int Oddnum;
	
	printf("enter the integer\n");
	scanf("%d", &num1);
	
	d1 = num1 % 10;
	d2 = d1/10;
	d3 = d2 % 10;
	d4 =d3/10;
	d5 = d4 % 10;

	sum = d1+d2+d3+d4+d5;
	avg = sum/5.0;

	if(num1<= 0){
		printf("no negative numbers or zeros!");
	}	
	
	else if(d1 % 2 != 0 || d2 %2 != 0 || d3%2 != 0 || d4%2!= 0|| d5%2 != 0){
	
		printf("%d, %d, %d, %d, %d\n", d5, d4, d3, d2, d1);
	}

	else{
		printf("no odd numbers");	
	}		
}
