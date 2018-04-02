/*Tyler Scott
April 3 2013
Write a program that reads a sequence of characters, character '%' will 
terminate the input. finds the number of lower case letters, the number of 
upper case letters, and the number of digits.*/

#include <stdio.h>

int main(){

	char letter;
	int count = 0, uppercase = 0, lowercase = 0, digits;
	char i; 

	printf("enter sequence of characters\n");
	i = getchar();
	while(i != '%'){
		if(i >= 'a' && i <= 'z'){
			lowercase++;
			
		}
		else if(i >= 'A' && i <= 'Z'){
			uppercase++;
		}
		else if(i >= 0 && i<= 9){
			digits++;
		}
		else{
			printf("error");
		}
		printf("there are %d lowercase letters\n", lowercase);
		printf("there are %d uppercase letters\n", uppercase);
		printf("number of lowercase digits are %d\n", digits);
		printf("number of uppercase digits are %d\n", digits);
		return 0;
	}
	}
