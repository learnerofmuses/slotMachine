/*Tyler Scott
March 20 2013
Write a program that inputs one integer between 0 and 100 which 
indicates student's grade. The program outputs the letter equivalent for 
numeric grade according to the following table:
A: 100 - 90
B: 89 - 75
C: 74 - 65
D: 64 - 60
F: 59 - 0
Your program must print error message if the input is outside of the valid 
range.

You can do the loop version of this program and input a series of 
non-negative integers between 0 and 100. Each integer indicates the 
student's grade. The first negative value will terminate the input. The 
program outputs the letter equivalent for each numeric grade according to 
the table above.*/

#include <stdio.h>

int main(){
	
	int num;
	int A_SCORE = 90;
	int B_SCORE = 80;
	int C_SCORE = 70;
	int D_SCORE = 60;
	printf("enter student grade\n");
	scanf("%d", &num);
	while(num > 0){
		
	 if(num <= 100 && num>= 90){
		printf("You have received an A. Great job!\n");
	}
	else if(num <= 89 && num >=80){
		printf("You have received a B. Good job!\n");
	}
	else if(num <= 79 && num >=70){
		printf("You have received a C. Try studying harder.\n");
	}
	else if(num <= 69 && num >=60){
		printf("You have received a D. Ask for help.\n");
	}
	else if(num < 60){
		printf("You have received an F. This is not good.\n");
	}
	else{
		printf("invalid input\n");
	}
	scanf("%d", &num);
	}
	return 0;
}

